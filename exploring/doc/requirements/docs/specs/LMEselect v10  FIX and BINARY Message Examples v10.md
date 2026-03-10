# LMEselect v10  FIX and BINARY Message Examples v10

*Source: LMEselect v10  FIX and BINARY Message Examples v10.pdf*

---

Page 1
Classification: Public 
LMEselect v10 FIX and BINARY 
Message Examples 
 
Please respond to:  
Trading Operations 
tradingoperationsgroup@lme.com


---
*Page 2*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 2
The following content provides a number of example common messages for the FIX (CGW, convenience 
gateway) and BINARY (PSG) gateways.  Where content of the message is specific to the participant, square 
brackets have been used with a description of what the reader needs to place in the tag location. 
 
The examples in this document should be used in conjunction with the FIX and Binary order entry specification 
documents available on the LME.com website: https://www.lme.com/ntpdocuments


---
*Page 3*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 3
 
Contents 
1 
FIX Examples ...................................................................................................................................... 4 
1.1 
Logon message ............................................................................................................................ 4 
1.2 
Logout message ........................................................................................................................... 4 
1.3 
New Order Single (New Order Single - Limit, Day) ........................................................................ 5 
1.4 
Amend Order (New Order Single - Limit, Day) ............................................................................... 6 
1.5 
Good til Date(GTD) (New Order Single - Limit, GTD) .................................................................... 7 
1.6 
Good til Cancel(GTC) (New Order Single - Limit, GTC) ................................................................. 8 
1.7 
Mass Cancel using SECURITYID ................................................................................................. 9 
2 
BINARY Examples .............................................................................................................................10 
2.1 
Logon ..........................................................................................................................................10 
2.2 
New Order Single - Limit, Day ......................................................................................................10 
2.3 
New Order Single - Limit, Good til Cancel(GTC)...........................................................................10 
2.4 
New Order Single - Limit, Good til Cancel(GTD)...........................................................................12 
2.5 
New Order Single – Stop Limit, Good til Date(GTD) .....................................................................12 
2.6 
New Order Single – Limit order – Amending the price ..................................................................13 
2.7 
Cancel Order (Based on the Amend Order in 2.5 example) ..........................................................14 
2.8 
Mass Cancellation based on SecurityID .......................................................................................14


---
*Page 4*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 4
1 
FIX Examples 
1.1 
Logon message 
MessageType(TAG35=A) 
1.1.1 Inbound message 
8=FIXT.1.1|9=0442|35=A|34=1|52=20230131-
09:20:17.516561900|49=[SENDERCOMPID]|56=LME|98=0|108=60|789=1|1402=[ENCRYPTEDPASSWOR
D] |1137=9|10=147| 
1.1.2 Outbound execution response message 
8=FIXT.1.1|9=97|35=A|49=LME|56=[SENDERCOMPID]|34=1|52=20230131-
09:20:17.501667000|1128=9|98=0|108=60|789=2|1409=0|1137=9|10=156| 
1.2 
Logout message 
MessageType(TAG35=5) 
1.2.1 Inbound message 
8=FIXT.1.1|9=0060|35=5|34=377|52=20230131-
16:01:31.330207600|49=[SENDERCOMPID]|56=LME|10=085| 
1.2.2 Outbound execution response message 
8=FIXT.1.1|9=96|35=5|49=LME|56=[TARGETCOMPID]|34=402|52=20230131-
16:01:31.337932000|1128=9|58=Response to Logout|1409=4|10=019|


---
*Page 5*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 5
1.3 
New Order Single (New Order Single - Limit, Day) 
MessageType(TAG35=D), Order type=Limit(TAG40=2),  Side=Buy(TAG54=1), Order 
quantity=2(TAG38=2), Price=1800(TAG44), TimeInForce=Day(TAG59=0) 
1.3.1 Inbound Order message 
8=FIXT.1.1|9=0253|35=D|34=389|52=20230131-
16:25:06.174727500|49=[SENDERCOMPID]|56=LME|11=0131161931004|453=3|448=11|447=D|452=11|44
8=67821234|447=P|452=301|448=1C|447=D|452=81|581=3|48=[SECURITYID]|22=8|54=1|60=20230131-
16:25:05.096071000|38=2|40=2|44=1800|528=A|529=D|10=090| 
1.3.2 Outbound execution response message – MessageType(TAG35=8) 
8=FIXT.1.1|9=355|35=8|49=LME|56=[TARGETCOMPID]||34=448|52=20230131-
16:48:54.873335000|1128=9|37=23031010000044901|11=0131161931007|453=5|448=[PARTYID - 
EXECUTING FIRM 
MNEMONIC]|447=D|452=1|448=11|447=D|452=11|448=[TARGETCOMPID]|447=D|452=36|448=1C|447=D|
452=81|448=67821234|447=P|452=301|17=d.0.lNw3hTp0RB|150=0|39=0|581=3|48=[SECURITYID]|22=8|5
4=1|38=2|40=2|44=1800|59=0|528=A|529=D|151=2|14=0|60=20230131-16:48:54.872063000|10=135|


---
*Page 6*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 6
1.4 
Amend Order (New Order Single - Limit, Day) 
Original order message : MessageType(TAG35=D), Order type=Limit(TAG40=2),  Side=Buy(TAG54=1), 
Order quantity=2(TAG38=2), Price=1800(TAG44), TimeInForce=Day(TAG59=0) 
1.4.1 Original inbound order message 
8=FIXT.1.1|9=0235|35=D|34=3|52=20221102-
08:45:10.870309800|49=[SENDERCOMPID]|56=LME|11=1101150701006|453=3|448=11|447=D|452=11|44
8=6782|447=P|452=301|448=CLI1|447=D|452=81|581=3|48=[SECUIRTYID] |22=8|54=1|60=20221102-
08:45:09.802237000|38=2|40=2|44=1800|59=0|528=A|529=D|10=153| 
1.4.2 Original outbound execution response message – MessageType(TAG35=8) 
8=FIXT.1.1|9=350|35=8|49=LME|56=[TARGETCOMPID]|34=96|52=20230203-
09:33:48.106110000|1128=9|37=23034010000002445|11=0202153100039|453=5|448=[PARTYID - 
EXECUTING FIRM 
MNEMONIC]|447=D|452=1|448=11|447=D|452=11|448=[SENDERCOMPID]|447=D|452=36|448=CLI1|447=
D|452=81|448=6782|447=P|452=301|17=d.0.N2Yzf9U1RB|150=0|39=0|581=3|48=[SECURITYID]|22=8|54=
1|38=1|40=2|44=1800|59=0|528=A|529=D|151=1|14=0|60=20230203-09:33:48.104648000|10=036| 
Amend price order message : MessageType(TAG35=G), Order type=Limit(TAG40=2),  
Side=Buy(TAG54=1), Order quantity=2(TAG38=2), Price=1400(TAG44), TimeInForce=Day(TAG59=0) 
1.4.3 Inbound amend order message 
8=FIXT.1.1|9=0213|35=G|34=4|52=20221102-
08:45:11.870371700|49=[SENDERCOMPID]|56=LME|11=1101150701007|41=1101150701006|453=1|448=
6782|447=P|452=301|48=[SECURITYID]|22=8|54=1|60=20221102-
08:45:09.802237000|38=2|40=2|44=1400|59=0|528=P|529=D|1724=5|10=177| 
1.4.4 Outbound execution amend message – MessageType(TAG35=8) 
8=FIXT.1.1|9=374|35=8|49=LME|56=[TARGETCOMPID]|34=97|52=20230203-
09:33:49.105789000|1128=9|37=23034010000002445|11=0202153100040|41=0202153100039|453=5|448=
[PARTYID - EXECUTING FIRM 
MNEMONIC]|447=D|452=1|448=11|447=D|452=11|448=[SENDERCOMPID]|447=D|452=36|448=CLI1|447=
D|452=81|448=6782|447=P|452=301|17=d.5.pcAAAAAAAE|150=5|39=0|581=3|48=[SECURITYID]|22=8|54
=1|38=2|40=2|44=1400|59=0|528=P|529=D|151=1|14=0|60=20230203-
09:33:49.104724000|1724=5|10=139|


---
*Page 7*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 7
1.5 
Good til Date(GTD) (New Order Single - Limit, GTD) 
Message Type(TAG35=D), Order type=Limit(TAG40=2),  Side=Buy(TAG54=1), Order 
quantity=2(TAG38=2), Price=1800(TAG44), TimeInForce=Good til date(GTD)(TAG59=6), 
ExpireDate(TAG432=YYYYMMDD) 
1.5.1 Inbound order message 
8=FIXT.1.1|9=0250|35=D|34=987|52=20230207-
15:34:22.361840200|49=[SENDERCOMPID]|56=LME|11=0207114751009|453=3|448=11|447=D|452=11|44
8=6782|447=P|452=301|448=1C|447=D|452=81|581=3|48=13746|22=8|54=1|60=20230207-
15:34:21.314471000|38=2|40=2|44=1800|59=6|528=A|529=D|432=20230621|10=119| 
1.5.2 Outbound execution response message – MessageType(TAG35=8) 
8=FIXT.1.1|9=363|35=8|49=LME|56=[TARGETCOMPID]|34=1941|52=20230207-
15:34:22.350851000|1128=9|37=23038010000001951|11=0207114751009|453=5|448=[PARTYID - 
EXECUTING FIRM 
MNEMONIC]|447=D|452=1|448=11|447=D|452=11|448=[SENDERCOMPID]|447=D|452=36|448=1C|447=D|
452=81|448=6782|447=P|452=301|17=c.0.fucYyKP2RB|150=0|39=0|581=3|48=13746|22=8|54=1|38=2|40=
2|44=1800|59=6|432=20230621|528=A|529=D|151=5|14=0|60=20230207-15:34:22.349827000|10=250|


---
*Page 8*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 8
1.6 
Good til Cancel(GTC) (New Order Single - Limit, GTC) 
Message Type(TAG35=D), Order type=Limit(TAG40=2),  Side=Buy(TAG54=1), Order 
quantity=2(TAG38=2), Price=1800(TAG44), TimeInForce=Good til Cancel(GTC)(TAG59=1) 
1.6.1 Inbound order message 
8=FIXT.1.1|9=0236|35=D|34=1039|52=20230207-
16:27:10.732660300|49=[SENDERCOMPID]|56=LME|11=0207162517006|453=3|448=11|447=D|452=11|44
8=6782|447=P|452=301|448=1C|447=D|452=81|581=3|48=[SECURITYID]|22=8|54=1|60=20230207-
16:27:09.658868000|38=2|40=2|44=1800|59=1|528=A|529=D|10=242| 
1.6.2 Outbound execution response message – MessageType(TAG35=8) 
8=FIXT.1.1|9=348|35=8|49=LME|56=[TARGETCOMPID]|34=2002|52=20230207-
16:27:10.737183000|1128=9|37=23038010000001954|11=0207162517006|453=5|448=[PARTYID - 
EXECUTING FIRM 
MNEMONIC]|447=D|452=1|448=11|447=D|452=11|448=[SENDERCOMPID]|447=D|452=36|448=1C|447=D|
452=81|448=6782|447=P|452=301|17=c.0.iucYyKP2RB|150=0|39=0|581=3|48=[SECURITYID]|22=8|54=1|3
8=2|40=2|44=1800|59=1|528=A|529=D|151=2|14=0|60=20230207-16:27:10.735546000|10=042|


---
*Page 9*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 9
1.7 
Mass Cancel using SECURITYID 
Message Type(TAG35=q), SecurityID(TAG48=[the securityID of the instrument you wish to cancel]) 
1.7.1 Inbound message 
8=FIXT.1.1|9=82|35=q|49=[SENDERCOMPID]|56=LME|34=2|52=20191119-
07:33:05|11=18|530=1|48=[SECURITYID]|22=8|60=20181022-09:38:06.057|10=252 
1.7.2 Outbound execution response message – MessageType(TAG35=r) 
8=FIXT.1.1|9=169|35=r|49=LME|56=[TARGETCOMPID]|34=6|52=20230202-
07:45:52.981108000|1128=9|11=0131161931016|1369=3023033510268435457|530=1|531=1|533=0|48=[S
ECURITYID]|22=8|60=20230202-07:45:52.980997000|10=233|


---
*Page 10*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 10
2 
BINARY Examples 
2.1 
Logon 
Message Type(3=5), 
2.1.1 Inbound message 
header{1=2|2=532|3=5|4=1|5=0|6=0|7=[COMPID]|8=1675949239234372000|9=0|}body{0=[PASSWORD]|2
=1|3=0|4=60|} 
2.1.2 Outbound execution report 
header{1=2|2=82|3=5|4=239|5=0|6=0|7=[COMPID]|8=20230210 
15:55:36.917251000|9=0|}body{2=203|3=0|4=60|} 
 
2.2 
New Order Single - Limit, Day 
Message Type(3=12), Side(6=1 Buy), Order Quantity(7=2), Order Type(8=2 Limit), Order 
Price(9=18000000000), TimeinForce(10=0 Day),  
2.2.1 Inbound message 
header{1=2|2=192|3=12|4=8|5=0|6=0|7=[COMPID]|8=1675856334806614000|9=0|} 
body{0=0207162517015|4=[SECURITYID]|5=1675856334681533000|6=1|7=2|8=2|9=1800000000|10=0|11
=D|12=A|13=3|19=111|26=222|30=1C|} 
2.2.2 Outbound execution response message – MessageType(3=8) 
Message Type(3=8) 
header{1=2|2=247|3=8|4=12|5=0|6=0|7=ADM002|8=20230208 11:38:55.138982000|9=0|} 
body{0=0207162517015|2=23039010000000993|4=[SECURITYID]|5=20230208 
11:38:55.137496000|6=1|7=2|8=2|9=1800000000|10=0|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|40=N|65=U.0.hftBHud2RB|67=0|68=0|69=[ENTERING TRADER]|80=0|81=2|} 
 
2.3 
New Order Single - Limit, Good til Cancel(GTC) 
Message Type(3=12), Side(6=1 Buy), Order Quantity(7=2), Order Type(8=2 Limit), Order 
Price(9=18000000000), TimeinForce(10=1 GTC) 
2.3.1 Inbound message 
header{1=2|2=192|3=12|4=8|5=0|6=0|7=[COMPID]|8=1675856334806614000|9=0|} 
body{0=0207162517015|4=[SECURITYID]|5=1675856334681533000|6=1|7=2|8=2|9=1800000000|10=1|11
=D|12=A|13=3|19=111|26=222|30=1C|} 
Message Type(3=8) 
2.3.2 Outbound execution response message – MessageType(3=8) 
header{1=2|2=247|3=8|4=12|5=0|6=0|7=ADM002|8=20230208 11:38:55.138982000|9=0|} 
body{0=0207162517015|2=23039010000000993|4=[SECURITYID]|5=20230208 
11:38:55.137496000|6=1|7=2|8=2|9=1800000000|10=1|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|40=N|65=U.0.hftBHud2RB|67=0|68=0|69=[ENTERING TRADER]|80=0|81=2|}


---
*Page 11*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 11


---
*Page 12*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 12
2.4 
New Order Single - Limit, Good til Cancel(GTD) 
Message Type(3=12), Side(6=1 Buy), Order Quantity(7=2), Order Type(8=2 Limit), Order 
Price(9=18000000000), TimeinForce(10=6 GTD) 
2.4.1 Inbound message 
header{1=2|2=192|3=12|4=8|5=0|6=0|7=[COMPID]|8=1675856334806614000|9=0|} 
body{0=0207162517015|4=[SECURITYID]|5=1675856334681533000|6=1|7=2|8=2|9=1800000000|10=6|11
=D|12=A|13=3|19=111|26=222|30=1C|34=[EXPIRY DATE YYYYMMDD]|} 
2.4.2 Outbound execution response message = MessageType(3=8) 
header{1=2|2=247|3=8|4=12|5=0|6=0|7=ADM002|8=20230208 11:38:55.138982000|9=0|} 
body{0=0207162517015|2=23039010000000993|4=[SECURITYID]|5=20230208 
11:38:55.137496000|6=1|7=2|8=2|9=1800000000|10=6|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|34=[EXPIRY DATE 
YYYYMMDD]|40=N|65=U.0.hftBHud2RB|67=0|68=0|69=[ENTERING TRADER]|80=0|81=2|} 
 
2.5 
New Order Single – Stop Limit, Good til Date(GTD) 
Message Type(3=12), Side(6=1 Buy), Order Quantity(7=2), Order Type(8=4 Stop Limit), Order 
Price(9=20100000000), TimeinForce(10=6 GTD), Expiry Date(34=YYYYMMDD), Trigger Price 
Type(35=2000000000), (36=4 Best Bid or Last Trade), Trigger Type(37=4 Price Movement) 
2.5.1 Inbound message 
header{1=2|2=206|3=12|4=24|5=0|6=0|7=[COMPID]|8=1675931912237216000|9=0|} 
body{0=0207162517043|4=[SECURITYID]|5=1675856334681533000|6=1|7=2|8=4|9=2010000000|10=6|11
=D|12=A|13=3|19=111|26=222|30=1C|34=20230604|35=2000000000|36=4|37=4|} 
2.5.2 Outbound execution response message = MessageType(3=8) 
header{1=2|2=261|3=8|4=34|5=0|6=0|7=[COMPID]|8=20230209 08:38:32.408301000|9=0|} 
body{0=0207162517043|2=23040010000001017|4=13746|5=20230209 
08:38:32.406376000|6=1|7=2|8=4|9=2010000000|10=6|11=D|12=A|13=3|14=[EXECUTING FIRM] 
|19=111|26=222|30=1C|34=[EXPIRY DATE 
YYYYMMDD]|35=2000000000|36=4|37=4|40=N|65=U.0.5f+qbRs2RB|67=0|68=0|69=[ENTERING 
TRADER]||80=0|81=2|}


---
*Page 13*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 13
2.6 
New Order Single – Limit order – Amending the price 
Message Type(3=12), Client Order ID(0=0207162517065e)Side(6=1 Buy), Order Quantity(7=20), Order 
Type(8=2 Limit), Order Price(9=2020000000), TimeInForce(10=0 Day) 
2.6.1 Original order inbound message 
header{1=2|2=192|3=12|4=298|5=0|6=0|7=[COMPID]|8=1675943022275394000|9=0|}body{0=02071625170
65e|4=[SECURITYID]|5=1675856334681533000|6=1|7=20|8=2|9=2020000000|10=0|11=D|12=A|13=3|19=1
11|26=222|30=1C|} 
2.6.2 Original order outbound execution report – MessageType(3=8) 
header{1=2|2=247|3=8|4=362|5=0|6=0|7=[COMPID]|8=20230209 
11:43:42.266379000|9=0|}body{0=0207162517065e|2=23040010000001301|4=[SECURITYID]|5=20230209 
11:43:42.263978000|6=1|7=20|8=2|9=2020000000|10=0|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|40=N|65=U.0.Vk+qbRs2RB|67=0|68=0|69=[ENTERING 
TRADER]||80=0|81=20|} 
2.6.3 Amend order inbound message 
Message Type(3=13), Client Order ID(0=0207162517066e), Original Client Order 
ID(3=0207162517065e) Side(6=1 Buy), Order Quantity(7=20), Order Type(8=2 Limit), Order 
Price(9=2020000000), TimeInForce(10=0 Day) 
header{1=2|2=211|3=13|4=299|5=0|6=0|7=ADM002|8=1675943022275394000|9=0|}body{0=020716251706
6e|3=0207162517065e|4=[SECURITYID]|5=1675856334681533000|6=1|7=20|8=2|9=2000000000|10=0|11
=D|12=A|13=3|19=111|26=222|30=1C|} 
2.6.4 Amend order outbound execution report – MessageType(3=8) 
header{1=2|2=266|3=8|4=363|5=0|6=0|7=[COMPID]8=20230209 
11:43:42.268205000|9=0|}body{0=0207162517066e|2=23040010000001301|3=0207162517065e|4=[SECU
RITYID]5=20230209 
11:43:42.266453000|6=1|7=20|8=2|9=2000000000|10=0|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|40=N|65=U.5.QMAAAAAAAEI|67=5|68=0|69=[EXECUTING 
TRADER]|80=0|81=20|}


---
*Page 14*

LMEselect v10 FIX and BINARY Message Examples
Version 1.0
 
 
Page 14
2.7 
Cancel Order (Based on the Amend Order in 2.5 example) 
Message Type(3=15), Client Order ID(0=0207162517067e), Original Client Order 
ID(3=0207162517066e) 
2.7.1 Inbound order cancel message 
header{1=2|2=128|3=15|4=314|5=0|6=0|7=[COMPID]|8=1675943482869734000|9=0|}body{0=02071625170
67e|3=0207162517066e|4=[SECURITYID]|5=1675856334681533000|6=1|} 
2.7.2 Outbound cancel execution report – MessageType(3=8) 
header{1=2|2=266|3=8|4=381|5=0|6=0|7=[COMPID]|8=20230209 
11:51:22.858252000|9=0|}body{0=0207162517067e|2=23040010000001301|3=0207162517066e|4=[SECU
RITYID]|5=20230209 
11:51:22.856804000|6=1|7=20|8=2|9=2000000000|10=0|11=D|12=A|13=3|14=[EXECUTING 
FIRM]|19=111|26=222|30=1C|40=N|65=U.4.Vk+qbRs2RB|67=4|68=4|69=[EXECUTING 
TRADER]|80=0|81=0|} 
 
2.8 
Mass Cancellation based on SecurityID 
Message Type(3=17) 
2.8.1 Inbound mass cancellation message 
header{1=2|2=110|3=17|4=79|5=0|6=0|7=[COMPID]|8=1676037223742060000|9=0|}body{0=020716251705
7|2=1|3=1|5=1676037223707053000|10=[SECURITYID]|} 
Execution reports = A proportionate number of execution reports will be received based on the orders place 
and cancelled against the SECUIRTYID.  In the mass cancellation execution report BP 6 indicates the 
number cancelled, in this example, 7 orders against the SECURITYID specified. 
2.8.2 Outbound mass cancellation execution report 
Message Type(3=18) 
 
header{1=2|2=136|3=18|4=115|5=0|6=0|7=ADM002|8=20230210 
13:53:43.738513000|9=0|}body{0=0207162517057|1=3023041010268435465|2=1|3=1|4=1|5=20230210 
13:53:43.738246000|6=7|10=13746|}
