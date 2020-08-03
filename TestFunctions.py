from User import Member
from User import Librarian

lib = Librarian('Gopal', 'Indore', 24, '994400555515', 'GOP975')
print(lib)
lib.addBook('Thermodynamics','P.K. Nag', 'June 1989', '1279')
lib.addBookItem('Thermodynamics', 'BTXPB5929C', 'T101')
lib.addBookItem('Thermodynamics', 'BTXPB5929C', 'T102')
lib.addBook('Machine Design', 'R.S. Khurmi', 'Februaru 1990', '2087')
lib.addBookItem('Machine Design', 'CDFTC6432B', 'M201')
lib.addBookItem('Machine Design', 'CDFTC6432B', 'M201') 
lib.addBook('Theory of Machines', 'Dr. A.G. Ambekar', 'September 1985', '2745')
lib.addBookItem('Theory of Machines', 'SMNQS6664A', 'TM301')
lib.addBookItem('Theory of Machines', 'SMNQS6664A', 'TM302')
lib.viewBooks()
lib.removeBookItem('SMNQS6664A')
lib.viewBooks()
lib.removeBook('Theory of Machines')
lib.viewBooks()

member1 = Member('Aditya', 'Indore', 24, '9424534453', 'ADI942')
member2 = Member('Harish', 'Indore', 25, '9791457862', 'HAR979')
print(member2)
member1.viewBooks()
member1.reserveBook('Thermodynamics')
member2.reserveBook('Machine Design')
member1.viewBooks()

lib.viewissuedBookItems()
lib.viewIssuerInfo()

member1.returnBook()
member2.returnBook()
member1.viewBooks()

member2.issuedBook('Thermodynamics')

lib.addMember('Mayur', 'Indore', '23', '9179030140', 'MAY917')
lib.viewMembers()
lib.searchMember('Mayur')
lib.removeMember('Harish')
member1.reserveBook('Machine Design')
