import os
import sys
import time
import re
import pyvisa

verNum = "v1.04, Aug 18, 2023"
mainAuthor = "Masashi Nogawa @ Qorvo"
debug = 0

license = '''\
Qorvo "Double Pulse Testing on Tektronix MSO5/6 Oscilloscope Example" Software License Agreement

This legally binding agreement, for the use of the licensed software installed upon acceptance of this License Agreement, is by and between Qorvo US, Inc, on behalf of itself and its Affiliates and subsidiaries ("Qorvo"), and either an individual or legal entity, including each Affiliate of such, as applicable, on whose behalf you are legally authorized to accept this License Agreement ("Licensee"). As used herein, "you," "your," or "Licensee" shall mean such individual or entity, including Affiliates of such entity.

Licensor is only willing to license the Licensed Software to you on condition that you accept all of the terms in this License Agreement.

By installing or otherwise using or copying the Licensed Software, you expressly agree to be bound by all of the terms of this License Agreement. If you do not agree to the terms of this License Agreement, you may not install, use, compile, or copy the Licensed Software, and you must delete any downloads or copies of the Licensed Software.


1. DEFINITIONS

"Affiliate" of a party means any other Person that directly, or indirectly through one or more intermediaries, controls, or is controlled by, or is under common control with the party. For purposes of this definition, the term "control" means the power (or, as applicable, the possession or exercise of the power) to direct, or cause the direction of, the management, governance, or policies of a given entity, directly or indirectly, through any applicable means (whether through the legal, beneficial, or equitable ownership, of more than fifty percent (50%) of the aggregate of all voting or equity interests or securities of such entity, through partnership, or through some other form of ownership interest, by contract, or other applicable legal document, or otherwise).

"Confidential Information" means all information (whether written, electronic, visual, or oral) disclosed by Licensor that is marked or identified as "confidential" or with a similar legend or designation, or that the Licensor otherwise considers in good faith to be confidential.

"Documentation" means all documents, in any form, associated with the Licensed Software, including, but not limited to, user manuals, instruction manuals, specifications, and other software-associated documentation.

"Intellectual Property Rights" means any and all registered and unregistered rights granted, applied for, or otherwise now or hereafter in existence under or related to any patent, copyright, trademark, trade secret, database protection, or other intellectual property rights Laws, and all similar or equivalent rights or forms of protection, in any part of the world.

"Licensed Software" means the Qorvo "Double Pulse Testing on Tektronix MSO5/6 Oscilloscope Example" Software of Licensor as provided to Licensee under this Agreement. Licensed Software also includes any additions, updates, and releases thereto issued by Licensor from time-to-time. Licensed Software may be provided in Object Code or Source Code form.

"Licensee Product" means a product developed by Licensee embodying Licensee Software.

"Licensee Software" means software developed by Licensee using the Licensed Software.

"Object Code" means the binary or machine-readable form of the Licensed Software to which it relates.

"Source Code" means the human readable source code of the Software to which it relates, in the programming language in which the Software was written, together with any and all related compile or command files, build scripts, or other scripts relating to the creation of the Object Code of the Software.


2. LICENSE

2.1. Use of Licensed Software. Licensor hereby grants to Licensee a worldwide, fully paid-up, non-exclusive, non-transferable license to use the Licensed Software to develop Licensee Software and to incorporate the Licensee Software into Licensee Products.

2.2. No Sale. The licenses granted under this License Agreement do not constitute a sale of the Licensed Software or any portion or copy of it.

2.3. Ownership. Licensee acknowledges Licensor owns and shall retain all right, title, and interest in and to:
2.3.1. the Licensed Software and updates, and Documentation, including all Intellectual Property Rights embodied therein;
2.3.2. all of the service marks, trademarks, trade names or any other designations associated with the Licensed Software; and
2.3.3. all copyrights, patent rights, trade secret rights, and other proprietary rights relating to the Licensed Software, the Documentation, or Licensor's Confidential Information. Licensee further acknowledges and agrees that it shall have no rights with respect to any of the foregoing other than the rights expressly set forth in this License Agreement.

2.4. Restrictions on Use. Licensee agrees not to remove any Licensor identification or notices of any proprietary, patent or copyright restrictions from the Licensed Software, Documentation, or any support material.


3. REPRESENTATIONS AND WARRANTIES

3.1. Mutual Representations and Warranties. Each party represents and warrants to the other party that: (a) it is duly organized, validly existing, and in good standing as a corporation or other entity under the Laws of the jurisdiction of its incorporation or other organization; (b) it has the full right, power, and authority to enter into, and to perform its obligations and grant the rights and licenses it grants or is required to grant under, this Agreement; (c) the execution of this Agreement by its Representative whose signature is set forth at the end of this Agreement has been duly authorized by all necessary corporate or organizational action of such party; and (d) when executed and delivered by both parties, this Agreement will constitute the legal, valid, and binding obligation of such party, enforceable against such party in accordance with its terms.

3.2. DISCLAIMER OF WARRANTIES. ALL QORVO MATERIALS, AND ANY OTHER INFORMATION OR MATERIALS PROVIDED BY QORVO ARE PROVIDED "AS IS" AND QORVO HEREBY DISCLAIMS ALL WARRANTIES, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHER, AND QORVO SPECIFICALLY DISCLAIMS ALL IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT, AND ALL WARRANTIES ARISING FROM COURSE OF DEALING, USAGE, OR TRADE PRACTICE. WITHOUT LIMITING THE FOREGOING, QORVO MAKES NO WARRANTY OF ANY KIND THAT THE SOFTWARE OR OTHER QORVO MATERIALS, OR ANY PRODUCTS OR RESULTS OF THE USE THEREOF, WILL MEET LICENSEE'S OR ANY OTHER PERSONS' REQUIREMENTS, OPERATE WITHOUT INTERRUPTION, ACHIEVE ANY INTENDED RESULT, BE COMPATIBLE OR WORK WITH ANY OTHER SOFTWARE, HARDWARE, OR OTHER SYSTEMS, OR BE SECURE, ACCURATE, COMPLETE, FREE OF HARMFUL CODE, OR ERROR FREE. ALL THIRD-PARTY MATERIALS ARE PROVIDED "AS IS" AND ANY REPRESENTATION OR WARRANTY OF OR CONCERNING ANY THIRD-PARTY MATERIALS IS STRICTLY BETWEEN LICENSEE AND THE THIRD-PARTY OWNER OR DISTRIBUTOR OF THE THIRD-PARTY MATERIALS.

4. LIMITATONS OF LIABILITY

NOTWITHSTANDING ANYTHING ELSE IN THIS AGREEMENT OR OTHERWISE, AND TO THE EXTENT PERMITTED BY APPLICABLE LAW, LICENSOR WILL IN NO EVENT BE LIABLE WITH RESPECT TO ANY SUBJECT MATTER OF THIS AGREEMENT UNDER ANY CONTRACT, TORT, OR OTHER LEGAL OR EQUITABLE THEORY FOR: (I) ANY DIRECT, INDIRECT, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, HOWEVER CAUSED AND WHETHER OR NOT ADVISED IN ADVANCE OF THE POSSIBILITY OF SUCH DAMAGES; (II) DAMAGES FOR LOST PROFITS OR LOST DATA; OR (III) COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR SERVICES.


5. INDEMNIFICATION

You agree to fully defend and indemnify Licensor and its employees, subcontractors, licensors, and agents from any and all claims, liabilities, and costs (including reasonable attorney's fees) related to: (i) Your use (including Your sublicensee's use, if permitted) of the Licensed Software; or you're your violation of the terms and conditions of this Agreement.

6. CONFIDENTIALITY

6.1. Protection of Confidential Information.  Licensee will protect Licensor's Confidential Information from unauthorized dissemination and use the same degree of care that Licensee uses to protect its own like information, but in no event less than a reasonable degree of care. Licensee will not disclose to third parties Licensor's Confidential Information without the prior written consent of Licensor. Licensee will not use Licensor's Confidential Information for purposes other than those necessary to use the Licensed Software. Notwithstanding the foregoing, Licensee may use or disclose Confidential Information to the extent Licensee is legally required to disclose such Confidential Information provided, however, that prior to any such required disclosure, the Licensee will notify Licensor and will cooperate fully with Licensor in protecting against any such disclosure and/or obtaining a protective order narrowing the scope of such disclosure and/or use of the Confidential Information. Licensee agrees that any breach of this Section would cause irreparable harm to Licensor for which monetary damages would not be adequate and therefore, in the event of a breach of this Section, Licensor shall be entitled to equitable relief in addition to any remedies it may have hereunder or at law.

6.2. Security. Licensee shall implement reasonable security measures to prevent unauthorized use or disclosure of Licensed Software.

6.3. Notification of Employees. Licensee will take appropriate action by instruction, agreement, or otherwise with its employees, agents, and contractors allowed access to the Confidential Information to satisfy its obligations under this Section 6.


7. TRADEMARKS, COPYRIGHTS, AND NOTICES

7.1. Trademarks.  Licensee is not granted any ownership in or license to the trademarks, marks, service marks or trade names, or good will associated with such marks or names (collectively, "Marks") of the Licensor. Licensee shall not use the Marks or confusingly similar marks in connection with any goods or services other than the Licensed Software or in a manner that dilutes, disparages, or harms the reputation of the Licensor.  Licensee agrees that any goodwill arising from its use of the Marks shall inure to the benefit of the Licensor who will be the sole and exclusive owner of such goodwill.

7.2. Use of Marks.  All advertising and other materials in which Licensor's Marks are used shall be subject to the prior written approval of Licensor.  Whenever a Licensee uses the Mark of the Licensor, Licensor shall indicate that such Mark is the property of the Licensor.

7.3. Defense of Trademarks. Licensee will not at any time contest, or assist others in contesting, the validity or enforceability of the Marks of Licensor or do, cause to be done, or tolerate any act or thing contesting or in any way impairing or tending to impair any said right, title, an interest of Licensor in such Marks.

7.4. Copyright Notice. Licensee shall include Licensor's copyright notice as required herein. The following copyright notice is required in Licensee Software: Copyright (c) 2023, Qorvo Inc.

7.5. Third-Party Notices. This license does not apply to any open source software contained in Licensed Software. Rather, the terms and conditions in the applicable open source software license shall apply to the open source software. Nothing in this Agreement limits your rights under, or grants you rights that supersede, any open source software license. You acknowledge that the open source software license is solely between you and the applicable licensor of the open source software. You shall comply with the terms of all applicable open source software licenses, if any. License and copyright information for the open source software are disclosed in the Licensed Software documentation. Licensed Software may include open source software licensed under the General Public License and/or the Lesser General Public License (or any other license requiring us to make a written offer to provide corresponding source code to you). You may obtain the corresponding source code for any such open source software from us for a period of three years after our last shipment of Licensed Software and without charge except for the cost of media, shipping, and handling, upon written request to Licensor. This offer is valid to anyone in receipt of Licensed Software. You may send your request in writing to the address below. Please make sure your request includes the version and name associated with the Licensed Software.

Qorvo US, Inc.
Customer Support - Power Management
7628 Thorndike Rd.
Greensboro, NC 27409

8. GOVERNING LAW; JURISDICTION; INJUNCTIVE RELIEF; ASSIGNMENT.

8.1. Governing Law and Jurisdiction. This Agreement is governed by and construed in accordance with the internal Laws of the State of Delaware without giving effect to any choice or conflict of law provision or rule that would require or permit the application of the laws of any jurisdiction other than those of the State of Delaware. Any legal Action arising out of or related to this Agreement or the licenses granted hereunder will be instituted exclusively in the federal courts of the United States or the courts of the State of Delaware in each case located in Wilmington and New Castle County, and each party irrevocably submits to the exclusive jurisdiction of such courts in any such Action. Service of process, summons, notice, or other document by mail to such party's address set forth herein will be effective service of process for any Action brought in any such court.

8.2. Injunctive Relief.  A breach of this Agreement adversely affecting Licensor's Intellectual Property Rights in the Licensed Software, Licensor's Products or Documentation may cause irreparable injury to Licensor for which monetary damages may not be an adequate remedy and Licensor. shall be entitled to equitable relief in addition to any remedies it may have hereunder or at law.

8.3. No Third-Party Beneficiaries. This Agreement is for the sole benefit of the parties hereto and their respective permitted successors and permitted assigns and nothing herein, express or implied, is intended to or shall confer upon any other Person any legal or equitable right, benefit, or remedy of any nature whatsoever, under or by reason of this Agreement.

8.4. Amendment and Modification; Waiver. No amendment to or modification of or rescission, termination, or discharge of this Agreement is effective unless it is in writing, identified as an amendment to or rescission, termination, or discharge of this Agreement and signed by an authorized Representative of each party. No waiver by any party of any of the provisions hereof is effective unless explicitly set forth in writing and signed by the party so waiving. Except as otherwise set forth in this Agreement, no failure to exercise, or delay in exercising, any rights, remedy, power, or privilege arising from this Agreement will operate or be construed as a waiver thereof; nor will any single or partial exercise of any right, remedy, power, or privilege hereunder preclude any other or further exercise thereof or the exercise of any other right, remedy, power, or privilege.

8.5. Entire Agreement. This Agreement constitutes the entire agreement between Licensee and Licensor regarding the subject matter of this Agreement, and supersedes all prior communications, negotiations, understandings, agreements or representations, either written or oral, if any. This Agreement may only be amended in a signed writing, duly executed by Licensee and Licensor.

8.6. Assignment. Licensee shall not assign or otherwise transfer any of its rights, or delegate or otherwise transfer any of its obligations or performance, under this Agreement, in each case whether voluntarily, involuntarily, by operation of law, or otherwise, without Qorvo's prior written consent. For purposes of the preceding sentence, and without limiting its generality, any merger, consolidation, or reorganization involving Licensee (regardless of whether Licensee is a surviving or disappearing entity) will be deemed to be a transfer of rights, obligations, or performance under this Agreement for which Qorvo's prior written consent is required. No delegation or other transfer will relieve Licensee of any of its obligations or performance under this Agreement. Any purported assignment, delegation, or transfer in violation of this Section 8.6 is void. This Agreement is binding upon and inures to the benefit of the parties hereto and their respective permitted successors and assigns.
'''


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    lfile = os.path.dirname(sys.executable) + "\\LICENSE"
else:
    lfile = os.path.dirname(__file__) + "\\LICENSE"


if not os.path.isfile(lfile):

  with open(lfile, "w") as f:
    f.write(license)

  print("First use notice:\nPlease read the license file at \"" + lfile + "\".\n")

  sys.exit(1)

########################################################

args = sys.argv

########################################################
rm = pyvisa.ResourceManager('@py')
# print(rm)

list = rm.list_resources()
#list = ('TCPIP0::192.168.0.101::inst0::INSTR', 'ASRL4::INSTR', 'ASRL5::INSTR', 'ASRL7::INSTR')

########################################################
use = f"""

Usage-1:
  {args[0]}        => no parameter to list equipment connected

Usage-2:
  {args[0]} <id/IP> <Ton1> <Toff1> <Ton2> <Toff2> <Ton3>
    <id/IP>:
             Integer "0" to "99" as an ID of your MSO-Scope, use "{args[0]}" without parameters for available IDs
         OR
             IP address in the format of 00.00.00.00 of your MSO-Scope
    <Ton1> : First pulse length, in us (micro-second)
    <Toff1>: Interval between the 1st and 2nd pulses, in us (micro-second)
    <Ton2> : Second pulse length, in us (micro-second)
    <Toff2>: [Optional] Interval between the 2nd and 3rd pulses, in us (micro-second)
    <Ton3> : [Optional] Second pulse length, in us (micro-second)

  Example-1: ""> {args[0]} 0 10 1 3""
      Selecting your MSO-Scope at <id> = 0,
      1st ON pulse (to charge coil current) is 10us,
      wait for 1us between 1st and 2nd ON pulses,
      2nd ON pulse is 3us

  Example-2: ""> {args[0]} 192.168.9.99 45.2 1 2 1 3.5""
      Selecting your MSO-Scope at IP address 192.168.9.99,
      1st ON pulse (to charge coil current) is 45.2us,
      wait for 1us between 1st and 2nd ON pulses,
      2nd ON pulse is 2us,
      wait for another 1us between 1st and 2nd ON pulses,
      3rd ON pulse is 3.5us,

"""

########################################################
if len(args) == 1:
  msg = f"""
Double pulse test on MSO-Scope {verNum} (main coding by {mainAuthor})
"""
  print(msg)


  print("Following equipment found...")

  idx = 0
  for a in list:
    print(str(idx) + ":    " + a)
    idx += 1

  print("\nRun \"<prompt> " + args[0] + " <id> <Ton1> <Toff1> <Ton2> <Toff2> <Ton3>\"")
  print("\nIf your MSO-Scope is not listed, specify your MSO-Scope's IP address directly in below format:")
  print("Run \"<prompt> " + args[0] + " 00.00.00.00 <Ton1> <Toff1> <Ton2> <Toff2> <Ton3>\"")
  rm.close()
  sys.exit(0)

########################################################
if not((len(args) == 5) or (len(args) == 7)):
  msg = f"""
Error:  wrong parameters
"""
  if len(args) == 6:
    msg = f"""
Error: <Ton3> parameter is missing
  """
  print(msg + use)
  rm.close()
  sys.exit(1)

########################################################
pIP = re.compile('\d+\.\d+\.\d+.\d')
if pIP.match(args[1]):
  IPAddr = args[1]
  args[1] = "100"

########################################################
#if not(args[1].isdigit() and args[2].isdigit() and args[3].isdigit() and args[4].isdigit()):

def notNumber():
  msg = ""

  if not(args[1].isdigit()):
    msg += "\nERROR: 1st parameter should be an integer \"0\" to \"99\" or an IP address in dotted-decimal 00.00.00.00\n"

  msg += "\nERROR: 2nd/3rd/4th/5th/6th parameter(s) should be a number: integer \"0\" to \"99\", or floating \"99.9\", NO unit: \"us\", \"(us)\"\n"

  print(msg + use)
  rm.close()
  sys.exit(1)

if not(args[1].isdigit()):
  notNumber()

try:
  ton1 = round(float(args[2]),1)
except ValueError:
  notNumber()
try:
  tof1 = round(float(args[3]),1)
except ValueError:
  notNumber()
try:
  ton2 = round(float(args[4]),1)
except ValueError:
  notNumber()

if len(args) == 7:
  try:
    tof2 = round(float(args[5]),1)
  except ValueError:
    notNumber()
  try:
    ton3 = round(float(args[6]),1)
  except ValueError:
    notNumber()


########################################################
id   = int(args[1])

if ((id < 0) or (id >= len(list))) and (id != 100):
  msg = """
Error:  Equipment <id> is our of range, please specify one ID of below.
Error:  Or specify your MSO-Scope IP address at the 1st parameter.
"""
  print(msg)

  idx = 0
  for a in list:
    print(str(idx) + ":    " + a)
    idx += 1

  print("\nRun \"> " + args[0] + " <id/IP> <Ton1> <Toff1> <Ton2> <Toff2> <Ton3>\"")
  rm.close()
  sys.exit(1)


########################################################
if id == 100:
  print("Target MSO-Scope: IP address at " + IPAddr)
else:
  print("Target MSO-Scope: " + list[id])
print("1st Pulse: " + str(ton1) + "(us)")
print("1st OFF  : " + str(tof1) + "(us)")
print("2nd Pulse: " + str(ton2) + "(us)")
if len(args) == 7:
  print("2nd OFF  : " + str(tof2) + "(us)")
  print("3rd Pulse: " + str(ton3) + "(us)")

CSV = b'TIME,ARB\n'

c = 0
CSV += str(c).encode() + b'e-7,0\r\n'
c += 1
for i in range(int(ton1*10)):
  CSV += str(c).encode() + b'e-7,5\r\n'
  c += 1
for i in range(int(tof1*10)):
  CSV += str(c).encode() + b'e-7,0\r\n'
  c += 1
for i in range(int(ton2*10)):
  CSV += str(c).encode() + b'e-7,5\r\n'
  c += 1
if len(args) == 7:
  for i in range(int(tof2*10)):
    CSV += str(c).encode() + b'e-7,0\r\n'
    c += 1
  for i in range(int(ton3*10)):
    CSV += str(c).encode() + b'e-7,5\r\n'
    c += 1
CSV += str(c).encode() + b'e-7,0\r\n'
c += 1

if debug:
  print(CSV)
  rm.close()
  sys.exit(1)

########################################################
if id == 100:
  MsoScopeHandle = rm.open_resource("TCPIP::" + IPAddr)
else:
  MsoScopeHandle = rm.open_resource(list[id])

MsoScopeHandle.write('FileSystem:MKDir "c:/QorvoDPT"')
MsoScopeHandle.query("*OPC?")

print(MsoScopeHandle.query('*IDN?'))
#    print(MSO6.query('FILESystem:CWD?'))
#    print(MSO6.query('FileSystem:Dir?'))

msg = 'FileSystem:WriteFile "c:/QorvoDPT/pulse_data.csv", '

#    print(MSO6.query('FileSystem:Dir?'))
#print(MSO6.query('FileSystem:Dir?'))

MsoScopeHandle.write('AFG:Output:Mode OFF')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Output:State OFF')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('FileSystem:Delete "c:/QorvoDPT/pulse_data.csv"')
MsoScopeHandle.write_binary_values(msg, CSV, datatype='s')
MsoScopeHandle.query("*OPC?")

#    print(MSO6.query('FileSystem:Dir?'))

MsoScopeHandle.write('AFG:Output:Load:Impedance Fifty')
MsoScopeHandle.query("*OPC?")
#MSO6.write('AFG:Amplitude 3.3;:AFG:Offset 1.65')
#MsoScopeHandle.query("*OPC?")

MsoScopeHandle.write('AFG:OUTPut:LOAd:IMPEDance HIGHZ')
MsoScopeHandle.query("*OPC?")
#MsoScopeHandle.write('AFG:LowLevel 0;:AFG:HighLevel 5')
MsoScopeHandle.write('AFG:Amplitude 3.3;:AFG:Offset 1.65')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Function Arb')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Arbitrary:Source "C:/QorvoDPT/pulse_data.csv"')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Output:Mode burst')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Burst:CCount 1')
MsoScopeHandle.query("*OPC?")
MsoScopeHandle.write('AFG:Period ' + str(c) + 'e-7')
MsoScopeHandle.query("*OPC?")

MsoScopeHandle.write('CALLOUTS:CALLOUT1')
MsoScopeHandle.write('CALLOUTS:CALLOUT1:COLOR "#FFFFFF"')
MsoScopeHandle.write('CALLOUTS:CALLOUT1:BOOKMARK:SOURCE CH1')
MsoScopeHandle.write('CALLOUTS:CALLOUT1:DISPLAYPOSition:X 78')
MsoScopeHandle.write('CALLOUTS:CALLOUT1:DISPLAYPOSition:Y 88')
MsoScopeHandle.write('CALLOUTS:CALLOUT1:FONT:BOLD')

an = str(ton1) + "us-" + str(tof1) + "us-" + str(ton2) + "us"
if len(args) == 7:
    an = an + "-" + str(tof2) + "us-" + str(ton3) + "us"
MsoScopeHandle.write('CALLOUTS:CALLOUT1:TEXT "' + an + '"')

MsoScopeHandle.close()
rm.close()

print('\n>>>> Your MSO scope is ready to run, hit the "Burst" button in the AFG dialog.\n')


