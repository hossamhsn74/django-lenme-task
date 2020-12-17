# Generated by Django 3.1.2 on 2020-12-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Funded', 'Funded'), ('Completed', 'Completed')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.loan')),
            ],
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('period', models.IntegerField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.borrower')),
            ],
        ),
        migrations.CreateModel(
            name='LoanOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestRate', models.IntegerField()),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.investor')),
            ],
        ),
        migrations.CreateModel(
            name='Investor_Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.investor')),
                ('paymentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.loan')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowerOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.borrower')),
                ('offerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.loanoffer')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower_Investor_Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.borrower')),
                ('investorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.investor')),
                ('loanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenme.loan')),
            ],
        ),
    ]