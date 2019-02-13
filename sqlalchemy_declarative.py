# coding: utf-8
"""Describes the sqlalchemy classes - generated using sqlacodegen
More useful for write and update operations"""
from sqlalchemy import BigInteger, Column, Float, MetaData, Table, Text

metadata = MetaData()


t_Acutesexuallytransmittedinfections = Table(
    'Acutesexuallytransmittedinfections', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Adultssmoking = Table(
    'Adultssmoking', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Alcoholspecifichospitalstaysunder18 = Table(
    'Alcoholspecifichospitalstaysunder18', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Allageallcausemortalityaggregatetrend = Table(
    'Allageallcausemortalityaggregatetrend', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Allethnicgroups = Table(
    'Allethnicgroups', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Asian = Table(
    'Asian', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Averagedeprivedquintile = Table(
    'Averagedeprivedquintile', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Black = Table(
    'Black', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Chinese = Table(
    'Chinese', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Deprivation = Table(
    'Deprivation', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Drugmisuse = Table(
    'Drugmisuse', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Earlydeathscancer = Table(
    'Earlydeathscancer', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Earlydeathscanceraggregatetrend = Table(
    'Earlydeathscanceraggregatetrend', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Earlydeathsheartdiseaseandstroke = Table(
    'Earlydeathsheartdiseaseandstroke', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Earlydeathsheartdiseasestrokeaggregatetrend = Table(
    'Earlydeathsheartdiseasestrokeaggregatetrend', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Excesswinterdeaths = Table(
    'Excesswinterdeaths', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_GCSEachieved5ACincEngMaths = Table(
    'GCSEachieved5ACincEngMaths', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Healthyeatingadults = Table(
    'Healthyeatingadults', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Hipfracturein65sandover = Table(
    'Hipfracturein65sandover', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Hospitalstaysforalcoholrelatedharm = Table(
    'Hospitalstaysforalcoholrelatedharm', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Hospitalstaysforselfharm = Table(
    'Hospitalstaysforselfharm', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Incidenceofmalignantmelanoma = Table(
    'Incidenceofmalignantmelanoma', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Increasingandhigherriskdrinking = Table(
    'Increasingandhigherriskdrinking', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Infantdeaths = Table(
    'Infantdeaths', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Leastdeprivedquintile = Table(
    'Leastdeprivedquintile', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Lessdeprivedquintile = Table(
    'Lessdeprivedquintile', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Lifeexpectancyfemale = Table(
    'Lifeexpectancyfemale', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Lifeexpectancymale = Table(
    'Lifeexpectancymale', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Longtermunemployment = Table(
    'Longtermunemployment', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Mixed = Table(
    'Mixed', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Moredeprivedquintile = Table(
    'Moredeprivedquintile', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Mostdeprivedquintile = Table(
    'Mostdeprivedquintile', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Newcasesoftuberculosis = Table(
    'Newcasesoftuberculosis', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Obeseadults = Table(
    'Obeseadults', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_ObesechildrenYear6 = Table(
    'ObesechildrenYear6', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Other = Table(
    'Other', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Peoplediagnosedwithdiabetes = Table(
    'Peoplediagnosedwithdiabetes', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Physicallyactiveadults = Table(
    'Physicallyactiveadults', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Proportionofchildreninpoverty = Table(
    'Proportionofchildreninpoverty', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', BigInteger),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Roadinjuriesanddeaths = Table(
    'Roadinjuriesanddeaths', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Smokinginpregnancy = Table(
    'Smokinginpregnancy', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Smokingrelateddeaths = Table(
    'Smokingrelateddeaths', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Startingbreastfeeding = Table(
    'Startingbreastfeeding', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Statutoryhomelessness = Table(
    'Statutoryhomelessness', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Teenagepregnancyunder18 = Table(
    'Teenagepregnancyunder18', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Unknown = Table(
    'Unknown', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_Violentcrime = Table(
    'Violentcrime', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)


t_White = Table(
    'White', metadata,
    Column('index', BigInteger, index=True),
    Column('ONS_CODE_OLD', Text),
    Column('ONS_CODE_NEW', Text),
    Column('AREA_NAME', Text),
    Column('ONS_CLUSTER', Text),
    Column('PERIOD', Text),
    Column('INDICATOR_VALUE', Float(53)),
    Column('LOWER_95_CI', Float(53)),
    Column('UPPER_95_CI', Float(53))
)
