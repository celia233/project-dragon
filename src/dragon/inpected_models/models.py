# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    bookid = models.AutoField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    bookitemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='BookItemID', unique=True)  # Field name made lowercase.
    bookname = models.CharField(db_column='BookName', max_length=256)  # Field name made lowercase.
    bookgenre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='BookGenre', blank=True, null=True)  # Field name made lowercase.
    bookdescription = models.CharField(db_column='BookDescription', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    bookcondition = models.IntegerField(db_column='BookCondition', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book'


class Clubmember(models.Model):
    memberid = models.AutoField(db_column='MemberID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    preferredname = models.CharField(db_column='PreferredName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    memberrank = models.ForeignKey('Clubrank', models.DO_NOTHING, db_column='MemberRank', blank=True, null=True)  # Field name made lowercase.
    prefpronoun = models.CharField(db_column='PrefPronoun', max_length=8, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    guildmember = models.IntegerField(db_column='GuildMember', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=20)  # Field name made lowercase.
    incidents = models.CharField(db_column='Incidents', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClubMember'


class Clubrank(models.Model):
    rankid = models.AutoField(db_column='RankID', primary_key=True)  # Field name made lowercase.
    rankname = models.CharField(db_column='RankName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClubRank'


class Collection(models.Model):
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  # Field name made lowercase.
    collectionname = models.CharField(db_column='CollectionName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Collection'


class Game(models.Model):
    gameid = models.AutoField(db_column='GameID', primary_key=True)  # Field name made lowercase.
    gameitemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='GameItemID', unique=True)  # Field name made lowercase.
    gamename = models.CharField(db_column='GameName', max_length=256)  # Field name made lowercase.
    gamegenre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='GameGenre', blank=True, null=True)  # Field name made lowercase.
    gamedescription = models.CharField(db_column='GameDescription', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    gamecondition = models.IntegerField(db_column='GameCondition', blank=True, null=True)  # Field name made lowercase.
    minplayers = models.IntegerField(db_column='MinPlayers', blank=True, null=True)  # Field name made lowercase.
    maxplayers = models.IntegerField(db_column='MaxPlayers', blank=True, null=True)  # Field name made lowercase.
    avegamelength = models.CharField(db_column='AveGameLength', max_length=32, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Game'


class Genre(models.Model):
    genreid = models.AutoField(db_column='GenreID', primary_key=True)  # Field name made lowercase.
    genrename = models.CharField(db_column='GenreName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genre'


class Interest(models.Model):
    interestid = models.AutoField(db_column='InterestID', primary_key=True)  # Field name made lowercase.
    interestname = models.CharField(db_column='InterestName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Interest'


class Item(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemtype = models.ForeignKey('Itemtype', models.DO_NOTHING, db_column='ItemType')  # Field name made lowercase.
    available = models.IntegerField(db_column='Available')  # Field name made lowercase.
    collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='Collection', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'


class Itemtag(models.Model):
    linktag = models.ForeignKey('Tag', models.DO_NOTHING, db_column='LinkTag')  # Field name made lowercase.
    taggeditem = models.ForeignKey(Item, models.DO_NOTHING, db_column='TaggedItem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemTag'


class Itemtype(models.Model):
    typeid = models.AutoField(db_column='TypeID', primary_key=True)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemType'


class Loan(models.Model):
    loanid = models.AutoField(db_column='LoanID', primary_key=True)  # Field name made lowercase.
    loantransactionid = models.ForeignKey('Transactions', models.DO_NOTHING, db_column='LoanTransactionID')  # Field name made lowercase.
    loanitemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='LoanItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Loan'


class Memberinterest(models.Model):
    memberid = models.ForeignKey(Clubmember, models.DO_NOTHING, db_column='MemberID')  # Field name made lowercase.
    interestid = models.ForeignKey(Interest, models.DO_NOTHING, db_column='InterestID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberInterest'


class Tag(models.Model):
    tagid = models.AutoField(db_column='TagID', primary_key=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tag'


class Transactions(models.Model):
    transactionid = models.AutoField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    borrowerid = models.ForeignKey(Clubmember, models.DO_NOTHING, db_column='BorrowerID')  # Field name made lowercase.
    approverid = models.ForeignKey(Clubmember, models.DO_NOTHING, db_column='ApproverID')  # Field name made lowercase.
    dateborrowed = models.DateTimeField(db_column='DateBorrowed')  # Field name made lowercase.
    returnconfirmerid = models.ForeignKey(Clubmember, models.DO_NOTHING, db_column='ReturnConfirmerID')  # Field name made lowercase.
    datereturned = models.DateTimeField(db_column='DateReturned')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'
