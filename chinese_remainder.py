from Gcd import GCD


class ChineseRemainder:
    """
    A class that solves systems of linear congruence
    """

    def chinese_remainder(self, N):
        """
        Implements the chinese remainder theorem to solve
        systesm of linear congruence
        """

        # create empty lists to store essential variables
        r_list = []
        m_list = []
        M_list = []
        s_list = []
        x_list = []

        # get r & m values from user for each linear congruence in the series
        # add each r & m value to the appropriate list
        for _ in range(0, N):
            r_i = int(input(f"Enter the r{_ + 1} value: "))
            m_i = int(input(f"Enter the m{_ + 1} value: "))

            r_list.append(r_i)
            m_list.append(m_i)

        # check if all m_i are co-prime using nested loops
        for i in range(0, N):
            for val in range(i + 1, N):
                number_theory_variables = GCD(m_list[i], m_list[val])
                gcd = number_theory_variables.gcd()
                # if all m_i are not coprime end the algorithm & print message
                if gcd != 1:
                    print("""
                There is no unique solution to this system of linear congruence.
                The m values are not all co-prime.\n""")
                    return

        # calculate M
        M = 1
        for num in m_list:
            M *= num

        # calculate  M_i for each linear congruence
        # and add to M_list
        for j in range(0, N):
            M_i = M/m_list[j]
            M_list.append(M_i)

        # calculate s_i for each linear congruence (multiplicative inverse of s[i])
        # add to s list
        for k in range(0, N):
            number_theory_variables2 = GCD(M_list[k], m_list[k])
            number_theory_variables2.gcd()
            bez_coef = number_theory_variables2.bezout()
            s_i = bez_coef[0]
            # if s_i is out of range m_i, convert to be in range
            if s_i < 0 or s_i > m_list[k]:
                s_i = s_i % m_list[k]
            s_list.append(s_i)

        # calculate x_0 using formula x_0 = sum(r_i x s_i x M_i)
        for l in range(0, N):
            x_i = r_list[l] * s_list[l] * M_list[l]
            x_list.append(x_i)
        x_0 = sum(x_list)

        # find the solution to the system by calculating x_0 mod M
        solution = x_0 % M
        print(f"The solution to your system of linear congruences is: x = {solution}")
