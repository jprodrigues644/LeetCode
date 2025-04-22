"""  On vous donne une chaîne de caractères s représentant un relevé de présence pour un étudiant, où chaque caractère indique si l'étudiant était absent, en retard ou présent ce jour-là. Le relevé ne contient que les trois caractères suivants :

'A' : Absent

'L' : En retard

'P' : Présent

L'étudiant est éligible à une récompense de présence s’il remplit les deux critères suivants :

L'étudiant a été absent ('A') strictement moins de 2 jours au total.

L'étudiant n’a jamais été en retard ('L') pendant 3 jours consécutifs ou plus.

Retourner true si l’étudiant est éligible à la récompense de présence, sinon retourner false """

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count("A") >= 2 : 
            return False 
        if 'LLL' in s :
            return False 
        return True  
sol = Solution()
print(sol.checkRecord('LLAPP'))

    

    
     
        
        
        