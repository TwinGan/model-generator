# Order Entry Gateway FIX Specification v 1 9 1

*Source: Order Entry Gateway FIX Specification v 1 9 1.pdf*

---

THE LONDON METAL EXCHANGE 
10 Finsbury Square, London EC2A 1AJ | Tel +44 (0)20 7113 8888 
Registered in England no 2128666. Registered office as above.  
LME.COM 
 
 
Order Entry Gateway 
FIX Specification 
Please respond to:  
tradingoperations@lme.com


---
*Page 2*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 2 
 
 
Table of Contents 
1 Session Management ................................................................................................................... 11 
1.1 
Authentication ...................................................................................................................... 11 
1.1.1 
Comp ID ....................................................................................................................... 11 
1.1.2 
Password Encryption ................................................................................................... 11 
1.1.3 
Password ..................................................................................................................... 12 
1.1.4 
Change Password ....................................................................................................... 12 
1.2 
Establishing a FIX Session .................................................................................................. 13 
1.3 
Message Sequence Numbers ............................................................................................. 13 
1.4 
Heartbeat and Test Request ............................................................................................... 14 
1.5 
Terminating a FIX Session .................................................................................................. 14 
1.6 
Re-establishing a FIX Session ............................................................................................ 14 
1.7 
Sequence Reset .................................................................................................................. 14 
1.8 
Fault Tolerance .................................................................................................................... 15 
1.9 
Checksum Validation ........................................................................................................... 15 
2 Recovery ....................................................................................................................................... 16 
2.1 
General Message Recovery ................................................................................................ 16 
2.2 
Resend Request .................................................................................................................. 16 
2.3 
Logon Message Processing – Next Expected Message Sequence .................................... 17 
2.4 
Possible Duplicates ............................................................................................................. 17 
2.5 
Possible Resends ................................................................................................................ 17 
2.6 
Gap Fills ............................................................................................................................... 17 
2.7 
Transmission of Missed Messages ..................................................................................... 18 
2.8 
Technical Halt ...................................................................................................................... 18 
3 Service Description ...................................................................................................................... 19 
3.1 
Security Identification ........................................................................................................... 19 
3.2 
Security Creation ................................................................................................................. 19 
3.2.1 
Strategies ..................................................................................................................... 19 
3.3 
Order Submission ................................................................................................................ 21 
3.4 
Order Types ......................................................................................................................... 21 
3.5 
Order Validity Conditions ..................................................................................................... 23 
3.6 
Order Types and Permitted Order Validity Conditions ........................................................ 23 
3.7 
Order Identification .............................................................................................................. 24


---
*Page 3*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 3 
 
 
3.8 
Order Expiry ......................................................................................................................... 24 
3.9 
Order Restatement .............................................................................................................. 24 
3.10 
Order Amendment ............................................................................................................... 25 
3.11 
Order Cancellation ............................................................................................................... 26 
3.12 
Mass Cancellation ............................................................................................................... 26 
3.13 
Cancel on Disconnect .......................................................................................................... 27 
3.14 
Auto Cross ........................................................................................................................... 27 
3.15 
Request for Quote (RFQ) .................................................................................................... 34 
3.16 
Speed Bumps ...................................................................................................................... 34 
3.17 
Message Throttling .............................................................................................................. 42 
3.18 
Security Definition Throttle .................................................................................................. 42 
3.19 
Merged Order Books ........................................................................................................... 42 
3.20 
Self Execution Prevention (SEP) ......................................................................................... 45 
3.21 
Inflight Order Processing ..................................................................................................... 46 
3.22 
Trade Reporting ................................................................................................................... 47 
3.23 
Order Attribute Type Usage ................................................................................................. 47 
4 Message Definitions ..................................................................................................................... 49 
4.1 
Supported Messages ........................................................................................................... 49 
4.2 
Inbound Messages .............................................................................................................. 50 
4.3 
Outbound Messages ............................................................................................................ 51 
4.4 
Data Types .......................................................................................................................... 51 
4.5 
Required Fields .................................................................................................................... 52 
4.6 
Message Header ................................................................................................................. 53 
4.7 
Message Trailer ................................................................................................................... 54 
4.8 
Administrative Messages ..................................................................................................... 54 
4.8.1 
Logon (A) ..................................................................................................................... 54 
4.8.2 
Heartbeat (0) ................................................................................................................ 56 
4.8.3 
Test Request (1) .......................................................................................................... 56 
4.8.4 
Resend Request (2) ..................................................................................................... 56 
4.8.5 
Sequence Reset (4) ..................................................................................................... 60 
4.8.6 
Logout (5) .................................................................................................................... 60 
4.8.7 
Reject (3) ..................................................................................................................... 61 
4.9 
Other Messages .................................................................................................................. 62


---
*Page 4*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 4 
 
 
4.9.1 
Business Message Reject (j) ....................................................................................... 62 
4.9.2 
News (B) ...................................................................................................................... 62 
4.10 
Parties Component Block .................................................................................................... 64 
4.10.1 
PartyRole Usage .......................................................................................................... 66 
4.11 
Application Messages .......................................................................................................... 71 
4.11.1 
Security Definition Request (c) .................................................................................... 71 
4.11.2 
Security Definition (d) .................................................................................................. 74 
4.11.3 
New Order Single (D) .................................................................................................. 77 
4.11.4 
New Order Cross (s) .................................................................................................... 83 
4.11.5 
Order Cancel Replace Request (G) ............................................................................ 88 
4.11.6 
Order Cancel Request (F) ........................................................................................... 95 
4.11.7 
Order Cancel Reject (9) ............................................................................................... 96 
4.11.8 
Cross Order Cancel Request (u) ................................................................................. 98 
4.11.9 
Execution Report (8) .................................................................................................. 100 
4.11.10 
Order Mass Cancel Request (q) ............................................................................ 126 
4.11.11 
Order Mass Cancel Report (r) ............................................................................... 128 
4.11.12 
Quote Request (R) ................................................................................................. 130 
4.11.13 
Quote Response (AJ) ............................................................................................ 132 
4.11.14 
Quote Request Reject (AG) ................................................................................... 133 
Appendix A: 
Inflight Order Handling ........................................................................................ 136 
A.1 
Standard Gateway Behaviour ............................................................................................ 136 
A.2 
Inflight Cancellation ........................................................................................................... 136 
A.3 
Inflight Amendment ............................................................................................................ 137 
A.4 
Inflight Amendment and Cancellation ................................................................................ 138 
A.5 
Multiple Inflight Amendments and a Cancellation ............................................................. 139 
A.6 
Multiple Inflight Amendments and Cancellations ............................................................... 140 
Appendix B: 
Speed Bump Inflight Order Handling ................................................................ 143 
B.1 
Speed Bump Message Flow .............................................................................................. 143 
B.2 
Inflight Cancellation in Speed Bump .................................................................................. 144 
B.3 
Inflight Cancellation past Speed Bump .............................................................................. 144 
B.4 
Inflight Amendment Speed Bumped .................................................................................. 145 
B.5 
Inflight Amendment not Speed Bumped ............................................................................ 146


---
*Page 5*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 5 
 
 
Document History 
Version 
Date 
Change Description 
1.0 
31/12/2019 
Initial draft 
1.1 
09/04/2020 
Updated following internal review 
1.2 
28/01/2022 
Internal updates 
1.3 
24/03/2023 
Internal review 
1.4 
23/06/2023 
RelatedHighPrice (1819) and RelatedLowPrice (1820) added to Order 
Cancel Reject (9)  
4.11.7 added example message flow for Order rejected price limits 
breached. References to Market to Limit in message flow examples 
corrected to Market. RelatedHighPrice (1819) description includes Stop 
order handling 
4.11.7.1 RelatedHighPrice (1819) and RelatedLowPrice (1820) 
conditional for Order Cancelled (Unsolicited) 
1.5 
13/10/2023 
1.1.2 password encryption example added 
3.2.1 strategy creation clarified 
4.4 timestamp precision 
4.8.7 and 4.9.1 Text (58) is conditionally required if reject reason is Other 
4.10.1 301 description 
4.11.1 LegRatioQty (632) description and message flow examples 
4.11.4 message description and party block 
1.6 
15/03/2024 
1.1.4.1 password reuse policy 
1.2 duplicate connection termination removed 
3.4 Stop Market and Stop Limit description 
3.6.1 EncryptedPassword (1402) and EncryptedNewPassword (1404) 
length 450 
3.9, 3.10 and 4.11.4 restated triggered Stop orders change order type 
3.10 and 4.11.4 amendment of attributes and party details 
3.12 and 3.18 cancellation by tradable instrument 
4.10.1 LEI usage 
4.11.6 OrdStatus description


---
*Page 6*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 6 
 
 
Version 
Date 
Change Description 
4.11.7 OrderOrgination (1724) data type Int, ExecType (150) = ‘E’ 
Pending Replace returned in speedbump order handling 
4.11.7.1 Restated, footnote added for triggered Stops. Triggered, 
mandatory tags. Rejections, Clearing Firm removed 
1.7 
19/07/2024 
1.1.2 public key location 
3.8 expiry conditions 
4.4 added String data type 
4.8.7 and 4.9.1 Text (58) optional 
4.10.1 PartyID format where Alphanumeric changed to String 
4.11.7 ExpireDate (432) description 
1.7.1 
09/08/2024 
1.1.1 TargetCompID (56) for Production environment 
1.7.2 
16/09/2024 
2.8 Technical Halt 
1.8 
29/10/2024 
2.8 Technical Halt 
4.4 String data type 
4.11.7.1 replaced P with C 
1.8.1 
04/02/2025 
4.4 special character usage 
1.8.2 
17/05/2025 
4.10.1 Guidance for population of: 
a) ClientID where PartyIDsource = P Client Short Code 
b) Decision Maker  
c) Investment Decision within Firm (IDM) and Investment Decision 
Country 
d) Execution Within Firm and Execution Decision Country 
e) Client Branch Country 
f) Regulatory references 
4.11.3 Regulatory references  
4.11.4 Party block amendment guidance, and regulatory references 
4.11.7 Regulatory references 
1.9.0 
09/09/2025 
3.3 Note to include Cross Orders 
3.7 Note to include Cross Orders  
3.11 Note to include Cross Orders  
3.14 Auto Cross description


---
*Page 7*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 7 
 
 
Version 
Date 
Change Description 
4.1 New Order Cross and Cross Order Cancel Request added to 
Supported Messages 
4.2 New Order Cross and Cross Order Cancel Request added to 
Inbound Messages 
4.11.4 New Order Cross message 
4.11.8 Cross Order Cancel Request message 
4.11.9 Cross Order related fields added to the Execution Report 
4.11.9.1 Cross Order related fields added to the Execution Report Matrix 
1.9.01 
22/10/2025 
4.11.7 Updated the description to include Cross Order Cancel Request   
and added a new enum to tag 434  
4.9.1 Added a new enum to tag 380 for Cross order volume mismatch 
3.7 Optional cross cancel attributes clarified 
3.10 Optional cross cancel attributes clarified and updated the number of 
messages returned 
3.13 Optional cross cancel attributes clarified 
Updated some example flows 
4.11.8 Clarified the number of messages returned  
4.11.10 Updated to include Cross orders 
4.9.1 Removed ‘Cross order volume mismatch enum from tag 380 
4.11.9 Updated to include cross processing 
1.9.1  
02/12/2025 
4.11.9 Updated tag 548 to include conditional reason


---
*Page 8*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 8 
 
 
Preface 
This document describes the LME implementation of the FIX protocol based on FIX 5.0 SP2 
Specification with relevant extension packs. 
The document assumes the reader has an understanding of the FIX protocol, see 
http://www.fixprotocol.org/. 
This document should be read in conjunction with related materials on LME.com for LMEselect v10. 
Delivery Phasing 
This document covers all the functionality available in LMEselect 10 however functionality will be 
delivered in phased releases.  
Functionality that will be included in a later release is specified in the following table and shown 
throughout the document in dark grey italics. The initial release will contain all functionality that is not 
specified in the table. 
Function 
Reference 
Futures strategies: 
• 
3 Month Average 
• 
6 Month Average 
• 
12 Month Average 
• 
Carry Average 
3.2.1.1 Exchange Defined Strategy Types 
4.11.1 Security Definition Request (c) 
Options strategies: 
• 
Call spread 
• 
Put spread 
3.2.1.1 Exchange Defined Strategy Types 
4.11.1 Security Definition Request (c) 
Custom strategies 
3.2.1 Strategies 
3.2.1.2 Custom Strategies 
4.11.1 Security Definition Request (c) 
4.11.2 Security Definition (d) (Example Message Flows) 
4.11.7.1 Execution Report (8) (Example Message Flows) 
Option contracts 
3.2 Security Creation 
3.2.1.1 Exchange Defined Strategy Types 
3.2.1.2 Custom Strategies 
4.11.1 Security Definition Request (c) 
4.11.2 Security Definition (d) (Example Message Flows) 
Order types: 
• 
Market 
3.4 Order Types 
3.6 Order Types and Permitted Order Validity Conditions


---
*Page 9*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 9 
 
 
Function 
Reference 
• 
Stop Market 
• 
Iceberg 
• 
Post Only 
• 
One Cancels Other 
3.10 Order Amendment (DisplayQty) 
4.11.3 New Order Single (D) 
4.11.4 Order Cancel Replace Request (G) 
4.11.7 Execution Report (8) 
4.11.7.1 Execution Report Matrix 
Order validity condition: 
• 
Fill or Kill (FOK) 
3.5 Order Validity Conditions 
3.6 Order Types and Permitted Order Validity Conditions 
4.11.3 New Order Single (D) 
4.11.4 Order Cancel Replace Request (G) 
4.11.7 Execution Report (8) 
Request for Cross 
4.11.4 New Order Cross (s) 
4.11.8 Cross Order Cancel Request (u) 
4.11.9 Execution Report (8) 
Request for Quote 
3.14 Request for Quote (RFQ) 
3.16 Message Throttling 
4.1 Supported Messages 
4.2 Inbound Messages 
4.3 Outbound Messages 
4.10.11 Quote Request (R) 
4.11.11 Quote Response (AJ) 
4.11.12 Quote Request Reject (AG) 
Speed Bumps 
3.15 Speed Bumps 
4.11.7 Execution Report (8) 
4.11.7.1 Execution Report Matrix 
Appendix B: Speed Bump Inflight Order Handling 
Self Execution Prevention 
3.19 Self Execution Prevention (SEP) 
4.11.3 New Order Single (D) 
4.11.7 Execution Report (8) 
4.11.7.1 Execution Report Matrix


---
*Page 10*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 10


---
*Page 11*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 11 
 
 
1 
Session Management 
1.1 Authentication 
1.1.1 
Comp ID 
A FIX session is established by sending a Logon (35=A) request which includes the sender and the 
target in the Message Header: 
• 
SenderCompID (49) – the party initiating the session. 
• 
TargetCompID (56) – the acceptor of the session as per configuration. 
For messages sent to the Exchange, the client should use the session CompID allocated by the 
Exchange to populate SenderCompID (49). A single client may have multiple connections to the 
gateway i.e. multiple FIX sessions, each with its own Comp ID. 
The TargetCompID (56) in messages sent to the Exchange is environment specific as follows: 
Production:  
• 
CGLME 
Member Test environments: 
• 
LMEMTA 
• 
LMEMTB 
1.1.2 
Password Encryption 
The client should specify their password in EncryptedPassword (1402) in the Logon request.  
To encrypt the password, the client is expected to use a 2048-bit RSA 
(http://en.wikipedia.org/wiki/RSA_(algorithm)) public key circulated by the Exchange on 
https://www.lme.com/Trading/Systems/LMEselect. The binary output of the RSA encryption must be 
represented in Big Endian PKCS #1 with padding scheme OAEP 
(https://en.wikipedia.org/wiki/PKCS_1) and then converted to an alphanumeric value by means of 
standard base-64 encoding (http://en.wikipedia.org/wiki/Base64) when communicating with the 
gateway.  
Password encryption example: 
public static String encrypt(String value) throws CrytographyException { 
try { 
Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-1AndMGF1Padding"); 
cipher.init(Cipher.ENCRYPT_MODE, publicKey); 
byte [] bytes = cipher.doFinal(value.getBytes()); 
return Base64.getEncoder().encodeToString(bytes); 
} catch (NoSuchAlgorithmException | NoSuchPaddingException | 
InvalidKeyException | IllegalBlockSizeException | BadPaddingException e) { 
throw new CrytographyException(e.getMessage()); 
} 
} 
…….


---
*Page 12*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 12 
 
 
 
String pubKey = new String(keyBytes, "UTF-8"); 
 
pubKey = pubKey.replaceAll("(-+BEGIN PUBLIC KEY-+\\r?\\n|-+END PUBLIC KEY-
+\\r?\\n?)", ""); 
 
pubKey = pubKey.replaceAll("(-+BEGIN RSA PUBLIC KEY-+\\r?\\n|-+END RSA 
PUBLIC KEY-+\\r?\\n?)", ""); 
 
pubKey = pubKey.replaceAll("\\n|\\r",""); 
 
KeyFactory keyFactory = KeyFactory.getInstance("RSA"); 
 
X509EncodedKeySpec keySpec = new 
X509EncodedKeySpec(Base64.getDecoder().decode(pubKey.getBytes())); 
 
publicKey = keyFactory.generatePublic(keySpec); 
1.1.3 
Password 
The gateway authenticates the participant’s Logon (35=A) request and sends a Logon (35=A) 
response containing SessionStatus (1409) which indicates whether the logon attempt was successful 
or not. 
Repeated failures in password validation will result in the client account being locked. The participant 
is expected to contact the Exchange to unlock the client account. 
1.1.4 
Change Password 
Each new Comp ID will be assigned a password by the Exchange. The client is expected to change 
this password upon initial logon. 
A password change can be made in a Logon (35=A) request. The client should specify the new 
encrypted password in EncryptedNewPassword (1404) and the current encrypted password in 
EncryptedPassword (1402).  
The new password must comply with Exchange’s password policy. The status of the new password 
(i.e. whether it is accepted or rejected) will be specified in the SessionStatus (1409) response from 
the gateway. The new password, if accepted, will be effective for subsequent logins. 
1.1.4.1 Password Policy 
The Exchange requires the password to contain: 
• 
Minimum of 8 characters 
• 
At least one number 
• 
Combination of uppercase and lowercase characters. 
Password history is retained and therefore the last 24 passwords cannot be reused.


---
*Page 13*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 13 
 
 
1.2 Establishing a FIX Session 
The client must wait for a successful Logon response before sending additional messages. If 
additional messages are received from the client before the exchange of Logon messages, the 
TCP/IP connection with the client will be disconnected. 
If a Logon (35=A) attempt fails for the following reasons, the gateway will send a Logout (35=5) or a 
Reject (35=3) and then terminate the session:  
• 
Password failure 
• 
Comp ID is locked 
• 
Logon is not permitted during this time 
For all other reasons, including the following, the gateway will terminate the session without sending 
a Logout or Reject: 
• 
Invalid Comp ID 
Inbound message sequence number will not be incremented if the connection is abruptly terminated 
due to the logon failure.  
If a session level failure occurs due to a message sent by the client which contains a sequence 
number that is less than what is expected and the PossDup (43) is not set to Y = Yes, then the 
gateway will send a Logout (35=5) and terminate the FIX session. In this scenario the inbound 
sequence number will not be incremented. 
1.3 Message Sequence Numbers 
As outlined in the FIX protocol, the client and gateway will each maintain a separate and independent 
set of incoming and outgoing message sequence numbers. Sequence numbers should be initialized 
to 1 (one) at the start of the day and be incremented throughout the session. Either side of a FIX 
session will track the: 
• 
NextExpectedMsgSeqNum (789) (starting at 1) in Logon (35=A) 
• 
MsgSeqNum (34) in the Message Header (starting at 1); with respect to the contra-party. 
The MsgSeqNum (34) in the Message Header is always incremented by the sender, whereas the 
NextExpectedMsgSeqNum (789) is only updated as a result of an incoming message. 
Monitoring sequence numbers will enable parties to identify and react to missed messages and to 
gracefully synchronize applications when reconnecting during a FIX session. 
Any message sent by either side of a FIX session will increment the sequence number unless 
explicitly specified for a given message type.  
If any message sent by one side of a FIX session contains a sequence number that is LESS than the 
NextExpectedMsgSeqNum (789) then the other side of this session is expected to send a Logout 
message and terminate the FIX connection immediately, unless the PossDup flag is set to Y = Yes 
A FIX session will not be continued to the next trading day. Both sides are expected to initialize (reset 
to 1) the sequence numbers at the start of each day.  At the start of each trading day if the client 
starts with a NextExpectedMsgSeqNum (789) greater than 1 then the gateway will send a Logout 
message and terminate the session immediately without any further exchange of messages.


---
*Page 14*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 14 
 
 
1.4 Heartbeat and Test Request 
The client and the gateway will use the Heartbeat (35=0) message to monitor the communication line 
during periods of inactivity and to verify that the interfaces at each end are available.  
The gateway will send a Heartbeat anytime it has not transmitted a message for the heartbeat 
interval. The client is expected to employ the same logic. 
If the gateway detects inactivity for a period longer than 3 heartbeat intervals, it will send a Test 
Request message to force a Heartbeat from the client. If a response to the Test Request (35=1) is 
not received within a reasonable transmission time (recommended being an elapsed time equivalent 
to 3 heartbeat intervals), the gateway will send a Logout (35=5) and break the TCP/IP connection 
with the client. The client is expected to employ similar logic if inactivity is detected on the part of the 
gateway. 
1.5 Terminating a FIX Session 
Session termination can be initiated by either the gateway or the client by sending a Logout (35=5). 
Upon receiving the Logout request, the contra party will respond with a Logout message signifying a 
Logout reply. Upon receiving the Logout reply, the receiving party will terminate the connection. 
If the contra-party does not reply with either a Resend Request or a Logout reply, the Logout initiator 
should wait for 60 seconds prior to terminating the connection.  
The client is expected to terminate each FIX connection at the end of each trading day before the 
gateway is shut down. Any open FIX connections will be terminated by the gateway sending a Logout 
when the service is shut down. Under exceptional circumstances, for example, a slow consumer, the 
gateway may initiate the termination of a connection during the trading day by sending a Logout. 
If, during the exchange of Logout messages, the client or the gateway detects a sequence gap, it 
should send a Resend Request. 
1.6 Re-establishing a FIX Session 
If a FIX connection is terminated during the trading day it may be re-established via an exchange of 
Logon messages. 
Once the FIX session is re-established, the message sequence numbers will continue from the last 
message successfully transmitted prior to the termination as described in 2.7 Transmission of Missed 
Messages.  
1.7 Sequence Reset 
Gap-fill mode can be used by one side when skipping session level messages which can be ignored 
by the other side.  
During a FIX session the gateway or the client may use the Sequence Reset (35=4) message in Gap 
Fill mode if either side wishes to increase the expected incoming sequence number of the other 
party. 
It will not be possible to reset the client sequence number to 1 using the Logon message. Should a 
reset be required the participant should contact the Exchange.


---
*Page 15*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 15 
 
 
The client is required to support a manual request by Exchange to initialize sequence numbers prior 
to the next login attempt. 
1.8 Fault Tolerance 
After a failure on client side or on gateway side, the client is expected to be able to continue the 
same session. 
If the sequence number is reset to 1 by the gateway, all previous messages will not be available for 
the client side. 
The client and the gateway are expected to negotiate on the NextExpectedMsgSeqNum (789) and 
Next To Be Received Sequence number by contacting the Exchange prior to initiating the new 
session and consequently manually setting the sequence number for both ends after having a direct 
communication with the participant. 
1.9 Checksum Validation 
The gateway performs a checksum validation on all incoming messages into the input services. 
Incoming messages that fail the checksum validation will be rejected and the connection will be 
dropped by the gateway without sending a logout. 
Conversely, in case of a checksum validation failure, the client is expected to drop the connection 
and take any appropriate action before reconnecting.  
Messages that fail the checksum validation should not be processed.


---
*Page 16*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 16 
 
 
2 
Recovery 
2.1 General Message Recovery 
Message gaps may occur which are detected via the tracking of incoming sequence numbers. 
Recovery will be initiated if a gap is identified when an incoming message sequence number is found 
to be greater than NextExpectedMsgSeqNum (789) during Logon or the MsgSeqNum (34) at other 
times. 
The Resend Request will indicate the BeginSeqNo (7) and EndSeqNo (16) of the message gap 
identified and when replying to a Resend Request, the messages are expected to be sent strictly 
honouring the sequence. 
If messages are received outside of the BeginSeqNo and EndSeqNo, then the recovering party is 
expected to queue those messages until the gap is recovered. 
During the message recovery process, the recovering party will increment the Next Expected 
Sequence number accordingly based on the messages received. If messages applicable to the 
message gap are received out of sequence then the recovering party will drop these messages. 
The party requesting the Resend Request can specify “0” in the EndSeqNo to indicate that they 
expect the sender to send ALL messages starting from the BeginSeqNo.In this scenario, if the 
recovering party receives messages with a sequence greater than the BeginSeqNo, out of sequence, 
the message will be ignored. 
Administrative messages such as Sequence Reset, Heartbeat and Test Request which can be 
considered irrelevant for a retransmission could be skipped using the Sequence Reset message in 
gap-fill mode. Note that the gateway expects the client to skip Sequence Reset messages when 
replying to a Resend Request at all times. 
When resending messages, the gateway would use either PossDup or PossResend flag to indicate 
whether the messages were retransmitted earlier. If PossDup flag is set to Y = Yes, it indicates that 
the same message with the given sequence number with the same business content may have been 
transmitted earlier. In the case where PossResend flag is set to Y = Yes, it indicates that the same 
business content may have been transmitted previously but under the different message sequence 
number. In this case business contents needs to be processed to identify the resend. For example, in 
Execution Reports the ExecID (17) may be used for this purpose. 
2.2 Resend Request 
The client may use the Resend Request (35=2) message to recover any lost messages. This 
message may be used in one of three modes: 
1. 
To request a single message. The BeginSeqNo and EndSeqNo should be the same. 
2. 
To request a specific range of messages. The BeginSeqNo should be the first message of the 
range and the EndSeqNo should be the last of the range. 
3. 
To request all messages after a particular message. The BeginSeqNo should be the sequence 
number immediately after that of the last processed message and the EndSeqNo should be zero 
(0).


---
*Page 17*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 17 
 
 
2.3 Logon Message Processing – Next Expected Message Sequence 
The session initiator should supply the NextExpectedMsgSeqNum (789) the value next expected 
from the session acceptor in MsgSeqNum (34). The session acceptor should validate the logon 
request including that NextExpectedMsgSeqNum (789) does not represent a gap. It then constructs 
its logon response with NextExpectedMsgSeqNum (789) containing the value next expected from the 
session initiator in MsgSeqNum (34) having incremented the number above the logon request if that 
was the sequence expected. 
The session initiator must wait until the logon response is received in order to submit application 
messages. Once the logon response is received, the initiator must validate that 
NextExpectedMsgSeqNum (789) does not represent a gap.  
In case of gap detection from either party (lower than the next to be assigned sequence) recover all 
messages from the last message delivered prior to the logon through the specified 
NextExpectedMsgSeqNum (789) sending them in order, then gap fill over the sequence number 
used in logon and proceed sending newly queued messages with a sequence number one higher 
than the original logon. 
Neither side should generate a Resend Request (35=2) based on MsgSeqNum (34) of the incoming 
Logon message but should expect any gaps to be filled automatically by following the Next Expected 
Sequence processing described above. Whilst the gateway is resending messages to the client, the 
gateway does not allow another Resend Request (35=2) from the client. If a new Resend Request is 
received during this time, the gateway will terminate the session immediately without sending the 
Logout (35=5) message. 
Note that indicating the NextExpectedMsgSeqNum (789) in the Logon (35=A) is mandatory. 
2.4 Possible Duplicates 
The gateway handles possible duplicates according to the FIX protocol. The client and the gateway 
use the PossDupFlag (43) field to indicate that a message may have been previously transmitted 
with the same MsgSeqNum (34). 
2.5 Possible Resends 
The gateway does not handle possible resends for the client-initiated messages (e.g. New Order, 
etc.) and the message will be processed without considering the value in the PossResend (97) field. 
Any message with duplicate ClOrdID (11) will be rejected based on the Client Order ID uniqueness 
check and messages which conform to the uniqueness check will be processed as normal 
messages. 
The gateway may use the PossResend (97) field to indicate that an application message may have 
already been sent under a different MsgSeqNum (34). The client should validate the contents (e.g. 
ExecID (17)) of such a message against those of messages already received during the current 
trading day to determine whether the new message should be ignored or processed. 
2.6 Gap Fills 
The following messages are expected to be skipped using gap-fills when being retransmitted: 
1. 
Logon


---
*Page 18*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 18 
 
 
2. 
Logout 
3. 
Heartbeat 
4. 
Test Request 
5. 
Resend Request  
6. 
Sequence Reset 
All other messages are expected to be replayed within a retransmission. 
2.7 Transmission of Missed Messages 
The Execution Report, Order Mass Cancel Report, Business Message Reject, Reject and News 
messages generated during a period when a client is disconnected from the gateway will be sent to 
the client when it next reconnects on the same business day. In the unlikely event the disconnection 
was due to a gateway outage, some messages may not be retransmitted and the messages which 
will be retransmitted will include a PossResend (97) set to Y = Yes. 
2.8 Technical Halt 
In the event of a system component failure, a technical halt will be applied and the Market Data 
service will publish the Trading State = Technical Halt. On receipt of this message, market 
participants are required to clear their public and private order books of all orders including persisted 
orders. Order cancellations will not be transmitted by the gateway.


---
*Page 19*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 19 
 
 
3 
Service Description 
3.1 Security Identification 
Each tradable instruments will be identified using a SecurityID (48) which can be a maximum of 19 
digits. It is required to specify SecurityIDSource (22) as ‘8’ Exchange Symbol in conjunction with the 
SecurityID (48). 
3.2 Security Creation 
A Security Definition Request (35=c) can be submitted to create a new tradable instrument: 
Instrument Request Type 
FIX Tag 
Option strike 
SecurityType (167) = OPT 
MaturityDate (541) 
StrikePrice (202) 
PutOrCall (201) 
Strategy 
SecurityType (167) = MLEG 
SecuritySubType (762) 
LegSecurityID (602) 
LegSecurityIDSource (603) 
LegRatioQty (623) 
LegSide (624) 
LegPrice (566) [Optional] 
3.2.1 
Strategies 
A trader can submit Security Definition Request (35=c) for an Exchange defined strategy type or a 
custom strategy. A Delta Hedge strategy can be submitted as a custom strategy. 
A strategy can be submitted from either a buy or sell perspective and must include the strategy legs 
in order of expiry. A Security Definition Request expressed from a sell perspective will be returned 
with a SecurityResponseType (323) = ‘2’ Accept security proposal with revisions as indicated in the 
message and the resulting strategy will be created from the buy side perspective.


---
*Page 20*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 20 
 
 
3.2.1.1 Exchange Defined Strategy Types 
The following defined strategy types are supported: 
Futures Strategies 
SecuritySubType (762) 
Strategy Name 
Definition (from buy perspective) 
1 
Carry 
Buy near leg, sell far leg 
3 
Average 3M 
Buying 3 consecutive (monthly) legs 
4 
Average 6M 
Buying 6 consecutive (monthly) legs 
5 
Average 12M 
Buying 12 consecutive (monthly) legs 
6 
Carry Average 
Buy an outright (e.g. 3M), sell a Future Average 
(e.g. first quarter 2023). 
An Average strategy is only permitted in monthly prompts and only the front leg needs to be specified 
as the remaining legs will be consecutive.  
A Carry Average is the only permitted nested strategy type.  
Options Strategies 
SecuritySubType (762) 
Strategy Name 
Definition (from buy perspective) 
7 
Call Spread 
Buy a (call) strike, sell a (call) higher strike within 
the same option expiry 
8 
Put Spread 
Buy a (put) strike, sell a (put) lower strike within the 
same option expiry 
3.2.1.2 Custom Strategies 
A non-Exchange defined strategy can be submitted as a custom strategy using either: 
• 
SecuritySubType (762) = ‘2’ Custom (Futures) 
• 
SecuritySubType (762) = ‘9’ Custom (Delta Hedge) 
• 
SecuritySubType (762) = ‘10’ Custom (Options). 
A custom strategy can consist of up to five legs in a Futures contract or premium quoted Option. 
Each leg in the strategy must be in the same contract except for a delta hedge strategy in premium-
based options where the last 1 to 2 legs belong to the underlying futures contract. Note, an Exchange 
defined strategy cannot be used within a custom strategy. 
For example, a Futures Butterfly can be defined as buy Month 1, sell Month 2 twice and buy Month 3.


---
*Page 21*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 21 
 
 
 
3.3 Order Submission 
It is possible to submit orders for outright futures, options series or strategies using any of the order 
types specified in 3.4.1 Order Types. An individual order can be submitted using New Order Single 
(35=D) which includes a unique Client Order identifier in the ClOrdID (11), see Order Identification.  
A cross order can be submitted using New Order Cross (35=s) which includes a unique CrossID 
(548), see Error! Reference source not found. 
Multiple orders can be submitted using Mass Quotes available in the Binary protocol. 
3.4 Order Types 
The following order types are supported: 
Order Type 
FIX Tag and Value 
Limit 
An order submitted with a price and volume that will trade at the limit 
price or better for as much of its stated volume as is available in the 
order book. 
OrdType (40) = 2  
Price (44) 
Market 
An order submitted with a volume specified but no price. The order is 
executed at the best available price(s) up / down to their assigned limit 
price. Any order volume which is not fully executed rests in the order 
book as a limit order at the assigned limit price. 
OrdType (40) = 1


---
*Page 22*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 22 
 
 
Order Type 
FIX Tag and Value 
Stop Market 
An order that is submitted but not visible in the order book until it is 
triggered by the last traded price and/or best bid/offer. Once triggered 
the order is entered into the order book as a Stop Market order.  
A previously triggered Stop order will be restated as a Limit order. 
StopPx (99) and TriggeringInstruction component block tags will not be 
present. 
OrdType (40) = 3  
StopPx (99) 
TriggerType (1100) = 4  
TriggerPriceType (1107)  
Stop Limit 
An order that is submitted but not visible in the order book until it is 
triggered by the last traded price and/or best bid/offer. Once triggered 
the order is entered into the order book as a Stop Limit order at the 
specified price.  
A previously triggered Stop order will be restated as a Limit order. 
StopPx (99) and TriggeringInstruction component block tags will not be 
present. 
OrdType (40) = 4 
Price (44) 
StopPx (99) 
TriggerType (1100) = 4  
TriggerPriceType (1107) 
Iceberg 
An order submitted with a visible order quantity and a total order 
quantity. The visible order quantity must be fully executed before it can 
be replenished with the next visible order quantity. 
OrdType (40) = 2  
Price (44) 
DisplayQty (1138) 
OrderQty (38) 
Post Only 
The order must rest in the order book before it can trade. If the order 
can be executed on entry into the order book it is rejected. If an 
amendment to the order can result in execution it also is rejected and 
the original order remains. 
OrdType (40) = 2 
Price (44) 
ExecInst (18) = 6 
One Cancels Other (OCO) 
A single order which is a combination of a Limit and a Stop. On 
submission the Limit price and a Stop trigger price is specified.  
A partial trade at the Limit price will reduce the quantity available in the 
OCO. If the order is traded out at the Limit price the Stop component 
will be cancelled. Similarly if the Stop is triggered then the Limit 
component is cancelled.  
Note: No Execution Report will be generated for the cancelled 
component. 
OrdType (40) = 2 
Price (44) 
TriggerType (1100) = 4 
TriggerPrice (1102) 
TriggerPriceType (1107) 
TriggerNewPrice (1110)  
TriggerOrderType (1111)


---
*Page 23*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 23 
 
 
3.5 Order Validity Conditions 
Validity Condition 
FIX Tag and Value 
Day 
An order that will expire at the end of the day. 
TimeInForce (59) = 0 
(default) 
Good Till Cancelled (GTC) 
An order that is valid until it is either cancelled or matched. 
TimeInForce (59) = 1 
Immediate or Cancel (IOC) 
An order that is executed at the stated price or better for as much order 
volume that is available. Any order volume that cannot be traded is 
cancelled. 
TimeInForce (59) = 3 
Fill or Kill (FOK) 
An order that is only executed if there is sufficient volume available, at 
the stated price or better, for them to execute fully. Otherwise the 
entire order is cancelled. 
TimeInForce (59) = 4 
Good Till Date (GTD) 
The order is valid until the end of the trading date specified. 
TimeInForce (59) = 6 
ExpireDate (432) 
Note: A GTC or GTD order cannot be entered into the TOM prompt.  
A GTD will be rejected if the expiry date entered is the current trading date. A GTD in a single prompt 
will be rejected if the date entered exceeds the last trading date. 
3.6 Order Types and Permitted Order Validity Conditions 
Order Type 
Day 
GTC 
IOC 
FOK 
GTD 
Limit 
✔  
✔  
✔  
✔  
✔  
Market 
✔  
✔  
✔  
✔  
✔  
Stop Market 
✔  
✔  
 
 
✔  
Stop Limit 
✔  
✔  
 
 
✔  
Iceberg 
✔  
✔  
 
 
✔  
Post Only 
✔  
✔  
 
 
✔  
OCO 
✔  
✔  
 
 
✔


---
*Page 24*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 24 
 
 
3.7 Order Identification 
On order submission a ClOrdID (11) is specified by the originator. The client should comply with the 
FIX protocol and ensure the Client Order IDs are unique for the duration of the trading day and has 
not been used already for a currently persisted order belonging to this CompID. When an order is 
accepted, the system assigns an OrderID (37) that is unique for all orders. When modifying or 
deleting an order the OrigClOrdID (41) is used to identify the order.  
A cross order is specified by the originator using a CrossID (548) instead. For each of the bid / ask 
order contained in the cross order, a ClOrdID (11) is used to identify the order. When the cross order 
is accepted, the system assigns a HostCrossID (961) for the whole cross order, and an OrderID (37) 
for each of the orders within the cross order. When cancelling a cross order, the OrigCrossID (551) is 
used to identify the cross order. The HostCrossID (961) and OrigClOrdID (41) are optional and will be 
validated if specified. If any of these attributes do not match the original cross order, the cancel 
request will be rejected 
3.8 Order Expiry 
No Execution Report will be sent for orders with a TimeInForce (59) = ‘0’ Day when they expire at the 
end of the trading day.  
At the end of the day, the order originator will receive an Execution Report with ExecType (150) and 
OrdStatus (39) = ‘C’ Expired for TimeInForce (59) = ‘1’ Good Till Cancelled and TimeInForce (59) = 
‘6’ Good Till Date in the following cases:  
• 
ExpireDate (432) has passed for a Good Till Date order* 
• 
Last trading date for the tradable instrument has passed 
• 
To prevent restatement into the Tom order book 
• 
Any other Exchange specific configuration for order expiry of persisted orders 
• 
Strategy contains a leg that has expired or meets any of the conditions above 
• 
Legs of a strategy have the same prompt date. 
*Note where the expiry date is a non-business date, the order will expire at the start of the next 
trading date. 
3.9 Order Restatement 
GTC/GTD orders that have not hit their expiry condition are persisted when the respective instrument 
enters the Close state. The order originator is notified by Execution Report with ExecType (150) and 
OrdStatus (39) = ‘3’ Done for Day. 
On initial logon on the next trading day, Execution Reports are sent for persisted orders that have 
been returned with ExecType (150) = ‘D’ Restated, OrdStatus (39) = ‘0’ New or ‘1’ Partially Filled and 
ExecRestatementReason (378) = ‘1’ GT renewal / restatement. 
A previously triggered Stop order will be restated as a Limit order. StopPx (99) and 
TriggeringInstruction component block tags will not be present.


---
*Page 25*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 25 
 
 
3.10 Order Amendment 
An order can be amended by using an Order Cancel Replace Request (35=G) and specifying the 
OrigClOrdID (41). The client can optionally specify the OrderID (37) in the Order Cancel Replace 
Request message. If the OrderID (37) is specified, the system will validate whether the OrderID is 
associated with the correct order as identified using the OrigClOrdID (41). The Order Cancel Replace 
Request will be rejected if the specified OrderID (37) is invalid based on this validation.  
The following order attributes can be modified if they have been specified on the original order: 
• 
Price (44) 
• 
StopPx (99) 
• 
OrderQty (38)   
• 
DisplayQty (1138)  
• 
ExpireDate (432)  
• 
TriggerPrice (1102)  
• 
TriggerNewPrice (1110)  
• 
OrderCapacity (528) 
• 
OrderRestrictions (529) 
If an attribute listed above is not present in the Order Cancel Replace Request it will retain its original 
value. 
For the following attribute, if value(s) have been previously specified and are not specified in the 
Order Cancel Replace Request it indicates that the values have been removed 
• 
OrderOrigination (1724) 
• 
OrderAttributeType (2594) 
• 
Text (58) 
The PartyID (448) on the following MiFID regulatory reporting roles can be amended if the PartyRole 
(452):  
• 
300 Investment Decision Within Firm  
• 
302 Investment Decision Country 
• 
303 Execution Decision Country 
• 
304 Client Branch Country 
For the above roles, if the party was not specified on the original order, it can be added. If previously 
included it can be amended or can be omitted to indicate that the party has been removed.  
The client cannot amend an order that is fully filled or cancelled or expired.  
The StopPx (99), TriggerPrice (1102) or TriggerNewPrice (1110) cannot be amended if the Stop 
order has been triggered. Note, a previously triggered Stop Limit or Stop Market order will be 
restated with an OrdType (40) = 2 Limit.  
If the client sends an Order Cancel Replace Request for an order for which an Order Cancel Replace 
Request is being processed the second Order Cancel Replace Request is rejected. If an Order 
Cancel Request is submitted for an Order Cancel Replace Request that is being processed, the 
incoming Order Cancel Request will be accepted.


---
*Page 26*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 26 
 
 
3.11 Order Cancellation 
An individual order can be cancelled using Order Cancel Request (35=F) by specifying the 
OrigClOrdID (41).  
The client can optionally specify the OrderID (37) in the Order Cancel Request. If the OrderID (37) is 
specified, the system will validate whether the OrderID is associated with the correct order as 
identified by the OrigClOrdID. The Order Cancel Request will be rejected if the specified OrderID is 
invalid based on this validation. 
A cross order can be cancelled using Cross Order Cancel Request (u) by specifying the OrigCrossID 
(551). 
The HostCrossID (961) and OrigClOrdID (41) are optional and will be validated if specified. If any of 
these attributes do not match the original cross order, the cancel request will be rejected. 
A successful cancellation will return an Execution Report (35=8). If the cancellation request is 
rejected, an Order Cancel Reject (35=9) is sent containing CxlRejReason (102). 
 
3.12 Mass Cancellation 
Multiple orders can be cancelled using Order Mass Cancel Request (35=q) by specifying which 
orders are to be cancelled: 
Cancellation Type 
FIX Tag and Value 
All orders for a FIX Comp ID 
MassCancelRequestType (530) = 7 
All orders for a tradable instrument 
MassCancelRequestType (530) = 1 
SecurityID (48) 
SecurityIDSource (22) 
All orders for a specified contract 
MassCancelRequestType (530) = 3 
SecurityExchange (207) 
ProductComplex (1227) 
Symbol (55) 
All orders for an end client account 
MassCancelRequestType (530) = 7 
PartyRole (452) = ‘81’ Broker Client ID  
All orders for a specific contract and side of the 
market 
MassCancelRequestType (530) = 3 
SecurityExchange (207) 
ProductComplex (1227) 
Symbol (55)


---
*Page 27*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 27 
 
 
Cancellation Type 
FIX Tag and Value 
Side (54) 
If the Order Mass Cancel Request is accepted, Execution Reports will be sent for each order 
cancellation and reference the ClOrdID (11) provided on the Order Mass Cancel Request. An Order 
Mass Cancel Report (35=r) will follow and specify the TotalAffectedOrders (533) in the 
MassCancelResponse (531). 
If the Order Mass Cancel Request is rejected, an Order Mass Cancel Report will be sent with the 
MassCancelResponse (531) = ‘0’ Cancel Request Rejected and will include the 
MassCancelRejectReason (532).   
A mass cancellation request for a tradable instrument will not result in the cancellation of any orders 
in a merged tradable instrument. Orders will only be cancelled in the SecurityID (48) specified in the 
Order Mass Cancel Request. 
3.13 Cancel on Disconnect 
The gateway will not automatically cancel a user’s non-persisted orders in the event of a Logout. A 
user should explicitly cancel such orders prior to Logout using an Order Mass Cancel Request 
(35=q).  
On order submission a user can specify whether non-persisted orders should be cancelled on system 
disconnection (due to, for example, a network issue or in the event of inactivity such as too many 
missed heartbeats) using ExecInst (18) = ‘o’ Cancel on Connection Loss.  
On detection of a loss of connectivity, the system will use ExecInst (18) = ‘o’ Cancel on Connection 
Loss to determine whether a user’s non-persisted orders are cancelled. 
This feature does not guarantee that all live orders will be successfully cancelled as executions that 
occur very near to the time of disconnect may not be reported to the client. It also depends on the 
tradable instrument trading state when the abrupt disconnection is identified by the Exchange 
system. 
3.14 Auto Cross 
A New Order Cross (35=s) indicates a trading interest in a specific instrument which is published to 
market participants via a Request for Cross (RFC) on the Market Data service. The platform will then 
wait for a predefined period, then we will determine whether the cross order will be executed on 
book, offbook, a mixture of both on and offbook, or if the cross is cancelled. The Cross order will 
contain a buy and a sell order with the same price and quantity. 
CrossID (548) is used for the identifier of the cross, then an individual ClOrdID (11) for the order 
specified on each side. When an order is accepted, the system assigns a HostCrossID (761) in 
response to the CrossID (548), and an OrderID (37) for each of the individual order.  
CrossType (549) specifies whether a guaranteed or non guaranteed cross is requested. 
CrossPrioritization (550) indicates the order on which side of the Cross Order is prioritized.


---
*Page 28*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 28 
 
 
A pair of Execution Reports (35=8), one for the order on each side, will be returned by the gateway to 
acknowledge a successful Cross Request. The HostCrossID (761) and CrossID (548) will be 
returned in the Execution Report. 
Amendment to the Cross Order is not allowed. Cancellation can be done via Cross Order Cancel 
Request (35=u), by specifying the OrigCrossID (551). The HostCrossID (961) and OrigClOrdID (41) 
are optional and will be validated if specified. If any of these attributes do not match the original cross 
order, the cancel request will be rejected. 
 
Example message flow 
The cross is rejected at gateway due to a session level rule violation 
 
 
The cross is rejected due to business level rule violation


---
*Page 29*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 29 
 
 
The cross passes initial validation checks and is accepted. One side then fails revalidation checks 
resulting in the cross being cancelled


---
*Page 30*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 30 
 
 
 
The initiating side is crossed offbook with the non initiating side


---
*Page 31*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 31 
 
 
 
The initiating side is filled in the orderbook. The non initiating side is cancelled


---
*Page 32*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 32 
 
 
 
The initiating side is filled against multiple price levels in the orderbook. The non initiating side is 
cancelled 
 
A NewOrderCross is submitted and passes validation. Execution Reports are returned to the member 
indicating the orders are held in the RFC interval …


---
*Page 33*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 33 
 
 
The initiating side is partially filled in the orderbook. The residual volume is crossed offbook against 
the non initiating side, whose residual volume is then cancelled 
A NewOrderCross is submitted and passes validation. Execution Reports are returned to the member 
indicating the orders are held in the RFC interval …


---
*Page 34*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 34 
 
 
3.15 Request for Quote (RFQ) 
A Quote Request (35=R) indicates a trading interest in a specific instrument which is published to 
market participants by the Market Data service. 
The Quote Request will include the QuoteRequestType (303) which specifies whether a single quote 
or streaming quotes are requested. It can optionally specify the side and the quantity for which a 
price is required. 
A Quote Response (35=AJ) will be returned by the gateway to acknowledge a successful Quote 
Request. 
Trading participants can then respond using standard order functionality. 
3.16 Speed Bumps  
Exchange contracts may be configured with speed bumps. A speed bump will only be applicable to 
New Order Single and Order Cancel Replace Requests.  
Passive orders, Order Cancel Requests, Order Mass Cancel Requests and Mass Quotes will be 
exempt.  
The status of an order in a speed bump will be reported in ExecTypeReason (2431) in the Execution 
Report: 
101 = Order accepted but speed bump applied 
102 = Order added after speed bump 
103 = Order cancelled whilst in speed bump delay 
104 = Original order is in speed bump enforced delay  
105 = Order updated after speed bump delay 
106 = Amend is in speed bump delay 
107 = Order amended after speed bump delay 
108 = Order rejected after speed bump delay 
109 = Unsolicited cancel while in speed bump 
Order submission is speed bumped 
If an order is submitted but is subject to a speed bump, the order is held and not added to the order 
book until the order has been released from the speed bump. The Execution Report sent in 
acknowledgement includes an ExecTypeReason (2431) = ‘101’ Order accepted but speed bump 
applied. 
The Execution Report sent once the order has cleared the speed bump and is added to the order 
book includes ExecType (150) = ‘D’ Restated and ExecTypeReason (2431) = ‘102’ Order added after 
speed bump.


---
*Page 35*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 35 
 
 
 
Order cancellation for a speed bumped order 
An order cancellation submitted while an order is in the speed bump will be processed without any 
delay as the Order Cancel Request is not subject to speed bump conditions. The Execution Report 
sent in response to the cancellation includes ExecTypeReason (2431) = ‘103’ Order cancelled whilst 
in speed bump delay.


---
*Page 36*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 36 
 
 
Executable order amendment for a speed bumped order will be speed bumped 
An order is submitted which is subject to a speed bump. An Order Cancel Replace Request is 
submitted while the order submission is in the speed bump queue. The amended order is executable 
and therefore speed bumped. The Execution Report for the order amendment includes 
ExecTypeReason (2431) = ‘106’ Amend is in speed bump delay. The Order Cancel Replace Request 
will not be processed until the original order has cleared the speed bump.  
The Execution Report sent when the original order submission is released from the speed bump and 
added to the order book includes ExecType (150) = ‘D’ Restated, OrdStatus (39) = ‘E’ Pending 
Replace and ExecTypeReason (2431) = ‘102’ Order added after speed bump. 
Another Execution Report is sent when the order amendment clears the speed bump and replaces 
the original order. The Execution Report includes ExecType (150) = ‘5’ Replaced and 
ExecTypeReason (2431) = ‘107’ Order amended after speed bump delay.


---
*Page 37*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 37 
 
 
 
Non-executable order amendment for a speed bumped order will not be speed bumped 
An order is submitted which is subject to a speed bump. An Order Cancel Replace Request is 
submitted while the order submission is in the speed bump queue. The amended order will rest in the 
order book and is therefore not subject to speed bump conditions. The Order Cancel Replace 
Request will not be processed until the original order has cleared the speed bump therefore the 
Execution Report for the amendment includes ExecType (150) = ‘E’ Pending Replace and 
ExecTypeReason (2431) = ‘104’ Original order is in speed bump enforced delay.  
The Execution Report sent once the order submission has cleared the speed bump and is added to 
the order book includes ExecType (150) = ‘D’ Restated and ExecTypeReason (2431) = ‘102’ Order 
added after speed bump.


---
*Page 38*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 38 
 
 
When the order is replaced the Execution Report includes ExecType (150) = ‘5’ Replaced and 
ExecTypeReason (2431) = ‘105’ Order updated after speed bump delay. 
 
Executable order amendment for a resting order will be speed bumped 
An order amendment is submitted for a resting order that was previously speed bumped. The Order 
Cancel Replace Request is speed bumped as the amended order will not provide liquidity. The 
Execution Report for the amendment includes ExecType (150) = ‘E’ Pending Replace with and 
ExecTypeReason (2431) = ‘106’ Amend is in speed bump delay. 
When the order is replaced the Execution Report includes ExecType (150) = ‘5’ Replaced and 
ExecTypeReason (2431) = ‘107’ Order amended after speed bump delay.


---
*Page 39*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 39 
 
 
 
Speed bumped order is cancelled due to validation failure (inflight speed bumped amendment 
is also cancelled) 
An order is submitted which is subject to a speed bump. An Order Cancel Replace is accepted which 
is also subject to speed bump conditions. The original order submission fails business validation on 
clearing the speed bump and is cancelled. The Execution Report includes ExecType (150) = ‘4’ 
Cancelled and ExecTypeReason (2431) = ‘108’ Order rejected after speed bump delay with the 
reason for the business validation failure in RejectText (1328). An Order Cancel Reject is sent for the 
order amendment.


---
*Page 40*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 40 
 
 
 
Immediate or Cancel speed bumped order fails validation and is cancelled 
An Immediate or Cancel order is submitted which is subject to a speed bump. The order fails 
validation on clearing the speed bump as it cannot be executed and is therefore cancelled. The 
Execution Report includes ExecType (150) = ‘4’ Cancelled and ExecTypeReason (2431) = ‘108’ 
Order rejected after speed bump delay with the reason in RejectText (1328) = No quantity available 
at price stated.


---
*Page 41*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 41 
 
 
 
Note: In the absence of a speed bump an IOC will be rejected if no quantity is available at the price 
stated.    
Unsolicited order cancellation while in speed bump 
An order is submitted which is speed bumped. While the order is in the speed bump, the Exchange 
invokes a Trading Halt and all orders are pulled. The Execution Report sent for the order in the speed 
bump includes ExecType (150) = ‘4’ Cancelled with ExecTypeReason (2431) = ‘109’ Unsolicited 
cancel while in speed bump and RejectText (1328) = Cancelled due to halt.


---
*Page 42*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 42 
 
 
 
3.17 Message Throttling 
The Exchange imposes a message throttle which limits the maximum number of order submissions, 
amends, Quote Requests (35=R) and Security Definition Requests (35=c) that can be submitted per 
second by a FIX Comp ID. Messages submitted in excess of the throttle limit in any given whole 
second will result in those messages being rejected by the gateway and will be notified by a Business 
Message Reject (35=j). 
Security Definition Requests are included in the message throttle but also have their own throttle 
limits.  
Note, order cancellation messages are exempt from throttling. 
A system protection throttle will disconnect a user if the incoming message volume exceeds a 
multiple of the threshold limit. Reconnection is permitted after a second. 
3.18 Security Definition Throttle 
The number of Security Definition Requests (35=c) that can be submitted by a FIX Comp ID are set 
at per day rate and also included in the per second message throttle. A user breaching the daily limit 
will have further message submissions rejected by the gateway. 
3.19 Merged Order Books 
The LME prompt date structure for futures is such that two different prompts can share the same 
actual date on specific trading dates, for example, on the 3rd Wednesday of a month a 3M rolling 
prompt date will have the same prompt date as the monthly prompt date. On the trading date on 
which the prompts share the same actual date prompt, the order books for both prompts will be 
merged. TOM and Cash prompts will never merge.


---
*Page 43*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 43 
 
 
Strategy order books that include a rolling leg will also merge. This can occur if a leg or legs share 
the same actual prompt date. 
The merging of order books only affects execution and market data publication. Prompt dates in the 
merged order book will be available for order entry. The instrument identifier of the rolling prompt will 
be used by the Market Data service.  
GTC and GTD orders will be merged into the order book with precedence and will return to the order 
book into which they were entered when the order books are no longer merged. 
A mass cancellation request for a tradable instrument will not result in the cancellation of any orders 
in a merged tradable instrument. Orders will only be cancelled in the SecurityID specified in the Order 
Mass Cancel Request.


---
*Page 44*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 44


---
*Page 45*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 45 
 
 
3.20 Self Execution Prevention (SEP) 
A member can guard against traders in their organisation executing orders with each other.  
A member can use SEP functionality without configuring a SEP handling action in which case the 
Exchange configured response type would be triggered to cancel the incoming order. Alternatively a 
member can configure SEP identifiers and specify the action to be taken if two orders with an 
identical SEP ID could execute.  
A SEP ID will be specified as a maximum of 9 digits. A member will use a Party Entitlements 
Definition Request (35=DA) submitted via the Risk Management Gateway to define the SEP 
configuration as described in the Risk Management Gateway FIX Specification. This configuration 
will be effective from the next trading day. 
A SEP ID can be entered in the SelfMatchPreventionID (2362) on order submission. If orders with an 
identical SEP ID from the same member firm can cross, the SEP handling action that has been 
configured is triggered to cancel either the incoming or resting order or both (incoming and resting). 
The Execution Report sent for the cancelled order will contain RejectText (1328) = Self Match 
prevented. 
The availability of SEP functionality will be determined by the Exchange. If an order is submitted with 
the SelfMatchPreventionID (2362) populated and SEP is not available for the SecurityID (48) 
specified, the order will be rejected. The Execution Report sent will contain RejectText (1328) = Self 
Match Prevention not configured for the tradable instrument.


---
*Page 46*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 46 
 
 
Self Execution Prevention triggered – resting order cancelled 
 
3.21 Inflight Order Processing 
The gateway will accept a single inflight amend or cancellation request whilst processing a new 
order. The amend request is queued until the preceding request has been processed. Multiple inflight 
messages will be rejected. 
For example, a New Order Single is submitted followed immediately afterwards by an Order Cancel 
Replace Request. An Execution Report is returned for the order submission and then the 
amendment.


---
*Page 47*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 47 
 
 
 
See Appendix A: Inflight Order Handling and Appendix B: Speed Bump Inflight Order Handling for 
more examples. 
3.22 Trade Reporting 
When an outright order matches the trade half will be assigned an identifier which will be reported in 
the TrdMatchID (880) on the Execution Report (35=8). A strategy trade will be reported in a single 
Execution Report including the leg details. The legs of strategy trade will be assigned a LegAllocID 
(1366) which will be shared with either the LegAllocID of another strategy trade or the TrdMatchID of 
an outright trade. 
3.23 Order Attribute Type Usage 
The OrderAttributeGrp is used to specify additional attributes on the order. The following values are 
supported for OrderAttributeType (2594):  
0 = Aggregated order 
1 = Pending allocation 
2 = Liquidity provision order 
3 = Risk reduction order. 
OrderAttributeValue (2595) will always be set to Y.


---
*Page 48*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 48 
 
 
An order will be rejected if a client identifier or a value of 0 to indicate no client is submitted for the 
client short code i.e. PartyIDSource (447) = P and PartyRole (452) = ‘3’ Client ID for an order 
specified as either 0 = Aggregated order or 1 = Pending allocation.  
An order will also be rejected that specifies both 0 = Aggregated order and 1 = Pending allocation.


---
*Page 49*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 49 
 
 
4 
Message Definitions 
4.1 Supported Messages  
Message 
Logon (A) 
Establishes a FIX session 
Heartbeat (0) 
Used to check connectivity 
Test Request (1) 
Used to verify a connection is still active 
Resend Request (2) 
Request the retransmission of messages 
Reject (3) 
Issued when a message is received but cannot be properly processed due to a session-level 
rule violation 
Sequence Reset (4) 
Indicates there is a gap in the message sequence numbers 
Logout (5) 
Terminates a FIX session 
Business Message Reject (j) 
Reject an application level message which fulfils session level rules 
News (B) 
Disseminates text information 
Security Definition Request (c)  
Request the creation of a tradable instrument 
Security Definition (d) 
Response to a Security Definition Request


---
*Page 50*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 50 
 
 
Message 
New Order Single (D) 
Submit a new order for execution 
New Order Cross (s) 
Submit a new cross order 
Order Cancel Replace Request (G) 
Amend an existing order 
Order Cancel Request (F) 
Request the cancellation of all the remaining quantity of an existing order 
Order Cancel Reject (9) 
Reports that an Order Cancel Request or Order Cancel Replace Request has been rejected 
Cross Order Cancel Request (u) 
Request the cancellation of a cross order 
Execution Report (8) 
Sent in response to order and fill related client messages 
Order Mass Cancel Request (q) 
Cancel multiple orders 
Order Mass Cancel Report (r) 
Acknowledgement of an Order Mass Cancel Request  
Quote Request (R) 
Requests prices from market participants 
Quote Response (AJ) 
Acknowledgement of a Quote Request 
Quote Request Reject (AG) 
Reports that a Quote Request has been rejected 
4.2 Inbound Messages 
• 
Logon (A) 
• 
Heartbeat (0)


---
*Page 51*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 51 
 
 
• 
Test Request (1) 
• 
Resend Request (2) 
• 
Sequence Reset (4) 
• 
Logout (5) 
• 
Security Definition Request (c) 
• 
New Order Single (D) 
• 
New Order Cross (s) 
• 
Order Cancel Replace Request (G) 
• 
Order Cancel Request (F) 
• 
Cross Order Cancel Request (u) 
• 
Order Mass Cancel Request (q) 
• 
Quote Request (R) 
4.3 Outbound Messages 
• 
Logon (A) 
• 
Heartbeat (0) 
• 
Test Request (1) 
• 
Resend Request (2) 
• 
Sequence Reset (4) 
• 
Logout (5) 
• 
Reject (3) 
• 
Business Message Reject (j) 
• 
News (B) 
• 
Security Definition (d) 
• 
Order Cancel Reject (9) 
• 
Execution Report (8) 
• 
Order Mass Cancel Report (r) 
• 
Quote Response (AJ) 
• 
Quote Request Reject (AG) 
4.4 Data Types 
Data types used are based on the published standard FIX specifications. The field length in 
characters is shown in brackets. The length of numeric fields is the number of digits in that value and 
not the size of the value in bytes. If a data type has a specific value this will be provided in the 
description. 
Data Type 
Format 
UTCTimestamp (27) 
Incoming 
YYYYMMDD-HH:mm:ss.SSSSSS 
YYYYMMDD-HH:mm:ss.SSSSSSSSS 
Timestamps will be represented as UTC and accepted to 
microsecond or nanosecond precision


---
*Page 52*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 52 
 
 
Data Type 
Format 
Outgoing 
YYYYMMDD-HH:mm:ss.SSSSSSSSS 
Note: Timestamps will be represented as UTC up to microsecond 
precision with the nanosecond element being represented by trailing 
zeros. 
Price (20) 
Can be up to 12 significant digits before the decimal point (with 
provision for a negative value) and at the most 6 decimal places 
For example, 
1234567891234.567891 
-123456789123.456789 
String (n) 
Permitted ASCII characters are A-Z, a-z, 0-9.  
Note, special characters are also permitted for the following attributes: 
Tag / PartyID 
Underscore 
Hyphen 
ClOrdID (11) 
✔ 
✔ 
OrigClOrdID (41) 
✔ 
✔ 
CrossID (548) 
✔ 
✔ 
OrigCrossID (551) 
✔ 
✔ 
PartyID (448) for PartyRole (452) 
 
 
‘81’ Broker Client ID 
✔ 
✔ 
‘11’ Order Origination Trader 
✔ 
X 
‘3’ Client ID (Proprietary/Custom) 
✔ 
X 
‘24’ Customer Account 
✔ 
X 
Note: Text in the News message and rejection reasons can contain 
other ASCII characters and spaces. 
4.5 Required Fields 
The following conventions are used for fields in the message definitions:


---
*Page 53*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 53 
 
 
Y  
 Required by FIX 
Y*  
 Required by LME  
C  
 Conditionally required by FIX  
C*  
 Conditionally required by LME  
N  
 Not required / optional.    
4.6 Message Header 
Tag 
Field Name 
Req 
Data Type 
Description 
8 
BeginString 
Y 
String (8) 
Always set to FIXT.1.1  
9 
BodyLength 
Y 
Length (4) 
Message length, in bytes, forward to the 
CheckSum field. 
Maximum value 9999 
35 
MsgType 
Y 
String (3) 
Defines message type. 
1128 
ApplVerID 
N 
String (1) 
Version of FIX used in the message: 
9 = FIX50SP2 
Returned by the gateway 
49 
SenderCompID 
Y 
String (10) 
Identifies the sender of the message, 
see Comp ID 
56 
TargetCompID 
Y 
String (10) 
Identifies the receiver of the message, 
see Comp ID 
34 
MsgSeqNum 
Y 
SeqNum (9) 
Outbound message sequence number. 
Always incremented by the sender. 
43 
PossDupFlag 
N 
Boolean 
Indicates whether the message was 
previously transmitted with the same 
MsgSeqNum (34).  
Absence of this field is interpreted as 
original transmission (N). 
97 
PossResend 
N 
Boolean 
Indicates whether the message was 
previously transmitted under a different 
MsgSeqNum (34).


---
*Page 54*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 54 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Absence of this field is interpreted as 
original transmission (N). 
52 
SendingTime 
Y 
UTCTimestamp 
Time the message was transmitted. 
122 
OrigSendingTime 
C 
UTCTimestamp 
Conditionally required for messages sent 
as a result of a Resend Request (2).  
If the original time is not available, this 
should be the same value as 
SendingTime (52). 
4.7 Message Trailer 
Tag 
Field Name 
Req 
Data Type 
Description 
10 
CheckSum 
Y 
String (7) 
Standard check sum described by FIX 
protocol.  
Always last field in the message; i.e. 
serves, with the trailing <SOH>, as the 
end-of-message delimiter.  
Always defined as three characters. 
4.8 Administrative Messages 
4.8.1 
Logon (A) 
The first messages exchanged in a FIX session are the Logon request and the Logon response. The 
main purposes of the Logon request and response are: 
• 
To authenticate the client. 
• 
To agree on the sequence numbers. 
On initial logon the status of persisted orders is communicated to the FIX session by the publication 
of Execution Reports for all open orders. 
The list of available tradable instruments for the current trading day will be published by the Market 
Data service independently of the FIX Logon request. 
Tag 
Field Name 
Req 
Data Type 
Description 
98 
EncryptMethod 
Y 
Int 
Method for encryption.  
Valid value is: 0 = None 
108 
HeartBtInt 
Y 
Int 
Heartbeat interval in seconds.


---
*Page 55*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 55 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
789 
NextExpectedMsgSeqNum 
Y* 
SeqNum 
(9) 
Next expected MsgSeqNum (34) value 
to be received. Always updated as a 
result of an incoming message. 
1400 
EncryptedPasswordMethod 
N 
Int 
Enumeration defining the encryption 
method used to encrypt password 
fields: 
101 = RSA 
1402 
EncryptedPassword 
Y 
Data (450) 
Encrypted password – encrypted via 
the method specified in 
EncryptedPasswordMethod (1400) 
1404 
EncryptedNewPassword 
N 
Data (450) 
Encrypted new password – encrypted 
via the method specified in 
EncryptedPasswordMethod (1400) 
1137 
DefaultApplVerID  
Y 
String (1) 
The default version of FIX being used 
in this session: 
9 = FIX50SP2 
A Logon message is returned in response to an incoming Logon message to initiate a FIX session. 
The SessionStatus (1409) indicates whether the logon attempt was successful or not. 
Tag 
Field Name 
Req 
Data Type 
Description 
98 
EncryptMethod 
Y 
Int 
Method for encryption.  
Valid value is: 0 = None 
108 
HeartBtInt 
Y 
Int 
Heartbeat interval in seconds. 
789 
NextExpectedMsgSeqNum 
Y* 
SeqNum 
(9) 
Next expected MsgSeqNum (34) value 
to be received. Always updated as a 
result of an incoming message. 
1409 
SessionStatus 
N 
Int 
Status of the FIX session. 
Valid values: 
0 = Session active  
1 = Session password changed  
1137 
DefaultApplVerID  
Y 
String (1) 
The default version of FIX being used 
in this session: 
9 = FIX50SP2


---
*Page 56*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 56 
 
 
Example Message Flow 
Initial Logon 
 
4.8.2 
Heartbeat (0) 
Heartbeat (35=0) is sent at the interval specified in HeartBtInt (108) in Logon (35=A). It is also sent in 
response to a Test Request (35=1). 
Tag 
Field Name 
Req 
Data Type 
Description 
112 
TestReqID 
C 
String (20) 
Conditionally required if the heartbeat is a 
response to a Test Request (1). The value in 
this field should echo the TestReqID (112) 
received in the Test Request. 
4.8.3 
Test Request (1) 
Test Request (35=1) can be sent by either the client or gateway to verify a connection is active. The 
recipient responds with a Heartbeat (35=0). 
Tag 
Field Name 
Req 
Data Type 
Description 
112 
TestReqID 
Y 
String (20) 
Identifier included in Test Request message 
to be returned in resulting Heartbeat (0). 
4.8.4 
Resend Request (2) 
Resend Request (35=2) is used to initiate the retransmission of messages if a sequence number gap 
is detected. 
To request a single message. The BeginSeqNo and EndSeqNo should be the same. 
To request a specific range of messages. The BeginSeqNo should be the first message of the range 
and the EndSeqNo should be the last of the range.


---
*Page 57*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 57 
 
 
To request all messages after a particular message. The BeginSeqNo should be the sequence 
number immediately after that of the last processed message and the EndSeqNo should be zero (0). 
Tag 
Field Name 
Req 
Data Type 
Description 
7 
BeginSeqNo 
Y 
SeqNum 
(9) 
Message sequence number of the first 
message in the range to be resent. 
16 
EndSeqNo 
Y 
SeqNum 
(9) 
Sequence number of the last message 
expected to be resent. 
This may be set to 0 to request the sender to 
transmit ALL messages starting from 
BeginSeqNo (7). 
Example Message Flow 
Resend Request for a range of messages


---
*Page 58*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 58 
 
 
Resend Request for all messages after a particular message


---
*Page 59*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 59 
 
 
Resend Request - incoming message buffered by Client 
A Resend Request is submitted but before gap fill messages have been transmitted an incoming 
message is received. The client will hold the message until all the gap fill messages have been 
received and then process the buffered message. All messages should be processed in sequence 
number order.


---
*Page 60*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 60 
 
 
4.8.5 
Sequence Reset (4) 
Sequence Reset (35=4) allows the client or the gateway to increase the expected incoming sequence 
number of the other party. 
In a Gap Fill it is sent as notification of the next sequence number to be transmitted. 
Tag 
Field Name 
Req 
Data Type 
Description 
123 
GapFillFlag 
N 
Boolean 
Indicates that the Sequence Reset message 
is replacing administrative or application 
messages which will not be resent. 
Valid values: 
Y = Gap Fill message, MsgSeqNum (34) field 
valid. 
N = Sequence Reset, ignore MsgSeqNum 
(tag 34). 
If omitted default value is N. 
36 
NewSeqNo 
Y 
SeqNum 
(9) 
Sequence number of the next message to be 
transmitted. 
4.8.6 
Logout (5) 
Logout (35=5) initiates or confirms the termination of a FIX session. FIX clients should terminate their 
sessions gracefully by logging out. 
If a FIX user is disabled by LME Market Operations while logged in then a Logout message will be 
sent to the user and the session will be disconnected. 
If a FIX user has their password reset by LME Market Operations and attempts to login with their 
previous password, the user will receive a Logout with SessionStatus (1409) = ‘100’ Password 
change is required. 
Tag 
Field Name 
Req 
Data Type 
Description 
1409 
SessionStatus 
N 
Int 
Session status at time of logout. 
Valid values: 
3 = New session password does not comply 
with policy 
4 = Session logout complete 
5 = Invalid username or password 
6 = Account locked 
7 = Logons are not allowed at this time 
8 = Password expired 
100 = Password change is required 
101 = Other


---
*Page 61*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 61 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
58 
Text 
C 
String (50) 
Reason for logout. 
Conditionally required if SessionStatus (1409) 
= ‘101’ Other 
4.8.7 
Reject (3) 
Reject (35=3) will be sent when a message is received but cannot be properly processed by the 
gateway due to a session level rule violation. For example, a message missing a mandatory tag. 
Tag 
Field Name 
Req 
Data Type 
Description 
45 
RefSeqNum 
Y 
SeqNum 
(9) 
Sequence number of the message which 
caused the rejection. 
371 
RefTagID 
N 
Int 
If a message is rejected due to an issue 
with a particular field its tag number will be 
indicated. 
372 
RefMsgType 
N 
String (2) 
Message type of the rejected message. 
373 
SessionRejectReason N 
Int 
Code specifying the reason for the session 
level rejection: 
Valid values: 
0 = Invalid Tag Number 
1 = Required Tag Missing 
2 = Tag not defined for this message 
4 = Tag specified without a value 
5 = Value is incorrect (out of range) for this 
tag 
6 = Incorrect data format for value 
9 = CompID problem 
10 = Sending Time Accuracy problem 
11 = Invalid Msg Type 
13 = Tag appears more than once 
15 = Repeating group fields out of order 
16 = Incorrect NumInGroup count for 
repeating group 
99 = Other. 
58 
Text 
N 
String (50) 
Text specifying the reason for the rejection.


---
*Page 62*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 62 
 
 
4.9 Other Messages 
4.9.1 
Business Message Reject (j) 
Once an application level message passes validation at FIX session level it will then be validated at 
business level. If business level validation detects an error condition then a rejection should be 
issued. Many business level messages have specific tags for rejection handling where a specific tag 
is not available the Business Message Reject message (35=j) will be returned. 
Tag 
Field Name 
Req 
Data Type 
Description 
45 
RefSeqNum 
N 
SeqNum 
(9) 
Sequence number of the message which 
caused the rejection. 
372 
RefMsgType 
Y 
String (2) 
Message type of the rejected message. 
379 
BusinessRejectRefID 
N 
String (20) 
Client specified unique identifier on the 
message that was rejected. 
For example, for a New Order Single this 
would be the client specified identifier in 
the ClOrdID (11). 
380 
BusinessRejectReason Y 
Int 
Code specifying the reason for the 
rejection of the message. 
Valid values: 
0 = Other 
2 = Unknown Security 
3 = Unsupported Message Type 
5 = Conditionally required field missing 
8 = Throttle limit exceeded 
9 = Throttle limit exceeded, session will be 
disconnected. 
58 
Text 
N 
String (50) 
Text specifying the reason for the 
rejection. 
4.9.2 
News (B) 
A News message (35=B) is a general free format message from the exchange. A News message is 
also sent in response to a market maker protection breach, see Market Maker Protection in the Order 
Entry Gateway Binary Specification. 
Tag 
Field Name 
Req 
Data Type 
Description 
1472 
NewsID 
Y* 
String (20) 
Unique identifier for News message. 
1473 
NewsCategory 
Y* 
Int 
Category of News message.


---
*Page 63*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 63 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Valid values: 
101 = Market message 
102 = Market Maker Protection 
42 
OrigTime 
Y* 
UTCTimestamp 
Time of message origination 
148 
Headline  
Y 
String (75) 
Specifies the headline text either Market 
message or Market Maker Protection 
Component Block <LinesOfTextGrp> 
33 
NoLinesOfText 
Y 
NumInGrp (1) 
Specifies the number of repeating lines 
of text specified.  
This value is always set to 1. 
>58 
Text 
Y 
String (250) 
Free text field for Market message or 
one of the following for Market Maker 
Protection: 
• 
Cumulative percent over time 
breached 
• 
Volume over time breached 
• 
Number of tradable instruments 
traded over time breached  
End Component Block


---
*Page 64*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 64 
 
 
Example Message Flow 
Market Maker Protection breached 
 
4.10 Parties Component Block 
Tag 
Field Name 
Req Data Type 
Description 
453 
NoPartyIDs 
Y* 
NumInGrp (2) 
Number of parties specified. 
>448 
PartyID 
Y* 
String 
See PartyRole 
Usage 
Party identifier/code.  
Required if NoPartyIDs (453) > 0. 
>447 
PartyIDSource 
Y* 
Char 
Source of the PartyID (448) value. Required if 
NoPartyIDs (453) > 0. 
Valid values: 
P = Client Short Code 
D = Proprietary/Custom 
E = ISO Country Code (i.e. two letter ISO 
country code)  
N = Legal Entity ID - LEI  
>452 
PartyRole 
Y* 
Int 
Role of the specified PartyID (448). Required if 
NoPartyIDs (453) > 0. 
Valid values: 
1 = Executing Firm  
3 = Client ID


---
*Page 65*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 65 
 
 
Tag 
Field Name 
Req Data Type 
Description 
4 = Clearing Firm  
7 = Entering Firm  
11 = Order Origination Trader  
24 = Customer Account  
26 = Correspondent broker 
36 = Entering Trader  
66 = Market Maker 
81 = Broker Client ID 
122 = Decision Maker  
300 = Investment Decision Within Firm 
301 = Execution Within Firm 
302 = Investment Decision Country 
303 = Execution Decision Country 
304 = Client Branch Country


---
*Page 66*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 66 
 
 
4.10.1 
PartyRole Usage 
PartyRole (452) values used by LME are described below:  
PartyRole (452) 
PartyID (448) 
format  
PartyIDSource (447) 
Description 
Usage 
1  
Executing Firm 
Char (3) 
D = Proprietary/Custom Identifier of the executing firm. 
Cannot be entered in requests but will be returned in 
Execution Reports. 
N/A for order entry 
Used for Transaction 
Reporting and Order 
Record Keeping 
3 
Client ID 
Int (8 bytes)  
P = Client Short Code 
Client short code identifier. 
Required only for client orders i.e. AccountType (581) = 1, 
8 or 101 where OrderAttributeType (2594) = 0 or 1 has not 
been specified, see Order Attribute Type Usage.  
Note: PartyID (448) can be set to 0 = No Client for if there 
is no client where AccountType (581) = 3.  
PartyID (448) is not valid if populated with either 1, 2 or 3. 
 Mandatory where OrderCapacity (528) is populated with A 
(agency) = AOTC or R (riskless principal) = MTCH 
Conditionally required for 
Client orders 
Used for Transaction 
Reporting and Order 
Record Keeping 
Up to two instances 
of PartyRole (452) = '3' 
Client ID can be specified 
 
 Validated at point of reporting


---
*Page 67*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 67 
 
 
PartyRole (452) 
PartyID (448) 
format  
PartyIDSource (447) 
Description 
Usage 
String (<=40)  
D = Proprietary/Custom Proprietary or Custom Client ID as assigned by the 
member. 
Required only for client orders i.e. AccountType (581) = 1, 
8 or 101. 
but PartyIDSource (447) 
values must be unique.  
String (<=40)  
N = Legal Entity ID 
LEI. 
Optional 
Up to two instances 
of PartyRole (452) = '3' 
Client ID can be specified 
but PartyIDSource (447) 
values must be unique. 
4 
Clearing Firm 
Char (3) 
D = Proprietary/Custom Identifier of the clearing firm. A 3 character broker code 
(Member mnemonic). 
Cannot be entered in requests but is returned in Execution 
Reports for all fills. 
N/A for order entry 
Used for Transaction 
Reporting and Order 
Record Keeping 
7 
Entering Firm 
Char (3) 
D = Proprietary/Custom Identifier of the entering firm. A 3 character broker code 
(Member mnemonic). 
Required for MiFID as agent relationships are not captured 
in the LME participant structure. 
Optional 
Used for Transaction 
Reporting and Order 
Record Keeping


---
*Page 68*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 68 
 
 
PartyRole (452) 
PartyID (448) 
format  
PartyIDSource (447) 
Description 
Usage 
11  
Order Origination 
Trader 
String (<=40) 
D = Proprietary/Custom Order Origination Trader (associated with Order Origination 
Firm i.e. trader who initiates/submits the order). 
Required as could be more than one individual under a FIX 
Comp ID. 
Required in New Order Single and will be returned in 
Execution Reports. 
Mandatory for House and 
Client orders 
24  
Customer 
Account  
String (<=30) 
D = Proprietary/Custom Identification of the Client Account Code where the 
AccountType (581) = 1, 8 or 101. 
Conditional - Mandatory 
for Client orders 
26  
Correspondent 
broker - Non-
executing broker 
Char (3) 
D = Proprietary/Custom A 3 character broker code (Member mnemonic). 
Optional 
Used for Order Record 
Keeping 
36 
Entering Trader 
String (<=10) 
D = Proprietary/Custom Identifier of the trader entering the order. Cannot be 
entered in requests but will be returned in Execution 
Reports. 
N/A for order entry 
66 
Market Maker 
Char (1) 
D = Proprietary/Custom This should be set to Y if the trader qualifies for a Market 
Maker initiative 
Optional 
81 
Broker Client ID 
String (<=16) 
D = Proprietary/Custom Identifier of the entity in a risk group. 
Required in New Order Single and will be returned in 
Execution Reports. 
Mandatory used for Risk 
Management


---
*Page 69*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 69 
 
 
PartyRole (452) 
PartyID (448) 
format  
PartyIDSource (447) 
Description 
Usage 
122 
Decision Maker 
Int (8 bytes) 
P = Client Short Code 
Decision maker short code, used under the power of 
representation clause where the investment decision maker 
may be a third party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 2017/590 . 
Required only for client orders i.e. AccountType (581) = 1, 
8 or 101. 
Conditional 
Used for Transaction 
Reporting 
300 
Investment 
Decision Within 
Firm 
Int (8 bytes) 
P = Client Short Code 
Short code to identify the individual or algorithm within the 
investment firm who is responsible for the investment 
decision. 
Mandatory where OrderCapacity (528) is populated with P 
(principal) = DEAL, in accordance with the UK version of 
Commission Delegated Regulation (EU) No 2017/590 
Conditional 
Used for Transaction 
Reporting and Order 
Record Keeping 
301 
Execution Within 
Firm 
Int (8 bytes) 
P = Client Short Code 
Short code to identify the individual or algorithm within the 
investment firm who is responsible for the execution. 
Short code 3 (NORE) used where the decision on 
execution venue was made by a client or a person outside 
of the executing firm. 
Where OrderOrigination (1724) is populated with 5, the 
short code should always be 3 (NORE). 
Required in New Order Single and Order Cancel Replace 
Requests and will be returned in Execution Reports. 
Mandatory for House and 
Client orders 
Used for Transaction 
Reporting and Order 
Record Keeping


---
*Page 70*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 70 
 
 
PartyRole (452) 
PartyID (448) 
format  
PartyIDSource (447) 
Description 
Usage 
302 
Investment 
Decision Country 
Char (2) 
E = ISO Country Code 
ISO Country Code of the branch responsible for the person 
making the investment decision. 
 Mandatory where Investment Decision Within Firm (300) 
is populated with a short code representing an individual 
Conditional 
Used for Transaction 
Reporting 
303 
Execution 
Decision Country 
Char (2) 
E = ISO Country Code 
ISO Country Code of the branch responsible for the person 
making the execution decision. 
 Mandatory where Execution within Firm (EDM) is 
populated with a short code representing an individual. 
Conditional 
Used for Transaction 
Reporting 
304 
Client Branch 
Country 
Char (2) 
E = ISO Country Code 
ISO Country Code to identify the branch that received the 
client order or made an investment decision for a client. 
Mandatory where AccountType (581) = 1, 8 or 101 
Conditional  
Used for Transaction 
Reporting 
 
 Validated at point of reporting


---
*Page 71*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 71 
 
 
4.11 Application Messages 
4.11.1 
Security Definition Request (c) 
Security Definition Request (35=c) is used to request the creation of either an option strike or a 
strategy. A Security Definition (35=d) will be sent in response to the request. 
Tag 
Field Name 
Req 
Data Type 
Description 
320 
SecurityReqID 
Y 
String (18) 
Unique ID of a Security Definition 
Request. 
321 
SecurityRequestType 
Y 
String (1) 
Type of Security Definition Request. 
1 = Request security identity for the 
specifications provided 
Component Block <Instrument> 
207 
SecurityExchange 
Y* 
Exchange (4) 
Market which is used to identify the 
security: 
XLME 
1227 
ProductComplex 
Y* 
String (4) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base  
55 
Symbol 
Y* 
String (20) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future). 
167 
SecurityType 
Y* 
String (4) 
Indicates the type of security whether 
outright or strategy e.g. MLEG for 
strategy.  
Valid values: 
OPT = Option 
MLEG = Multileg instrument 
762 
SecuritySubType 
Y* 
Int 
Indicates the security sub type. 
Valid values: 
0 = Outright 
1 = Carry 
2 = Custom (Futures) 
3 = 3 Month Average 
4 = 6 Month Average


---
*Page 72*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 72 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
5 = 12 Month Average 
6 = Carry Average 
7 = Call Spread 
8 = Put Spread 
9 = Custom (Delta Hedge) 
10 = Custom (Options) 
541 
MaturityDate 
C* 
LocalMktDate Expiration date for options (YYYYMMDD) 
Conditionally required if SecurityType 
(167) = ‘OPT’ Option. 
Not required if SecurityType (167) = 
MLEG. 
202 
StrikePrice 
C* 
Price (20) 
Strike Price for an Option. 
Conditionally required if SecurityType 
(167) = ‘OPT’ Option. 
201 
PutOrCall 
C* 
Int 
Used to express option right 
Valid values:  
0 = Put  
1 = Call 
Conditionally required if SecurityType 
(167) = ‘OPT’ Option. 
Component Block <InstrmtLegGrp> 
555 
NoLegs 
C* 
NumInGrp (1) Conditionally required if SecurityType 
(167) = 'MLEG'  
Number of InstrumentLeg repeating group 
instances. Cannot be more than 5 or less 
than 2.  
Note this will only be 1 for a 3 Month 
Average, 6 Month Average and 12 Month 
Average. 
Component Block <InstrumentLeg> 
>602 
LegSecurityID 
C* 
Int 
SecurityID of the leg derived from the 
SecurityID (48) of the outright. 
Conditionally required if SecurityType 
(167) = MLEG.


---
*Page 73*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 73 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
For an Average strategy only the 
LegSecurityID of the first leg of the 
strategy is provided as the other months 
are consecutive. 
>603 
LegSecurityIDSource 
C* 
String (1) 
Identifies the source of the LegSecurityID 
value. 
Valid value: 
8 = Exchange defined. 
Conditionally required when 
LegSecurityID (602) is specified. 
>623 
LegRatioQty 
C* 
Float 
The ratio of quantity for this individual leg 
relative to the entire multileg security. 
Conditionally required if SecurityType 
(167) = MLEG. 
For example, for a custom strategy such 
as a Butterfly the leg ratio would be 1:2:1 
(1.000:2.000:1.000), for the first leg 
LegRatioQty = 1.000 (buy near contract 
month), second leg LegRatioQty = 2.000 
(sell two contracts in far month) and third 
leg LegRatioQty = 1.000 (buy one contract 
in yet farther month). 
For a Carry Average the front leg must 
include a ratio for the number of average 
legs. For example, 3M-3Q (Jul/Aug/Sep) 
Carry Average, 3M leg LegRatioQty = 
3.000, legs 2/3/4 would have LegRatioQty 
= 1.000. 
For a Delta Hedge Custom, this is the 
delta used to determine the covering 
quantity.  
>624 
LegSide 
C* 
Char 
The side of this individual leg. 
Valid values: 
1 = Buy 
2 = Sell. 
Conditionally required if SecurityType 
(167) = MLEG.


---
*Page 74*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 74 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
>566 
LegPrice 
C* 
Price 
Used to specify an anchor price for a leg 
as part of the definition or creation of the 
strategy - not used for execution price. 
Conditionally required for the futures legs 
of SecuritySubType (762) = '9' Delta 
Hedge Custom to specify the underlying 
futures price. 
End Component Blocks 
4.11.2 
Security Definition (d) 
Security Definition (35=d) will be returned to the originator of the Security Definition Request (35=c) 
to accept, accept with revisions or reject the creation of a tradable instrument. Market participants will 
be notified of a newly created instrument by the Market Data service. 
Tag 
Field Name 
Req 
Data Type 
Description 
320 
SecurityReqID 
Y* 
String (18) 
Client generated ID supplied on the 
Security Definition Request. 
322 
SecurityResponseID 
Y* 
String (20) 
Unique ID of a Security Definition (d) 
message. 
323 
SecurityResponseType 
Y* 
Int 
Type of Security Definition message 
response. 
Valid values:  
1 = Accept security proposal 
2 = Accept security proposal with 
revisions as indicated in the message 
5 = Reject security proposal 
1607 
SecurityRejectReason 
C 
Int 
Identifies the reason a security definition 
request is being rejected. 
Conditionally required to specify a 
rejection reason when 
SecurityResponseType (323) = ‘5’ Reject 
security proposal. 
Valid values:  
99 = Other 
101 = Throttle limit exceeded  
102 = Invalid strike price 
103 = LegSecurityID (602) does not exist


---
*Page 75*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 75 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
104 = Invalid prompt date 
105 = Invalid SecuritySubType (762) 
Component Block <Instrument> 
48 
SecurityID 
C* 
Int 
Tradable instrument identifier 
Conditionally required if 
SecurityResponseType (323) = '1' 
Accept security proposal or ‘2’ Accept 
security proposal with revisions as 
indicated in the message 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the SecurityID 
(48): 
8 = Exchange Symbol 
Conditionally required when SecurityID 
(48) is specified. 
End Component Block 
58 
Text 
C* 
String (75) 
Identifies the reason for rejection. 
Conditionally required if 
SecurityRejectReason (1607) = ‘99’ 
Other 
Example Message Flows 
Option Strike Request


---
*Page 76*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 76 
 
 
Futures Strategy Request 
 
Inverse Custom Strategy Request


---
*Page 77*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 77 
 
 
Delta Hedge Strategy Request – Call Spread versus underlying 
 
4.11.3 
New Order Single (D) 
New Order Single (35=D) is used to submit a new order for execution. An Execution Report (35=8), 
Reject (35=3) or Business Message Reject (35=j) is sent in response.  
Tag 
Field Name 
Req 
Data Type 
Description 
11 
ClOrdID 
Y 
String (18) 
Unique identifier set by the order 
originator. 
Component Block <Parties> 
Y* 
See Parties Component Block 
The following PartyRole (452) values are mandatory:  
'11' Order Origination Trader  
‘81’ Broker Client ID  
'301' Execution Within Firm 
581 
AccountType 
Y* 
Int 
Specifies the type of account 
associated with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) 
= Gross OSA 
101 = Client OSA


---
*Page 78*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 78 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
For contracts assigned to the T4 
booking model only 3 = House is 
valid whereas for the T2 booking 
model all account types are valid. 
18 
ExecInst 
N 
MultipleCharValue Instructions for order handling. If 
more than one instruction is 
applicable to an order, this field can 
contain multiple instructions 
separated by space. 
Valid values: 
6 = Participate but don’t initiate 
(required for Post only order 
submission) 
o = Cancel on connection loss 
Component Block <DisplayInstruction> 
1138 
DisplayQty 
C* 
Qty 
Visible quantity.  
Conditionally required for Iceberg 
orders. 
If present, must be < OrderQty (38) 
End Component Block 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
Y 
Char 
Side of the order 
Valid values: 
1 = Buy 
2 = Sell


---
*Page 79*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 79 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the message was 
generated. 
Component Block <OrderQtyData> 
38 
OrderQty 
Y 
Qty 
Total quantity of the order. 
End Component Block 
40 
OrdType 
Y 
Char 
Order type applicable to the order. 
Valid values: 
1 = Market 
2 = Limit 
3 = Stop Market 
4 = Stop Limit  
44 
Price 
 C 
Price (20) 
Price of the order. 
Conditionally required if OrdType 
(40) = ‘2’ Limit or ‘4’ Stop Limit 
99 
StopPx 
C 
Price (20) 
The Stop trigger price. 
Conditionally required if OrdType 
(40): 
3 = Stop Market 
4 = Stop Limit 
TriggerPriceType (1107) is required 
if a Stop Price is specified. 
Component Block <TriggeringInstruction> 
1100 
TriggerType 
C 
Char 
Trigger prompt for stop order 
elements.  
Conditionally required if any other 
Triggering tags are specified. 
Valid value: 
4 = Price Movement 
1102 
TriggerPrice 
C* 
Price (20) 
Stop order price of the OCO. 
Conditionally required for an OCO. 
1107 
TriggerPriceType 
C* 
Char 
Type of price event that triggers the 
stop order:


---
*Page 80*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 80 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Valid values: 
2 = Last Trade  
4 = Best Bid or Last Trade 
5 = Best Offer or Last Trade 
Conditionally required if StopPx 
(99) or TriggerPrice (1102) is 
specified 
1110 
TriggerNewPrice 
C* 
Price (20) 
Limit order price of the stop once 
triggered. 
Conditionally required if Trigger 
Order Type (1111) = '2' Limit 
1111 
TriggerOrderType 
C* 
Char 
Order type of the stop once 
triggered. 
Valid values: 
1 = Market 
2 = Limit 
Conditionally required for an OCO. 
End Component Block 
59 
TimeInForce 
N 
Char 
Specifies how long the order 
remains in effect. 
Valid values: 
0 = Day 
1 = Good Till Cancel 
3 = Immediate or Cancel 
4 = Fill or Kill 
6 = Good Till Date 
Absence of this field indicates Day. 
432 
ExpireDate 
C 
LocalMktDate 
The expiry date of an order. 
Conditionally required if 
TimeInForce (59) = Good Till Date. 
Format is YYYYMMDD. 
528 
OrderCapacity 
Y* 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL


---
*Page 81*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 81 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
R (riskless principal) = MTCH 
529 
OrderRestrictions 
Y* 
Char 
Restrictions associated with an 
order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
58 
Text 
N 
String (50) 
Free text. 
1724 
OrderOrigination 
N 
Int 
Identifies the origin of the order. 
Valid value: 
5 = Order received from a direct 
access or sponsored access 
customer (the trader has direct 
electronic access – DEA). 
Absence of this field indicates DEA 
= false 
2362 
SelfMatchPreventionID 
N 
Int (9) 
Identifies an order that should not 
be matched to an opposite order if 
both buy and sell orders for the 
trade contain the same 
SelfMatchPreventionID (2362) and 
are submitted by the same 
member. 
Component Block <OrderAttributeGrp> 
2593 
NoOrderAttributes 
N 
NumInGrp (1) 
Number of order attribute entries. 
>2594 
OrderAttributeType 
C* 
Int 
The type of order attribute, see 
Order Attribute Type Usage.  
Conditionally required if 
NoOrderAttributes (2593) > 0.  
Valid values: 
0 = Aggregated order. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580  Article 2(3), 
when OrderAttributeValue (2595) = 
Y, it signifies that the order consists 
of several orders aggregated


---
*Page 82*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 82 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
together. This maps to the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580  
value "AGGR".  
1 = Pending allocation. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580  Article 2(2), 
when OrderAttributeValue (2595) = 
Y, it signifies that the order 
submitter "is authorized under the 
legislation of a Member State to 
allocate an order to its client 
following submission of the order to 
the trading venue and has not yet 
allocated the order to its client at 
the time of the submission of the 
order". This maps to the UK version 
of Commission Delegated 
Regulation (EU) No 2017/580 value 
"PNAL". 
2 = Liquidity Provision Order. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580  Article 3, when 
OrderAttributeValue (2595) = Y, it 
signifies that the order was 
submitted "as part of a market 
making strategy pursuant to Articles 
17 and 18 of the UK version of 
Directive 2014/65/EU or is 
submitted as part of another activity 
in accordance with Article 3" (of the 
UK version of Commission 
Delegated Regulation (EU) No 
2017/580). 
3 = Risk Reduction Order. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/590Article 4(2)(i), 
when OrderAttributeValue (2595) = 
Y, it signifies that the commodity 
derivative order is a transaction "to


---
*Page 83*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 83 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
reduce risk in an objectively 
measurable way in accordance with 
Article 57 of the UK version of 
Directive 2014/65/EU". 
>2595 
OrderAttributeValue 
C* 
String (1) 
The value associated with the order 
attribute type specified in 
OrderAttributeType (2594). 
Conditionally required if 
NoOrderAttributes (2593) > 0. 
Valid value: 
Y = Yes 
End Component Block 
Example Message Flow 
Market order 
 
4.11.4 
New Order Cross (s) 
New Order Cross (35=s) is used to submit a cross order into a market. The cross order contains two 
sides: a buy and a sell. An Execution Report (35=8), Reject (35=3) or Business Message Reject 
(35=j) is sent in response.  
Tag 
Field Name 
Req 
Data Type 
Description 
548 
CrossID 
Y 
String (18) 
Unique identifier set by 
the order originator.


---
*Page 84*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 84 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
549 
CrossType 
Y 
Int 
Type of cross being 
submitted to a market 
Valid values:  
101 = Guaranteed 
102 = Non-Guaranteed 
550 
CrossPrioritization  
Y 
Int 
Indicates if one side or 
the other of a cross order 
should be prioritized 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
Component Block <SideCrossOrdModGrp> 
552 
NoSides 
Y 
Int 
Number of Side repeating 
group instances, must be 
2 sides.  
>54 
Side 
Y 
Char 
Side of the order 
Valid values: 
1 = Buy 
2 = Sell 
>11 
ClOrdID 
Y 
String (18) 
Unique identifier set by 
the order originator. 
>Component Block <Parties> 
Y* 
See Parties Component Block 
The following PartyRole (452) values are 
mandatory:  
'11' Order Origination Trader  
‘81’ Broker Client ID  
'301' Execution Within Firm 
>581 
AccountType 
Y* 
Int 
Specifies the type of 
account associated with 
the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office 
account (JBO) = Gross 
OSA


---
*Page 85*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 85 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
101 = Client OSA 
For contracts assigned to 
the T4 booking model 
only 3 = House is valid 
whereas for the T2 
booking model all account 
types are valid. 
>Component Block <OrderQtyData> 
>38 
OrderQty 
Y 
Qty 
Total quantity of the 
order. Must be the same 
on Buy and Sell side of 
Cross.  
>End Component Block <OrderQtyData> 
>528 
OrderCapacity 
Y* 
Char 
Indicates the trading 
capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = 
MTCH 
>529 
OrderRestrictions 
Y* 
Char 
Restrictions associated 
with an order. 
Valid values: 
D = Non-algorithmic 
(human) 
E = Algorithmic (algo) 
>Component Block <OrderAttributeGrp> 
>2593 
NoOrderAttributes 
N 
NumInGrp (1) 
Number of order attribute 
entries. 
>>2594 
OrderAttributeType 
C* 
Int 
The type of order 
attribute, see Order 
Attribute Type Usage.  
Valid values: 
0 = Aggregated order. In 
the context of the UK


---
*Page 86*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 86 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
version of Commission 
Delegated Regulation 
(EU) No 2017/580  Article 
2(3), when 
OrderAttributeValue 
(2595) = Y, it signifies that 
the order consists of 
several orders 
aggregated together. This 
maps to the UK version of 
Commission Delegated 
Regulation (EU) No 
2017/580  value "AGGR".  
1 = Pending allocation. In 
the context of the UK 
version of Commission 
Delegated Regulation 
(EU) No 2017/580  Article 
2(2), when 
OrderAttributeValue 
(2595) = Y, it signifies that 
the order submitter "is 
authorized under the 
legislation of a Member 
State to allocate an order 
to its client following 
submission of the order to 
the trading venue and has 
not yet allocated the order 
to its client at the time of 
the submission of the 
order". This maps to the 
UK version of 
Commission Delegated 
Regulation (EU) No 
2017/580 value "PNAL". 
2 = Liquidity Provision 
Order. In the context of 
the UK version of 
Commission Delegated 
Regulation (EU) No 
2017/580  Article 3, when 
OrderAttributeValue 
(2595) = Y, it signifies that


---
*Page 87*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 87 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
the order was submitted 
"as part of a market 
making strategy pursuant 
to Articles 17 and 18 of 
the UK version of 
Directive 2014/65/EU or is 
submitted as part of 
another activity in 
accordance with Article 3" 
(of the UK version of 
Commission Delegated 
Regulation (EU) No 
2017/580). 
3 = Risk Reduction Order. 
In the context of the UK 
version of Commission 
Delegated Regulation 
(EU) No 2017/590Article 
4(2)(i), when 
OrderAttributeValue 
(2595) = Y, it signifies that 
the commodity derivative 
order is a transaction "to 
reduce risk in an 
objectively measurable 
way in accordance with 
Article 57 of the UK 
version of Directive 
2014/65/EU". 
 
Conditionally required if 
NoOrderAttributes (2593) 
> 0.  
>>2595 
OrderAttributeValue 
C* 
String (1) 
The value associated with 
the order attribute type 
specified in 
OrderAttributeType 
(2594). 
Valid value: 
Y = Yes


---
*Page 88*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 88 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Conditionally required if 
NoOrderAttributes (2593) 
> 0. 
>End Component Block <OrderAttributeGrp> 
End Component Block < SideCrossOrdModGrp > 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument 
identifier 
22 
SecurityIDSource 
Y* 
String (1) 
Identifies the source of 
the SecurityID (48): 
8 = Exchange Symbol 
Conditionally required 
when SecurityID (48) is 
specified. 
End Component Block < Instrument > 
18 
ExecInst 
N 
Char 
Instructions for order 
handling.  
Valid values: 
o = Cancel on connection 
loss 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the 
message was generated. 
40 
OrdType 
Y 
Char 
Order type applicable to 
the order. 
Valid values: 
2 = Limit  
44 
Price 
 Y* 
Price (20) 
Price of the order. 
58 
Text 
N 
String (50) 
Free text. 
4.11.5 
Order Cancel Replace Request (G) 
Order Cancel Replace Request (35=G) is used to change the parameters of an existing order. If 
successful an Execution Report (35=8) is returned to confirm replacement of the order otherwise an 
Order Cancel Reject (35=9) is returned if the request is rejected and the order remains unchanged.


---
*Page 89*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 89 
 
 
The following tags will not be available on an Order Cancel Replace Request and will therefore retain 
the value supplied on order entry: 
• 
AccountType (581) 
• 
SelfMatchPreventionID (2362) 
• 
TriggerPriceType (1107)  
• 
TriggerOrderType (1111). 
Similarly the Party details that cannot be amended will also not be present and therefore remain 
unchanged. The submission of party details that cannot be amended will result in the Order Cancel 
Replace Request being rejected. 
Tag 
Field Name 
Req 
Data Type 
Description 
37 
OrderID 
N 
String (19) 
A unique order identifier assigned by 
the trading system. This identifier is 
not changed by cancel/replace 
messages; it will remain the same for 
all chain of orders. 
Component Block <Parties> 
Y* 
See Parties Component Block 
The PartyID (448) of the following mandatory PartyRole 
(452) can be modified:  
301 = Execution Within Firm 
 
The PartyID (448) of the following PartyRole (452) values 
can be modified 
300 = Investment Decision Within Firm 
302 = Investment Decision Country 
303 = Execution Decision Country 
304 = Client Branch Country 
For the above roles, if the party was not specified on the 
original order, it can be added. If previously included it can 
be amended or it can be omitted to indicate that the party 
has been removed and not retained from previous order 
submissions. 
41 
OrigClOrdID 
Y 
String (18) 
Original order identified as the order to 
be amended. It is the ID of the latest 
non-rejected order (not the initial order 
of the day). 
11 
ClOrdID 
Y 
String (18) 
Unique identifier set by the order 
originator.


---
*Page 90*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 90 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
18 
ExecInst 
C* 
MultipleCharValue 
Instructions for order handling. If more 
than one instruction is applicable to an 
order, this field can contain multiple 
instructions separated by space. 
Valid value: 
6 = Participate but don’t initiate 
(required for Post only order 
submission) 
o = Cancel on connection loss 
Conditionally required if specified on 
the original order and must match the 
previous submission. 
Component Block <DisplayInstruction> 
1138 
DisplayQty 
C* 
Qty 
Visible quantity for an Iceberg order. 
Conditionally required if specified on 
the original order. 
End Component Block 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument identifier. 
Must be the same as the original 
order. 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the SecurityID 
(48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
Y 
Char 
Must be the same value as original 
order. 
Valid values: 
1 = Buy 
2 = Sell


---
*Page 91*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 91 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the message was 
generated. 
Component Block <OrderQtyData> 
38 
OrderQty 
Y 
Qty 
New order quantity. Note: this is not 
the LeavesQty (151) but the new total 
quantity of the order. 
End Component Block 
40 
OrdType 
Y 
Char 
The order type must be the same as 
the original order however a 
previously triggered Stop Limit or Stop 
Market order will be restated as a Limit 
order.  
Valid values: 
1 = Market 
2 = Limit 
3 = Stop Market 
4 = Stop Limit 
44 
Price 
C 
Price (20) 
Price of the order. 
Conditionally required for all Limit 
order types. 
99 
StopPx 
C 
Price (20) 
The Stop trigger price. 
Conditionally required if OrdType (40): 
3 = Stop Market 
4 = Stop Limit. 
Component Block <TriggeringInstruction> 
1100 
TriggerType 
C* 
Char 
Trigger prompt for stop order 
elements.  
Conditionally required if OCO 
Triggering tags are specified.  
Not required if StopPx (99) is 
specified. 
Valid value: 
4 = Price Movement


---
*Page 92*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 92 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
1102 
TriggerPrice 
C* 
Price (20) 
Stop order price of the OCO. 
Conditionally required if specified on 
the original order. 
1110 
TriggerNewPrice 
C* 
Price (20) 
Limit order price of the stop once 
triggered. Conditionally required if 
specified on the original order. 
End Component Block 
59 
TimeInForce 
C* 
Char 
Specifies how long the order remains 
in effect. Conditionally required if 
specified on the original order and 
must match with the previous 
submission.  
Valid values: 
0 = Day 
1 = Good Till Cancel 
3 = Immediate or Cancel 
4 = Fill or Kill 
6 = Good Till Date 
Absence of this field indicates Day. 
432 
ExpireDate 
C 
LocalMktDate 
The expiry date of an order. 
Conditionally required if TimeInForce 
(59) = Good Till Date is specified. 
Format is YYYYMMDD. 
528 
OrderCapacity 
Y* 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
529 
OrderRestrictions 
Y* 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
58 
Text 
N 
String (50) 
Free text. Can be amended if 
supplied.


---
*Page 93*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 93 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
If the field is not specified on the 
original order and is added this 
indicates an amendment. 
Absence of the field indicates that 
previously entered free text has been 
removed. 
1724 
OrderOrigination 
N 
Int 
Identifies the origin of the order. 
Valid value: 
5 = Order received from a direct 
access or sponsored access (the 
trader has direct electronic access – 
DEA) 
Absence of this field indicates DEA = 
false 
Component Block <OrderAttributeGrp> 
An OrderAttributeType (2594) e.g. 3 = Risk Reduction Order specified on the original order and 
present on the amendment indicates that the attribute is unchanged.  
Absence of the attribute indicates that it has been removed. 
If an attribute is not specified on the original order and is added this indicates an amendment. 
2593 
NoOrderAttributes 
N 
NumInGrp (1) 
Number of order attribute entries. 
>2594 
OrderAttributeType 
C* 
Char 
The type of order attribute, see Order 
Attribute Type Usage.  
Conditionally required if 
NoOrderAttributes (2593) > 0. 
Valid values: 
0 = Aggregated order. In the context of 
the UK version of Commission 
Delegated Regulation (EU) No 
2017/580 Article 2(3), when 
OrderAttributeValue (2595) = Y, it 
signifies that the order consists of 
several orders aggregated together. 
This maps to the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580 value "AGGR". 
1 = Pending allocation. In the context 
of the UK version of Commission


---
*Page 94*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 94 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Delegated Regulation (EU) No 
2017/580 Article 2(2), when 
OrderAttributeValue (2595) = Y, it 
signifies that the order submitter "is 
authorized under the legislation of a 
Member State to allocate an order to 
its client following submission of the 
order to the trading venue and has not 
yet allocated the order to its client at 
the time of the submission of the 
order". This maps to the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580 value "PNAL". 
2 = Liquidity Provision Order. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/580 Article 3, when 
OrderAttributeValue (2595) = Y, it 
signifies that the order was submitted 
"as part of a market making strategy 
pursuant to Articles 17 and 18 of the 
UK version of Directive 2014/65/EU or 
is submitted as part of another activity 
in accordance with Article 3" (of the 
UK version of Commission Delegated 
Regulation (EU) No 2017/580). 
3 = Risk Reduction Order. In the 
context of the UK version of 
Commission Delegated Regulation 
(EU) No 2017/590 Article 4(2)(i), when 
OrderAttributeValue (2595) = Y, it 
signifies that the commodity derivative 
order is a transaction "to reduce risk in 
an objectively measurable way in 
accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
>2595 
OrderAttributeValue C* 
String (1) 
The value associated with the order 
attribute type specified in 
OrderAttributeType (2594). 
Conditionally required if 
NoOrderAttributes (2593) > 0. 
Valid value:


---
*Page 95*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 95 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Y = Yes 
End Component Block 
Example Message Flow 
Amend Order 
 
4.11.6 
Order Cancel Request (F) 
Order Cancel Request (35=F) is used to cancel the remaining quantity of an existing order. An 
Execution Report (35=8) is returned to confirm cancellation or an Order Cancel Reject (35=9) if the 
cancel is rejected. 
Tag 
Field Name 
Req 
Data Type 
Description 
41 
OrigClOrdID 
Y 
String (18) 
Order identifier for the order to cancel. It is 
the ID of the latest non-rejected order (not 
the initial order of the day).


---
*Page 96*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 96 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
37 
OrderID 
N 
String (19) 
A unique order identifier set by the trading 
system. This identifier is not changed by 
cancel/replace messages; it will remain the 
same for all chain of orders. 
11 
ClOrdID 
Y 
String (18) 
Unique identifier set by the order originator. 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when SecurityID (48) 
is specified. 
End Component Block 
54 
Side 
Y 
Char 
Side of the order. 
Valid values: 
1 = Buy 
2 = Sell 
60 
TransactTime 
Y 
UTCTimestamp Timestamp when the message was 
generated.  
4.11.7 
Order Cancel Reject (9) 
Order Cancel Reject (35=9) is returned in response to Order Cancel/Replace Request (35=G), Order 
Cancel Request (35=F) or Cross Order Cancel Request (u) that cannot be honoured. The unchanged 
order will remain in the order book if it has not already been cancelled or has expired. 
Tag 
Field Name 
Req 
Data Type 
Description 
37 
OrderID 
Y 
String (19) 
A unique order identifier set by the trading 
system. This identifier is not changed by 
cancel/replace messages; it will remain 
the same for all chain of orders. 
Set to NONE when OrdStatus (39) = 
Rejected and CxlRejReason (102) = ‘1’ 
Unknown order.


---
*Page 97*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 97 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
11 
ClOrdID 
Y 
String (18) 
Unique identifier set by the order 
originator. 
41 
OrigClOrdID 
Y 
String (18) 
Original order identified for the order to 
modify. It is the ID of the latest non-
rejected order (not the initial order of the 
day). 
39 
OrdStatus 
Y 
Char 
Order status as at the time of rejection. 
Valid values: 
0 = New 
1 = Partially Filled 
2 = Filled 
3 = Done for day 
4 = Cancelled 
6 = Pending Cancel 
8 = Rejected 
A = Pending New 
C = Expired 
E = Pending Replace 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the message was 
generated.  
434 
CxlRejResponseTo 
Y 
Char 
Identifies the type of request that an Order 
Cancel Reject (9) is in response to. 
Valid values: 
1 = Order Cancel Request (F) / Cross 
Order Cancel Request (u) 
2 = Order Cancel/Replace Request (G) 
102 
CxlRejReason 
Y* 
Int 
Code that identifies the reason for the 
rejection. 
Valid values: 
0 = Too late to cancel 
1 = Unknown order 
3 = Order already in Pending Cancel or 
Pending Replace Status 
6 = Duplicate ClOrderID (11) received 
18 = Invalid price increment 
99 = Other


---
*Page 98*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 98 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
1328 
RejectText 
C* 
String (75) 
Conditionally required if CxlRejReason 
(102) = '99' Other. 
 Text specifying the reason for rejection. 
1819 
RelatedHighPrice 
C* 
Price 
Upper price limit value 
1820 
RelatedLowPrice 
C* 
Price 
Lower price limit value 
4.11.8 
Cross Order Cancel Request (u) 
Cross Order Cancel Request (35=u) is used to cancel a cross order held in the RFC interval. An 
Execution Report (35=8) per side is returned to confirm cancellation, or an Order Cancel Reject 
(35=9) per side is returned if the cancel is rejected. 
 
Tag 
Field Name 
Req 
Data Type 
Description 
548 
CrossID 
Y 
String (18) 
Unique identifier set by 
the originator. 
551 
OrigCrossID 
Y 
String (18) 
Unique identifier of the 
original cross, set by the 
originator. 
549 
CrossType 
Y 
Int 
Type of cross being 
submitted to a market 
Valid values:  
101 = Guaranteed 
102 = Non-Guaranteed 
550 
CrossPrioritization  
Y 
Int 
Indicates which side of 
the cross will be 
prioritized 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
Component Block <SideCrossOrdCxlGrp> 
552 
NoSides 
Y 
Int 
Number of Side repeating 
group instances, must be 
2 sides.


---
*Page 99*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 99 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
>54 
Side 
Y 
Char 
Side of the order 
Valid values: 
1 = Buy 
2 = Sell 
>41 
OrigClOrdID 
N 
String (18) 
Unique identifier of the 
original order, set by the 
order originator. 
>11 
ClOrdID 
Y 
String (18) 
Unique identifier set by 
the order originator. 
End Component Block < SideCrossOrdCxlGrp > 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument 
identifier 
22 
SecurityIDSource 
Y* 
String (1) 
Identifies the source of 
the SecurityID (48): 
8 = Exchange Symbol 
Conditionally required 
when SecurityID (48) is 
specified. 
End Component Block < Instrument > 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the 
message was generated. 
961 
HostCrossID 
N 
String (19) 
A unique order identifier 
assigned by the trading 
system. This identifier is 
not changed by cancel 
messages; it will remain 
the same for all chain of 
cross orders.


---
*Page 100*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 100 
 
 
4.11.9 
Execution Report (8) 
Execution Report (35=8) is used to: 
• 
confirm the receipt of an order 
• 
confirm changes to an existing order (i.e. accept cancel and replace requests) 
• 
confirm or convey an order cancellation or expiration 
• 
convey order or trade cancellation by Market Operations 
• 
convey fill information 
• 
convey triggering of a stop order 
• 
reject orders 
• 
convey speed bump processing 
• 
convey information about restated long orders carried from one trading day to the next. 
• 
convey cross order processing 
ExecType (150) identifies the purpose of the execution report message and OrdStatus (39) conveys 
the current state of the order. 
The attributes that can be returned in an Execution Report for each execution type are listed in the 
Execution Report Matrix. 
Tag 
Field Name 
Req 
Data Type 
Description 
37 
OrderID 
Y 
String (19) 
A unique order identifier set by 
the trading system. This identifier 
is not changed by cancel/replace 
messages; it will remain the 
same for all chain of orders. 
11 
ClOrdID 
Y* 
String (18) 
Client specified identifier in the 
message that caused this 
Execution Report. 
41 
OrigClOrdID 
C 
String (18) 
ClOrdID (11) of the previous 
order (NOT the initial order of the 
day) as assigned by the 
institution. Identifies the previous 
order in cancel and 
cancel/replace requests. 
Conditionally required according 
to Execution Report Matrix. 
961 
HostCrossID 
C* 
String (19) 
Unique order identifier used by 
exchange to reference a cross.


---
*Page 101*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 101 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
 Conditionally required if CrossID 
is populated 
Component Block <Parties> 
Y* 
See Parties Component Block 
548 
CrossID 
C* 
String (18) 
Identifier for the cross order, set 
by the trader. Unique per trader, 
per day.  
Conditional Required for Cross 
Order 
551 
OrigCrossID 
C* 
String (18) 
CrossID referencing the cross to 
be cancelled 
Conditionally required if CrossID 
is populated 
549 
CrossType 
C* 
Int 
Type of cross submitted to the 
market.  
 
Identifies whether it is a 
guaranteed or non guaranteed 
cross.  
 
Valid values:  
101 = Guaranteed 
102 = Non-Guaranteed 
 
Conditionally required if CrossID 
is populated 
550 
CrossPrioritization 
C* 
int 
Indicates which side of the cross 
order should be prioritised. 
Identifies the initiating side.  
 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
 
Conditionally required if CrossID 
is populated 
1430 
VenueType 
C* 
Char 
Valid values:  
O = Offbook 
B = Central limit order book 
(CLOB)


---
*Page 102*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 102 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Conditionally required if CrossID 
is populated and ExecType (150) 
= ‘F’ Trade. 
880 
TrdMatchID 
C* 
String (19) 
Identifier assigned by the trading 
system which joins buy and sell 
half trades. 
Conditionally required if 
ExecType (150) = ‘F’ Trade. 
17 
ExecID 
Y 
String (19) 
Unique identifier assigned by the 
trading system to the execution 
message. 
19 
ExecRefID 
C* 
String (19) 
Reference identifier used with 
Trade Cancel execution type. 
Conditionally required if 
ExecType (150) = ‘H’ Trade 
Cancel. 
150 
ExecType 
Y 
Char 
Describes the specific Execution 
Report. 
Valid values: 
0 = New 
3 = Done  
4 = Cancelled  
5 = Replaced 
8 = Rejected 
C = Expired  
D = Restated  
E = Pending Replace 
F = Trade  
H = Trade Cancel 
L = Triggered or Activated by the 
System  
39 
OrdStatus 
Y 
Char 
Identifies current status of order. 
Valid values: 
0 = New 
1 = Partially Filled 
2 = Filled 
3 = Done for day 
4 = Cancelled


---
*Page 103*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 103 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
6 = Pending Cancel 
8 = Rejected 
A = Pending New 
C = Expired 
E = Pending Replace 
103 
OrdRejReason 
C* 
Int 
Code to identify reason for order 
rejection. 
Conditionally required if 
ExecType (150) = ‘8’ Rejected 
Valid values: 
6 = Duplicate Order 
15 = Unknown Account(s) 
18 = Invalid price increment 
99 = Other 
378 
ExecRestatementReason C* 
Int 
Conditionally required if 
ExecType (150) = ‘D’ Restated. 
The reason for restatement. 
Valid values: 
1 = GT renewal / restatement 
99 = Other. See 
ExecTypeReason (2431) for 
speed bump handling. 
581 
AccountType 
Y* 
Int 
Specifies the type of account 
associated with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account 
(JBO) = Gross OSA 
101 = Client OSA 
For contracts assigned to the T4 
booking model only 3 = House is 
valid whereas for the T2 booking 
model all account types are valid. 
1115 
OrderCategory 
C* 
Char 
Conditionally required for a trade 
from an implied order when 
ExecType (150) = ‘F’ Trade.


---
*Page 104*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 104 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Defines the type of interest 
behind a trade (fill or partial fill). 
Valid value: 
7 = Implied Order 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
Y 
Char 
Side of the order 
Valid values: 
1 = Buy 
2 = Sell 
Component Block <OrderQtyData> 
38 
OrderQty 
Y* 
Qty 
Total order quantity of the order. 
End Component Block 
40 
OrdType 
Y* 
Char 
Order type applicable to the 
order. 
Valid values: 
1 = Market 
2 = Limit 
3 = Stop Market 
4 = Stop Limit  
44 
Price 
C 
Price (20) 
The order price.  
Conditionally required if OrdType 
(40) = ‘2’ Limit or ‘4’ Stop Limit. 
99 
StopPx 
C* 
Price (20) 
The Stop trigger price. 
Conditionally required if OrdType


---
*Page 105*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 105 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
(40) = ‘3’ Stop Market or ‘4’ Stop 
Limit. 
TriggerPriceType (1107) is 
required if StopPx is specified. 
Component Block <TriggeringInstruction> 
1100 
TriggerType 
C* 
Char 
Trigger prompt for the stop order 
elements.  
Conditionally required if any other 
Triggering tags are specified. 
Valid value: 
4 = Price Movement 
1102 
TriggerPrice 
C* 
Price (20) 
Stop order price of the OCO. 
Conditionally required for an 
OCO. 
1107 
TriggerPriceType 
C* 
Char 
Type of price event that triggers 
the stop order: 
Valid values: 
2 = Last Trade 
4 = Best Bid or Last Trade 
5 = Best Offer or Last Trade 
Conditionally required if StopPx 
(99) or TriggerPrice (1102) is 
specified 
1110 
TriggerNewPrice 
C* 
Price (20) 
Limit order price of the stop once 
triggered. 
Conditionally required if 
TriggerOrderType (1111) = '2' 
Limit 
1111 
TriggerOrderType 
C* 
Char 
Order type of the order once 
triggered. 
Valid values: 
1 = Market 
2 = Limit 
Conditionally required for an 
OCO.


---
*Page 106*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 106 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
End Component Block 
59 
TimeInForce 
Y* 
Char 
Specifies how long the order 
remains in effect. 
Valid values: 
0 = Day 
1 = Good Till cancel (GTC) 
3 = Immediate or cancel (IOC) 
4 = Fill or Kill 
6 = Good Till Date (GTD) 
432 
ExpireDate 
C 
LocalMktDate 
The expiry date of an order. 
Conditionally required if 
TimeInForce (59) = ‘0’ Day or ‘6’ 
Good Till Date. 
Format is YYYYMMDD. 
18 
ExecInst 
C* 
MultipleCharValue 
Instructions for order handling. If 
more than one instruction is 
applicable to an order, this field 
can contain multiple instructions 
separated by space. 
Valid values: 
6 = Participate but don’t initiate 
for Post Only orders 
o = Cancel on connection loss 
Conditionally required according 
to Execution Report Matrix. 
1057 
AggressorIndicator 
C* 
Boolean 
Indicates if a matching order is an 
aggressor or not in the trade. 
Y = Aggressor 
N = Passive 
Conditionally required if 
ExecType (150) = ‘F’ Trade. 
528 
OrderCapacity 
Y* 
Char 
Designates the capacity of the 
firm placing the order. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL


---
*Page 107*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 107 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
R (riskless principal) = MTCH 
529 
OrderRestrictions 
Y* 
MultipleCharValue 
Indicates if the order is entered 
either by an algo trader or a 
human. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
32 
LastQty 
C 
Qty 
Conditionally required if 
ExecType (150) = ‘F’ Trade.  
The total volume of this trade. 
31 
LastPx 
C 
Price (20) 
Conditionally required if 
ExecType (150) = ‘F’ Trade.  
The price of this trade. 
151 
LeavesQty 
Y 
Qty 
The quantity open for further 
execution.  
If OrdStatus (39) = '4' Cancelled, 
'C' Expired or '8' Rejected then 
LeavesQty (151) could be 0 
otherwise LeavesQty (151) will 
be OrderQty (38) - CumQty (14) 
14 
CumQty 
Y 
Qty 
The quantity of the order that has 
been executed so far. 
60 
TransactTime 
Y* 
UTCTimestamp 
Timestamp when the message 
was generated.  
Component Block <DisplayInstruction> 
1138 
DisplayQty 
C* 
Qty 
Visible quantity for Iceberg 
orders. 
Conditionally required for an 
Iceberg order. 
End Component Block 
58 
Text 
C* 
String (50) 
Contains the value supplied in 
this field on the order.


---
*Page 108*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 108 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Conditionally required according 
to Execution Report Matrix. 
Component Block <InstrmtLegExecGrp> 
555 
NoLegs 
C* 
NumInGrp (2) 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument. 
Number of InstrumentLeg 
repeating group instances. 
Component Block <InstrumentLeg> - Required if NoLegs (555) > 0. 
>602 
LegSecurityID 
C* 
Int 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument. 
Multileg tradable instrument's 
individual SecurityID. 
>603 
LegSecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
LegSecurityID (602) is specified. 
>624 
LegSide 
C* 
Char 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument. 
The side of this individual leg 
(multileg security). 
Valid values: 
1 = Buy 
2 = Sell 
End Component Block 
>1366 
LegAllocID 
C* 
String (19) 
Strategy leg trade identifier 
assigned by the trading system 
which is shared by half trades. 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument.


---
*Page 109*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 109 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
>637 
LegLastPx 
C* 
Price (20) 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument. 
Execution price assigned to the 
leg of the multileg tradable 
instrument. 
>1418 
LegLastQty 
C* 
Qty 
Conditionally required if 
ExecType (150) = ‘F’ Trade on a 
multileg tradable instrument. 
Fill quantity for the instrument 
leg. 
End Component Block 
1328 
RejectText 
C* 
String (75) 
Identifies the reason for rejection. 
Conditionally required if 
ExecTypeReason (2431) = '4' 
Unsolicited order cancellation or 
OrdRejReason (103) = ‘99’ 
Other. 
1724 
OrderOrigination 
C* 
Int 
Origin of the order 
Valid value: 
5 = Order received from a direct 
access or sponsored access 
customer (the trader has direct 
electronic access – DEA) 
Absence of this field indicates 
DEA = false. 
Conditionally required according 
to Execution Report Matrix. 
2431 
ExecTypeReason 
C* 
Int 
The initiating event for the 
Execution Report. 
Conditionally required to report: 
• 
unsolicited cancellation 
• 
order status in New 
Order Cross processing


---
*Page 110*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 110 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
• 
order status in speed 
bump processing. 
Valid values: 
4 = Unsolicited order cancellation 
101 = Order accepted but speed 
bump applied 
102 = Order added after speed 
bump 
103 = Order cancelled whilst in 
speed bump delay 
104 = Original order is in speed 
bump enforced delay 
105 = Order updated after speed 
bump delay 
106 = Amend is in speed bump 
delay 
107 = Order amended after 
speed bump delay 
108 = Order rejected after speed 
bump delay 
109 = Unsolicited cancel while in 
speed bump 
120 = Order held in RFC interval 
2362 
SelfMatchPreventionID 
C* 
Int (9) 
Identifies an order that should not 
be matched to an opposite order 
if both buy and sell orders for the 
trade contain the same 
SelfMatchPreventionID (2362) 
and are submitted by the same 
member. 
Conditionally required according 
to Execution Report Matrix.  
Component Block <OrderAttributeGrp> - Conditionally required if specified. 
2593 
NoOrderAttributes 
C* 
NumInGrp (1) 
Number of order attribute entries. 
>2594 
OrderAttributeType 
C* 
Int 
The type of order attribute, see 
Order Attribute Type Usage.  
Conditionally required if 
NoOrderAttributes (2593) > 0. 
Valid values:


---
*Page 111*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 111 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
0 = Aggregated order. In the 
context of the UK version of 
Commission Delegated 
Regulation (EU) No 2017/580 
Article 2(3), when 
OrderAttributeValue (2595) = Y, it 
signifies that the order consists of 
several orders aggregated 
together. This maps to the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580  
value "AGGR". 
1 = Pending allocation. In the 
context of the UK version of 
Commission Delegated 
Regulation (EU) No 2017/580 
Article 2(2), when 
OrderAttributeValue (2595) = Y, it 
signifies that the order submitter 
"is authorized under the 
legislation of a Member State to 
allocate an order to its client 
following submission of the order 
to the trading venue and has not 
yet allocated the order to its client 
at the time of the submission of 
the order". This maps to the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580 
value "PNAL". 
2 = Liquidity Provision Order. In 
the context of the UK version of 
Commission Delegated 
Regulation (EU) No 2017/580 
Article 3, when 
OrderAttributeValue (2595) = Y, it 
signifies that the order was 
submitted "as part of a market 
making strategy pursuant to 
Articles 17 and 18 of the UK 
version of Directive 2014/65/EU 
or is submitted as part of another 
activity in accordance with Article 
3" (of the UK version of


---
*Page 112*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 112 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Commission Delegated 
Regulation (EU) No 2017/580). 
3 = Risk Reduction Order. In the 
context of the UK version of 
Commission Delegated 
Regulation (EU) No 2017/590 
Article 4(2)(i), when 
OrderAttributeValue (2595) = Y, it 
signifies that the commodity 
derivative order is a transaction 
"to reduce risk in an objectively 
measurable way in accordance 
with Article 57 of the UK version 
of Directive 2014/65/EU". 
>2595 
OrderAttributeValue 
C* 
String (1) 
The value associated with the 
order attribute type specified in 
OrderAttributeType (2594). 
Conditionally required if 
NoOrderAttributes (2593) > 0. 
Valid value: 
Y = Yes 
End Component Block 
1819 
RelatedHighPrice 
C* 
Price 
Upper price limit value 
For Stop orders, this will be the 
stop tolerance band. 
1820 
RelatedLowPrice 
C* 
Price 
Lower price limit value


---
*Page 113*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 113 
 
 
Example Message Flows 
OCO submitted, Stop triggered and Limit cancelled 
An OCO order is submitted as a Limit offer with a Market Stop trigger price of 6808, an incoming offer 
triggers the Stop order and cancels Limit element of the OCO. An Execution Report is not sent for 
cancellation. The triggered Market Stop is converted to a Limit order at a trigger new price of 6808.


---
*Page 114*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 114 
 
 
OCO Partial Trade 
OCO is submitted as Limit offer for 15 lots at 1825 with a Market Stop trigger price of 1780. 
A Limit bid is submitted at 1830 for 10 lots. The OCO order is not triggered but trades 10 lots with the 
incoming order. The OCO remains in the order book with a residual volume of 5 lots


---
*Page 115*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 115 
 
 
Implied trade


---
*Page 116*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 116 
 
 
 
Custom strategy Butterfly trades


---
*Page 117*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 117 
 
 
Order cancellation by Exchange


---
*Page 118*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 118 
 
 
Order rejected price limits breached


---
*Page 119*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 119 
 
 
4.11.9.1 Execution Report Matrix 
An Execution Report can be returned in response to a request e.g. New Order Single (35=D) or unsolicited in response to a particular action. 
The tags that can be included are contingent on the purpose of the message and any mandatory or conditionally supplied tags specified by the originator in the initiating request 
or returned response to a particular action. 
Legend: 
M = Mandatory 
C = Conditional 
The following table indicates the tags that will be returned for specific execution types: 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
OrderID (37) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
ClOrdID (11) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
OrigClOrdID (41) 
 
 
 
 
M 
M 
M 
M 
 
 
 
 
 
 
 
HostCrossID (961) 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
Parties component block 
PartyRole (452) 
 
1 = Executing Firm  
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M


---
*Page 120*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 120 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
3 = Client ID 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
4 = Clearing Firm  
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
7 = Entering Firm  
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
11 = Order Origination 
Trader  
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
24 = Customer Account  
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
26 = Correspondent 
broker 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
36 = Entering Trader  
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
66 = Market Maker 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
81 = Broker Client ID 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
122 = Decision Maker  
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
300 = Investment 
Decision Within Firm 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
301 = Execution Within 
Firm 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M


---
*Page 121*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 121 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
302 = Investment 
Decision Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
303 = Execution Decision 
Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
304 = Client Branch 
Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
CrossID (548) 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
OrigCrossID (551) 
 
 
 
 
 
 
 
C 
C 
 
 
 
 
 
 
CrossType (549) 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
CrossPrioritization (550) 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
VenueType (1430) 
 
 
 
 
 
 
 
 
 
 
 
C 
C 
C 
 
TrdMatchID (880) 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
ExecID (17) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
ExecRefID (19) 
 
 
 
 
 
 
 
 
 
 
 
 
 
M 
 
ExecType (150) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M


---
*Page 122*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 122 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
OrdStatus (39) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
OrdRejReason (103) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
M 
ExecRestatementReason 
(378) 
 
M 
 
M 
 
 
 
 
 
 
 
 
 
 
 
AccountType (581) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
OrderCategory (1115) 
 
 
 
 
 
 
 
 
 
 
 
C 
C 
C 
 
SecurityID (48) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
SecurityIDSource (22) 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
Side (54) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
OrderQty (38) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
OrdType (40) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
Price (44) 
C 
C 
M 
C 
C 
C 
C 
C 
C 
C 
C 
M 
M 
M 
C


---
*Page 123*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 123 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
StopPx (99) 
C 
C* 
M 
 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TriggerType (1100) 
C 
C1 
M 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TriggerPrice (1102) 
C 
C1 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TriggerPriceType (1107) 
C 
C1 
M 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TriggerNewPrice (1110) 
C 
C1 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TriggerOrderType (1111) 
C 
C1 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
TimeInForce (59) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
ExpireDate (432) 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
ExecInst (18) 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
C 
AggressorIndicator 
(1057) 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
OrderCapacity (528) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
 
* StopPx (99) and TriggeringInstruction component block tags will not be present when a previously triggered Stop order is restated as a Limit order.


---
*Page 124*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 124 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
OrderRestrictions (529) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
LastQty (32) 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
LastPx (31) 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
LeavesQty (151) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
CumQty (14) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
TransactTime (60) 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
M 
DisplayQty (1138) 
C 
C 
 
C 
C 
C 
C 
C 
C 
C 
C 
C 
 
C 
C 
Text (58) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
NoLegs (555) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
LegSecurityID (602) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
LegSecurityIDSource 
(603) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
LegSide (624) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
LegAllocID (1366) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C


---
*Page 125*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 125 
 
 
Tag 
Order 
Accepted 
Order 
Restated 
(GTC/GTD) 
Order 
Triggered 
Order 
Restated 
(Speed 
Bump) 
Order 
Replaced 
Order 
Pending 
Replace 
Order 
Replaced 
(after 
Speed 
Bump) 
Order 
Cancelled 
(Solicited) 
Order 
Cancelled 
(Unsolicited) 
Order 
Expired 
Done 
for 
Day 
Outright 
Filled 
Strategy 
Filled 
Trade 
Busted 
Order 
Rejected 
LegLastPx (637) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
LegLastQty (1418) 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
RejectText (1328) 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
OrderOrigination (1724) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
ExecTypeReason (2431) 
C 
 
 
M 
 
M 
M 
C 
M 
 
 
 
 
 
 
SelfMatchPreventionID 
(2362) 
C 
C 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
NoOrderAttributes (2593) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
OrderAttributeType 
(2594) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
OrderAttributeValue 
(2595) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
RelatedHighPrice (1819) 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
RelatedLowPrice (1820) 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C


---
*Page 126*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 126 
 
 
4.11.10 Order Mass Cancel Request (q) 
Order Mass Cancel Request (35=q) is used to cancel the remaining quantity of a group of orders 
matching criteria specified within the message. Persisted orders will be included in the cancellation 
request. An Execution Report will be sent for each order cancelled followed by the Order Mass 
Cancel Report (35=r).  
Cross orders that are held in an RFC interval and match the criteria specified in the Order Mass 
Cancel Request will be included in the cancellation request. If one of the orders in a cross matches 
the criteria specified then both orders in the cross will be cancelled. The TotalAffectedOrders (533) 
count in the Order Mass Cancel Report (35=r) will include both sides 
Order Mass Cancel Report will be returned if the request is accepted or rejected. 
Tag 
Field Name 
Req 
Data Type 
Description 
11 
ClOrdID 
Y 
String (18) 
Unique ID of Order Mass Cancel 
Request as assigned by the 
institution. 
This identifier will be returned in 
ClOrdID (11) in the Execution 
Report of each order cancelled. 
530 
MassCancelRequestType Y 
Char 
Specifies the type of cancellation 
requested 
Valid values: 
1 = Cancel orders for a Security ID 
(tradable instrument) 
3 = Cancel orders for a Product 
(contract e.g. CADF - Copper 
Future) 
7 = Cancel all orders 
Component Block <Parties> 
C* 
 
See Parties Component Block 
Conditionally required for 
MassCancelRequestType (530) = '7' 
(Cancel all orders) to specify the 
PartyID (448) when cancelling 
orders for a specific end client, 
PartyRole (452) = '81' Broker Client 
ID. 
If not specified, orders will be 
cancelled for the FIX Comp ID of the 
message originator. 
Component Block <Instrument>


---
*Page 127*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 127 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
207 
SecurityExchange 
C* 
Exchange (4) 
Market which is used to identify the 
security: 
XLME 
Conditionally required if Symbol (55) 
is specified only valid for 
MassCancelRequestType (530) = ‘3’ 
Cancel orders for a Product. 
1227 
ProductComplex 
C* 
String (4) 
Identifies an entire suite of products 
for a given market. 
Valid values: 
LME = Base  
Conditionally required if Symbol (55) 
is specified only valid for 
MassCancelRequestType (530) = ‘3’ 
Cancel orders for a Product 
55 
Symbol 
C* 
String (20) 
Symbol for the LME contract code 
e.g. CADF (Copper Future) or OCDF 
(Copper Monthly Average Future) 
Conditionally required if 
MassCancelRequestType (530) = '3' 
Cancel orders for a Product 
48 
SecurityID 
C* 
Int 
Tradable instrument identifier. 
Conditionally required if 
MassCancelRequestType (530) = '1' 
Cancel orders for a Security ID. 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
N 
Char 
Optional qualifier to indicate the side 
of the market for which orders are to 
be cancelled. Can be used if


---
*Page 128*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 128 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
MassCancelRequestType (530) = '3' 
Cancel orders for a Product. 
Absence of this field indicates that 
orders are to be cancelled 
regardless of side. 
60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the message was 
generated. 
4.11.11 Order Mass Cancel Report (r) 
Order Mass Cancel Report (35=r) is returned in response to an Order Mass Cancel Request (35=q). 
Each affected order that is cancelled is acknowledged with a separate Execution Report (35=8). 
Tag 
Field Name 
Req 
Data Type 
Description 
11 
ClOrdID 
N 
String (18) 
ClOrdID provided on the Order 
Mass Cancel Request. 
1369 
MassActionReportID 
Y 
String (20) 
Unique Identifier for the Order Mass 
Cancel Report assigned by the 
system 
530 
MassCancelRequestType 
Y 
Char 
Specifies the type of cancellation 
required: 
Valid values: 
1 = Cancel orders for a SecurityID 
3 = Cancel orders for a Product 
(Symbol) 
7 = Cancel all orders 
531 
MassCancelResponse 
Y 
Char 
Indicates the action taken on the 
cancel request: 
Valid values: 
0 = Cancel request rejected 
1 = Cancel orders for a SecurityID 
3 = Cancel orders for a Product 
(Symbol) 
7 = Cancel all orders 
532 
MassCancelRejectReason C* 
Int 
Indicates why the Order Mass 
Cancel Request was rejected. 
Conditionally required if


---
*Page 129*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 129 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
MassCancelResponse (531) = ‘0’ 
Cancel request rejected. 
Valid values: 
1 = Invalid or Unknown Security 
3 = Invalid or Unknown Product 
99 = Other 
533 
TotalAffectedOrders 
Y* 
Int 
Indicates the total number of orders 
affected by the Order Mass Cancel 
Request. 
Component Block <Parties> 
C* 
 
See  Parties Component Block 
Conditionally required for 
MassCancelRequestType (530) = 7 
(Cancel all orders) to specify the 
PartyID (448) when cancelling 
orders for a specific end client, 
PartyRole (452) = '81' Broker Client 
ID. 
Component Block <Instrument> 
207 
SecurityExchange 
C* 
Exchange (4) 
Market which is used to identify the 
security: 
XLME 
Conditionally required if Symbol 
(55) is specified. 
1227 
ProductComplex 
C* 
String (4) 
Identifies an entire suite of products 
for a given market. 
Valid values: 
LME = Base  
Conditionally required if Symbol 
(55) is specified 
55 
Symbol 
C* 
String (20) 
Symbol for the LME contract code 
e.g. CADF (Copper Future) or 
OCDF (Copper Monthly Average 
Future) 
Conditionally required if 
MassCancelRequestType (530) = 
'3' Cancel orders for a Product


---
*Page 130*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 130 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
48 
SecurityID 
C* 
Int 
Tradable instrument identifier. 
Conditionally required if 
MassCancelRequestType (530) = 
'1' Cancel orders for a Security ID. 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
N 
Char 
Optional qualifier to indicate the 
side of the market for which orders 
are to be cancelled. Can be used if 
MassCancelRequestType (530) = 
'3' Cancel orders for a Product. 
Absence of this field indicates that 
orders are to be cancelled 
regardless of side. 
60 
TransactTime 
Y* 
UTCTimestamp Timestamp when the message was 
generated. 
58 
Text 
C* 
String (75) 
Identifies the reason for rejection. 
Conditionally required if 
MassCancelRejectReason (532) = 
'99' Other. 
4.11.12 Quote Request (R) 
Quote Request (35=R) is used to requests prices from market participants. 
The Quote Request is disseminated via the Market Data service to market participants. If successful 
a Quote Response (35=AJ) is sent in acknowledgement otherwise a Quote Request Reject (AG) is 
returned if the request is rejected. 
Tag 
Field Name 
Req 
Data Type 
Description 
131 
QuoteReqID 
Y 
String (18) 
Client specified identifier for quote 
request.


---
*Page 131*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 131 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
Component Block <QuotReqGrp>  
146 
NoRelatedSym 
Y 
NumInGrp (1) 
Number of related symbols (instruments) 
in this request. 
The value can only be 1. 
Component Block <Instrument> 
>48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
>22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the SecurityID 
(48): 
8 = Exchange Symbol 
Conditionally required when SecurityID 
(48) is specified. 
End Component Block 
>303 
QuoteRequestType 
Y* 
Int 
Indicates the type of Quote Request being 
generated. 
Valid values: 
1 = Manual - used to indicate a single 
quote request 
2 = Automatic - used to indicate a 
streaming quote request 
>54 
Side 
N 
Char 
Side of order. If not defined indicates a 
two-sided quote is required. 
Valid values: 
1 = Buy 
2 = Sell 
>60 
TransactTime 
Y 
UTCTimestamp 
Timestamp when the message was 
generated.  
Component Block <OrderQtyData> 
>38 
OrderQty 
N 
Qty 
Order quantity. 
If not entered, a volume of 0 will be 
published 
End Component Blocks


---
*Page 132*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 132 
 
 
4.11.13 Quote Response (AJ) 
Quote Response (35=AJ) is returned by the gateway to acknowledge a successful Quote Request 
(35=R). 
Tag 
Field Name 
Req 
Data Type 
Description 
693 
QuoteResponseID 
Y 
String (18) 
Message reference for the Quote 
Response. 
131 
QuoteReqID 
Y 
String (18) 
Identifier supplied on Quote 
Request (R) message. 
694 
QuoteRespType 
Y 
Int 
Identifies the type of Quote 
Response. 
Valid value: 
11 = Accept 
Component Block <Instrument> 
48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
54 
Side 
C* 
Char 
Side of order. 
Valid values: 
1 = Buy 
2 = Sell 
Conditionally required if specified 
on the original message. 
60 
TransactTime 
Y 
UTCTimestamp Timestamp when the message 
was generated.  
Component Block <OrderQtyData> 
38 
OrderQty 
C* 
Qty 
Order quantity. 
Conditionally required if specified 
on the original message.


---
*Page 133*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 133 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
End Component Block 
Example Message Flow 
Successful RFQ Submission 
 
4.11.14 Quote Request Reject (AG) 
Quote Request Reject (35=AG) notifies the originator that their Quote Request (35=R) has been 
rejected. 
Tag 
Field Name 
Req 
Data Type 
Description 
131 
QuoteReqID 
Y 
String (18) 
Client specified identifier for the 
quote request. 
658 
QuoteRequestRejectReason Y 
Int 
Reason the Quote Request (R) 
was rejected. 
Valid value: 
99 = Other.  
Text (58) will contain more specific 
information. 
Component Block <QuotReqRjctGrp> 
146 
NoRelatedSym 
Y 
NumInGrp (1) 
Number of related symbols 
(instruments) in the Quote 
Request.


---
*Page 134*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 134 
 
 
Tag 
Field Name 
Req 
Data Type 
Description 
The value can only be 1. 
Component Block <Instrument> 
>48 
SecurityID 
Y* 
Int 
Tradable instrument identifier 
>22 
SecurityIDSource 
C* 
String (1) 
Identifies the source of the 
SecurityID (48): 
8 = Exchange Symbol 
Conditionally required when 
SecurityID (48) is specified. 
End Component Block 
>54 
Side 
C* 
Char 
Side of order. 
Valid values: 
1 = Buy 
2 = Sell 
Conditionally required if specified 
on the original message. 
>60 
TransactTime 
Y 
UTCTimestamp Timestamp when the message 
was generated.  
Component Block <OrderQtyData> 
>38 
OrderQty 
C* 
Qty 
Order quantity. 
Conditionally required if specified 
on the original message. 
End Component Blocks 
58 
Text 
C* 
String (75) 
Identifies the reason for rejection. 
Conditionally required if 
QuoteRequestRejectReason (658) 
= '99' Other.


---
*Page 135*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 135 
 
 
Example Message Flow 
Quote Request rejected


---
*Page 136*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 136 
 
 
Appendix A: Inflight Order Handling 
A.1 
Standard Gateway Behaviour 
No inflight order handling, order instructions follow platform acknowledgement. 
 
1. 
A new order is submitted by the client and confirmed by the Matching Engine (ME). 
2. 
This is followed by an amendment to the parent order which is also confirmed. 
3. 
Followed by a cancellation of the amended order which is also confirmed. 
A.2 
Inflight Cancellation 
Cancellation for the parent order is queued in the gateway until an acknowledgement has been 
received from the ME by the gateway. 
 
1. 
A new order is submitted by the client. 
2. 
Whilst the trading platform (gateway and ME) is processing the new order request, the client 
sends a cancellation request. The cancellation request is queued in the gateway until the 
gateway has received an acknowledgement for the new order from the ME.


---
*Page 137*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 137 
 
 
3. 
On receipt of the acknowledgement for the parent order from the ME, the gateway releases the 
cancellation request to the ME to be processed. 
4. 
Once the cancellation has been processed by the ME. The ME sends an acknowledgement to 
the gateway which is sent onward to the client. 
A.3 
Inflight Amendment 
The process for an inflight amendment follows an identical process to that for an inflight cancellation. 
 
1. 
 A new order is submitted. 
2. 
Whilst the new order request is being processed, the client sends an amendment request. The 
amendment is queued in the gateway. 
3. 
On receipt of the acknowledgement for the parent order from the ME, the gateway releases the 
amendment request to the ME. 
4. 
Once the amendment has been processed by the ME and the order has been replaced. The ME 
sends an acknowledgement to the gateway which is sent onward to the client.


---
*Page 138*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 138 
 
 
A.4 
Inflight Amendment and Cancellation 
Inflight amendment and cancellation request are queued in the gateway until an acknowledgement 
has been received for the previous instruction by the gateway from the ME. 
 
1. 
A new order is submitted.  
2. 
Followed by an amendment to the original order (before the parent order has been 
acknowledged) and is queued at the gateway until parent order is acknowledged.  
3. 
Followed by a cancellation for the amendment (before the parent and amendment have been 
acknowledged). This is queued in the gateway until the parent order and then the amendment 
has been processed. 
4. 
The ME sends an acknowledgement for the parent order to the gateway. The gateway forwards 
an acknowledgement back to the client and releases the amendment request to the ME.


---
*Page 139*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 139 
 
 
5. 
Once the amendment has been processed by the ME and the order has been replaced. The ME 
sends an acknowledgement for the amended order to the gateway. The gateway forwards the 
acknowledgement to the client and releases the cancellation to the ME.  
6. 
The cancellation is processed after all the previous instructions have been 
processed/acknowledged. 
A.5 
Multiple Inflight Amendments and a Cancellation 
The Gateway permits a single amendment request, a second amendment request to replace the 
inflight amendment for the parent order is rejected. 
An amendment request submitted for the parent order followed by a second amendment request 
which is rejected. A cancellation request for the amended parent order is queued in the gateway until 
the initial amendment request is acknowledged by the ME. 
 
1. 
A new order submitted and acknowledged, followed by an amendment to the parent order. 
2. 
Before the amendment has been processed by the ME, a second amendment instruction is 
submitted. 
3. 
The second amendment is rejected as the initial amendment is in progress. 
4. 
A cancellation request is submitted for the amendment in progress is queued at the gateway 
until the amendment has been processed. 
5. 
The ME sends an acknowledgement for the amended order to the gateway. The gateway 
forwards the acknowledgement to the client and releases the cancellation to the ME. 
6. 
The cancellation is processed after all the previous instructions have been 
processed/acknowledged.


---
*Page 140*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 140 
 
 
A.6 
Multiple Inflight Amendments and Cancellations 
Example 1: Two inflight amendments followed by a cancellation referencing the original 
parent, followed by a cancellation referencing a rejected amendment request and one more 
referencing the amended order 
An amendment request submitted for the parent order followed by a second amendment request 
which is rejected (only one inflight amendment request is permitted). Multiple cancellation requests 
are submitted which are rejected due to incorrectly referencing previous order instructions. A 
cancellation for the original parent order is rejected followed by a cancellation request for the second 
amendment request which was rejected. A cancellation request for the amended parent order is 
queued until the amendment is actually processed. 
 
1. 
A new order is submitted and fully acknowledged.  
2. 
The first amendment to the parent order is submitted. 
3. 
Before the first amendment has been processed, a second amendment instruction is submitted. 
4. 
The second amendment is rejected by the gateway as the existing amendment is in progress. 
5. 
A cancellation instruction submitted for the parent order is rejected as it refers to cancelling the 
parent ClOrdID rather than ClOrdID of the amendment.


---
*Page 141*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 141 
 
 
6. 
A second cancellation is submitted referencing the second amendment instruction that was 
rejected. This cancellation request is also rejected as it refers to the ClOrdID of the amendment 
that has already been rejected. 
7. 
A cancellation is submitted for the amendment in progress is queued until the amendment has 
been processed.  
8. 
The ME sends an acknowledgement for the amended order to the gateway. The gateway 
forwards the acknowledgement to the client and releases the cancellation to the ME 
9. 
The cancellation is then processed after all the previous instructions are 
processed/acknowledged. 
Example 2: Two inflight amendments followed by a cancellation referencing the original 
parent and a cancellation referencing the amended order 
An amendment request received for a parent order followed by a second amendment request which 
is rejected (only one inflight amendment request is permitted). A cancellation for the original parent 
order is rejected due to incorrectly referencing previous order instructions. A second cancellation 
request is submitted for the amended order which is queued and then processed. 
 
1. 
A new order is submitted and fully acknowledged. 
2. 
The first amendment to the parent order is submitted.


---
*Page 142*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 142 
 
 
3. 
Before the first amendment has been processed, a second amendment instruction is submitted. 
4. 
Before any of the above have been processed, a cancellation is submitted referencing the 
parent order and the second amendment. 
5. 
The second amendment instruction is rejected by the gateway as an existing amendment is in 
progress. 
6. 
The first cancellation submitted for the parent order is rejected as it refers to cancelling the 
parent ClOrdID rather than ClOrdID of the amendment still pending. 
7. 
The second cancellation instruction is rejected as a second inflight cancellation is not permitted 
and also the request refers to cancelling an unknown ClOrdID. 
8. 
A third cancellation instruction is submitted which references the amendment in progress. This 
request is queued until the amendment has been processed.  
9. 
The ME sends an acknowledgement for the amended order to the gateway. The gateway 
forwards the acknowledgement to the client and releases the cancellation to the ME 
10. The cancellation is then processed after all previous instructions are processed/acknowledged.


---
*Page 143*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 143 
 
 
Appendix B: Speed Bump Inflight Order Handling 
B.1 
Speed Bump Message Flow 
The message flow follows that described in 3.13 Speed Bumps - Executable order amendment for a 
resting order will be speed bumped. 
 
1. 
A new order is submitted and acknowledged as being speed bumped.  
2. 
The order is added to the order book and acknowledged once it has cleared the speedbump.  
3. 
An amendment is submitted for the parent order and acknowledged as being speed bumped.  
4. 
The amended order replaces the parent and is acknowledged once it has cleared the speed 
bump. 
5. 
A cancellation is submitted which is exempt from the speed bump cancels the amended order in 
the order book.


---
*Page 144*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 144 
 
 
B.2 
Inflight Cancellation in Speed Bump 
The message flow follows that described in 3.13 Speed Bumps - Order cancellation for a speed 
bumped order.  
 
1. 
A new order submitted and acknowledged as being speed bumped. 
2. 
A cancellation is submitted for the order which is in the speed bump. 
3. 
The cancellation is exempt from the speed bump cancels the order in the speed bump.  
B.3 
Inflight Cancellation past Speed Bump 
The message flow follows that described in 3.13 Speed Bumps - Order submission is speed bumped 
but also includes a cancellation. 
 
1. 
A new order is submitted and acknowledged as being speed bumped. The order is added to the 
order book and acknowledged once it has cleared the speedbump.  
2. 
A cancellation is submitted which is exempt from the speed bump cancels the order in the order 
book. 
Note: The cancellation can be sent regardless of whether acknowledgements have been received for 
the previous instruction.


---
*Page 145*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 145 
 
 
B.4 
Inflight Amendment Speed Bumped 
The message flow follows that described in 3.13 Speed Bumps - Executable order amendment for a 
speed bumped order will be speed bumped. 
 
1. 
A new order is submitted and acknowledged as being speed bumped.  
2. 
An amendment is submitted for the order in the speedbump. The amendment is acknowledged 
as being speed bumped according to the execution check. 
3. 
Amendment will not be processed until the parent order has cleared the speed bump and been 
added to the order book.  
4. 
The parent order is added to the order book and acknowledged once it has cleared the 
speedbump. 
5. 
The amendment is released from the speed bump and replaces the parent order. The amended 
order is acknowledged once it has been added to the order book.


---
*Page 146*

Order Entry Gateway 
FIX Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 146 
 
 
B.5 
Inflight Amendment not Speed Bumped 
The message flow follows that described in 3.13 Speed Bumps - Non-executable order amendment 
for a speed bumped order will not be speed bumped.  
 
1. 
A new order is submitted and acknowledged as being speed bumped. 
2. 
An amendment is submitted for the order in the speed bump. The amendment is not speed 
bumped but cannot be processed until the parent order has cleared the speed bump. 
3. 
The parent order is added to the order book and acknowledged once it has cleared the 
speedbump 
4. 
The amendment is then released from the queue and replaces the parent order. The amended 
order is acknowledged once it has been added to the order book.
