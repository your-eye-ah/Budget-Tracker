from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Entry
from . import db
from .forms import EntryForm
from datetime import datetime


main = Blueprint('main', __name__)

@main.route('/')
def index():
    entries = Entry.query.order_by(Entry.date.desc()).all()

    total_income = sum(e.amount for e in entries if e.type == 'Income')
    total_expense = sum(e.amount for e in entries if e.type == 'Expense')
    net_balance = total_income - total_expense
    recent_entries = entries[:5]

    return render_template('index.html',
                           entries=entries,
                           total_income=total_income,
                           total_expense=total_expense,
                           net_balance=net_balance,
                           recent_entries=recent_entries)


@main.route('/add', methods=['GET', 'POST'])
def add_entry():
    form = EntryForm()

    if form.validate_on_submit():
        new_entry = Entry(
            type=form.type.data,
            amount=form.amount.data,
            category=form.category.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(new_entry)
        db.session.commit()
        flash('Entry added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add_entry.html', form=form)

@main.route('/visualizations')
def visualizations():
    from sqlalchemy import func
    from .models import Entry
    from collections import defaultdict
    from datetime import datetime


    # Aggregate expense totals by category
    category_data = (
        db.session.query(Entry.category, func.sum(Entry.amount))
        .filter(Entry.type == 'Expense')
        .group_by(Entry.category)
        .all()
    )

    labels = [row[0] for row in category_data]
    values = [row[1] for row in category_data]



    # Aggregate income and expenses by month
    entries = Entry.query.all()
    monthly_data = defaultdict(lambda: {'Income': 0, 'Expense': 0})

    for entry in entries:
        month = entry.date.strftime('%Y-%m')
        monthly_data[month][entry.type] += entry.amount

    # Sort months chronologically
    sorted_months = sorted(monthly_data.keys())

    bar_labels = sorted_months
    bar_income = [monthly_data[m]['Income'] for m in sorted_months]
    bar_expense = [monthly_data[m]['Expense'] for m in sorted_months]

    return render_template(
    'visualizations.html',
    labels=labels,
    values=values,
    bar_labels=bar_labels,
    bar_income=bar_income,
    bar_expense=bar_expense
    )

@main.route('/tables')
def tables():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    entries = Entry.query.order_by(Entry.date.desc()).paginate(page=page, per_page=per_page)
    return render_template('tables.html', entries=entries)


@main.route('/edit/<int:entry_id>', methods=['POST'])
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    entry.type = request.form['type']
    entry.amount = float(request.form['amount'])
    entry.category = request.form['category']
    entry.description = request.form['description']
    entry.date = datetime.strptime(request.form['date'], "%Y-%m-%d").date()
    db.session.commit()
    flash('Entry updated.', 'success')
    return redirect(url_for('main.tables'))

@main.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted.', 'danger')
    return redirect(url_for('main.tables'))
