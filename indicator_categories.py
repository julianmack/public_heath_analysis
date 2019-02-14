"""Indicator categories"""
A = "A"   #Our Communities
B = "B"   #Children's and young people's health
C = "C"   #Adults' health and lifestyle
D = "D"   #Disease and poor health
E = "E"   #Life expectancy and causes of death

# I used the actegories in the following document:
# https://www.isleofwightccg.nhs.uk/Downloads/Health%20and%20Wellbeing%20Profile/HealthProfile2012IsleofWight00MW.pdf

ind_cat = {
"obesechildrenyear6": B,
"other": D,
"peoplediagnosedwithdiabetes": D,
"physicallyactiveadults": C,
"proportionofchildreninpoverty": A,
"roadinjuriesanddeaths": E,
"smokinginpregnancy": B,
"smokingrelateddeaths": E,
"acutesexuallytransmittedinfections": D,
"adultssmoking": C,
"alcoholspecifichospitalstaysunder18": B,
"allethnicgroups": D,
"asian": D,
"averagedeprivedquintile": A,
"black": D,
"chinese": D,
"deprivation": A,
"drugmisuse": D,
"earlydeathscancer": E,
"earlydeathsheartdiseaseandstroke": E,
"excesswinterdeaths": E,
"gcseachieved5acincengmaths": A,
"healthyeatingadults": C,
"hipfracturein65sandover": D,
"hospitalstaysforalcoholrelatedharm": D,
"hospitalstaysforselfharm": D,
"incidenceofmalignantmelanoma": D,
"increasingandhigherriskdrinking": C,
"infantdeaths": E,
"leastdeprivedquintile": A,
"lessdeprivedquintile": A,
"lifeexpectancyfemale": E,
"lifeexpectancymale": E,
"longtermunemployment": A,
"mixed": D,
"moredeprivedquintile": A,
"mostdeprivedquintile": A,
"newcasesoftuberculosis": D,
"obeseadults": C,
"startingbreastfeeding": B,
"statutoryhomelessness": A,
"teenagepregnancyunder18": B,
"unknown": D,
"violentcrime": A,
"white": D,
}
