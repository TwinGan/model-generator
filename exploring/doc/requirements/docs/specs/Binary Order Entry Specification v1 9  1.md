# Binary Order Entry Specification v1 9  1

*Source: Binary Order Entry Specification v1 9  1.pdf*

---

THE LONDON METAL EXCHANGE 
10 Finsbury Square, London EC2A 1AJ | Tel +44 (0)20 7113 8888 
Registered in England no 2128666. Registered office as above.  
LME.COM 
 
 
Order Entry Gateway 
Binary Specification 
Please respond to:  
tradingoperations@lme.com


---
*Page 2*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 2 
 
 
Table of Contents 
1 Session Management ................................................................................................................... 12 
1.1 
Authentication ...................................................................................................................... 12 
1.1.1 
Comp ID ....................................................................................................................... 12 
1.1.2 
Password Encryption ................................................................................................... 12 
1.1.3 
Password ..................................................................................................................... 13 
1.1.4 
Change Password ....................................................................................................... 13 
1.2 
Establishing a Binary Session ............................................................................................. 14 
1.3 
Message Sequence Numbers ............................................................................................. 14 
1.4 
Heartbeat and Test Request ............................................................................................... 14 
1.5 
Terminating a Binary Session .............................................................................................. 15 
1.6 
Re-establishing a Binary Session ........................................................................................ 15 
1.7 
Sequence Reset .................................................................................................................. 15 
1.8 
Fault Tolerance .................................................................................................................... 16 
1.9 
Checksum Validation ........................................................................................................... 16 
2 Recovery ....................................................................................................................................... 17 
2.1 
General Message Recovery ................................................................................................ 17 
2.2 
Resend Request .................................................................................................................. 17 
2.3 
Logon Message Processing – Next Expected Message Sequence .................................... 18 
2.4 
Possible Duplicates ............................................................................................................. 18 
2.5 
Possible Resends ................................................................................................................ 18 
2.6 
Gap Fills ............................................................................................................................... 18 
2.7 
Transmission of Missed Messages ..................................................................................... 19 
2.8 
Technical Halt ...................................................................................................................... 19 
3 Service Description ...................................................................................................................... 20 
3.1 
Security Identification ........................................................................................................... 20 
3.2 
Security Creation ................................................................................................................. 20 
3.2.1 
Strategies ..................................................................................................................... 20 
3.3 
Order Submission ................................................................................................................ 22 
3.4 
Order Types ......................................................................................................................... 22 
3.5 
Order Validity Conditions ..................................................................................................... 24 
3.6 
Order Types and Permitted Order Validity Conditions ........................................................ 24 
3.7 
Order Identification .............................................................................................................. 25


---
*Page 3*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 3 
 
 
3.8 
Order Expiry ......................................................................................................................... 25 
3.9 
Order Restatement .............................................................................................................. 26 
3.10 
Order Amendment ............................................................................................................... 26 
3.11 
Order Cancellation ............................................................................................................... 27 
3.12 
Mass Cancellation ............................................................................................................... 28 
3.13 
Cancel on Disconnect .......................................................................................................... 29 
3.14 
Mass Quote ......................................................................................................................... 29 
3.15 
Auto Cross ........................................................................................................................... 31 
3.16 
Request for Quote (RFQ) .................................................................................................... 37 
3.17 
Speed Bumps ...................................................................................................................... 37 
3.18 
Message Throttling .............................................................................................................. 48 
3.19 
Security Definition Throttle .................................................................................................. 49 
3.20 
Merged Order Books ........................................................................................................... 49 
3.21 
Self Execution Prevention (SEP) ......................................................................................... 51 
3.22 
Market Maker Protection (MMP) .......................................................................................... 52 
3.23 
Inflight Order Processing ..................................................................................................... 53 
3.24 
Trade Reporting ................................................................................................................... 54 
3.25 
Client ID Usage .................................................................................................................... 55 
4 Message Definitions ..................................................................................................................... 56 
4.1 
Inbound Messages .............................................................................................................. 56 
4.2 
Outbound Messages ............................................................................................................ 56 
4.3 
Data Types .......................................................................................................................... 57 
4.4 
Message Composition ......................................................................................................... 59 
4.4.1 
Field Presence Map ..................................................................................................... 60 
4.4.2 
Repeating Blocks and Nested Repeating Blocks ........................................................ 60 
4.5 
Required Fields .................................................................................................................... 62 
4.6 
Message Header ................................................................................................................. 62 
4.7 
Message Trailer ................................................................................................................... 63 
4.8 
Administrative Messages ..................................................................................................... 63 
4.8.1 
Logon (5) ..................................................................................................................... 63 
4.8.2 
Heartbeat (0) ................................................................................................................ 64 
4.8.3 
Test Request (1) .......................................................................................................... 65 
4.8.4 
Resend Request (2) ..................................................................................................... 65


---
*Page 4*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 4 
 
 
4.8.5 
Sequence Reset (4) ..................................................................................................... 69 
4.8.6 
Logout (6) .................................................................................................................... 69 
4.8.7 
Reject (3) ..................................................................................................................... 70 
4.9 
Other Messages .................................................................................................................. 70 
4.9.1 
Business Message Reject (7) ...................................................................................... 70 
4.9.2 
News (40) .................................................................................................................... 71 
4.10 
Application Messages .......................................................................................................... 73 
4.10.1 
Security Definition Request (10) .................................................................................. 73 
4.10.2 
Security Definition (11) ................................................................................................ 75 
4.10.3 
New Order Single (12) ................................................................................................. 78 
4.10.4 
New Order Cross (27) .................................................................................................. 85 
4.10.5 
Amend Order (13) ........................................................................................................ 94 
4.10.6 
Order Amend Rejected (14)....................................................................................... 103 
4.10.7 
Cancel Order (15) ...................................................................................................... 104 
4.10.8 
Order Cancel Rejected (16) ....................................................................................... 105 
4.10.9 
Cancel Cross Order (28) ............................................................................................ 106 
4.10.10 
Execution Report (8) .............................................................................................. 107 
4.10.11 
Mass Cancel Request (17) .................................................................................... 135 
4.10.12 
Mass Cancel Report (18) ....................................................................................... 137 
4.10.13 
Mass Quote (22) .................................................................................................... 141 
4.10.14 
Mass Quote Ack (23) ............................................................................................. 144 
4.10.15 
Quote Request (20) ............................................................................................... 152 
4.10.16 
Quote Request Ack (21) ........................................................................................ 152 
4.10.17 
MMP Reset Request (30) ...................................................................................... 154 
4.10.18 
MMP Reset Ack (31) .............................................................................................. 155


---
*Page 5*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 5 
 
 
Document History 
Version 
Date 
Change Description 
1.0 
27/07/2020 
Initial draft 
1.1 
28/01/2022 
Internal review 
1.2 
24/03/2023 
Internal review 
1.3 
23/06/2023 
4.10.8 added example message flow for order rejected price limits 
breached. Related High Price description includes Stop order handling 
4.10.8 and 4.10.8.1 Direct Electronic Access, Aggregated Order, 
Pending Allocation Order, Liquidity Provision Order, Risk Reduction 
Order and Cancel on Disconnect changed to mandatory. Related High 
Price and Related Low Price conditional for Order Cancelled 
(Unsolicited) 
4.10.4 updated Cancel on Disconnect description 
1.4 
13/10/2023 
1.1.2 password encryption example added 
3.2.1 strategy creation clarified 
4.8.7 and 4.9.1 Text is conditionally required if reject code is Other 
4.10.1 Leg Ratio description and message flow examples 
4.10.8 LastPrice Int64 
1.5 
15/03/2024 
1.1.4 footnote added 
1.1.4.1 password reuse policy 
1.2 duplicate connection termination removed 
3.4 Stop Market and Stop Limit description 
3.9, 3.10 and 4.10.4 restated triggered Stop orders change order type 
3.10 handling for Text and Client Branch Country 
3.12 and 3.19 cancellation by tradable instrument 
4.8.5 Gap Fill default value added 
4.10.3 LEI optional 
4.10.8 Exec Type = ‘E’ Pending Replace returned in speedbump order 
handling 
4.10.8.1 Restated, footnote added for triggered Stops. Triggered, 
mandatory fields. Rejections, Clearing Firm removed 
1.6 
19/07/2024 
1.1.2 public key location


---
*Page 6*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 6 
 
 
Version 
Date 
Change Description 
3.8 expiry conditions 
4.3 additional information on String data type 
4.8.1 Password/New Password String length 
4.8.7/4.9.1 Reference Field Name String length  
4.8.7 and 4.9.1 Text (58) optional 
4.10.8 Expiry Date description, updated message flows 
1.6.1 
02/09/2024 
4.8.1 Password/New Password String length reverted to 450 
1.6.2 
16/09/2024 
2.8 Technical Halt 
1.7 
29/10/2024 
2.8 Technical Halt 
4.3 String data type 
4.10.8.1 replaced P with C 
1.8 
04/02/2025 
4.3 special character usage 
4.8.7/4.9.1 Reference Field Name String length reverted to 50 
1.8.2 
17/05/2025 
4.10.3, 4.10.4, 4.10.8 Guidance for population of: 
a) Client ID Short Code 
b) Decision Maker  
c) Investment Decision within Firm (IDM) and Investment Decision 
Country 
d) Execution Within Firm and Execution Decision Country 
e) Client Branch Country 
f) Regulatory references 
 
1.9.0 
11/09/2025 
3.3 Mention Cross Order 
3.7 Mention Cross Order 
3.11 Mention Cross Order 
3.15 Explain Cross Order 
4.10.4 New Order Cross 
4.10.9 Cancel Cross Order 
4.10.10 Add cross order related fields in Execution Report 
4.10.10.1 Add cross order related fields in Execution Report Matrix


---
*Page 7*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 7 
 
 
Version 
Date 
Change Description 
1.9.01 
 
 
 
11/11/2025 
 
 
 
4.9.1 Added a new enum to Business Reject Code 
4.10.8 Updated the description to include Cancel Cross Order messages 
4.10.9 Updated the description to include Order Cancel Reject 
3.7 Optional cross cancel attributes clarified 
3.11 Optional cross cancel attributes clarified and updated the number of 
messages returned 
3.15 Optional cross cancel attributes clarified and corrected an example 
flow 
4.10.9 Clarified the number of messages returned 
4.10.11 Updated to include Cross orders 
4.9.1 Remove ‘Cross order volume mismatch’ enum  
4.10.10 Updated to include cross processing 
Corrected typos 
4.10.10 Corrected Execution with Firm advice 
1.9.1 
02/12/2025 
Updated version


---
*Page 8*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 8 
 
 
Preface 
This document describes the binary interface protocol of the LME Order Entry Gateway.  
The terminology used, message format, message flow and event models described throughout this 
document are similar to that of FIX 5.0 SP2 protocol specifications (https://www.fixtrading.org) where 
applicable, with some specific changes for performance and adaptability reasons. 
Message flow examples in this document are illustrations and do not contain all the mandatory fields. 
The presence of (…) denotes that fields have been omitted. 
Bit position is shown as BP in the message definitions. 
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
4.10.1 Security Definition Request (10) 
Options strategies: 
• 
Call spread 
• 
Put spread 
3.2.1.1 Exchange Defined Strategy Types 
4.10.1 Security Definition Request (10) 
Custom strategies 
3.2.1. Strategies 
3.2.1.2 Custom Strategies 
4.10.1 Security Definition Request (10) 
4.10.2 Security Definition (11) (Example Message Flows) 
4.10.8 Execution Report (8) (Example Message Flow) 
Option contracts 
3.2 Security Creation 
3.2.1.1 Exchange Defined Strategy Types 
3.2.1.2 Custom Strategies 
4.10.1 Security Definition Request (10)


---
*Page 9*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 9 
 
 
Function 
Reference 
4.10.2 Security Definition (11) (Example Message Flows) 
Order types: 
• 
Market 
• 
Stop Market 
• 
Iceberg 
• 
Post Only 
• 
One Cancels Other 
3.4 Order Types 
3.6 Order Types and Permitted Order Validity Conditions 
3.10 Order Amendment (Display Quantity) 
4.10.3 New Order Single (12) 
4.10.4 Amend Order (13) 
4.10.8 Execution Report (8) 
4.10.8.1 Execution Report Matrix 
Order validity condition: 
• 
Fill or Kill (FOK) 
3.5 Order Validity Conditions 
3.6 Order Types and Permitted Order Validity Conditions 
4.10.3 New Order Single (12) 
4.10.4 Amend Order (13) 
4.10.8 Execution Report (8) 
Mass Quote 
2.7 Transmission of Missed Messages 
3.7 Order Identification 
3.3 Order Submission 
3.10 Order Amendment 
3.11 Order Cancellation 
3.12 Mass Cancellation 
3.14 Mass Quote 
3.17 Message Throttling 
3.24 Client ID Usage 
4.1 Inbound Messages 
4.2 Outbound Messages 
4.4.2 Repeating Blocks and Nested Repeating Blocks 
4.10.7 Order Cancel Rejected (16) 
4.10.8 Execution Report (8) 
4.10.8.1 Execution Report Matrix 
4.10.9 Mass Cancel Request (17) 
4.10.10 Mass Cancel Report (18)


---
*Page 10*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 10 
 
 
Function 
Reference 
4.10.11 Mass Quote (22) 
4.10.12 Mass Quote Ack (23) 
Request for Cross 
4.10.4 New Order Cross (27) 
4.10.9 Cancel Cross Order (28) 
4.10.10 Execution Report (8) 
Request for Quote 
2.7 Transmission of Missed Messages 
3.15 Request for Quote (RFQ) 
3.17 Message Throttling 
4.1 Inbound Messages 
4.2 Outbound Messages 
4.10.13 Quote Request (20) 
4.10.14 Quote Request Ack (21) 
Speed Bumps 
3.16 Speed Bumps 
4.10.8 Execution Report (8) 
4.10.8.1 Execution Report Matrix 
Self Execution Prevention 
3.20 Self Execution Prevention (SEP) 
4.10.3 New Order Single (12) 
4.10.4 Amend Order (13) 
4.10.8 Execution Report (8) 
4.10.8.1 Execution Report Matrix 
Market Maker Protection 
2.7 Transmission of Missed Messages 
3.7 Order Identification 
3.17 Message Throttling 
3.21 Market Maker Protection (MMP) 
4.1 Inbound Messages 
4.2 Outbound Messages 
4.9.2 News (40) 
4.10.15 MMP Reset Request (30) 
4.10.16 MMP Reset Ack (31)


---
*Page 11*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 11


---
*Page 12*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 12 
 
 
1 
Session Management 
1.1 Authentication 
1.1.1 
Comp ID 
A participant user should use the Comp ID (a unique session identifier) provided by the Exchange for 
each session in order to connect to the gateway. A single participant may have multiple connections 
to the gateway, i.e. multiple binary order entry sessions, each with its own Comp ID. 
The messages sent to the gateway should contain the Comp ID assigned to the client in the field 
Comp ID in the header section of a message. 
1.1.2 
Password Encryption 
The binary protocol requires Password and New Password to be encrypted when they are sent in the 
Logon (5) message from the client to the gateway.  
To encrypt the password, the client is expected to use a 2048-bit RSA 
(https://en.wikipedia.org/wiki/RSA_(cryptosystem)) public key circulated by the Exchange on 
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
 
String pubKey = new String(keyBytes, "UTF-8"); 
 
pubKey = pubKey.replaceAll("(-+BEGIN PUBLIC KEY-+\\r?\\n|-+END PUBLIC KEY-
+\\r?\\n?)", ""); 
 
pubKey = pubKey.replaceAll("(-+BEGIN RSA PUBLIC KEY-+\\r?\\n|-+END RSA 
PUBLIC KEY-+\\r?\\n?)", ""); 
 
pubKey = pubKey.replaceAll("\\n|\\r",""); 
 
KeyFactory keyFactory = KeyFactory.getInstance("RSA");


---
*Page 13*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 13 
 
 
X509EncodedKeySpec keySpec = new 
X509EncodedKeySpec(Base64.getDecoder().decode(pubKey.getBytes())); 
 
publicKey = keyFactory.generatePublic(keySpec); 
1.1.3 
Password 
The client should specify their password in the Password field of the Logon (5) message. This 
password must be in encrypted form. For security reasons, the client is expected to prefix the login 
time, in UTC format (YYYYMMDDHHMMSS), to the password before encryption. The client must 
ensure that login time is in accurate UTC.  
The gateway will extract the login time prefix from the decrypted password string and validate that it 
is within the acceptable tolerance of the actual current time. A logon request from the client that fails 
this validation is rejected by the gateway.  
The gateway validates the password, any validation failure will result in logon attempt being 
unsuccessful. 
Repeated failures in password validation will result in the client account being locked. The participant 
is expected to contact the Exchange to unlock the client account. 
1.1.4 
Change Password 
Each new Comp ID will be assigned a password by the Exchange. The client is expected to change 
this password upon initial logon. 
Each new Comp ID will be assigned a password on registration. The client is expected to change the 
password upon first logon whenever a password is (re)issued by the Exchange.  
Password change request can be made together with Logon (5) request. The client should specify 
the encrypted new password in the New Password field and the current encrypted password in the 
Password field.  
The new password must comply with Exchange’s password policy1. The status of the new password 
(i.e. whether it is accepted or rejected) will be specified in the Session Status response from the 
gateway. The new password, if accepted, will be effective for subsequent logins. If the new password 
provided fails validation, the gateway will reject the logon attempt.   
1.1.4.1 Password Policy 
The Exchange requires the password to contain: 
• 
Minimum of 8 characters 
• 
At least one number 
• 
Combination of uppercase and lowercase characters. 
Password history is retained and therefore the last 24 passwords cannot be reused. 
 
1 Note: The new password should not include the timestamp before it is encrypted. The timestamp 
should only be used for the login password.


---
*Page 14*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 14 
 
 
1.2 Establishing a Binary Session 
The client must wait for a successful Logon (5) response from the gateway before sending additional 
messages. If any message is received from the client before the exchange of logon messages, the 
TCP/IP connection with the client will be disconnected. 
If a logon attempt fails, the gateway will send a Logout (6) and terminate the session; the Session 
Status of the Logout (6) message will indicate the reason for the logout. 
If a session level failure occurs due to a message sent by the client which contains a sequence 
number that is less than what is expected and the PossDup is not set to 1 (Yes), then the gateway 
will send a Logout (6) and terminate the binary connection. In this scenario, the inbound sequence 
number will not be incremented but the outbound sequence number will be incremented. 
If the gateway does not respond to the session initiation (client initiated Logon message), it is 
recommended that the client wait for a duration of 60 seconds prior to terminating the connection. 
The client is expected to retry session initiation after an elapsed time duration of 60 seconds. 
If a client is disconnected abruptly or via a Logout message from the gateway, it is recommended 
that the client wait for a duration of 10 seconds prior to reconnecting to the gateway. 
1.3 Message Sequence Numbers 
The client and the gateway will each maintain a separate and independent set of incoming and 
outgoing message sequence numbers. Sequence numbers should be initialized to one (1) at the start 
of the day and be incremented throughout the session. Either side of a binary session will track the: 
• 
Next Expected MsgSeqNum (starting at 1) in Logon (5) 
• 
Sequence Number in the Message Header (starting at 1) to the contra-party. 
The Sequence Number in the Message Header is always incremented by the sender, whereas the 
Next Expected MsgSeqNum is only updated as a result of an incoming message. 
Monitoring sequence numbers will enable either parties to identify and react to the missed messages 
and gracefully synchronize applications when reconnecting a binary session. 
Any message sent by either side of a binary session will increment the sequence number unless 
explicitly specified for a given message type.  
If any message sent by one side of a binary session contains a sequence number that is LESS than 
the Next Expected MsgSeqNum then the other side of this session is expected to send a Logout 
message and terminate the binary connection immediately, unless the PossDup indicator is set to 1 
(Yes) 
A binary session will not be continued to the next trading day. Both sides are expected to initialize 
(reset to 1) the sequence numbers at the start of each day.  At the start of each trading day if the 
client starts with a Next Expected MsgSeqNum greater than 1 then the gateway will send a Logout 
message and terminate the session immediately without any further exchange of messages. 
1.4 Heartbeat and Test Request 
The client and the gateway will use the Heartbeat (0) message to monitor the communication line 
during periods of inactivity and to verify that the interfaces at each end are available.


---
*Page 15*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 15 
 
 
The gateway will send a Heartbeat anytime it has not transmitted a message for the duration of the 
heartbeat interval. The client is expected to employ the same logic. 
If the gateway detects inactivity for a period longer than 3 heartbeat intervals, it will send a Test 
Request message to force a Heartbeat from the client. If a response to the Test Request is not 
received within a reasonable transmission time (recommended being an elapsed time equivalent to 3 
heartbeat intervals), the gateway will send a Logout (6) and break the TCP/IP connection with the 
client. The client is expected to employ similar logic if inactivity is detected on the part of the gateway. 
1.5 Terminating a Binary Session 
Session termination can be initiated by either the gateway or the client by sending a Logout (6) 
message. Upon receiving the logout request, the contra party will respond with a Logout (6) message 
signifying a logout reply. Upon receiving the logout reply, the receiving party will terminate the 
connection. 
If the contra-party does not reply with either a Resend Request (2) or a Logout (6) reply, the logout 
initiator should wait for 60 seconds prior to terminating the connection.  
The client is expected to terminate each binary session at the end of each trading day before the 
gateway service is shut down. Any open binary connection will be terminated by the gateway by 
sending a Logout (6) when the service is shut down. Under exceptional circumstances, the gateway 
may initiate the termination of a connection during the trading day by sending the Logout (6) 
message. 
If, during the exchange of logout messages, the client or the gateway detects a sequence gap, it 
should send a Resend Request (2). 
1.6 Re-establishing a Binary Session 
If a binary connection is terminated during the trading day, it may be re-established via an exchange 
of Logon messages. 
Once the binary session is re-established, the message sequence numbers will continue from the 
last message successfully transmitted prior to the termination as described in 2.7 Transmission of 
Missed Messages. 
1.7 Sequence Reset 
Gap-fill mode can be used by one side when skipping session level messages which can be ignored 
by the other side.  
During a binary session the gateway or the client may use the Sequence Reset (4) message in Gap 
Fill mode if either side wishes to increase the expected incoming sequence number of the other 
party. 
It will not be possible to reset the client sequence number to 1 using the Logon message. Should a 
reset be required the participant should contact the Exchange. 
The client is required to support a manual request by Exchange to initialize sequence numbers prior 
to the next login attempt.


---
*Page 16*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 16 
 
 
1.8 Fault Tolerance 
After a failure on the client side or on the gateway side, the client is expected to be able to continue 
with the same session. 
If the sequence number is reset to one (1) by the gateway, all previous messages from the gateway 
will not be available for the client side. 
The client and the gateway are expected to negotiate on the Next Expected MsgSeqNum and Next 
To Be Received Sequence number by contacting the Exchange prior to initiating the new session 
and consequently manually setting the sequence number for both ends after having a direct 
communication with the participant. 
1.9 Checksum Validation 
The gateway performs a checksum validation on all incoming messages into the input services. 
Incoming messages that fail the checksum validation will be rejected and the connection will be 
dropped by the gateway without sending a logout. 
Conversely, the gateway stamps an identically calculated checksum field on all outgoing messages 
from the input interfaces. In case of a checksum validation failure, the client is expected to drop the 
connection and take any appropriate action before reconnecting. Messages that fail the checksum 
validation should not be processed. 
This checksum is a CRC32C value with the polynomial 0x1EDC6F41, presented as a 32-bit unsigned 
integer (http://en.wikipedia.org/wiki/Cyclic_redundancy_check#CRC-32C).


---
*Page 17*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 17 
 
 
2 
Recovery 
2.1 General Message Recovery 
Message gaps may occur which are detected via the tracking of incoming sequence numbers. 
Recovery will be initiated if a gap is identified when an incoming message sequence number is found 
to be greater than Next Expected MsgSeqNum during Logon or the Sequence Number at other 
times. 
The Resend Request (2) will indicate the Start Sequence and End Sequence of the message gap 
identified and when replying to a Resend Request (2), the messages are expected to be sent strictly 
honouring the sequence. 
If messages are received outside of the Start Sequence and End Sequence, then the recovering 
party is expected to queue those messages until the gap is recovered. 
During the message recovery process, the recovering party will increment the Next Expected 
MsgSeqNum accordingly based on the messages received. If messages applicable to the message 
gap are received out of sequence then the recovering party will drop these messages. 
The party requesting the Resend Request (2) can specify “0” in the End Sequence to indicate that 
they expect the sender to send ALL messages starting from the Start Sequence. In this scenario, if 
the recovering party receives messages with a sequence greater than the Start Sequence, out of 
sequence, the message will be ignored. 
Administrative messages such as Sequence Reset (4), Heartbeat (0) and Test Request (1) which 
can be considered irrelevant for a retransmission could be skipped using the Sequence Reset (4) 
message in gap-fill mode. Note that the gateway expects the client to skip Sequence Reset (4) 
messages when replying to a Resend Request (2) at all times. 
When resending messages, the gateway would use either PossDup or PossResend indicator to 
indicate whether the messages were retransmitted earlier. If PossDup is set, it indicates that the 
same message with the given sequence number with the same business content may have been 
transmitted earlier. In the case where PossResend is set, it indicates that the same business content 
may have been transmitted previously but under the different message sequence number. In this 
case business contents needs to be processed to identify the resend. For example, in execution 
reports the Exec ID may be used for this purpose. 
2.2 Resend Request 
The client may use the Resend Request (2) message to recover any lost messages. This message 
may be used in one of three modes: 
1. 
To request a single message. The Start Sequence and End Sequence should be the same. 
2. 
To request a specific range of messages. The Start Sequence should be the first message of 
the range and the End Sequence should be the last of the range. 
3. 
To request all messages after a particular message. The Start Sequence should be the 
sequence number immediately after that of the last processed message and the End Sequence 
should be zero (0).


---
*Page 18*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 18 
 
 
2.3 Logon Message Processing – Next Expected Message Sequence 
The session initiator should supply the Next Expected MsgSeqNum the value next expected from the 
session acceptor in Sequence Number. The session acceptor should validate the logon request 
including that Next Expected MsgSeqNum does not represent a gap. It then constructs its logon 
response with Next Expected MsgSeqNum containing the value next expected from the session 
initiator in Sequence Number having incremented the number above the logon request if that was the 
sequence expected. 
The session initiator must wait until the logon response is received in order to submit application 
messages. Once the logon response is received, the initiator must validate that Next Expected 
MsgSeqNum does not represent a gap.  
In case of gap detection from either party (lower than the next to be assigned sequence) recover all 
messages from the last message delivered prior to the logon through the specified Next Expected 
MsgSeqNum sending them in order, then gap fill over the sequence number used in logon and 
proceed sending newly queued messages with a sequence number one higher than the original 
logon. 
Neither side should generate a Resend Request (2) based on Sequence Number of the incoming 
Logon message but should expect any gaps to be filled automatically by following the Next Expected 
Sequence processing described above. Whilst the gateway is resending messages to the client, the 
gateway does not allow another Resend Request (2) from the client. If a new Resend Request (2) is 
received during this time, the gateway will terminate the session immediately without sending the 
Logout (6) message. 
Note that indicating the Next Expected MsgSeqNum in Logon (5) is mandatory. 
2.4 Possible Duplicates 
The gateway handles possible duplicates in the same way as the FIX protocol. The client and the 
gateway use the PossDup field to indicate that a message may have been previously transmitted 
with the same Sequence Number. 
2.5 Possible Resends 
The gateway does not handle possible resends for the client-initiated messages (e.g., New Order, 
Mass Quote, etc.) and all the messages will be processed without considering the value in the 
PossResend field. Any message with duplicate Client Order ID will be rejected based on the Client 
Order ID uniqueness check and those messages that conform to the uniqueness check will be 
processed as normal messages. 
The gateway may use the PossResend field to indicate that an application message may have 
already been sent under a different sequence number. The client should validate the contents (e.g., 
Exec ID) of such a message against those of messages already received during the current trading 
day to determine whether the new message should be ignored or processed. 
2.6 Gap Fills 
The following messages are expected to be skipped using gap-fills when being retransmitted: 
1. 
Logon


---
*Page 19*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 19 
 
 
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
Following messages will be sent to the client when it reconnects if such messages were generated 
during a period when this client was disconnected from the gateway: 
• 
Execution Report (includes order reject) 
• 
Order Amend Rejected 
• 
Order Cancel Rejected 
• 
Mass Cancel Report 
• 
Business Message Reject 
• 
Reject  
• 
Quote Request Ack 
• 
Mass Quote Ack 
• 
Security Definition 
• 
MMP Reset Ack 
• 
News. 
In the unlikely event the disconnection was due to an outage of the gateway, Business Message 
Reject and Reject messages may not be retransmitted, and the other messages which will be 
retransmitted to the client will include a PossResend set to 1 (Yes). 
2.8 Technical Halt 
In the event of a system component failure, a technical halt will be applied and the Market Data 
service will publish the Trading State = Technical Halt. On receipt of this message, market 
participants are required to clear their public and private order books of all orders including persisted 
orders. Order cancellations will not be transmitted by the gateway.


---
*Page 20*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 20 
 
 
3 
Service Description 
3.1 Security Identification 
Each Tradable Instrument will be identified using the Security ID field which can be a maximum of 19 
digits. 
3.2 Security Creation 
A Security Definition Request (10) can be submitted to create a new tradable instrument: 
Instrument Request Type 
Binary Fields 
Options strike 
Security Type = 2 
Security Sub Type = 0 
Maturity Date 
Strike Price 
Put or Call 
Strategy 
Security Type = 3 
Security Sub Type = 1 to 10 
Leg Security ID 
Leg Ratio 
Leg Side 
Leg Price 
3.2.1 
Strategies 
A trader can submit Security Definition Request (10) for an Exchange defined strategy type or a 
custom strategy. A Delta Hedge strategy can be submitted as a custom strategy. 
 A strategy can be submitted from either a buy or sell perspective and must include the strategy legs 
in order of expiry. A Security Definition Request expressed from a sell perspective will be returned 
with a Security Response Type = ‘2’ Accept security proposal with revisions as indicated in the 
message and the resulting strategy will be created from the buy side perspective.


---
*Page 21*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 21 
 
 
3.2.1.1 Exchange Defined Strategy Types 
The following defined strategy types are supported: 
Futures Strategies 
Security Sub Type 
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
Security Sub Type 
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
A non-Exchange defined strategy can be submitted in a Security Definition Request as a custom 
strategy using either: 
• 
Security Sub Type = ‘2’ Custom (Futures) 
• 
Security Sub Type = ‘9’ Custom (Delta Hedge) 
• 
Security Sub Type = ‘9’ Custom (Options). 
A custom strategy may consist of up to five legs in a Futures contract or premium quoted Option. 
Each leg in the strategy must be in the same contract except for a delta hedge custom strategy in 
premium-based options where the last 1 to 2 legs belong to the underlying futures contract. Note, an 
Exchange defined strategy cannot be used within a custom strategy. 
For example, a Futures Butterfly is defined as buy Month 1, sell Month 2 twice and buy Month 3.


---
*Page 22*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 22 
 
 
 
3.3 Order Submission 
It is possible to submit orders for outright futures, options series or strategies using any of the order 
types specified in 3.4.1 Order Types. An individual order can be submitted using New Order Single 
(12) whereas multiple orders can be submitted using Mass Quote (22). 
A cross order can be submitted using New Order Cross (27) which includes a unique CrossID, see 
Auto Cross 
3.4 Order Types 
The following order types are supported: 
Order Type 
Binary Field 
Limit 
An order submitted with a price and volume that will trade at the limit 
price or better for as much of its stated volume as is available in the 
order book. 
Order Type = 2  
Order Price 
Market 
An order submitted with a volume specified but no price. The order is 
executed at the best available price(s) up / down to their assigned limit 
price. Any order volume which is not fully executed rests in the order 
book as a limit order at the assigned limit price. 
Order Type = 10 
Stop Market 
An order that is submitted but not visible in the order book until it is 
triggered by the last traded price and/or best bid/offer. Once triggered 
the order is entered into the order book as a Stop Market order. 
Order Type = 3 
Trigger Price 
Trigger Price Type


---
*Page 23*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 23 
 
 
Order Type 
Binary Field 
A previously triggered Stop order will be restated as a Limit order. 
Triggering fields will not be present. 
Stop Limit 
An order that is submitted but not visible in the order book until it is 
triggered by the last traded price and/or best bid/offer. Once triggered 
the order is entered into the order book as a Stop Limit order at the 
specified price. 
A previously triggered Stop order will be restated as a Limit order. 
Triggering fields will not be present. 
Order Type = 4 
Trigger Price 
Trigger Price Type 
Order Price 
Iceberg 
An order submitted with a visible order quantity and a total order 
quantity. The visible order quantity must be fully executed before it can 
be replenished with the next visible order quantity. 
Order Type = 11 
Order Price 
Display Quantity 
Order Quantity 
Post Only 
The order must rest in the order book before it can trade. If the order 
can be executed on entry into the order book it is rejected. If an 
amendment to the order can result in execution it also is rejected and 
the original order remains. 
Order Type = 12 
Order Price 
One Cancels Other (OCO) – Market 
A single order which is a combination of a Limit and a Stop. On 
submission the Limit price and a Stop trigger price is specified.  
A partial trade at the Limit price will reduce the quantity available in the 
OCO. If the order is traded out at the Limit price the Stop component 
will be cancelled. Similarly if the Stop is triggered then the Limit 
component is cancelled.  
Note: No Execution Report will be generated for the cancelled 
component. 
If the Stop component is triggered the order becomes a Market order. 
Order Type = 13 
Order Price 
Trigger Price 
Trigger Price Type 
One Cancels Other (OCO) – Limit 
A single order which is a combination of a Limit and a Stop. On 
submission the Limit price and a Stop trigger price is specified.  
Order Type = 14 
Order Price 
Trigger Price


---
*Page 24*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 24 
 
 
Order Type 
Binary Field 
A partial trade at the Limit price will reduce the quantity available in the 
OCO. If the order is traded out at the Limit price the Stop component 
will be cancelled. Similarly if the Stop is triggered then the Limit 
component is cancelled.  
Note: No Execution Report will be generated for the cancelled 
component. 
If the Stop component is triggered it becomes a Limit order at a new 
price. 
Trigger Price Type 
Trigger New Price 
3.5 Order Validity Conditions 
Validity Condition 
Binary Field 
Day 
An order that will expire at the end of the day. 
Time In Force = 0 
Good Till Cancelled (GTC) 
An order that is valid until it is either cancelled or matched. 
Time In Force = 1 
Immediate or Cancel (IOC) 
An order that is executed at the stated price or better for as much order 
volume that is available. Any order volume that cannot be traded is 
cancelled. 
Time In Force = 3 
Fill or Kill (FOK) 
An order that is only executed if there is sufficient volume available, at 
the stated price or better, for them to execute fully. Otherwise the 
entire order is cancelled. 
Time In Force = 4 
Good Till Date (GTD) 
The order is valid until the end of the trading date specified. 
Time In Force = 6 
Expire Date 
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


---
*Page 25*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 25 
 
 
Order Type 
Day 
GTC 
IOC 
FOK 
GTD 
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
Market 
✔  
✔  
 
 
✔  
OCO Limit 
✔ 
✔  
 
 
✔  
3.7 Order Identification 
The client must specify a Client Order ID when submitting a New Order Single (12), Amend Order 
(13), Cancel Order (15) or Mass Cancel Request (17). As with the FIX protocol, the client should 
ensure that each Client Order ID for this Comp ID is unique for the duration of the trading day and 
has not been used already for any of the currently persisted orders belonging to this Comp ID.  
In addition, a Quote ID supplied on a Mass Quote (22) and MMP Reset Request ID supplied in a 
MMP Reset Request (30) must also be unique and must not have been specified as a Client Order 
ID. 
When an order is accepted, the system assigns an Order ID that is unique for all orders and quotes.  
When modifying or cancelling an order, the Original Client Order ID is used to identify the original 
order. 
A cross order is specified by the originator using Cross ID instead. For each of the bid / ask order 
contained in the cross order, Client Order ID is used to identify the order. When the cross order is 
accepted, the system assigns a Host Cross ID for the whole cross order, and an Order ID for each of 
the orders within the cross order.  
When cancelling a cross order, the Original Cross ID is used to identify the cross order. The Host 
Cross ID and Original Client Order ID are optional and will be validated if specified. If any of these 
attributes do not match the original cross order, the cancel request will be rejected. 
 
3.8 Order Expiry 
No Execution Report will be sent for orders with a Time in Force = ‘0’ Day when they expire at the 
end of the trading day.


---
*Page 26*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 26 
 
 
At the end of the day, the order originator will receive an Execution Report with Exec Type = ‘C’ and 
Order Status = ‘12’ Expired for Time in Force = ‘1’ Good Till Cancelled and Time in Force = ‘6’ Good 
Till Date in the following cases:  
• 
Expiry Date has passed for a Good Till Date order* 
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
GTC/GTD orders that have not hit their expiry condition are persisted when the respective tradable 
instrument enters the Close state. The order originator is notified by Execution Report with Exec 
Type = ‘3’ and Order Status = 3 = Done for Day. 
On initial logon on the next trading day, Execution Reports are sent for persisted orders that have 
been returned with Exec Type = ‘D’ Restated, Order Status = ‘0’ New or ‘1’ Partially Filled and Exec 
Restatement Reason = ‘1’ GT renewal / restatement. 
A previously triggered Stop order will be restated as a Limit order.  
3.10 Order Amendment 
An order can be amended by using Amend Order (13) and specifying the Original Client Order ID. 
The client can optionally specify the Order ID in the Amend Order (13). If Order ID is specified the 
system will validate whether the Order ID is associated with the correct order as identified using the 
Original Client Order ID. The Amend Order (13) will be rejected if the specified Order ID is invalid 
based on this validation. 
The following order attributes can be modified if they have been specified on the original order: 
• 
Order Price  
• 
Trigger Price 
• 
Trigger New Price 
• 
Order Quantity  
• 
Display Quantity  
• 
Expiry Date  
• 
Order Capacity 
• 
Order Restrictions 
• 
Execution Decision Within Firm.


---
*Page 27*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 27 
 
 
The following optional order attributes can be modified. If the attribute is not present in the Amend 
Order (13), this indicates that the default value will be used: 
• 
Direct Electronic Access  
• 
Aggregated Order 
• 
Pending Allocation Order 
• 
Liquidity Provision Order 
• 
Risk Reduction Order. 
The following optional order attributes can be added or modified. If the attribute is not present in the 
Amend Order (13) it indicates that the value have been removed or not applicable: 
• 
Text 
• 
Investment Decision Within Firm  
• 
Investment Decision Country  
• 
Execution Decision Country 
• 
Client Branch Country. 
The client cannot amend an order that is fully filled or cancelled or expired.  
Amend Order (13) cannot be used to amend an order submitted using Mass Quote.  
The Trigger Price or Trigger New Price cannot be amended if the Stop order has been triggered. 
Note, a previously triggered Stop Limit or Stop Market order will be restated as a Limit order. 
If the client sends an Amend Order (13) for an order for which an Amend Order (13) or a Cancel 
Order (15) is already being processed the incoming Amend Order (13) is rejected. 
3.11 Order Cancellation 
An individual order can be cancelled using Cancel Order (15) by specifying the Original Client Order 
ID. 
The client can optionally specify the Order ID in the Cancel Order (15). If the Order ID is specified the 
system will validate whether the Order ID is associated with the correct order as identified using the 
Original Client Order ID. The Cancel Order (15) will be rejected if the specified Order ID is invalid 
based on this validation. 
A successful cancellation will return an Execution Report (8). If the cancellation request is rejected, 
an Order Cancel Rejected (16) is sent containing the reason for rejection. 
A cross order can be cancelled using Cancel Cross Order (28) by specifying the Original Cross ID. 
The Host Cross ID and Original Client Order ID are optional and will be validated if specified. If any of 
these attributes do not match the original cross order, the cancel request will be rejected. 
A successful cancellation of a cross order will return an Execution Report (8) per side. If the 
cancellation request is rejected, an Order Cancel Rejected (16) per side is sent containing the reason 
for rejection.


---
*Page 28*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 28 
 
 
The client may not cancel an order that is fully filled or cancelled or expired. 
Cancel Order (15) cannot be used to cancel an order submitted using Mass Quote. 
If the client sends a Cancel Order (15) for an order for which a Cancel Order (15) is already being 
processed the incoming Cancel Order (15) is rejected. 
If the client sends a cancel request for an order for which an amendment is being processed the 
incoming cancel request will be processed (i.e. accepted or rejected) once the outcome of the 
amendment is known. 
3.12 Mass Cancellation 
Multiple orders/quotes can be cancelled using Mass Cancel Request (17) by specifying which 
orders/quotes are to be cancelled: 
Cancellation Type 
Binary Field 
All orders/quotes for a Comp ID 
Mass Cancel Request Type = 7 
Mass Cancel Scope 
All orders/quotes for a specific tradable 
instrument 
Mass Cancel Request Type= 1 
Mass Cancel Scope 
Security ID 
All orders/quotes for a specific contract 
Mass Cancel Request Type= 3 
Mass Cancel Scope 
Contract Code 
All orders/quotes for a specific contract and side 
of the market 
Mass Cancel Request Type= 3 
Mass Cancel Scope 
Contract Code 
Side 
All quotes for a specific Quote ID 
Mass Cancel Request Type = 101 
Mass Cancel Scope = 2 
Quote ID 
All orders/quotes for a specific end client 
Mass Cancel Request Type= 7 
Mass Cancel Scope 
Broker Client ID


---
*Page 29*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 29 
 
 
If the Mass Cancel Request is accepted, Execution Reports will be sent for each order cancellation 
and will include the Client Order ID provided on the Mass Cancel Request (17). The Mass Cancel 
Report (18) will reflect the action taken and indicate the Total Affected Orders. 
If the Mass Cancel Request is rejected, the Mass Cancel Response = ‘0’ Cancel Request Rejected 
and will include the Mass Cancel Reject Reason.   
A mass cancellation request for a tradable instrument will not result in the cancellation of any orders 
in a merged tradable instrument. Orders will only be cancelled in the SecurityID specified in the Mass 
Cancel Request (17). 
3.13 Cancel on Disconnect 
The gateway will not automatically cancel a user’s non-persisted orders and quotes in the event of a 
Logout. A user should explicitly cancel such orders and quotes prior to Logout using a Mass Cancel 
Request (17). 
On order submission, a user can specify whether non-persisted orders should be cancelled on 
system disconnection (due to, for example, a network issue or in the event of inactivity such as too 
many missed heartbeats) using Cancel on Disconnect. 
On detection of a loss of connectivity, the system will determine whether a user’s non-persisted 
orders are to be cancelled based on Cancel on Disconnect attribute for an order. Orders from a Mass 
Quote are by default classified as non-persisted orders and are therefore automatically cancelled. 
This feature does not guarantee that all live orders will be successfully cancelled as executions that 
occur very near to the time of disconnect may not be reported to the client. It also depends on the 
tradable instrument trading state when the abrupt disconnection is identified by the Exchange 
system. 
3.14 Mass Quote 
Multiple orders can be submitted by permissioned trading users in multiple tradable instruments in 
the same contract using a Mass Quote (22).  
Orders in the form of quotes are submitted as a quote pair (bid and offer) in a quote entry with a 
Quote Entry ID. Up to 20 quote entries can be submitted in a Mass Quote.  
Each quote entry is related to a Quote Set which identifies the tradable instrument. All the quote sets 
must belong to the same contract. Within each quote set, up to three prices levels can be specified 
using Quote Price Level.  
Quote entries within a Mass Quote can be replaced or cancelled using a Mass Quote.   
Replacement quotes can overwrite or cancel both sides of a quote entry or a single side of a quote 
pair leaving the other side unchanged. Note, an existing quote entry is identified using the Security 
ID, Quote Price Level and Side. If there is no such quote entry, the instruction will result in a new 
quote.  
Cancellation is indicated by a zero value for Bid Size for bid side or Offer Size for offer side and a null 
value for Bid Price or Offer Price.


---
*Page 30*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 30 
 
 
Unchanged is indicated by a value of -1 for Bid Size for bid side or Offer Size for offer side and a null 
value for Bid price or Offer Price. The quote side that has not changed will retain its current price time 
priority.  
During mass quote processing, resting quotes that will be updated are removed to prevent execution 
with replacement quotes. An Execution Report will be sent for each quote side cancelled. An 
Execution Report will be sent to report quotes that have been replaced and replacement quotes that 
have been rejected. Order Cancel Reject (16) will be returned for cancellations that have been 
rejected.  
The Quote Price Level that is assigned to a quote pair will remain unchanged by either cancellation 
or replacement. For example, if three price level have been specified in a Quote Set, the cancellation 
of quote pair at a quote price level will not reorder the quote price level of the other two quote entries 
in the Quote Set.   
A single sided quote can be submitted with a dummy quote to make up the quote pair. The dummy 
quote is indicated by a value of -1 for Bid Size/Offer Size and a null value for Bid Price/Offer Price as 
specified in 4.3 Data Types. 
For each quote entry side in the Mass Quote, an Execution Report (8) is returned to indicate whether 
the quote entry has been accepted or rejected. The Execution Report (8) can be mapped back to the 
quote in the Mass Quote message through the: 
1. 
Quote ID returned as Client Order ID  
2. 
Quote an amendment Entry ID returned as Secondary Client Order ID. 
If a cancellation to a quote side fails validation Order Cancel Rejected (16) will be returned. 
Crossed quotes submitted in the same quote pair will be rejected but will be executed if supplied in 
different quote pairs. 
If a Mass Quote message is rejected, the gateway will return a Mass Quote Ack (23) containing the 
Quote Reject Reason. For example, if quotes for different contracts have been specified. 
An order resulting from a quote is always treated as a Limit order which expires at the end of the 
current day. In the event of a system related connection loss, orders from Mass Quotes will be 
automatically cancelled, see 3.11 Cancel on Disconnect. 
An order resulting from a quote is assigned the order attributes as defined in the Mass Quote 
message and will be assigned as a Liquidity Provision Order in the Execution Report.  For an existing 
quote that is being amended, only the following attributes will be amended:  
• 
Bid Size 
• 
Bid Price 
• 
Offer Size 
• 
Offer Price. 
All other order attributes that are not amendable will retain their original value.


---
*Page 31*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 31 
 
 
3.15 Auto Cross 
A New Order Cross indicates a trading interest in a specific instrument which is published to market 
participants via a Request for Cross (RFC) on the Market Data service. The platform will then wait for 
a predefined period, then we will determine whether the cross order will be executed on book, 
offbook, a mixture of both on and offbook, or if the cross is cancelled. The Cross order will contain a 
buy and a sell order with the same price and quantity within itself. 
Cross ID is used for the identifier of the cross, then an individual Client Order ID for the order 
specified on each side. When an order is accepted, the system assigns a Host Cross ID in response 
to the Cross ID, and an Order ID for each of the individual order.  
Cross Type specifies whether a guaranteed or non guaranteed cross is requested. CrossPrioritization 
indicates the order on which side of the Cross Order is prioritized. 
A pair of Execution Reports, one for the order on each side, will be returned by the gateway to 
acknowledge a successful Cross Request. The Host Cross ID and Cross ID will be returned in the 
Execution Report. 
Amendment to the Cross Order is not allowed. Cancellation can be done via Cancel Cross Order, by 
specifying Original Cross ID. The Host Cross ID and Original Client Order ID are optional and will be 
validated if specified. If any of these attributes do not match the original cross order, the cancel 
request will be rejected.  
 
Example message flow 
The cross is rejected at gateway due to a session level rule violation 
 
 
The cross is rejected due to business level rule violation


---
*Page 32*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 32 
 
 
The cross passes initial validation checks and is accepted. One side then fails revalidation checks 
resulting in the cross being cancelled


---
*Page 33*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 33 
 
 
 
The initiating side is crossed offbook with the non initiating side


---
*Page 34*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 34 
 
 
 
The initiating side is filled in the orderbook. The non initiating side is cancelled


---
*Page 35*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 35 
 
 
The initiating side is filled against multiple price levels in the orderbook. The non initiating side is 
cancelled


---
*Page 36*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 36 
 
 
The initiating side is partially filled in the orderbook. The residual volume is then crossed offbook 
against the non initiating side. The non initiating sides residual volume is cancelled


---
*Page 37*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 37 
 
 
 
3.16 Request for Quote (RFQ) 
A Quote Request (20) indicates a trading interest in a specific instrument which is published to 
market participants by the Market Data service. 
The Quote Request (20) will include the Quote Request Type which specifies whether a single quote 
or streaming quotes are requested. It can optionally specify the side and the quantity for which a 
price is required. 
A Quote Request Ack (21) will be returned by the gateway in response to a Quote Request. 
Trading participants can respond to an RFQ using standard order and quote functionality. 
3.17 Speed Bumps 
Exchange contracts may be configured with speed bumps. A speed bump will only be applicable to 
New Order Single (12) and Amend Order (13).  
Passive orders, cancellations using Cancel Order (15) or Mass Cancel Request (17) and Mass Quote 
(22) will be exempt.  
The status of an order in a speed bump will be reported in Exec Type Reason in the Execution 
Report (8): 
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
acknowledgement includes an Exec Type Reason = ‘101’ Order accepted but speed bump applied. 
The Execution Report sent once the order has cleared the speed bump and is added to the order 
book includes Exec Type = ‘D’ Restated and Exec Type Reason = ‘102’ Order added after speed 
bump.


---
*Page 38*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 38 
 
 
 
Order cancellation for a speed bumped order 
An order cancellation submitted while an order is in the speed bump will be processed without any 
delay as the Cancel Order (15) is not subject to speed bump conditions. The Execution Report sent 
in response to the cancellation includes Exec Type Reason = ‘103’ Order cancelled whilst in speed 
bump delay.


---
*Page 39*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 39 
 
 
 
Executable order amendment for a speed bumped order will be speed bumped 
An order is submitted which is subject to a speed bump. An Amend Order (13) is submitted while the 
order submission is in the speed bump queue. The amended order is executable and therefore 
speed bumped. The Execution Report for the order revision includes Exec Type Reason = ‘106’ 
Amend is in speed bump delay. The Amend Order will not be processed until the original order has 
cleared the speed bump.  
The Execution Report sent when the original order submission is released from the speed bump and 
added to the order book includes Exec Type = ‘D’ Restated, Order Status = ‘14’ Pending Replace 
and Exec Type Reason = ‘102’ Order added after speed bump. 
Another Execution Report is sent when the order revision clears the speed bump and replaces the 
original order. The Execution Report includes Exec Type = ‘5’ Replaced and Exec Type Reason 
(2431) = ‘107’ Order amended after speed bump delay.


---
*Page 40*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 40


---
*Page 41*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 41 
 
 
Non-executable order amendment for a speed bumped order will not be speed bumped 
An order is submitted which is subject to a speed bump. An Amend Order (13) is submitted while the 
order submission is in the speed bump queue. The amended order will rest in the order book and is 
therefore not subject to speed bump conditions. The Amend Order will not be processed until the 
original order has cleared the speed bump therefore the Execution Report for the revision includes 
Exec Type = ‘E’ Pending Replace and Exec Type Reason = ‘104’ Original order is in speed bump 
enforced delay.  
The Execution Report sent once the order submission has cleared the speed bump and is added to 
the order book includes Exec Type = ‘D’ Restated and Exec Type Reason = ‘102’ Order added after 
speed bump. 
When the order is replaced the Execution Report includes Exec Type = ‘5’ Replaced and Exec Type 
Reason = ‘105’ Order updated after speed bump delay.


---
*Page 42*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 42


---
*Page 43*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 43 
 
 
Executable order amendment for a resting order will be speed bumped 
An order amendment is submitted for a resting order that was previously speed bumped. The Amend 
Order is speed bumped as the amended order will not provide liquidity. The Execution Report for the 
amendment includes Exec Type= ‘E’ Pending Replace with and Exec Type Reason = ‘106’ Amend is 
in speed bump delay. 
When the order is replaced the Execution Report includes Exec Type = ‘5’ Replaced and Exec Type 
Reason = ‘107’ Order amended after speed bump delay.


---
*Page 44*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 44


---
*Page 45*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 45 
 
 
Speed bumped order is cancelled due to validation failure (inflight speed bumped amendment 
is also cancelled) 
An order is submitted which is subject to a speed bump. An Amend Order (13) is accepted which is 
also subject to speed bump conditions. The original order submission fails business validation on 
clearing the speed bump and is cancelled. The Execution Report includes Exec Type = ‘4’ Cancelled 
and Exec Type Reason = ‘108’ Order rejected after speed bump delay with the reason for the 
business validation failure in Reason Text. An Order Amend Rejected (14) is sent for the order 
amend.


---
*Page 46*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 46


---
*Page 47*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 47 
 
 
Immediate or Cancel speed bumped order fails validation and is cancelled 
An Immediate or Cancel order is submitted which is subject to a speed bump. The order fails 
validation on clearing the speed bump as it cannot be executed and is therefore cancelled. The 
Execution Report includes Exec Type = ‘4’ Cancelled and Exec Type Reason = ‘108’ Order rejected 
after speed bump delay with the reason in Reason Text = No quantity available at price stated. 
 
Note: In the absence of a speed bump an IOC will be rejected if no quantity is available at the price 
stated. 
Unsolicited order cancellation while in speed bump 
An order is submitted which is speed bumped. While the order is in the speed bump, the Exchange 
invokes a Trading Halt and all orders are pulled. The Execution Report sent for the order in the speed 
bump includes Exec Type) = ‘4’ Cancelled with Exec Type Reason = ‘109’ Unsolicited cancel while in 
speed bump and Reason Text = Cancelled due to halt.


---
*Page 48*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 48 
 
 
 
3.18 Message Throttling 
The Exchange imposes a message throttle which limits the maximum number of messages that can 
be submitted per second by a Comp ID using the following messages: 
• 
New Order Single (12) 
• 
Amend Order (13) 
• 
New Order Cross (27) 
• 
Quote Request (20) 
• 
Security Definition Request (10) 
• 
Mass Quote (22) 
• 
MMP Reset Request (30). 
Security Definition Requests are included in the message throttle but also have their own throttle 
limits. 
Each Mass Quote message is counted as a single message irrespective of the number of quote pairs 
present in the message. 
Messages submitted in excess of the throttle limit in any given whole second will result in those 
messages being rejected by the gateway and will be notified by a Business Message Reject (7). 
Note, Cancel Order (15) and Mass Cancel (17) messages are exempt from throttling.


---
*Page 49*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 49 
 
 
A system protection throttle will disconnect a user if the incoming message volume exceeds a 
multiple of the threshold limit. Reconnection is permitted after a second. 
3.19 Security Definition Throttle 
The number of Security Definition Request (10) messages that can be submitted by a Comp ID is set 
at per day rate and also included in the per second message throttle. A user breaching the daily limit 
will have further Security Definition Request (10) submissions rejected by the gateway. 
3.20 Merged Order Books 
The LME prompt date structure for futures is such that two different prompts can share the same 
actual date on specific trading dates, for example, on the 3rd Wednesday of a month a 3M rolling 
prompt date will have the same prompt date as the monthly prompt date. On the trading date on 
which the prompts share the same actual date prompt, the order books for both prompts will be 
merged. TOM and Cash prompts will never merge.  
Strategy order books that include a rolling leg will also merge. This can occur if a leg or legs share 
the same actual prompt date. 
The merging of order books only affects execution and market data publication. Prompt dates in the 
merged order book will be available for order entry. The instrument identifier of the rolling prompt will 
be used by the Market Data service.  
GTC and GTD orders will be merged into the order book with precedence and will return to the order 
book into which they were entered when the order books are no longer merged. 
A mass cancellation request for a tradable instrument will not result in the cancellation of any orders 
in a merged tradable instrument. Orders will only be cancelled in the SecurityID specified in the Mass 
Cancel Request (17).


---
*Page 50*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 50


---
*Page 51*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 51 
 
 
3.21 Self Execution Prevention (SEP) 
A member can guard against traders in their organisation executing orders with each other.  
A member can use SEP functionality without configuring a SEP handling action in which case the 
Exchange configured response type would be triggered to cancel the incoming order. Alternatively a 
member can configure SEP identifiers and specify the action to be taken if two orders with an 
identical SEP ID could execute.  
A SEP ID will be specified as a maximum of 9 digits. A Member Risk Manager can use the Risk 
Management interface to define the SEP configuration as described in the Risk Management 
Gateway FIX Specification. This configuration will be effective from the next trading day. 
A SEP ID can be entered in the Self Match Prevention ID on order submission. If orders with an 
identical SEP ID from the same member firm can cross the SEP handling action that has been 
configured is triggered to cancel either the incoming or resting order or both (incoming and resting). 
The Execution Report sent for the cancelled order will contain Reason Text = Self Match prevented. 
The availability of SEP functionality will be determined by the Exchange. If an order is submitted with 
the Self Match Prevention ID populated and SEP is not available for the Security ID specified, the 
order will be rejected. The Execution Report (8) sent will contain Reason Text = Self Match 
Prevention not configured for the tradable instrument.


---
*Page 52*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 52 
 
 
Self Execution Prevention triggered – resting order cancelled 
 
3.22 Market Maker Protection (MMP) 
Market Maker Protection will be available to permissioned trading users. A Member Risk Manager 
will use the Risk Management interface to specify the level of protection that should apply to a trading 
user in a particular contract as described in the Risk Management Gateway FIX Specification. 
The Member Risk Manager will specify the protection type and protection limit measured over a 
configured time period which is defined in seconds. This time period defines the length of the rolling 
time interval for MMP recalculation which is used to determine if the quantity limit has been reached.


---
*Page 53*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 53 
 
 
The following protection types can be configured: 
• 
Cumulative percent over time - Total percentage of orders executed within the configured 
time period 
• 
Volume over time - Total count of volume executed within the configured time period 
• 
Number of tradable instruments traded over time - Total count of option strikes within the 
configured time period. 
If an MMP limit is breached the protection response is triggered to pull orders and reject further 
orders until MMP is explicitly reset by the trading user using an MMP Reset Request (30). The MMP 
reset will only affect the MMP limit that has been breached. 
Note, whenever a protection response is triggered, the corresponding trading user will be notified by 
a News (40) message. 
Once MMP is reset order and quote submission can resume. 
3.23 Inflight Order Processing 
The gateway will accept a single inflight amend or cancellation request whilst processing a new 
order. The amend request is queued until the preceding request has been processed. Multiple inflight 
messages will be rejected. 
For example, a New Order Single (12) is submitted followed immediately afterwards by an Amend 
Order (13). An Execution Report (8) is returned for the order submission and then the amendment.


---
*Page 54*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 54 
 
 
 
Refer to Appendix A: Inflight Order Handling and Appendix B: Speed Bump Inflight Order Handling in 
the Order Entry Gateway FIX Specification for more examples. 
3.24 Trade Reporting 
When an outright order matches, a trade half will be assigned an identifier which will be reported in 
the Trade ID on the Execution Report (8).  
A strategy trade half will be reported in a single Execution Report including the leg details. The legs 
of strategy trade will be assigned a Leg Allocation ID which will be shared with either the Leg 
Allocation ID of another strategy trade or the Trade ID of an outright trade.


---
*Page 55*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 55 
 
 
3.25 Client ID Usage 
Of the following client identifiers only two can be specified for an order or Mass Quote: 
• 
Client ID Short Code 
• 
Legal Entity ID 
• 
Proprietary Client ID.


---
*Page 56*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 56 
 
 
4 
Message Definitions 
4.1 Inbound Messages 
• 
Logon (5) 
• 
Heartbeat (0) 
• 
Test Request (1) 
• 
Resend Request (2) 
• 
Sequence Reset (4) 
• 
Logout (6) 
• 
Security Definition Request (10) 
• 
New Order Single (12) 
• 
New Order Cross (27) 
• 
Amend Order (13) 
• 
Cancel Order (15) 
• 
Cancel Cross Order (28) 
• 
Mass Cancel Request (17) 
• 
Mass Quote (22) 
• 
Quote Request (20) 
• 
MMP Reset Request (30). 
4.2 Outbound Messages 
• 
Logon (5) 
• 
Heartbeat (0) 
• 
Test Request (1) 
• 
Resend Request (2) 
• 
Sequence Reset (4) 
• 
Logout (6) 
• 
Reject (3) 
• 
Business Message Reject (7) 
• 
News (40) 
• 
Security Definition (11) 
• 
Order Amend Rejected (14) 
• 
Order Cancel Rejected (16) 
• 
Execution Report (8)


---
*Page 57*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 57 
 
 
• 
Mass Cancel Report (18) 
• 
Mass Quote Ack (23) 
• 
Quote Request Ack (21) 
• 
MMP Reset Ack (31). 
4.3 Data Types 
Data Type 
Size (bytes) 
Format 
Char 
1 
ASCII Alphanumeric 
Permitted ASCII characters are A-Z, a-z, 0-9, underscore 
(‘_’) and space (‘ ’) 
String 
(n) 
Fixed length.  
These fields use standard Char bytes.  
Permitted ASCII characters are A-Z, a-z, 0-9. Note, special 
characters are also permitted for the following attributes:  
Field 
Underscore 
Hyphen 
Client Order ID 
✔ 
✔ 
Original Client 
Order ID 
✔ 
✔ 
CrossID  
✔ 
✔ 
OrigCrossID 
✔ 
✔ 
Broker Client ID 
✔ 
✔ 
Origination 
Trader 
✔ 
X 
Proprietary 
Client ID 
✔ 
X 
Customer 
Account 
✔ 
X 
Note: Text in the News message and rejection reasons 
can contain other ASCII characters and spaces. 
All fields of this data type will be null terminated and the 
length of the field will include this null character.


---
*Page 58*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 58 
 
 
Data Type 
Size (bytes) 
Format 
If the field value does not occupy the full length of the field, 
data after the null termination should be discarded.  
For incoming messages to the gateway validation enforces 
use of a null termination character somewhere between 
the 2nd and the final character: 
• 
If the field value occupies the full length of the field 
and does not include null character, the gateway 
will reject the message. 
• 
In case the field is empty, the first byte will be null 
filled. This is to indicate that the field is not 
applicable / not filled in. 
UInt8 
1 
Unsigned integer. 
Minimum value = 0 
Maximum value = 254 
Null value = 255 
Int8 
1 
Signed integer. 
Minimum value = -127 
Maximum value = 127 
Null value = -128 
UInt16 
2 
Little Endian encoded unsigned integer. 
Minimum value = 0 
Maximum value = 65,534 
Null value = 65,535 
Int16 
2 
Little Endian encoded signed integer. 
Minimum value = -32,767 
Maximum value = 32,767 
Null value = -32,768 
UInt32 
4 
Little Endian encoded unsigned integer 
Minimum value = 0 
Maximum value = 4,294,967,294 
Null value = 4,294,967,295 
Int32 
4 
Little Endian encoded signed integer. 
Minimum value = -2,147,483,647 
Maximum value = 2,147,483,647 
Null value = -2,147,483,648


---
*Page 59*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 59 
 
 
Data Type 
Size (bytes) 
Format 
UInt64 
8 
Little Endian encoded 64 bits signed integer 
Minimum value = 0 
Maximum value = 18,446,744,073,709,551,614 
Null value = 18,446,744,073,709,551,615 
Note: Timestamps will be represented as UTC up to 
microsecond precision with the nanosecond element being 
represented by trailing zeros. 
Int64 
8 
Little Endian encoded 64 bits unsigned integer 
Minimum value = -9,223,372,036,854,775,807 
Maximum value = 9,223,372,036,854,775,807 
Null value = -9,223,372,036,854,775,808 
Note: Prices will support 6 implied decimals. 
Bitmap Fixed Length 
16 
Bitmap Fixed Length provides up to 128 representation 
options. To indicate availability, set 1 to the applicable bit 
position and 0 for unavailability. 
Each bit in the presence map will represent a field and the 
sequence in which the fields should be included into the 
message will be based on the bit position (starting from 
the most significant bit position). 
Bitmap Variable 
Length 
(n) 
Bitmap Variable Length is used to indicate the presence of 
fields and nested repeating blocks in a repeating block. To 
indicate availability set 1 to the applicable bit position and 
0 for unavailability.  
The length of the bitmaps used for different repeating 
blocks may vary. 
4.4 Message Composition 
Each message comprises of the following logical components: 
1. 
Header 
2. 
Body 
3. 
Trailer 
Fields within a message are formed in the same order as the composition given above. 
 Fields present within the body of the message is defined through a field presence map where the 
present fields are indicated as part of the header.  
Fields that are part of the header and the trailer are considered mandatory.


---
*Page 60*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 60 
 
 
4.4.1 
Field Presence Map 
The binary protocol provides a concept of field presence maps per each message type where using 
these bitmap fields available within the message, senders could indicate the fields available within 
the message in a dynamic nature.  
Each bit in the presence map will represent a field and the sequence in which the fields should be 
included into the message will be based on the bit position (starting from the most significant bit 
position). All fields applicable to a particular presence map should be included in the message 
immediately following the applicable presence map. 
For example, consider an 8 bit presence map. 1st, 2nd and 3rd positions indicate Security ID, Client 
Order ID and Order Quantity respectively where rest of the positions have not been assigned to a 
field. 
To indicate the presence of the fields Security ID and Order Quantity the presence map will be set as 
shown below: 
Bit Position 
(BP) 
0 
1 
2 
3 
4 
5 
6 
7 
Represented 
field 
Security 
ID 
Client 
Order 
ID 
Order 
Quantity 
N/A 
N/A 
N/A 
N/A 
N/A 
Bit value 
(presence) 
1 
0 
1 
0 
0 
0 
0 
0 
Message view: 
Preceding fields of the message 
Presence Map 
1 
0 
1 
0 
0 
0 
0 
0 
Security ID 
12345 
Order Quantity 
1000 
Succeeding fields of the message 
The applicable data types and lengths of the body fields are provided in each message. Based on the 
available fields as indicated by the field presence map, the recipient of the message is expected to 
decode the message accordingly. 
Bit position for a field that commonly appears in multiple messages may be different; each message 
may have its own bit position for individual fields present in that message. 
4.4.2 
Repeating Blocks and Nested Repeating Blocks 
The binary message protocol supports repeating blocks within the message body while also allowing 
nested repeating blocks within a repeating block.


---
*Page 61*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 61 
 
 
When indicating a repeating block, the field presence map will only indicate the presence of the 
repeating block. Based on the repeating block construct, the receiving party is expected to evaluate 
the field contents and the numbers of repeating blocks. 
This specification describes the repeating block construct and the relevant field information such as 
the data types required to identify the message contents and also to calculate header and trailer 
information such as message length and checksums. 
Each repeating block construct will have a repeating block header field which is immediately followed 
by a field presence map which will indicate the presence of the applicable fields in that repeating 
block and any nested repeating blocks included within. 
For example, consider an 8-bit field presence map included in the message header of a Mass Quote 
for which there are 10 mandatory bits: 
BP 
0 
1 
2 
3 
4 
5 
6 
7 
Represented 
field 
Quote 
ID 
Transaction 
Time 
No 
Quote 
Sets 
N/A 
N/A 
N/A 
N/A 
N/A 
Bit value 
(presence) 
1 
1 
1 
0 
0 
0 
0 
0 
Position 2 indicates a repeating block which indicates the number of quote sets (i.e. number of quote 
pairs) present in the Mass Quote message. 
A sample No Quote Sets repeating block construct is given below: 
No Quote Sets 
Number of Quote Set repeating blocks.  
Valid values are 1 or n.  
(Repeating block header field) 
Quote Set Repeating Group Field Presence 
Map 
This will indicate the fields/nested repeating blocks 
present in this repeating block  
0 
Security ID 
Tradable Instrument identifier. 
1 
No Quote Entries 
Number of Quote Entry repeating blocks. 
Valid values are 1 to 3. 
(Repeating block header field) 
 
Quote Entry Field Presence Map 
This will indicate the fields/nested repeating blocks 
present in this repeating block 
 
0 
Quote Entry ID 
 
 
1 
Quote Price Level


---
*Page 62*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 62 
 
 
 
2 
Bid Size 
 
 
3 
Offer Size 
 
 
4 
Bid Price 
 
 
5 
Offer Price 
 
In the above message construct, No Quote Entries is a nested repeating block within the No Quote 
Sets repeating block. 
4.5 Required Fields 
The following conventions are used for fields in the message definitions: 
Y  
 Mandatory 
C  
 Conditionally required based on a specified condition or presence of another field 
N  
 Not required / optional 
4.6 Message Header 
Seq Field Name 
Req Data Type 
Description 
1 
Start of Message 
Y 
UInt8 
Indicates the starting point of a message.  
Always set to the ASCII STX character (0x02). 
2 
Length 
Y 
UInt16 
Length of the message including all the fields in 
the message (i.e. length of all header, body 
and trailer fields) 
3 
Message Type 
Y 
UInt8 
Defines the message type. 
4 
Sequence Number 
Y 
UInt32 
Outbound message sequence number. Always 
incremented by the sender. 
5 
PossDup 
Y 
UInt8 
Indicates whether the message was previously 
transmitted with the same sequence number: 
Valid values: 
0 = No (original transmission) 
1 = Yes (possible duplicate) 
6 
PossResend 
Y 
UInt8 
Indicates whether the message was previously 
transmitted under a different sequence 
number:


---
*Page 63*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 63 
 
 
Seq Field Name 
Req Data Type 
Description 
Valid values: 
0 = No (original transmission) 
1 = Yes (possible resend) 
7 
Comp ID 
Y 
String (11) 
Identifies the sender of the message. 
8 
Sending Time 
Y 
UInt64 
Time the message is transmitted. 
9 
Original Sending 
Time 
Y 
UInt64 
Time the message was originally transmitted.  
Applicable only if PossDup 1 = Yes (possible 
duplicate). If the original time is not available, 
this will be the same value as Sending Time. 
0 value otherwise.   
10 
Body Fields 
Presence Map 
Y 
Bitmap 
Fixed 
Length 
Indicates the list of fields that would be present 
immediately after this Body Fields Presence 
Map field. 
4.7 Message Trailer 
Seq Field Name 
Req 
Data Type 
Description 
1 
Checksum 
Y 
UInt32 
CRC32C based checksum. 
4.8 Administrative Messages 
4.8.1 
Logon (5) 
The Logon request and response are used to authenticate the client and agree on the sequence 
numbers. 
On initial logon the status of persisted orders is communicated by the publication of Execution 
Reports for all open orders. 
The list of available tradable instruments for the current trading day will be published by the Market 
Data service independently. 
BP 
Field Name 
Req Data Type 
Description 
0 
Password 
C 
String (450) 
Encrypted Password assigned to the Comp 
ID. 
Conditionally required in the Logon message 
initiated by the client.


---
*Page 64*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 64 
 
 
BP 
Field Name 
Req Data Type 
Description 
Absent in the Logon message sent by the 
gateway. 
1 
New Password 
N 
String (450) 
New encrypted Password for the Comp ID. 
May be present only in the Logon message 
initiated by the client 
2 
Next Expected 
MsgSeqNum 
Y 
UInt32 
Next expected message sequence number to 
be received. Always updated as a result of an 
incoming message. 
3 
Session Status  
C 
UInt8 
Status of the binary session. 
Valid values: 
0 = Session active  
1 = Session password change 
Conditionally required in the Logon message 
sent by the gateway. 
4 
Heartbeat Interval 
Y 
UInt32 
Heartbeat interval in seconds. 
Example Message Flow 
Initial Logon 
 
4.8.2 
Heartbeat (0) 
Heartbeat is sent at the interval specified in Logon (5). It is also sent in response to a Test Request 
(1). 
BP 
Field Name 
Req Data Type 
Description 
0 
Reference Test 
Request ID 
C 
String (21) 
Conditionally required if the Heartbeat is in 
response to a Test Request.


---
*Page 65*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 65 
 
 
BP 
Field Name 
Req Data Type 
Description 
The value in this field will echo the Test 
Request ID received in the Test Request. 
4.8.3 
Test Request (1) 
Test Request can be sent by either the client or gateway to verify a connection is active. The 
recipient responds with a Heartbeat (0). 
BP 
Field Name 
Req Data Type 
Description 
0 
Test Request ID 
Y 
String (21) 
Identifier included in Test Request message to 
be returned in resulting Heartbeat. 
4.8.4 
Resend Request (2) 
Resend Request is used to initiate the retransmission of messages if a sequence number gap is 
detected. 
To request a single message. The Start Sequence and End Sequence should be the same. 
To request a specific range of messages. The Start Sequence should be the first message of the 
range and the End Sequence should be the last of the range. 
To request all messages after a particular message. The Start Sequence should be the sequence 
number immediately after that of the last processed message and the End Sequence should be zero 
(0) 
BP 
Field Name 
Req Data Type 
Description 
0 
Start Sequence  
Y 
UInt32 
Sequence number of the first message 
expected to be resent. 
1 
End Sequence  
Y 
UInt32 
Sequence number of the last message 
expected to be resent. 
This may be set to 0 to request the sender to 
transmit ALL messages starting from Start 
Sequence Number.


---
*Page 66*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 66 
 
 
Example Message Flows 
Resend Request for a range of messages


---
*Page 67*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 67 
 
 
Resend Request for all messages after a particular message


---
*Page 68*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 68 
 
 
Resend Request - incoming message buffered by Client 
A Resend Request is submitted but before gap fill messages have been transmitted an incoming 
message is received. The client will hold the message until all the gap fill messages have been 
received and then process the buffered message. All messages should be processed in sequence 
number order.


---
*Page 69*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 69 
 
 
4.8.5 
Sequence Reset (4) 
Sequence Reset allows the client or the gateway to increase the expected incoming sequence 
number of the other party. 
In a Gap Fill it is sent as notification of the next sequence number to be transmitted. 
BP 
Field Name 
Req Data Type 
Description 
0 
Gap Fill 
N 
Char 
Indicates whether the sequence number is to 
be interpreted in Reset mode or Gap Fill mode: 
Valid values: 
N = Reset (ignore Sequence Number) 
Y = Gap Fill (Sequence Number valid) 
If omitted default value is N. 
1 
New Sequence 
Number 
Y 
UInt32 
Sequence number of the next message to be 
transmitted. 
4.8.6 
Logout (6) 
Logout initiates or confirms the termination of a client session. Clients should terminate their sessions 
gracefully by logging out. 
If a user is disabled by LME Market Operations while logged in then a Logout message will be sent to 
the user and the session will be disconnected. 
If a user has their password reset by LME Market Operations and attempts to login with their 
previous password, the user will receive a Logout with Session Status = ‘100’ Password change is 
required. 
BP 
Field Name 
Req Data Type 
Description 
0 
Session Status 
C 
UInt8 
Status of the binary session.  
Valid values: 
3 = New session password does not comply 
with the policy 
4 = Session logout complete 
5 = Invalid username or password 
6 = Account locked 
7 = Logons are not allowed at this time 
8 = Password expired 
100 = Password change is required 
101 = Other 
Conditionally required only if the message is 
generated by the gateway.


---
*Page 70*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 70 
 
 
BP 
Field Name 
Req Data Type 
Description 
1 
Logout Text 
C 
String (76) 
Reason for the Logout. 
Conditionally required if Session Status = ‘101’ 
Other 
4.8.7 
Reject (3) 
Reject will be sent when a message is received but cannot be properly processed by the gateway 
due to a session level rule violation. For example, populating a reserved bit position in a message will 
return Message Reject Code = ‘3’ Undefined field. 
BP 
Field Name 
Req Data Type 
Description 
0 
Message Reject 
Code 
Y 
UInt16 
Code specifying the reason for the session 
level rejection: 
Valid values: 
1 = Required field missing 
2 = Field not defined for this message 
3 = Undefined field 
4 = Field specified without a value 
5 = Value is incorrect for this field 
6 = Incorrect data format for value 
9 = Comp ID problem 
10 = Sending Time Accuracy problem 
11 = Invalid message type 
13 = Field appears more than once 
99 = Other 
1 
Reference Message 
Type 
N 
UInt8 
Message type of the rejected message. 
2 
Reference Field 
Name 
N 
String (50) 
Name of the field which caused the rejection. 
3 
Reference Sequence 
Number 
Y 
UInt32 
Sequence number of the message which 
caused the rejection. 
4 
Reason Text 
N 
String (76) 
Text specifying the reason for the rejection. 
4.9 Other Messages 
4.9.1 
Business Message Reject (7) 
Once an application level message passes validation at session level it will then be validated at 
business level. If business level validation detects an error condition then a rejection should be


---
*Page 71*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 71 
 
 
issued. Many business level messages have specific fields for rejection handling where a specific 
field is not available the Business Message Reject message will be returned. 
BP 
Field Name 
Req Data Type 
Description 
0 
Business Reject 
Code  
Y 
UInt16 
Code specifying the reason for the rejection of 
the message: 
Valid values: 
0 = Other 
2 = Unknown Security 
3 = Unspecified Message Type 
5 = Conditionally required field missing 
8 = Throttle limit exceeded  
9 = Throttle limit exceeded, session will be 
disconnected 
1 
Reason Text 
N 
String (76) 
Text specifying the reason for the rejection. 
2 
Reference Message 
Type  
Y 
UInt8 
Message type of the rejected message. 
3 
Reference Field 
Name  
N 
String (50) 
Name of the field which caused the rejection. 
4 
Reference Sequence 
Number  
N 
UInt32 
Sequence number of the message which 
caused the rejection. 
5 
Business Reject 
Reference ID  
N 
String (21) 
Client specified unique identifier on the 
message that was rejected. 
For example, for a New Order Single this would 
be the client specified identifier in the Client 
Order ID. 
4.9.2 
News (40) 
A News message is a general free format message from the exchange. A News message is also 
sent in response to a market maker protection breach, see 3.19 Market Maker Protection (MMP). 
BP 
Field Name 
Req Data Type 
Description 
0 
News ID 
Y 
String (21) 
Unique identifier assigned for the News 
message. 
1 
News Category 
Y 
UInt8 
Category of the News.  
Valid values: 
101 = Market message


---
*Page 72*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 72 
 
 
BP 
Field Name 
Req Data Type 
Description 
102 = Market Maker Protection 
2 
Origination Time 
Y 
UInt64 
Time of message origination. 
UTC Timestamp 
3 
News Text 
Y 
String (251) 
Free text field for Market message or one of 
the following for Market Maker Protection: 
• 
Cumulative percent over time 
breached 
• 
Volume over time breached 
• 
Number of tradable instruments 
traded over time breached  
Example Message Flow 
Market Maker Protection breached


---
*Page 73*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 73 
 
 
4.10 Application Messages 
4.10.1 
Security Definition Request (10) 
Security Definition Request is used to request the creation of either an option strike or a strategy. 
BP 
Field Name 
Req Data Type 
Description 
0 
Security Request ID 
Y 
String (19) 
Client specified unique identifier of the 
Security Definition Request. 
1 
Security Exchange 
Y 
String (5) 
The market which is used to identify the 
security. 
XLME 
2 
Product Complex  
Y 
String (5) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base 
3 
Symbol 
Y 
String (21) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future). 
4 
Security Type 
Y 
UInt8 
Indicates the type of security whether 
outright or strategy.  
Valid values:  
2 = Option 
3 = Multi-leg instrument 
5 
Security Sub Type 
Y 
UInt8 
Indicates the type of instrument to be 
created.  
Valid values:  
0 = Outright  
1 = Carry 
2 = Custom (Futures) 
3 = 3 Months Average 
4 = 6 Months Average 
5 = 12 Months Average 
6 = Carry Average 
7 = Call Spread 
8 = Put Spread 
9 = Custom (Delta Hedge) 
10 = Custom (Options) 
6 
Maturity Date 
C 
UInt32 
Expiration date for options.


---
*Page 74*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 74 
 
 
BP 
Field Name 
Req Data Type 
Description 
Conditionally required for Security Type = 
‘2’ Option. 
7 
Strike Price 
C 
Int64 
Strike price for an option.  
Conditionally required for Security Type = 
‘2’ Option. 
8 
Put or Call 
C 
UInt8 
Used to express option right 
Valid values: 
0 = Put 
1 = Call 
Conditionally required for Security Type = 
‘2’ Option. 
9 
No Legs 
C 
UInt8 
Number of legs repeating blocks. 
Cannot be less than 2 or more than 5. Note 
this will only be 1 for a 3 Month Average, 6 
Month Average and 12 Month Average. 
Conditionally required for Security Type = 
‘3’ Multi-leg instrument. 
 
Legs Body Fields 
Presence Map 
C 
Bitmap 
Variable 
Length (1) 
Conditionally required if No Legs > 0 where 
each repeating group represents a leg in the 
multi-leg instrument. 
 
0 
Leg Security ID 
Y 
UInt64 
Security ID of the leg. 
For an Average strategy, only the Security 
ID of the first leg of the strategy is provided 
as the other months are consecutive. 
 
1 
Leg Side 
Y 
UInt8 
The side of this individual leg.  
Valid values: 
1 = Buy 
2 = Sell 
 
2 
Leg Ratio 
Y 
UInt32 
With 3 implied decimals. 
For a delta hedge custom strategy, this is 
the delta used to determine the covering 
quantity. 
For all other strategies and also for an 
options leg in a delta hedge custom strategy


---
*Page 75*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 75 
 
 
BP 
Field Name 
Req Data Type 
Description 
this is the ratio of quantity for this individual 
leg relative to the entire multi-leg 
instrument. 
For example, for a custom strategy such as 
a Butterfly the leg ratio would be 1:2:1 
(1.000:2.000:1.000), for the first leg Leg 
Ratio = 1.000 (buy near contract month), 
second leg Leg Ratio = 2.000 (sell two 
contracts in far month) and third leg Leg 
Ratio = 1.000 (buy one contract in yet 
farther month). 
For a Carry Average the front leg must 
include a ratio for the number of average 
legs. For example, 3M-3Q (Jul/Aug/Sep) 
Carry Average, 3M leg Leg Ratio = 3.000, 
legs 2/3/4 would have Leg Ratio = 1.000. 
 
3 
Leg Price 
C 
Int64 
Used to specify an anchor price for a leg. 
Not used for execution price. 
Conditionally required for the futures legs of 
Security Sub Type = '9' Custom (Delta 
Hedge) to specify the underlying futures 
price. 
4.10.2 
Security Definition (11) 
Security Definition will be returned to the originator of the Security Definition Request (10) to accept, 
accept with revisions or reject the creation of a tradable instrument. Market participants will be 
notified of a newly created instrument by the Market Data service. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Security Request ID 
Y 
String (19) 
Client specified unique identifier of the 
Security Definition Request. 
1 
Security Response ID 
Y 
String (21) 
Unique ID assigned to Security Definition 
message. 
2 
Security Response 
Type 
Y 
UInt8 
Type of Security Definition message 
response. 
Valid values: 
1 = Accept security proposal


---
*Page 76*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 76 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
2 = Accept security proposal with revisions 
as indicated in the message 
5 = Reject security proposal 
3 
Security Reject 
Reason 
C 
UInt8 
Identifies the reason a security definition 
request is being rejected. 
Valid values: 
99 = Other 
101 = Throttle limit exceeded 
102 = Invalid strike price 
103 = LegSecurityID (602) does not exist 
104 = Invalid prompt date 
105 = Invalid SecuritySubType.(762) 
Conditionally required if Security Response 
Type = ‘5’ Reject security proposal. 
4 
Security ID 
C 
UInt64 
Tradable Instrument identifier. 
Conditionally required if Security Response 
Type = ‘1’ Accept security proposal or  
‘2’ Accept security proposal with revisions 
as indicated in the message. 
5 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Security Reject 
Reason = ‘99’ Other. 
Example Message Flows 
Option Strike Request


---
*Page 77*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 77 
 
 
Futures Strategy Request 
 
Inverse Custom Strategy Request


---
*Page 78*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 78 
 
 
Delta Hedge Strategy Request – Call Spread versus underlying 
 
4.10.3 
New Order Single (12) 
New Order Single is used to submit a new order for execution. An Execution Report (8), Reject (3) or 
Business Message Reject (7) is sent in response. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Client specified identifier of the order. 
4 
Security ID 
Y 
UInt64 
Tradable Instrument identifier. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
6 
Side 
Y 
UInt8 
Side of the order. 
Valid values: 
1 = Buy 
2 = Sell 
7 
Order Quantity 
Y 
Int32 
Total quantity of the order. 
8 
Order Type 
Y 
UInt8 
Order type applicable to the order. 
Valid values: 
2 = Limit 
3 = Stop Market 
4 = Stop Limit 
10 = Market 
11 = Iceberg 
12 = Post Only 
13 = One Cancels Other Market


---
*Page 79*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 79 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
14 = One Cancels Other Limit 
9 
Order Price 
Y 
Int64 
Price of the order. 
Must be null value if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘10’ Market. 
10 
Time in Force 
Y 
UInt8 
Specifies how long the order remains in 
effect. 
Valid values: 
0 = Day 
1 = Good Till Cancel (GTC) 
3 = Immediate Or Cancel (IOC) 
4 = Fill Or Kill (FOK) 
6 = Good Till Date (GTD) 
11 
Order Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
12 
Order Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
13 
Account Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA 
For contracts assigned to the T4 booking 
model only 3 = House is valid whereas for 
the T2 booking model all account types are 
valid.


---
*Page 80*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 80 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
15 
Client ID Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3. 
Not valid if populated with either 1, 2 or 3. 
Conditionally required for client orders 
Mandatory where Order Capacity is 
populated with A (agency) = AOTC or R 
(riskless principal) = MTCH  
16 
Legal Entity ID 
N 
String (41) 
LEI.  
17 
Proprietary Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
18 
Entering Firm 
N 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
19 
Origination Trader 
Y 
String (41) 
Order origination trader. 
20 
Customer Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
21 
Correspondent Broker 
N 
String (4) 
A 3 character broker code (Member 
mnemonic). 
23 
Market Maker 
N 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative. 
24 
Decision Maker 
C 
UInt64 
Decision maker short code, used under the 
power of representation clause where the 
investment decision maker may be a third 
party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590 . 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
 
 Validated at point of reporting


---
*Page 81*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 81 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
25 
Investment Decision 
within Firm (IDM) 
C 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the investment decision. 
Mandatory where Order Capacity is 
populated with P (principal) = DEAL, in 
accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/580 
26 
Execution within Firm 
(EDM) 
Y 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the execution. 
Short code 3 (NORE) used where the 
decision on execution venue was made by a 
client or a person outside of the executing 
firm. 
Where OrderOrigination is populated with 5, 
the short code should always be 3 (NORE). 
27 
Investment Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision. 
*Mandatory where Investment Decision 
Within Firm (IDM) is populated with a short 
code representing an individual 
28 
Execution Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision. 
Mandatory where Execution within Firm 
(EDM) is populated with a short code 
representing an individual. 
29 
Client Branch Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
Mandatory where Account Type = 1, 8 or 
101. 
 
 Validated at point of reporting


---
*Page 82*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 82 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
30 
Broker Client ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
31 
Text 
N 
String (51) 
Free text 
32 
Self Match Prevention 
ID 
N 
UInt32 
Identifies an order that should not be 
matched to an opposite order if both buy 
and sell orders for the trade contain the 
same Self Match Prevention ID and are 
submitted by the same member. 
33 
Display Quantity 
C 
UInt32 
Visible quantity of an Iceberg order.  
Conditionally required if Order Type = ‘11’ 
Iceberg. 
If present, must be < Order Quantity. 
34 
Expiry Date 
C 
UInt32 
The expiry date of an order. 
Conditionally required if Time In Force = ‘6’ 
Good ‘til Date. 
Format is YYYYMMDD. 
35 
Trigger Price 
C 
Int64 
Trigger price for stop orders. 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO Market 
Order Type = ‘14’ OCO Limit 
36 
Trigger Price Type 
C 
UInt8 
Type of price event that triggers the stop 
order: 
Valid values: 
2 = Last Trade  
4 = Best Bid or Last Trade 
5 = Best Offer or Last Trade 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO Market 
Order Type = ‘14’ OCO Limit 
37 
Trigger Type 
C 
UInt8 
Trigger prompt for stop order elements.


---
*Page 83*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 83 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO Market 
Order Type = ‘14’ OCO Limit 
 
Valid value: 
4 = Price Movement 
38 
Trigger New Price 
C 
Int64 
Limit order price of the stop once triggered. 
Conditionally required if Order Type = ‘14’ 
OCO Limit. 
40 
Cancel on Disconnect 
N 
Char 
Specifies whether the order should be 
cancelled on system disconnection: 
Valid values: 
Y = Yes 
N = No (default) 
41 
Direct Electronic 
Access 
N 
Char 
Signifies order received from a direct 
access or sponsored access customer. 
Valid value: 
Y = Yes 
Absence of this field infers No (default) 
42 
Aggregated Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(3), it signifies that the 
order consists of several orders aggregated 
together. This maps to the UK version of 
Commission Delegated Regulation (EU) No 
2017/580value "AGGR". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or Pending 
Allocation Order has been populated.   
43 
Pending Allocation 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(2), it signifies that the 
order submitter "is authorized under the


---
*Page 84*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 84 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
legislation of a Member State to allocate an 
order to its client following submission of the 
order to the trading venue and has not yet 
allocated the order to its client at the time of 
the submission of the order". This maps to 
the UK version of Commission Delegated 
Regulation (EU) No 2017/580value "PNAL". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or 
Aggregated Order has been populated.  
44 
Liquidity Provision 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 3, it signifies that the order 
was submitted "as part of a market making 
strategy pursuant to Articles 17 and 18 of 
the UK version of Directive 2014/65/EU or is 
submitted as part of another activity in 
accordance with Article 3" (of the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580). 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
45 
Risk Reduction Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/590Article 4(2)(i), it signifies that the 
commodity derivative order is a transaction 
"to reduce risk in an objectively measurable 
way in accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
Valid value: 
Y = Yes 
Absence of this field infers No (default).


---
*Page 85*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 85 
 
 
Example Message Flow 
Market order 
 
4.10.4 
New Order Cross (27) 
New Order Cross is used to submit a new cross order for execution. An Execution Report (8), Reject 
(3) or Business Message Reject (7) is sent in response. 
A Request for Cross message is disseminated via the Market Data service to market participants. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Cross ID 
Y 
String (19) 
Client specified identifier of the order. 
1 
Cross Type 
Y 
UInt8 
Type of cross being submitted to a market 
Valid values:  
101 = Guaranteed


---
*Page 86*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 86 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
102 = Non-Guaranteed 
2 
Cross Prioritization 
Y 
UInt8 
Indicates if one side or the other of a cross 
order should be prioritized 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
4 
Security ID  
Y 
UInt64 
Tradable Instrument identifier. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
7 
Order Quantity 
Y 
Int32 
Total quantity of the order. 
9 
Order Price 
Y 
Int64 
Price of the order. 
11 
Cancel on Disconnect 
N 
Char 
Specifies whether the order should be 
cancelled on system disconnection: 
Valid values: 
Y = Yes 
N = No 
Default N = No 
12 
Buy Side Client Order 
ID 
Y 
String (19) 
Client specified identifier of the order. 
13 
Buy Side Client ID 
Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3. 
Not valid if populated with either 1, 2 or 3. 
Conditionally required for client orders. 
Absence of this field indicates No Client. 
Mandatory where Order Capacity is 
populated with A (agency) = AOTC or R 
(riskless principal) = MTCH. 
14 
Buy Side Legal Entity 
ID 
N 
String (41) 
LEI.  
 
 Validated at point of reporting


---
*Page 87*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 87 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
15 
Buy Side Proprietary 
Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
16 
Buy Side Entering Firm 
N 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
17 
Buy Side Origination 
Trader 
Y 
String (41) 
Order origination trader. 
18 
Buy Side Customer 
Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
19 
Buy Side 
Correspondent Broker 
N 
String (4) 
A 3 character broker code (Member 
mnemonic). 
21 
Buy Side Market 
Maker 
N 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative. 
22 
Buy Side Decision 
Maker 
C 
UInt64 
Decision maker short code, used under the 
power of representation clause where the 
investment decision maker may be a third 
party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
23 
Buy Side Investment 
Decision within Firm 
(IDM) 
C 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the investment decision. 
Mandatory where Order Capacity is 
populated with P (principal) = DEAL, in 
accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/580 
24 
Buy Side Execution 
within Firm (EDM) 
Y 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the execution. 
Short code 3 (NORE) used where the 
decision on execution venue was made by a


---
*Page 88*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 88 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
client or a person outside of the executing 
firm. 
Where OrderOrigination is populated with 5, 
the short code should always be 3 (NORE). 
25 
Buy Side Investment 
Decision Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision. 
*Mandatory where Investment Decision 
Within Firm (IDM) is populated with a short 
code representing an individual 
26 
Buy Side Execution 
Decision Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision. 
Mandatory where Execution within Firm 
(EDM) is populated with a short code 
representing an individual. 
27 
Buy Side Client Branch 
Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
Mandatory where Account Type = 1, 8 or 
101. 
28 
Buy Side Broker Client 
ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
29 
Buy Side Account 
Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA. 
Must be the same as the original order. 
 
 Validated at point of reporting


---
*Page 89*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 89 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
30 
Buy Side Order 
Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
31 
Buy Side Order 
Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
35 
Buy Side Aggregated 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(3), it signifies that the 
order consists of several orders aggregated 
together. This maps to the UK version of 
Commission Delegated Regulation (EU) No 
2017/580value "AGGR". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or Pending 
Allocation Order has been populated.   
36 
Buy Side Pending 
Allocation Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(2), it signifies that the 
order submitter "is authorized under the 
legislation of a Member State to allocate an 
order to its client following submission of the 
order to the trading venue and has not yet 
allocated the order to its client at the time of 
the submission of the order". This maps to 
the UK version of Commission Delegated 
Regulation (EU) No 2017/580 value 
"PNAL". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or 
Aggregated Order has been populated.


---
*Page 90*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 90 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
37 
Buy Side Liquidity 
Provision Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 3, it signifies that the order 
was submitted "as part of a market making 
strategy pursuant to Articles 17 and 18 of 
the UK version of Directive 2014/65/EU or is 
submitted as part of another activity in 
accordance with Article 3" (of the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580). 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
38 
Buy Side Risk 
Reduction Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/590Article 4(2)(i), it signifies that the 
commodity derivative order is a transaction 
"to reduce risk in an objectively measurable 
way in accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
40 
Sell Side Client Order 
ID 
Y 
String (19) 
Client specified identifier of the order. 
41 
Sell Side Client ID 
Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3. 
Not valid if populated with either 1, 2 or 3. 
Conditionally required for client orders. 
Absence of this field indicates No Client. 
Mandatory where Order Capacity is 
populated with A (agency) = AOTC or R 
(riskless principal) = MTCH.  
 
 Validated at point of reporting


---
*Page 91*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 91 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
42 
Sell Side Legal Entity 
ID 
N 
String (41) 
LEI.  
43 
Sell Side Proprietary 
Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
44 
Sell Side Entering Firm 
N 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
45 
Sell Side Origination 
Trader 
Y 
String (41) 
Order origination trader. 
46 
Sell Side Customer 
Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
47 
Sell Side 
Correspondent Broker 
N 
String (4) 
A 3 character broker code (Member 
mnemonic). 
49 
Sell Side Market 
Maker 
N 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative. 
50 
Sell Side Decision 
Maker 
C 
UInt64 
Decision maker short code, used under the 
power of representation clause where the 
investment decision maker may be a third 
party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590 . 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
51 
Sell Side Investment 
Decision within Firm 
(IDM) 
C 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the investment decision. 
Mandatory where Order Capacity is 
populated with P (principal) = DEAL, in 
accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/580


---
*Page 92*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 92 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
52 
Sell Side Execution 
within Firm (EDM) 
Y 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the execution. 
Short code 3 (NORE) used where the 
decision on execution venue was made by a 
client or a person outside of the executing 
firm. 
Where OrderOrigination is populated with 5, 
the short code should always be 3 (NORE). 
53 
Sell Side Investment 
Decision Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision. 
*Mandatory where Investment Decision 
Within Firm (IDM) is populated with a short 
code representing an individual 
54 
Sell Side Execution 
Decision Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision. 
Mandatory where Execution within Firm 
(EDM) is populated with a short code 
representing an individual. 
55 
Sell Side Client Branch 
Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
Mandatory where Account Type = 1, 8 or 
101. 
56 
Sell Side Broker Client 
ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
57 
Sell Side Account 
Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
 
 Validated at point of reporting


---
*Page 93*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 93 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA. 
Must be the same as the original order. 
58 
Sell Side Order 
Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
59 
Sell Side Order 
Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
63 
Sell Side Aggregated 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(3), it signifies that the 
order consists of several orders aggregated 
together. This maps to the UK version of 
Commission Delegated Regulation (EU) No 
2017/580value "AGGR". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or Pending 
Allocation Order has been populated.   
64 
Sell Side Pending 
Allocation Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(2), it signifies that the 
order submitter "is authorized under the 
legislation of a Member State to allocate an 
order to its client following submission of the 
order to the trading venue and has not yet 
allocated the order to its client at the time of 
the submission of the order". This maps to 
the UK version of Commission Delegated 
Regulation (EU) No 2017/580value "PNAL". 
Valid value:


---
*Page 94*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 94 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or 
Aggregated Order has been populated.  
65 
Sell Side Liquidity 
Provision Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 3, it signifies that the order 
was submitted "as part of a market making 
strategy pursuant to Articles 17 and 18 of 
the UK version of Directive 2014/65/EU or is 
submitted as part of another activity in 
accordance with Article 3" (of the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580). 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
66 
Sell Side Risk 
Reduction Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/590Article 4(2)(i), it signifies that the 
commodity derivative order is a transaction 
"to reduce risk in an objectively measurable 
way in accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
68 
Text 
N 
String (51) 
Free text 
 
4.10.5 
Amend Order (13) 
Amend Order is used to change the parameters of an existing order. If successful an Execution 
Report (8) is returned to confirm replacement of the order otherwise an Order Amend Rejected (14) 
is returned if the request is rejected and the order remains unchanged. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Client specified identifier of the order.


---
*Page 95*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 95 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
2 
Order ID 
N 
UInt64 
Unique order identifier assigned by the 
trading system. 
3 
Original Client Order 
ID 
Y 
String (19) 
Original order identified as the order to be 
amended. 
4 
Security ID 
Y 
UInt64 
Tradable Instrument identifier. 
Must be the same as the original order. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
6 
Side 
Y 
UInt8 
Side of the order. 
Valid values: 
1 = Buy 
2 = Sell 
Must be the same as the original order. 
7 
Order Quantity 
Y 
Int32 
Total quantity of the order. 
8 
Order Type 
Y 
UInt8 
Order type applicable to the order. 
Valid values: 
2 = Limit 
3 = Stop Market 
4 = Stop Limit 
10 = Market 
11 = Iceberg 
12 = Post Only 
13 = One Cancels Other Market 
14 = One Cancels Other Limit. 
Must be the same as the original order 
however a previously triggered Stop Limit or 
Stop Market order will be restated as a Limit 
order. 
9 
Order Price 
Y 
Int64 
Price of the order. 
Must be null value if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘10’ Market. 
10 
Time in Force 
Y 
UInt8 
Specifies how long the order remains in 
effect.


---
*Page 96*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 96 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Valid values: 
0 = Day 
1 = Good Till Cancel (GTC) 
3 = Immediate Or Cancel (IOC) 
4 = Fill Or Kill (FOK) 
6 = Good Till Date (GTD). 
Must be the same as the original order. 
11 
Order Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
12 
Order Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
13 
Account Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA. 
Must be the same as the original order. 
15 
Client ID Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3 
Not valid if populated with either 1, 2 or 3 
Conditionally required for client orders  
Mandatory where Order Capacity is 
populated with A (agency) = AOTC or R 
(riskless principal) = MTCH 
 
 Validated at point of reporting


---
*Page 97*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 97 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Present only if specified on the original 
order and must be the same as the original 
order. 
16 
Legal Entity ID 
C 
String (41) 
LEI.  
Present only if specified on the original 
order and must be the same as the original 
order. 
17 
Proprietary Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
Present only if specified on the original 
order and must be the same as the original 
order. 
18 
Entering Firm 
C 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
Present only if specified on the original 
order and must be the same as the original 
order. 
19 
Origination Trader 
Y 
String (41) 
Order origination trader. 
Must be the same as the original order. 
20 
Customer Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
Present only if specified on the original 
order and must be the same as the original 
order. 
21 
Correspondent Broker 
C 
String (4) 
A 3 character broker code (Member 
mnemonic). 
Present only if specified on the original 
order and must be the same as the original 
order. 
23 
Market Maker 
C 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative.


---
*Page 98*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 98 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Present only if specified on the original 
order and must be the same as the original 
order. 
24 
Decision Maker 
C 
UInt64 
Decision maker short code, used under the 
power of representation clause where the 
investment decision maker may be a third 
party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
Present only if specified on the original 
order and must be the same as the original 
order. 
25 
Investment Decision 
within Firm (IDM) 
C 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the investment decision. 
Mandatory where OrderCapacity (528) is 
populated with P (principal) = DEAL, in 
accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590 
26 
Execution within Firm 
(EDM) 
Y 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the execution. 
Short code 3 (NORE) used where the 
decision on execution venue was made by a 
client or a person outside of the executing 
firm. 
Where OrderOrigination is populated with 5, 
the short code should always be 3 (NORE). 
27 
Investment Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision.


---
*Page 99*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 99 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Mandatory where Investment Decision 
Within Firm (IDM) is populated with a short 
code representing an individual 
28 
Execution Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision. 
*Mandatory where Execution within Firm 
(EDM) is populated with a short code 
representing an individual. 
29 
Client Branch Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
Mandatory where Account Type = 1, 8 or 
101. 
30 
Broker Client ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
Must be the same as the original order. 
31 
Text 
N 
String (51) 
Free text 
32 
Self Match Prevention 
ID 
C 
UInt32 
Identifies an order that should not be 
matched to an opposite order if both buy 
and sell orders for the trade contain the 
same Self Match Prevention ID and are 
submitted by the same member. 
Present only if specified on the original 
order and must be the same as the original 
order. 
33 
Display Quantity 
C 
UInt32 
Visible quantity of an Iceberg order.  
Conditionally required if Order Type = ‘11’ 
Iceberg. 
If present, must be < Order Quantity. 
34 
Expiry Date 
C 
UInt32 
The expiry date of an order. 
 
 Validated at point of reporting


---
*Page 100*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 100 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Conditionally required if Time In Force = ‘6’ 
Good ‘til Date. 
Format is YYYYMMDD. 
35 
Trigger Price 
C 
Int64 
Trigger price for stop orders. 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO-Market 
Order Type = ‘14’ OCO-Limit 
36 
Trigger Price Type 
C 
UInt8 
Type of price event that triggers the stop 
order: 
Valid values: 
2 = Last Trade  
4 = Best Bid or Last Trade 
5 = Best Offer or Last Trade 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO-Market 
Order Type = ‘14’ OCO-Limit. 
Present only if specified on the original 
order and must be the same as the original 
order. 
37 
Trigger Type 
C 
UInt8 
Trigger prompt for stop order elements.  
Valid value: 
4 = Price Movement. 
Present only if specified on the original 
order and must be the same as the original 
order. 
38 
Trigger New Price 
C 
Int64 
Limit order price of the stop once triggered. 
Conditionally required if Order Type = ‘14’ 
OCO-Limit. 
40 
Cancel on Disconnect 
N 
Char 
Specifies whether the order should be 
cancelled on system disconnection: 
Valid values:


---
*Page 101*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 101 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Y = Yes 
N = No 
Absence of this field infers No (default) 
41 
Direct Electronic 
Access 
N 
Char 
Signifies order received from a direct 
access or sponsored access customer. 
Valid value: 
Y = Yes 
Absence of this field infers No (default) 
42 
Aggregated Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(3), it signifies that the 
order consists of several orders aggregated 
together. This maps to the UK version of 
Commission Delegated Regulation (EU) No 
2017/580value "AGGR". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or Pending 
Allocation Order has been populated.   
43 
Pending Allocation 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(2), it signifies that the 
order submitter "is authorized under the 
legislation of a Member State to allocate an 
order to its client following submission of the 
order to the trading venue and has not yet 
allocated the order to its client at the time of 
the submission of the order". This maps to 
the UK version of Commission Delegated 
Regulation (EU) No 2017/580value "PNAL". 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
Not valid if Client ID Short Code or 
Aggregated Order has been populated.


---
*Page 102*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 102 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
44 
Liquidity Provision 
Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 3, it signifies that the order 
was submitted "as part of a market making 
strategy pursuant to Articles 17 and 18 of 
the UK version of Directive 2014/65/EU or is 
submitted as part of another activity in 
accordance with Article 3" (of the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580). 
Valid value: 
Y = Yes 
Absence of this field infers No (default). 
45 
Risk Reduction Order 
N 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/590Article 4(2)(i), it signifies that the 
commodity derivative order is a transaction 
"to reduce risk in an objectively measurable 
way in accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
Valid value: 
Y = Yes 
Absence of this field infers No (default).


---
*Page 103*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 103 
 
 
Example Message Flow 
Amend Order 
 
4.10.6 
Order Amend Rejected (14) 
Order Amend Rejected is returned when an Amend Order (13) request is rejected. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Client specified identifier of the order.  
2 
Order ID 
N 
UInt64 
Unique order identifier assigned by the 
trading system. 
3 
Original Client Order 
ID 
Y 
String (19) 
Original order identified as the order to be 
amended. 
4 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
5 
Order Status 
Y 
UInt8 
Order status as at the time of rejection:


---
*Page 104*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 104 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Valid values: 
0 = New 
1 = Partially Filled 
2 = Filled 
3 = Done for Day 
4 = Cancelled 
6 = Pending Cancel 
8 = Rejected 
10 = Pending New 
12 = Expired 
14 = Pending Replace 
6 
Amend Reject Code 
N 
UInt16 
Code that identifies the reason for the 
rejection. 
Valid values: 
0 = Too late to amend 
1 = Unknown order 
3 = Order already in Pending Cancel or 
Pending Replace Status 
6 = Duplicate Client Order ID received 
18 = Invalid price increment 
99 = Other 
7 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Amend Reject 
Code = ‘99’ Other 
8 
Related High Price 
C 
Int64 
Upper price limit value 
9 
Related Low Price 
C 
Int64 
Lower price limit value 
4.10.7 
Cancel Order (15) 
Cancel Order is used to cancel the remaining quantity of an existing order. An Execution Report (8) is 
returned to confirm cancellation or an Order Cancel Rejected (16) if the cancel is rejected. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Unique identifier set by the entering firm. 
2 
Order ID 
N 
UInt64 
Unique order identifier assigned by the 
trading system.


---
*Page 105*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 105 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
3 
Original Client Order 
ID 
Y 
String (19) 
Original order identified as the order to be 
cancelled. 
4 
Security ID  
Y 
UInt64 
Tradable Instrument identifier. 
Must be the same as the original order. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
6 
Side 
Y 
UInt8 
Side of the order. 
Valid values: 
1 = Buy 
2 = Sell 
Must be the same as the original order. 
4.10.8 
Order Cancel Rejected (16) 
Order Cancel Rejected is returned when a Cancel Order (15) request, a cancellation instruction for a 
quote side in a Mass Quote (22) is rejected or a Cancel Cross Order (28) is rejected. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Client specified identifier of the order. 
1 
Secondary Client 
Order ID 
N 
UInt8 
Quote Entry ID in a Mass Quote (22). 
2 
Order ID 
N 
UInt64 
Unique order identifier assigned by the 
trading system. 
3 
Original Client Order 
ID 
Y 
String (19) 
Original order identified as the order to be 
cancelled. 
Null for a Mass Quote. 
4 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
5 
Order Status 
Y 
UInt8 
Order status as at the time of rejection: 
Valid values: 
0 = New 
1 = Partially Filled 
2 = Filled 
3 = Done for Day 
4 = Cancelled 
6 = Pending Cancel


---
*Page 106*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 106 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
8 = Rejected 
10 = Pending New 
12 = Expired 
14 = Pending Replace 
6 
Cancel Reject Code 
Y 
UInt16 
Code that identifies the reason for the 
rejection. 
Valid values: 
0 = Too late to amend 
1 = Unknown order 
3 = Order already in Pending Cancel or 
Pending Replace Status 
6 = Duplicate Client Order ID received 
99 = Other 
7 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Cancel Reject 
Code = ‘99’ Other 
8 
Side 
N 
UInt8 
Optional qualifier to indicate the quote side 
in a Mass Quote (22). 
4.10.9 
Cancel Cross Order (28) 
Cancel Cross Order is used to cancel a cross order held in the RFC interval. An Execution Report (8) 
per side is returned to confirm cancellation or an Order Cancel Rejected (16) per side is returned if 
the cancel is rejected. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Cross ID 
Y 
String (19) 
Unique identifier set by the originator. 
1 
Host Cross ID 
N 
UInt64 
A unique order identifier assigned by the 
trading system. This identifier is not 
changed by cancel messages; it will remain 
the same for all chain of cross orders. 
2 
Original Cross ID 
Y 
String (19) 
Unique identifier of the original cross, set by 
the originator. 
3 
Transact Time 
Y 
UInt64 
Timestamp when the message was 
generated. 
4 
Security ID  
Y 
UInt64 
Tradable instrument identifier


---
*Page 107*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 107 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
5 
Cross Type 
Y 
UInt8 
Type of cross being submitted to a market 
Valid values:  
101 = Guaranteed 
102 = Non-Guaranteed 
6 
Cross Prioritization 
Y 
UInt8 
Indicates which side of the cross will be 
prioritized 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
7 
Buy Side Client Order 
ID 
Y 
String (19) 
Unique identifier set by the order originator. 
8 
Buy Side Original 
Client Order ID 
N 
String (19) 
Unique identifier of the original order, set by 
the order originator. 
9 
Sell Side Client Order 
ID 
Y 
String (19) 
Unique identifier set by the order originator. 
10 
Sell Side Original 
Client Order ID 
N 
String (19) 
Unique identifier of the original order, set by 
the order originator. 
 
4.10.10 Execution Report (8) 
Execution Report is used to: 
• 
confirm the receipt of an order submitted using New Order Single or Mass Quote 
• 
confirm changes to an existing order (i.e. accept cancel and replace requests) 
• 
confirm or convey an order cancellation or expiration 
• 
convey order or trade cancellation by Market Operations 
• 
convey triggering of a stop order 
• 
convey fill information 
• 
reject orders 
• 
convey speed bump processing 
• 
convey information about restated persisted orders carried from one trading day to the next. 
• 
convey cross order processing 
Exec Type identifies the purpose of the execution report message and Order Status conveys the 
current state of the order.


---
*Page 108*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 108 
 
 
The attributes that can be returned in an Execution Report for each execution type are listed in the 
Execution Report Matrix. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
The client specified identifier in the 
message that caused this Execution Report. 
For quotes this is mapped to Quote ID in a 
Mass Quote (22) 
1 
Secondary Client 
Order ID 
N 
UInt8 
Quote Entry ID in a Mass Quote (22). 
Conditionally required according to the 
Execution Report Matrix. 
2 
Order ID 
Y 
UInt64 
Unique order identifier assigned by the 
trading system. 
3 
Original Client Order 
ID 
C 
String (19) 
Client Order ID of the previous order (NOT 
the initial order of the day) as assigned by 
the institution.  
Identifies the previous order in cancel and 
cancel/replace requests. 
Conditionally required according to the 
Execution Report Matrix. 
Not applicable for an order from a Mass 
Quote (22). 
4 
Security ID 
Y 
UInt64 
Tradable Instrument identifier. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
6 
Side 
Y 
UInt8 
Side of the order. 
Valid values: 
1 = Buy 
2 = Sell 
7 
Order Quantity 
Y 
Int32 
Total quantity of the order. 
8 
Order Type 
Y 
UInt8 
Order type applicable to the order. 
Valid values: 
2 = Limit 
3 = Stop Market 
4 = Stop Limit 
10 = Market


---
*Page 109*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 109 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
11 = Iceberg 
12 = Post Only 
13 = One Cancels Other Market 
14 = One Cancels Other Limit 
9 
Order Price 
Y 
Int64 
Price of the order. 
10 
Time in Force 
Y 
UInt8 
Specifies how long the order remains in 
effect. 
Valid values: 
0 = Day 
1 = Good Till Cancel (GTC) 
3 = Immediate Or Cancel (IOC) 
4 = Fill Or Kill (FOK) 
6 = Good Till Date (GTD) 
11 
Order Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
12 
Order Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
13 
Account Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA 
For contracts assigned to the T4 booking 
model only 3 = House is valid whereas for 
the T2 booking model all account types are 
valid. 
14 
Executing Firm 
Y 
String (4) 
Identifier of the executing firm, a member 
mnemonic.


---
*Page 110*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 110 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
15 
Client ID Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3 
Not valid if populated with either 1, 2 or 3 
Conditionally required for client orders 
Mandatory where Order Capacity is 
populated with A (agency) = AOTC or R 
(riskless principal) = MTCH 
Conditionally required according to the 
Execution Report Matrix. 
16 
Legal Entity ID 
C 
String (41) 
LEI.  
Conditionally required according to the 
Execution Report Matrix. 
17 
Proprietary Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
Conditionally required according to the 
Execution Report Matrix. 
18 
Entering Firm 
C 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
Conditionally required according to the 
Execution Report Matrix. 
19 
Origination Trader 
Y 
String (41) 
Order origination trader. 
20 
Customer Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
Conditionally required according to the 
Execution Report Matrix. 
21 
Correspondent Broker 
C 
String (4) 
A 3 character broker code (Member 
mnemonic). 
 
 Validated at point of reporting


---
*Page 111*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 111 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Conditionally required according to the 
Execution Report Matrix. 
23 
Market Maker 
C 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative. 
Conditionally required according to the 
Execution Report Matrix. 
24 
Decision Maker 
C 
UInt64 
Decision maker short code, used under the 
power of representation clause where the 
investment decision maker may be a third 
party in accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/590. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
Conditionally required according to the 
Execution Report Matrix. 
25 
Investment Decision 
within Firm (IDM) 
C 
UInt64 
Short code to identify the individual or 
algorithm within the investment firm who is 
responsible for the investment decision. 
Mandatory where Order Capacity is 
populated with P (principal) = DEAL, in 
accordance with the UK version of 
Commission Delegated Regulation (EU) No 
2017/580 
Conditionally required according to the 
Execution Report Matrix. 
26 
Execution within Firm 
(EDM) 
Y 
UInt64 
Short code to identify the execution or 
algorithm within the investment firm who is 
responsible for the execution. 
Short code 3 (NORE) used where the 
decision on execution venue was made by a 
client or a person outside of the executing 
firm. 
Where Direct Electronic Access is 
populated with Y, the short code should 
always be 3 (NORE).


---
*Page 112*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 112 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
27 
Investment Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision. 
Mandatory where Investment Decision 
Within Firm (IDM) is populated with a short 
code representing an individual 
Conditionally required according to the 
Execution Report Matrix. 
28 
Execution Decision 
Country 
C 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision. 
Mandatory where Execution within Firm 
(EDM) is populated with a short code 
representing an individual. 
Conditionally required according to the 
Execution Report Matrix. 
29 
Client Branch Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
*Mandatory where Account Type = 1, 8 or 
101. 
Conditionally required according to the 
Execution Report Matrix. 
30 
Broker Client ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
31 
Text 
C 
String (51) 
Free text. 
Conditionally required according to the 
Execution Report Matrix. 
Not applicable for an order from a Mass 
Quote (22) 
32 
Self Match Prevention 
ID 
N 
UInt32 
Identifies an order that should not be 
matched to an opposite order if both buy 
and sell orders for the trade contain the 
 
 Validated at point of reporting


---
*Page 113*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 113 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
same Self Match Prevention ID and are 
submitted by the same member. 
Conditionally required according to the 
Execution Report Matrix. 
33 
Display Quantity 
C 
UInt32 
Visible quantity of an Iceberg order.  
Conditionally required if Order Type = ‘11’ 
Iceberg. 
If present, must be < Order Quantity. 
Not applicable for an order from a Mass 
Quote (22) 
34 
Expiry Date 
C 
UInt32 
The expiry date of an order. 
Conditionally required if Time In Force = ‘0’ 
Day or ‘6’ Good ‘til Date. 
Format is YYYYMMDD. 
Not applicable for an order from a Mass 
Quote (22) 
35 
Trigger Price 
C 
Int64 
Trigger price for stop orders. 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO Market 
Order Type = ‘14’ OCO Limit 
Not applicable for an order from a Mass 
Quote (22). 
36 
Trigger Price Type 
C 
UInt8 
Type of price event that triggers the stop 
order: 
Valid values: 
2 = Last Trade  
4 = Best Bid or Last Trade 
5 = Best Offer or Last Trade 
Conditionally required if:  
Order Type = ‘3’ Stop Market 
Order Type = ‘4’ Stop Limit 
Order Type = ‘13’ OCO Market 
Order Type = ‘14’ OCO Limit


---
*Page 114*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 114 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Not applicable for an order from a Mass 
Quote (22). 
37 
Trigger Type 
C 
UInt8 
Trigger prompt for stop order elements.  
Valid value: 
4 = Price Movement 
Not applicable for an order from a Mass 
Quote (22). 
38 
Trigger New Price 
C 
Int64 
Limit order price of the stop once triggered. 
Conditionally required if Order Type = ‘14’ 
OCO Limit. 
Not applicable for an order from a Mass 
Quote (22). 
40 
Cancel on Disconnect 
Y 
Char 
Specifies whether the order should be 
cancelled on system disconnection: 
Valid values: 
Y = Yes 
N = No 
Default N = No 
41 
Direct Electronic 
Access 
Y 
Char 
Signifies order received from a direct 
access or sponsored access customer. 
Valid value: 
Y = Yes 
Default N = No 
42 
Aggregated Order 
Y 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(3), it signifies that the 
order consists of several orders aggregated 
together. This maps to the UK version of 
Commission Delegated Regulation (EU) No 
2017/580value "AGGR". 
Valid value: 
Y = Yes 
Default N = No. 
Not valid if Client ID Short Code or Pending 
Allocation Order has been populated.


---
*Page 115*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 115 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
43 
Pending Allocation 
Order 
Y 
Char 
In the context the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 2(2), it signifies that the 
order submitter "is authorized under the 
legislation of a Member State to allocate an 
order to its client following submission of the 
order to the trading venue and has not yet 
allocated the order to its client at the time of 
the submission of the order". This maps to 
the UK version of Commission Delegated 
Regulation (EU) No 2017/580value "PNAL". 
Valid value: 
Y = Yes 
Default N = No. 
Not valid if Client ID Short Code or 
Aggregated Order has been populated.   
44 
Liquidity Provision 
Order 
Y 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/580Article 3, it signifies that the order 
was submitted "as part of a market making 
strategy pursuant to Articles 17 and 18 of 
the UK version of Directive 2014/65/EU, or 
is submitted as part of another activity in 
accordance with Article 3" (of the UK 
version of Commission Delegated 
Regulation (EU) No 2017/580). 
Valid value: 
Y = Yes 
Default N = No unless order is from a Mass 
Quote in which case the default is Y. 
45 
Risk Reduction Order 
Y 
Char 
In the context of the UK version of 
Commission Delegated Regulation (EU) No 
2017/590Article 4(2)(i), it signifies that the 
commodity derivative order is a transaction 
"to reduce risk in an objectively measurable 
way in accordance with Article 57 of the UK 
version of Directive 2014/65/EU". 
Valid value: 
Y = Yes


---
*Page 116*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 116 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Default N = No. 
46 
Quote Price Level 
N 
UInt8 
Indicates the price level being quoted. 
Valid values are 1, 2 or 3 (i.e. up to 3 price 
levels). 
51 
Cross ID 
C 
String (19) 
Identifier for the cross order, set by the 
trader. Unique per trader, per day.  
Conditionally Required for Cross Order 
52 
Host Cross ID 
C 
UInt64 
Unique order identifier used by exchange to 
reference a cross. 
Conditionally required if CrossID is 
populated 
53 
Original Cross ID 
C 
String (19) 
CrossID referencing the cross to be 
cancelled  
 
Conditionally required if CrossID is 
populated 
54 
Cross Type 
C 
UInt8 
Type of cross submitted to the market.  
 
Identifies whether it is a guaranteed or non 
guaranteed cross.  
 
Valid values:  
101 = Guaranteed 
102 = Non-Guaranteed 
 
Conditionally required if CrossID is 
populated 
55 
Cross Prioritization 
C 
UInt8 
Indicates which side of the cross order 
should be prioritised. Identifies the initiating 
side.  
 
Valid values:  
1 = Buy side is prioritized 
2 = Sell side is prioritized 
 
Conditionally required if CrossID is 
populated 
56 
Venue Type 
C 
Char 
Valid values:


---
*Page 117*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 117 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
O = Offbook 
B = Central limit order book (CLOB) 
 
Conditionally required if CrossID is 
populated and ExecType = ‘F’ Trade. 
65 
Exec ID 
Y 
String (21) 
Unique identifier assigned by the trading 
system to the execution message. 
66 
Exec Ref ID 
C 
String (21) 
Reference identifier used with Trade Cancel 
execution type. 
Conditionally required if Exec Type = ‘H’ 
Trade Cancel. 
Not applicable for an order from a Mass 
Quote (22) 
67 
Exec Type 
Y 
Char 
Describes the specific Execution Report. 
Valid values: 
0 = New 
3 = Done  
4 = Cancelled  
5 = Replaced 
6 = Pending Cancel 
8 = Rejected 
C = Expired  
D = Restated  
E = Pending Replace 
F = Trade 
H = Trade Cancel 
L = Triggered or Activated by the System  
68 
Order Status 
Y 
UInt8 
Identifies current status of order. 
Valid values: 
0 = New 
1 = Partially Filled 
2 = Filled 
3 = Done for day 
4 = Cancelled 
6 = Pending Cancel 
8 = Rejected 
10 = Pending New 
12 = Expired 
14 = Pending Replace


---
*Page 118*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 118 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
69 
Entering Trader 
Y 
String (11) 
Identifier of the trader entering the order. 
70 
Clearing Firm 
C 
String (4) 
Identifier of the clearing firm, a member 
mnemonic. 
Conditionally required if Exec Type = ‘F’ 
Trade. 
71 
Trade ID 
C 
UInt64 
Identifier assigned by the trading system 
which joins buy and sell half trades. 
Conditionally required if Exec Type = ‘F’ 
Trade. 
72 
Exec Restatement 
Reason 
C 
UInt16 
The reason for restatement. 
Valid values: 
1 = GT renewal / restatement 
99 = Other. See Exec Type Reason for 
speed bump handling. 
Conditionally required if Exec Type = ‘D’ 
Restated. 
Not applicable for an order from a Mass 
Quote (22) 
73 
Exec Type Reason 
C 
UInt8 
The initiating event for the Execution 
Report. 
Conditionally required to report: 
• 
unsolicited cancellation  
• 
order status in New Order Cross 
processing 
• 
 order status in speed bump 
processing. 
Valid values: 
4 = Unsolicited order cancellation 
101 = Order accepted but speed bump 
applied 
102 = Order added after speed bump 
103 = Order cancelled whilst in speed bump 
delay 
104 = Original order is in speed bump 
enforced delay


---
*Page 119*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 119 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
105 = Order updated after speed bump 
delay 
106 = Amend is in speed bump delay 
107 = Order amended after speed bump 
delay 
108 = Order rejected after speed bump 
delay 
109 = Unsolicited cancel while in speed 
bump 
120 = Order held in RFC interval 
74 
Order Category 
C 
UInt8 
Defines the type of interest behind a trade 
(fill or partial fill). 
Valid value: 
7 = Implied Order 
Conditionally required for a trade from an 
implied order when Exec Type = ‘F’ Trade. 
75 
Aggressor Indicator 
C 
Char 
Indicates if a matching order is an 
aggressor or not in the trade. 
Y = Aggressor 
N = Passive 
Conditionally required if Exec Type = ‘F’ 
Trade. 
Not applicable for an order from a Mass 
Quote (22) 
76 
Order Reject Reason 
N 
UInt16 
Code to identify reason for order rejection. 
Valid values: 
6 = Duplicate Order 
15 = Unknown Account(s) 
18 = Invalid price increment 
99 = Other. 
Conditionally required if Exec Type = ‘8’ 
Rejected. 
77 
Reason Text 
N 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Exec Type Reason 
= '4' Unsolicited order cancellation or Order 
Reject Reason = ‘99’ Other.


---
*Page 120*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 120 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
78 
Last Quantity 
C 
UInt32 
The total volume of this trade. 
Conditionally required if Exec Type = ‘F’ 
Trade.  
79 
Last Price 
C 
Int64 
The price of this trade. 
Conditionally required if Exec Type = ‘F’ 
Trade. 
80 
Cumulative Quantity 
Y 
UInt32 
The quantity of the order that has been 
executed so far. 
81 
Leaves Quantity 
Y 
UInt32 
The quantity open for further execution.  
82 
Related High Price 
C 
Int64 
Upper price limit value 
For Stop orders, this will be the stop 
tolerance band. 
83 
Related Low Price 
C 
Int64 
Lower price limit value 
84 
No Legs 
C 
UInt8 
Number of Instrument Leg repeating group 
instances. 
Conditionally required if Exec Type = ‘F’ 
Trade on a multileg tradable instrument. 
 
Legs Body Fields 
Presence Map 
C 
Bitmap 
Variable 
Length (1) 
Conditionally required if No Legs > 0 where 
each repeating group represents a leg in the 
multileg instrument. 
 
0 
Leg Security ID 
Y 
UInt64 
Multileg tradable instrument's individual 
Security ID. 
 
1 
Leg Side 
Y 
UInt8 
The side of this individual leg (multileg 
security). 
Valid values: 
1 = Buy 
2 = Sell 
 
2 
Leg Alloc ID 
Y 
UInt64 
Strategy leg trade identifier assigned by the 
trading system which is shared by half 
trades. 
 
3 
Leg Last Price 
Y 
Int64 
Execution price assigned to the leg of the 
multileg tradable instrument.


---
*Page 121*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 121 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
 
4 
Leg Last 
Quantity 
Y 
UInt32 
Fill quantity for the instrument leg.


---
*Page 122*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 122 
 
 
Example Message Flows 
OCO submitted, Stop triggered and Limit cancelled 
An OCO order is submitted as a Limit offer with a Stop Market trigger price of 6808, an incoming offer 
triggers the Stop order and cancels Limit element of the OCO. An Execution Report is not sent for 
cancellation. The triggered Stop Market is converted to a Limit order at a trigger new price of 6808.


---
*Page 123*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 123 
 
 
OCO Partial Trade 
OCO is submitted as Limit offer for 15 lots at 1825 with a Stop Market trigger price of 1780. 
A Limit bid is submitted at 1830 for 10 lots. The OCO order is not triggered but trades 10 lots with the 
incoming order. The OCO remains in the order book with a residual volume of 5 lots


---
*Page 124*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 124 
 
 
Implied trade


---
*Page 125*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 125 
 
 
Custom strategy Butterfly trades


---
*Page 126*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 126 
 
 
Order cancellation by Exchange 
 
Order rejected price limits breached


---
*Page 127*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 127 
 
 
4.10.10.1 Execution Report Matrix 
An Execution Report can be returned in response to a request e.g. New Order Single (12) or unsolicited in response to a particular action. 
The fields that can be included are contingent on the purpose of the message and any mandatory or conditionally supplied tags specified by the originator in the initiating request 
or returned response to a particular action. 
Legend: 
M = Mandatory 
C = Conditional 
O = Optional 
The following table indicates the field that will be returned for specific execution types: 
Field Name 
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
Executing Firm 
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
Client ID Short 
Code 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Legal Entity ID 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Proprietary 
Client ID 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Entering Firm 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C


---
*Page 128*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 128 
 
 
Field Name 
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
Origination 
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
Customer 
Account 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Correspondent 
Broker 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Market Maker 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Broker Client ID 
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
Decision Maker 
C 
C 
 
 
 
 
 
 
 
 
 
C 
C 
C 
C 
Investment 
Decision within 
Firm (IDM) 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
Execution 
Decision within 
Firm (EDM) 
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
Investment 
Decision 
Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C


---
*Page 129*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 129 
 
 
Field Name 
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
Execution 
Decision 
Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
Client Branch 
Country 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
Order Capacity 
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
Order 
Restrictions 
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
Direct 
Electronic 
Access 
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
Aggregated 
Order 
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
Pending 
Allocation Order 
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
Liquidity 
Provision Order  
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
Risk Reduction 
Order 
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
*Page 130*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 130 
 
 
Field Name 
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
Entering Trader 
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
Clearing Firm 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
Account Type 
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
Order ID 
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
Client Order ID 
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
Secondary 
Client Order ID 
O 
 
 
 
O 
 
 
O 
O 
 
 
O 
O 
O 
O 
Original Client 
Order ID 
 
 
 
 
M 
M 
M 
M 
 
 
 
 
 
 
 
Security ID 
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
Side 
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
Order Quantity 
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
Order Type 
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
Order Price 
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
Expiry Date 
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


---
*Page 131*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 131 
 
 
Field Name 
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
Cancel on 
Disconnect 
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
Transact Time 
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
Display 
Quantity 
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
Text 
C 
C 
 
 
C 
 
C 
 
 
 
 
C 
C 
C 
C 
Time in Force 
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
Self Match 
Prevention ID 
C 
C 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
Trigger Type 
C 
C2 
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
Trigger Price 
C 
C2 
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
Trigger Price 
Type 
C 
C2 
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
 
2 Will not be present when a previously triggered Stop order is restated as a Limit order.


---
*Page 132*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 132 
 
 
Field Name 
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
Trigger New 
Price 
C 
C2 
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
Quote Price 
Level 
C 
 
 
 
 
 
 
 
 
 
 
 
 
 
C 
Host Cross ID 
C 
 
 
 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
Cross ID 
C 
 
 
 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
Original Cross 
ID 
 
 
 
 
 
 
 
C 
 
 
 
 
 
 
 
Cross Type 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
Cross 
Prioritization 
C 
 
 
C 
 
 
 
C 
C 
 
 
C 
C 
C 
C 
Venue Type 
 
 
 
 
 
 
 
 
 
 
 
C 
C 
C 
 
Trade ID 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
Exec ID 
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
Exec Ref ID 
 
 
 
 
 
 
 
 
 
 
 
 
 
M 
 
Exec Type 
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
*Page 133*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 133 
 
 
Field Name 
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
Exec Type 
Reason 
C 
 
 
M 
 
M 
M 
C 
M 
 
 
 
 
 
 
Order Status 
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
Order Reject 
Reason 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
M 
Exec 
Restatement 
Reason 
 
M 
 
M 
 
 
 
 
 
 
 
 
 
 
 
Order Category 
 
 
 
 
 
 
 
 
 
 
 
C 
C 
C 
 
Aggressor 
Indicator 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
Last Quantity 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
Last Price 
 
 
 
 
 
 
 
 
 
 
 
M 
M 
M 
 
Leaves 
Quantity 
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
Cumulative 
Quantity 
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
*Page 134*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 134 
 
 
Field Name 
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
Reason Text 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
Related High 
Price 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
Related Low 
Price 
 
 
 
 
 
 
 
 
C 
 
 
 
 
 
C 
No Legs 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Legs Body 
Fields Presence 
Map 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Leg Security ID 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Leg Side 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Leg Alloc ID 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Leg Last Price 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C 
 
Leg Last 
Quantity 
 
 
 
 
 
 
 
 
 
 
 
 
M 
C


---
*Page 135*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 135 
 
 
4.10.11 Mass Cancel Request (17) 
Mass Cancel Request is used to cancel the remaining quantity of a group of orders and/or quotes 
matching criteria specified within the message. Persisted orders will be included in the cancellation 
request.  
A cross order held in an RFC interval and matches the criteria specified in the Mass Cancel Request 
will be included in the cancellation request. If one of the orders in a cross matches the criteria 
specified, then both orders in the cross will be cancelled. The Total Affected Orders count in the 
Mass Cancel Report will include both sides 
If the request is accepted, an Execution Report (8) will be sent for each order cancelled followed by 
Mass Cancel Report (18).  
If the request is rejected, Mass Cancel Report (18) will be returned indicating the reason. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
Y 
String (19) 
Unique ID of Mass Cancel Request as 
assigned by the institution. 
2 
Mass Cancel Request 
Type 
Y 
UInt8 
Specifies the type of cancellation 
requested. 
Valid values: 
1 = Cancel orders/quotes for a Security ID 
(tradable instrument) 
3 = Cancel orders/quotes for a Symbol 
(contract e.g. CADF - Copper Future) 
7 = Cancel all orders/quotes 
101 = Cancel quotes specified in Quote ID 
3 
Mass Cancel Scope 
Y 
UInt8 
Specifies the scope of the cancellation 
requested. 
Valid values: 
1 = Cancel orders only 
2 = Cancel quotes only 
3 = Cancel orders and quotes. 
Must be 2 = Cancel quotes if Mass Cancel 
Request Type = ‘101’ Cancel quotes 
specified in Quote ID. 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
7 
Security Exchange 
C 
String (5) 
Market which is used to identify the 
security: 
XLME


---
*Page 136*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 136 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Conditionally required if Symbol is 
specified. 
8 
Product Complex 
C 
String (5) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base  
Conditionally required if Symbol is 
specified. 
9 
Symbol 
C 
String (21) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future). 
Conditionally required if Mass Cancel 
Request Type = ‘3’ Cancel orders/quotes 
for a Symbol (contract). 
10 
Security ID 
C 
UInt64 
Tradable Instrument identifier. 
Conditionally required if Mass Cancel 
Request Type = ‘1’ Cancel orders/quotes 
for a Security ID. 
11 
Quote ID 
C 
String (19) 
Mass Quote Identifier. 
Conditionally required if Mass Cancel 
Request Type = ‘101’ Cancel quotes 
specified in Quote ID. 
12 
Broker Client ID 
N 
String (17) 
Identifier of the entity in a risk group. 
Can be used with Mass Cancel Request 
Type = ‘7’ Cancel all orders/quotes. 
13 
Side 
N 
UInt8 
Optional qualifier to indicate the side of the 
market for which orders are to be 
cancelled. Can be used if Mass Cancel 
Request Type = '3' Cancel orders/quotes 
for a Symbol (contract). 
Absence of this field indicates that 
orders/quotes are to be cancelled 
regardless of side.


---
*Page 137*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 137 
 
 
4.10.12 Mass Cancel Report (18) 
Mass Cancel Report is returned in response to a Mass Cancel Request (17). 
Each affected order that is cancelled is acknowledged with a separate Execution Report (8). 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Client Order ID 
N 
String (19) 
Unique ID of Mass Cancel Request as 
assigned by the institution. 
1 
Mass Action Report ID 
Y 
String (21) 
Unique Identifier for the Order Mass Cancel 
Report assigned by the system. 
2 
Mass Cancel Request 
Type 
Y 
UInt8 
Specifies the type of cancellation requested. 
Valid values: 
1 = Cancel orders/quotes for a Security ID 
(tradable instrument) 
3 = Cancel orders/quotes for a Symbol 
(contract e.g. CADF - Copper Future) 
7 = Cancel all orders/quotes 
101 = Cancel quotes specified in Quote ID 
3 
Mass Cancel Scope 
Y 
UInt8 
Specifies the scope of the cancellation 
requested. 
Valid values: 
1 = Cancel orders only 
2 = Cancel quotes only 
3 = Cancel orders and quotes. 
Must be 2 = Cancel quotes if Mass Cancel 
Request Type = ‘101’ Cancel quotes 
specified in Quote ID. 
4 
Mass Cancel 
Response 
Y 
UInt8 
Indicates the action taken on the cancel 
request: 
Valid values: 
0 = Cancel Request Rejected 
1 = Cancel orders/quotes for a Security ID  
3 = Cancel orders/quotes for a Symbol 
(contract)  
7 = Cancel all orders/quotes 
101 = Cancel quotes specified in Quote ID 
5 
Transact Time 
Y 
UInt64 
Time when the message was generated.


---
*Page 138*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 138 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
6 
Total Affected Orders 
Y 
UInt32 
Indicates the total number of orders affected 
by the Mass Cancel Request. 
7 
Security Exchange 
C 
String (5) 
Market which is used to identify the security: 
XLME 
Conditionally required if Symbol is specified. 
8 
Product Complex 
C 
String (5) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base  
Conditionally required if Symbol is specified. 
9 
Symbol 
C 
String (21) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future). 
Conditionally required if Mass Cancel 
Request Type = ‘3’ Cancel orders/quotes for 
a Symbol (contract). 
10 
Security ID 
C 
UInt64 
Tradable Instrument identifier. 
Conditionally required if Mass Cancel 
Request Type = ‘1’ Cancel orders/quotes for 
a Security ID. 
11 
Quote ID 
C 
String (19) 
Mass Quote Identifier. 
Conditionally required if Mass Cancel 
Request Type = ‘101’ Cancel quotes 
specified in Quote ID. 
12 
Broker Client ID 
C 
String (17) 
Identifier of the entity in a risk group. 
Can be used with Mass Cancel Request 
Type = ‘7’ Cancel all orders/quotes. 
13 
Side 
C 
UInt8 
Optional qualifier to indicate the side of the 
market for which orders are to be cancelled. 
Can be used if Mass Cancel Request Type 
= '3' Cancel orders/quotes for a Symbol 
(contract).


---
*Page 139*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 139 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
Absence of this field indicates that 
orders/quotes are to be cancelled 
regardless of side. 
14 
Mass Cancel Reject 
Reason 
C 
UInt16 
Code specifying the reason for the rejection. 
Valid values: 
1 = Invalid or Unknown Security 
3 = Invalid or Unknown Product 
99 = Other. 
Conditionally required if Mass Cancel 
Response = ‘0’ Cancel Request Rejected 
15 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Mass Cancel Reject 
Reason = ‘99’ Other.


---
*Page 140*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 140 
 
 
Example Message Flow 
Mass cancel orders and quotes in a contract


---
*Page 141*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 141 
 
 
4.10.13 Mass Quote (22) 
Mass Quote is used to enter and manage (amend and/or cancel) multiple orders submitted as quotes 
in a single contract. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Quote ID 
Y 
String (19) 
Client specified unique identifier for the 
Mass Quote. This maps to the Client Order 
ID in the Execution Report. 
1 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
2 
Account Type 
Y 
UInt8 
Specifies the type of account associated 
with the order. 
Valid values: 
1 = Client ISA 
3 = House 
8 = Joint back office account (JBO) = Gross 
OSA 
101 = Client OSA 
For contracts assigned to the T4 booking 
model only 3 = House is valid whereas for 
the T2 booking model all account types are 
valid. 
3 
Order Restrictions 
Y 
Char 
Restrictions associated with an order. 
Valid values: 
D = Non-algorithmic (human) 
E = Algorithmic (algo) 
4 
Order Capacity 
Y 
Char 
Indicates the trading capacity. 
Valid values: 
A (agency) = AOTC 
P (principal) = DEAL 
R (riskless principal) = MTCH 
6 
Client ID Short Code 
C 
UInt64 
Client short code identifier. If there is no 
client this can be populated with the value 
‘0’ = No Client for Account Type = 3 
Not valid if populated with either 1, 2 or 3. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
7 
Legal Entity ID 
C 
String (41) 
LEI.


---
*Page 142*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 142 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
8 
Proprietary Client ID 
C 
String (41) 
Proprietary or Custom Client ID as assigned 
by the member.  
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
9 
Entering Firm 
N 
String (4) 
Identifier of the entering firm, a member 
mnemonic. 
10 
Origination Trader 
Y 
String (41) 
Order origination trader. 
11 
Customer Account 
C 
String (31) 
Identification of the client account code 
where the Account Type = 1, 8 or 101. 
12 
Correspondent Broker 
N 
String (4) 
A 3 character broker code (Member 
mnemonic). 
14 
Market Maker 
N 
Char 
This should be set to Y if the trader qualifies 
for a Market Maker initiative. 
15 
Decision Maker 
C 
UInt64 
Decision maker short code, required on 
client orders to identify the investment 
decision maker. Also used under the power 
of representation clause where the 
investment decision maker may be a third 
party in accordance with Article 8 of 
Commission Delegated Regulation (EU) 
…/… 22 on transaction reporting under 
Article 26 of Regulation EU No 600/2014. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
16 
Investment Decision 
within Firm (IDM) 
N 
UInt64 
Short code to identify the individual who is 
responsible for the investment decision. 
17 
Execution Decision 
within Firm (EDM) 
Y 
UInt64 
Short code to identify the execution decision 
maker with the firm. 
18 
Investment Decision 
Country 
N 
String (3) 
ISO country code of the branch responsible 
for the person making the investment 
decision. 
19 
Execution Decision 
Country 
N 
String (3) 
ISO country code of the branch responsible 
for the person making the execution 
decision.


---
*Page 143*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 143 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
20 
Client Branch Country 
C 
String (3) 
ISO country code to identify the branch that 
received the client order or made an 
investment decision for a client. 
Conditionally required for client orders i.e. 
Account Type = 1, 8 or 101. 
21 
Broker Client ID 
Y 
String (17) 
Identifier of the entity in a risk group. 
22 
Self Match Prevention 
ID 
N 
UInt32 
Identifies an order that should not be 
matched to an opposite order if both buy 
and sell orders for the trade contain the 
same Self Match Prevention ID and are 
submitted by the same member. 
23 
Direct Electronic 
Access 
N 
Char 
Signifies order received from a direct 
access or sponsored access customer. 
Valid value: 
Y = Yes 
Absence of this field infers No (default) 
24 
Total Quote Entries 
Y 
UInt8 
Total number of Quote entries (pairs) in this 
message. 
Must be ≥ 1 and ≤ 20. 
25 
No Quote Sets 
Y 
UInt8 
The number of sets of quotes contained in 
the message. 
Must be ≥ 1 but ≤ Total Quote Entries. 
 
Quote Sets Field 
Presence Map 
Y 
Bitmap 
Variable 
Length (1) 
This will indicate the fields/nested repeating 
blocks present in this repeating block. 
 
1 
Security ID 
Y 
UInt64 
Tradable Instrument identifier. 
 
2 
No Quote Entries 
Y 
UInt8 
Number of Quote Entry repeating blocks.  
Must be ≥ 1 but ≤ 3. 
 
 
Quote Entry Field 
Presence Map 
Y 
Bitmap 
Variable 
Length (1) 
This will indicate the fields/nested repeating 
blocks present in this repeating block.


---
*Page 144*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 144 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
 
 
0 
Quote Entry 
ID 
Y 
UInt8 
Quote pair ID in a Mass Quote message. 
Starts from 1 and incremented by 1 for each 
quote pair in the message. 
The last value must be the same as Total 
Quote Entries in this message. 
 
 
1 
Quote Price 
Level 
Y 
UInt8 
Indicates the price level that is being 
submitted or modified. 
Valid values are 1, 2 or 3. 
 
 
2 
Bid Size 
Y 
Int32 
Bid quantity. 
Value 0 indicates cancellation of this side. 
Value -1 indicates no change to this side or 
a dummy quote.  
 
 
3 
Offer Size 
Y 
Int32 
Offer quantity. 
Value 0 indicates cancellation of this side. 
Value -1 indicates no change to this side or 
a dummy quote.  
 
 
4 
Bid Price 
Y 
Int64 
Bid price. 
Null value indicates dummy quote or a 
cancelled price. 
 
 
5 
Offer Price 
Y 
Int64 
Offer price. 
Null value indicates dummy quote or a 
cancelled price. 
4.10.14 Mass Quote Ack (23) 
Mass Quote Ack reports the rejection of a Mass Quote (22) at message level. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Quote ID 
Y 
String (19) 
Client specified unique identifier for the 
Mass Quote. This maps to the Client Order 
ID in the Execution Report. 
1 
Transact Time 
Y 
UInt64 
Time when the message was generated.


---
*Page 145*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 145 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
2 
Quote Status 
Y 
UInt8 
Status of the Mass Quote 
acknowledgement. 
Valid value: 
5 = Rejected 
3 
Quote Reject Reason 
Y 
UInt16 
Code specifying the reason for the rejection. 
Valid values: 
6 = Duplicate quote 
9 = Not authorized to quote security 
99 = Other 
4 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Quote Reject 
Reason = ‘99’ Other.


---
*Page 146*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 146 
 
 
Example Message Flows 
Mass Quote submission


---
*Page 147*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 147 
 
 
Entire Mass Quote rejected


---
*Page 148*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 148 
 
 
Mass Quote – individual quote rejections


---
*Page 149*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 149 
 
 
 
Crossed quotes within a Quote Entry rejected 
The bid for 6905 for 5 lots and offer at 6904.5 for 8 lots in Quote Entry ID = 2 can trade with each 
other.  The matching engine will reject a cross quote pair within a single Quote Entry. The originator 
of the Mass Quote will be notified of the rejection by an Execution Report for each quote pair.


---
*Page 150*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 150 
 
 
Mass Quote entries replaced


---
*Page 151*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 151 
 
 
Individual quotes cancelled


---
*Page 152*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 152 
 
 
4.10.15 Quote Request (20) 
Quote Request is used to requests prices from market participants. 
The Quote Request is disseminated via the Market Data service to market participants.  
BP 
Field Name 
Req 
Data Type 
Description 
0 
Quote Request ID 
Y 
String (19) 
Client specified identifier for the quote 
request. 
1 
Security ID  
Y 
UInt64 
Tradable Instrument identifier. 
2 
Quote Request Type 
Y 
UInt8 
Indicates the type of Quote Request being 
generated. 
Valid values: 
1 = Manual - used to indicate a single quote 
request 
2 = Automatic - used to indicate a streaming 
quote request 
3 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
4 
Side 
N 
UInt8 
Side of order. If not defined indicates a two-
sided quote is required. 
Valid values: 
1 = Buy 
2 = Sell 
5 
Quantity 
N 
Int32 
Order quantity. 
If not entered, a volume of 0 will be 
published. 
4.10.16 Quote Request Ack (21) 
Quote Request Ack (21) is returned by the gateway in response to a Quote Request (20). 
BP 
Field Name 
Req 
Data Type 
Description 
0 
Quote Request ID 
Y 
String (19) 
Client specified identifier for the quote 
request. 
1 
Security ID  
Y 
UInt64 
Tradable Instrument identifier. 
2 
Quote Request Type 
Y 
UInt8 
Indicates the type of Quote Request being 
generated. 
Valid values:


---
*Page 153*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 153 
 
 
BP 
Field Name 
Req 
Data Type 
Description 
1 = Manual - used to indicate a single quote 
request 
2 = Automatic - used to indicate a streaming 
quote request 
3 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
4 
Side 
C 
UInt8 
Side of order. If not defined indicates a two-
sided quote is required. 
Valid values: 
1 = Buy 
2 = Sell. 
Conditionally required if specified on the 
original message. 
5 
Quantity 
C 
Int32 
Order quantity. 
Conditionally required if specified on the 
original message. 
6 
Quote Request 
Response ID 
Y 
String (21) 
Unique identifier for the Quote Request Ack 
assigned by the system. 
7 
Quote Request 
Response 
Y 
UInt8 
Indicates the action taken as a result of the 
Quote Request. 
Valid values: 
0 = Quote Request Accepted 
1 = Quote Request Rejected 
8 
Quote Request Reject 
Reason 
C 
UInt8 
Code that identifies the reason for the 
rejection. 
Valid value: 
99 = Other 
Conditionally required if Quote Request 
Response = ‘1’ Quote Request Rejected. 
9 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if Quote Request 
Reject Reason = ‘99’ Other


---
*Page 154*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 154 
 
 
Example Message Flow 
RFQ Submission 
 
4.10.17 MMP Reset Request (30) 
MMP Reset Request is used to reinstate a trader (i.e. Comp ID) that has breached a Market Maker 
Protection type. 
BP 
Field Name 
Req 
Data Type 
Description 
0 
MMP Reset Request 
ID  
Y 
String (19) 
Client specified identifier for the MMP 
Reset request. 
1 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
2 
Security Exchange 
Y 
String (5) 
Market which is used to identify the 
security: 
XLME 
3 
Product Complex 
Y 
String (5) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base  
4 
Symbol 
Y 
String (21) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future).


---
*Page 155*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 155 
 
 
4.10.18 MMP Reset Ack (31) 
MMP Reset Ack is returned in response to an MMP Reset Request (30). 
BP 
Field Name 
Req 
Data Type 
Description 
0 
MMP Reset Request 
ID  
Y 
String (19) 
Client specified identifier for the MMP 
Reset request. 
1 
Transact Time 
Y 
UInt64 
Time when the message was generated. 
2 
Security Exchange 
Y 
String (5) 
Market which is used to identify the 
security: 
XLME 
3 
Product Complex 
Y 
String (5) 
Identifies an entire suite of products for a 
given market. 
Valid values: 
LME = Base  
4 
Symbol 
Y 
String (21) 
Symbol for the LME contract code e.g. 
CADF (Copper Future) or OCDF (Copper 
Monthly Average Future). 
5 
MMP Reset Response 
ID  
Y 
String (21) 
Unique identifier for the MMP Reset 
Response Ack assigned by the system. 
6 
MMP Reset Response 
Y 
UInt8 
Specifies the action taken as a result of the 
MMP Reset Request message. 
Valid values: 
0 = Accepted 
2 = Rejected 
7 
MMP Reset Reject 
Reason 
C 
UInt8 
Code that identifies the reason for the 
rejection. 
Conditionally required when MMP Reset 
Response = ‘2’ Rejected 
Valid values: 
98 = Not authorised 
99 = Other 
8 
Reason Text 
C 
String (76) 
Text specifying the reason for the rejection. 
Conditionally required if MMP Reset Reject 
Reason = ‘99’ Other.


---
*Page 156*

Order Entry Gateway 
Binary Specification 
Version 1.9.1 
LME Classification: Public  
 
 
Page 156 
 
 
Example Message Flow 
MMP Reset requested
