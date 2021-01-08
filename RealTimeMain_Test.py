import RealTimeMain
import unittest

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    #register
    def test_a(self):
        self.assertEqual(RealTimeMain.registerToDb_help('R@gmail.com', 'roni', '123'), True)
        self.assertEqual(RealTimeMain.registerToDb_help('J@gmail.com', 'roni', '123'), True)
        self.assertEqual(RealTimeMain.registerToDb_help('V@gmail.com', 'roni', '123'), True)
        self.assertFalse(RealTimeMain.registerToDb_help('R@gmail.com', 'roni', '123'), False)
        self.assertFalse(RealTimeMain.registerToDb_help('J@gmail.com', 'roni', '123'), False)
        self.assertFalse(RealTimeMain.registerToDb_help('V@gmail.com', 'roni', '123'), False)

    #login
    def test_b(self):
        self.assertEqual(RealTimeMain.loginUserhelp('R@gmail.com','123'), True)
        self.assertEqual(RealTimeMain.loginUserhelp('J@gmail.com','123'), True)
        self.assertEqual(RealTimeMain.loginUserhelp('V@gmail.com','123'), True)
        self.assertEqual(RealTimeMain.loginUserhelp('H@gmail.com','123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('U@gmail.com','123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('Y@gmail.com','123'), False)

    #change password
    def test_c(self):
        self.assertEqual(RealTimeMain.changePassword_help('123','1234'), True)
        self.assertEqual(RealTimeMain.changePassword_help('1234','123432'), True)
        self.assertEqual(RealTimeMain.changePassword_help('123432','12342'), True)
        self.assertEqual(RealTimeMain.changePassword_help('12342','123423'), True)
        self.assertEqual(RealTimeMain.changePassword_help('123423','123'), True)
        self.assertEqual(RealTimeMain.changePassword_help('654','123'), False)
        self.assertEqual(RealTimeMain.changePassword_help('128723','123'), False)
        self.assertEqual(RealTimeMain.changePassword_help('333','123'), False)
        self.assertEqual(RealTimeMain.changePassword_help('23222','123'), False)
    #reg bussiness
    def test_d(self):
        self.assertEqual(RealTimeMain.regBuis_help('Google','0','https://www.google.co.il/?hl=iw' ,'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', '10:00 - 23:00', 'Google site is the best', 'R@gmail.com' ), True)
        self.assertEqual(RealTimeMain.regBuis_help('Fox','0','https://www.terminalx.com/brands/fox-main/fox' ,'https://media.terminalx.com/pub/media/catalog/category/fox-logo.jpg', '10:00 - 23:00', 'Fox site is the best', 'J@gmail.com' ), True)
        self.assertEqual(RealTimeMain.regBuis_help('sony','0','https://www.sony.com/' ,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAeFBMVEUAAAD///93d3fV1dXw8PDo6OhCQkL6+vqkpKQpKSl6enqioqKpqaloaGiXl5exsbFSUlLFxcWEhIS+vr7d3d01NTVfX1/Y2NgJCQnl5eXv7++JiYnMzMyRkZGzs7M9PT06OjpKSkofHx8nJydvb29ZWVkZGRllZWVQDcK8AAAEN0lEQVR4nO3Y6ZKiSBiFYRAtUBFF3EWsve7/Dkckv9xIKyai6JqJ6Pf50dGVJstJcoMoAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgr/BSLOvJTb0sVt/Vu16W9fFW71jm5+1v3dzPfZWxo15H0bYuaz/CrkqdemlztX59no3E7MUUb03xzYdTr9PVe7KL3wfN9z6J+5br2z9PTr1LqF5isqzt8pE5vVO/jKKzf45Dd3qnbMiAlZx0vK+rcj+2LmMnXOl8aVJVpUnbSI2Zc4sXKV74CZ2WeJAwHT5gZfrFbn7qJ9TXb+ShXaTW8aDaIM+WJ3OTuar3kmfzbhSM8yxf3+tlR11tMs/UZfNctXSTZfPhAu66s3qzy27jJZyr+9lMrVqZKjxZZVYXqKzipi34sArOoVr3Ub75eShH17r9JsudhCN1O7VbSYr3piixulpiiu8t9GwfqztFoYuOfnMNYuL0KEttJ1RT6NGvJE/irEvshFb9opdQ94BYxkfX2NNoYGrGyF78H7ZWQjVAvLm11fVma2JwEsbjT1UcSBjpJao7bZe4dx8/tpfLpOOkyYuRCXEp5tKeabCPtr7U0TMpaBOennXEVC2p94T+VmIj7dD+0c2wi0HDmUs70k2VLV7tOiv1yyhwvAqv54t7wmhrdgYrc5ne7evZWK5x8WsMwd2laMfCDAhphUPgcNXV9PyQdM/k06yXo8cJD3Lx6vP+v+WfCCjLRYC+3lI93NDhjfdbIr1Od//7gwknjK6647T/lMOnu3sKbcak8wRT2OT5yt86oZlI4kyNssAgs9t33/95KOtNHKYademlsD18huawdmM3epDQ2uoNvhA6XndF5exIFWuauHkNHKme1ET+thJaO8168SihPnk6+EKofGbz7E3+f/1aZ01t9dpuipS5dB04PpWnpNgJ9Z5HjbPwUqC2qOfgjwOYxtZipgvPKqUaiSpG4tcz6+GXFDgJow+nR4QTbh433yDahIGVXLWsulfZ0/Tf/jf+GHITRld7MQo/pt9IGDp7F0r2+ak32oQMInMCL2H0dvpfJLT296K+l8uOXN7TvQk98MrhJzR7s/82YXz0Poyo90G9i5GHNbE337Ic2PN827u9hTP5PqEa8gO+87qmcvm0vMi+/iNTC4e1EdUzf6kmlWkhQ0ze8V9v7+7dF4NknuXWsfKdpJfw9vqf1XL9ZZYFXuIGTNhdZpJMzNzgPNeVGVCbqqrN4qk3d1vnVI11bPEgofuRKg7vfIdIWD2Vgf1341/uEtgSxLX5nvg4oXo16r05/ErCtzhN2yGwqOztaVqvQxd7r90bmsztjcjB+Qjqriyr9iNq7wV6G/5y+ufsirxpmnw+++Zj9qpo7t/G91U+C+3iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAv/IPQ9orBoNUYRIAAAAASUVORK5CYII=', '10:00 - 23:00', 'sony site is the best', 'V@gmail.com' ), True)
        self.assertEqual(RealTimeMain.regBuis_help('LG','0','https://www.google.co.il/?hl=iw' ,'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', '10:00 - 23:00', 'LG site is the best', 'R@gmail.com' ), True)
        self.assertEqual(RealTimeMain.regBuis_help('Google','0','https://www.google.co.il/?hl=iw' ,'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', '10:00 - 23:00', 'Google site is the best', 'R@gmail.com' ), False)
        self.assertEqual(RealTimeMain.regBuis_help('Fox', '0', 'https://www.terminalx.com/brands/fox-main/fox',
                                                   'https://media.terminalx.com/pub/media/catalog/category/fox-logo.jpg',
                                                   '10:00 - 23:00', 'Fox site is the best', 'J@gmail.com'), False)
        self.assertEqual(RealTimeMain.regBuis_help('sony', '0', 'https://www.sony.com/',
                                                   'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAeFBMVEUAAAD///93d3fV1dXw8PDo6OhCQkL6+vqkpKQpKSl6enqioqKpqaloaGiXl5exsbFSUlLFxcWEhIS+vr7d3d01NTVfX1/Y2NgJCQnl5eXv7++JiYnMzMyRkZGzs7M9PT06OjpKSkofHx8nJydvb29ZWVkZGRllZWVQDcK8AAAEN0lEQVR4nO3Y6ZKiSBiFYRAtUBFF3EWsve7/Dkckv9xIKyai6JqJ6Pf50dGVJstJcoMoAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgr/BSLOvJTb0sVt/Vu16W9fFW71jm5+1v3dzPfZWxo15H0bYuaz/CrkqdemlztX59no3E7MUUb03xzYdTr9PVe7KL3wfN9z6J+5br2z9PTr1LqF5isqzt8pE5vVO/jKKzf45Dd3qnbMiAlZx0vK+rcj+2LmMnXOl8aVJVpUnbSI2Zc4sXKV74CZ2WeJAwHT5gZfrFbn7qJ9TXb+ShXaTW8aDaIM+WJ3OTuar3kmfzbhSM8yxf3+tlR11tMs/UZfNctXSTZfPhAu66s3qzy27jJZyr+9lMrVqZKjxZZVYXqKzipi34sArOoVr3Ub75eShH17r9JsudhCN1O7VbSYr3piixulpiiu8t9GwfqztFoYuOfnMNYuL0KEttJ1RT6NGvJE/irEvshFb9opdQ94BYxkfX2NNoYGrGyF78H7ZWQjVAvLm11fVma2JwEsbjT1UcSBjpJao7bZe4dx8/tpfLpOOkyYuRCXEp5tKeabCPtr7U0TMpaBOennXEVC2p94T+VmIj7dD+0c2wi0HDmUs70k2VLV7tOiv1yyhwvAqv54t7wmhrdgYrc5ne7evZWK5x8WsMwd2laMfCDAhphUPgcNXV9PyQdM/k06yXo8cJD3Lx6vP+v+WfCCjLRYC+3lI93NDhjfdbIr1Od//7gwknjK6647T/lMOnu3sKbcak8wRT2OT5yt86oZlI4kyNssAgs9t33/95KOtNHKYademlsD18huawdmM3epDQ2uoNvhA6XndF5exIFWuauHkNHKme1ET+thJaO8168SihPnk6+EKofGbz7E3+f/1aZ01t9dpuipS5dB04PpWnpNgJ9Z5HjbPwUqC2qOfgjwOYxtZipgvPKqUaiSpG4tcz6+GXFDgJow+nR4QTbh433yDahIGVXLWsulfZ0/Tf/jf+GHITRld7MQo/pt9IGDp7F0r2+ak32oQMInMCL2H0dvpfJLT296K+l8uOXN7TvQk98MrhJzR7s/82YXz0Poyo90G9i5GHNbE337Ic2PN827u9hTP5PqEa8gO+87qmcvm0vMi+/iNTC4e1EdUzf6kmlWkhQ0ze8V9v7+7dF4NknuXWsfKdpJfw9vqf1XL9ZZYFXuIGTNhdZpJMzNzgPNeVGVCbqqrN4qk3d1vnVI11bPEgofuRKg7vfIdIWD2Vgf1341/uEtgSxLX5nvg4oXo16r05/ErCtzhN2yGwqOztaVqvQxd7r90bmsztjcjB+Qjqriyr9iNq7wV6G/5y+ufsirxpmnw+++Zj9qpo7t/G91U+C+3iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAv/IPQ9orBoNUYRIAAAAASUVORK5CYII=',
                                                   '10:00 - 23:00', 'sony site is the best', 'V@gmail.com'), False)
        self.assertEqual(RealTimeMain.regBuis_help('LG', '0', 'https://www.google.co.il/?hl=iw',
                                                   'https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                                                   '10:00 - 23:00', 'LG site is the best', 'R@gmail.com'), False)
    #add user
    def test_e(self):
        self.assertEqual(RealTimeMain.addUser_help('H@gmail.com', 'roni', '123'), True)
        self.assertEqual(RealTimeMain.addUser_help('K@gmail.com', 'roni', '123'), True)
        self.assertEqual(RealTimeMain.addUser_help('G@gmail.com', 'roni', '123'), True)
        self.assertEqual(RealTimeMain.addUser_help('K@gmail.com', 'roni', '123'), False)
        self.assertEqual(RealTimeMain.addUser_help('H@gmail.com', 'roni', '123'), False)
        self.assertEqual(RealTimeMain.addUser_help('G@gmail.com', 'roni', '123'), False)
    #add review
    def test_f(self):
        pass
        self.assertEqual(RealTimeMain.review_help('Dog', 'Best site ever'), True)
        self.assertEqual(RealTimeMain.review_help('user44', 'Best site ever'), True)
        self.assertEqual(RealTimeMain.review_help('Max', 'Best site ever'), True)
        self.assertEqual(RealTimeMain.review_help('Yosi', 'Best site ever'), True)
        self.assertEqual(RealTimeMain.review_help('Josh', 'Best site ever'), True)
    #delete Review
    def test_g(self):
        self.assertEqual(RealTimeMain.deleteReview_help('Dog'), True)
        self.assertEqual(RealTimeMain.deleteReview_help('user44'), True)
        self.assertEqual(RealTimeMain.deleteReview_help('Max'), True)
        self.assertEqual(RealTimeMain.deleteReview_help('Yosi'), True)
        self.assertEqual(RealTimeMain.deleteReview_help('Josh'), True)

    # delete user
    def test_h(self):
        self.assertEqual(RealTimeMain.deleteUser_help('R@gmail.com', 'YES'),True)
        self.assertEqual(RealTimeMain.deleteUser_help('J@gmail.com', 'YES'),True)
        self.assertEqual(RealTimeMain.deleteUser_help('V@gmail.com', 'YES'),True)
        self.assertEqual(RealTimeMain.deleteUser_help('G@gmail.com', 'YES'),True)
        self.assertEqual(RealTimeMain.deleteUser_help('H@gmail.com', 'YES'),True)
        self.assertEqual(RealTimeMain.deleteUser_help('K@gmail.com', 'YES'),True)

    def test_i(self):
        self.assertEqual(RealTimeMain.loginUserhelp('R@gmail.com', '123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('J@gmail.com', '123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('V@gmail.com', '123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('H@gmail.com', '123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('U@gmail.com', '123'), False)
        self.assertEqual(RealTimeMain.loginUserhelp('Y@gmail.com', '123'), False)


if __name__ == '__main__':
    unittest.main()