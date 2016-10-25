This is a jumbo-7 patched version of John the Ripper 1.7.9 that I created for MacOS X (Intel CPUs ONLY) and not an official release.  It has been statically linked to OpenSSL 0.9.8x and includes support for OpenMP allowing the use of multiple cores in Intel CPUs.  The gcc 4.7.2 compiler was used to generate all binaries.  You should be familiar with John 1.7.9 to use this program.  It supports the following algorithms:

- Traditional DES
- BSDI DES
- FreeBSD MD5
- OpenBSD Blowfish
- Kerberos AFS DES
- LM DES
- Dynamic hashes (md4, md5, phpass, Cisco PIX, HTTP Digest Access Auth, sha1  - SEE DYNAMIC in doc directory)
- Eggdrop Blowfish
- DIGEST-MD5 C/R
- Lotus Notes/Domino 6 More Secure Internet Password
- EPiServer SID salted SHA-1
- HTTP Digest access authentication MD5
- Invision Power Board 2.x salted MD5
- Kerberos v4 TGT DES
- Kerberos v5 TGT 3DES
- MSCHAPv2 C/R MD4 DES
- LM C/R DES
- LMv2 C/R MD4 HMAC-MD5
- NTLMv1 C/R MD4 DES (ESS MD5)
- NTLMv2 C/R MD4 HMAC-MD5
- HalfLM C/R DES
- Netscreen MD5 
- NT MD4 [128/128 X2 SSE2-16]
- PHPS md5(md5($pass).$salt)
- Post.Office MD5
- Mac OS X 10.4 - 10.6 salted SHA-1
- CRC-32
- GOST R 34.11-94
- Mac OS X Keychain PBKDF2-HMAC-SHA-1 3DES
- Lotus Notes/Domino 5
- Generic salted MD4 
- MediaWiki md5($s.'-'.md5($p))
- M$ Cache Hash MD4
- M$ Cache Hash 2 (DCC2) PBKDF2-HMAC-SHA-1
- MS Kerberos 5 AS-REQ Pre-Auth MD4 MD5 RC4
- MS SQL SHA-1
- MS SQL 2005 SHA-1
- MySQL 4.1 double-SHA-1
- MySQL
- Netscape LDAP SHA-1
- NT MD4 [128/128 SSE2 intrinsics 12x]
- ODF SHA-1 Blowfish
- Office 2007/2010 SHA-1/AES
- Oracle 11g SHA-1
- Oracle 10 DES 
- osCommerce md5($salt.$pass)
- phpass MD5 ($P$9)
- PIX MD5
- PKZIP
- RACF DES
- Raw MD4
- Raw MD5
- Raw SHA-1
- Raw SHA-1 LinkedIn
- md5(unicode($p))
- Salted SHA-1
- SAP CODVN B (BCODE)
- SAP CODVN F/G (PASSCODE)
- Generic salted SHA-1 
- SIP MD5
- VNC DES
- WoltLab BB3 salted SHA-1
- HMAC MD5
- HMAC SHA-1
- Raw SHA-0 
- Raw SHA-224
- Raw SHA-256
- Raw SHA-384
- Raw SHA-512
- HMAC SHA-224 
- HMAC SHA-256 
- HMAC SHA-384
- HMAC SHA-512
- Mac OS X 10.7+ salted SHA-512
- hMailServer salted SHA-256 
- Sybase ASE salted SHA-256
- DragonFly BSD $3$ SHA-256 w/ bug, 64-bit
- DragonFly BSD $4$ SHA-512 w/ bugs, 64-bit
- DragonFly BSD $3$ SHA-256 w/ bug, 32-bit
- DragonFly BSD $4$ SHA-512 w/ bugs, 32-bit
- Drupal 7 $S$ SHA-512 (x16385)
- sha256crypt (rounds=5000)
- sha512crypt (rounds=5000)
- EPiServer salted SHA-1/SHA-256
- KeePass SHA-256 AES
- Password Safe SHA-256
- Raw SHA-1 (pwlen <= 15)
- Mozilla SHA-1 3DES
- Tripcode DES
- SSH RSA/DSA (one 2048-bit RSA and one 1024-bit DSA key) 
- PDF MD5 RC4 
- WPA-PSK PBKDF2-HMAC-SHA-1
- RAR3 SHA-1 AES (4 characters)
- WinZip PBKDF2-HMAC-SHA-1
- dummy


Refer to http://www.openwall.com/john for more details.

The included binaries are:

john - for use on Intel MacOS X computers. (Intel 32-bit and 64-bit).  To run the Intel 32-bit version on a 64-bit MacOS X computer to take advantage of SSE2 optimized algorithms, run the following command:  

arch -i386 ./john 

For example, arch -i386 ./john -test -format:mssql

On Intel Macs, it is recommended you run "./john" because the 64-bit software is faster for most common hashes.  You should only run "arch -i386 ./john" if cracking a particular hash will benefit from SSE2 acceleration (i.e. MSSQL or MSSQL05)

-- 
Erik Winkler <ewinkler@erols.com>
