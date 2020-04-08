"""
Given an array of strings, group anagrams together.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
"""
from collections import defaultdict

# This solution fails on the last unit test -- takes too long
class Solution2:
    def compare_words(self, ref_word, cmp_word):
        current_word_converted = tuple(sorted(ref_word))
        compare_word_converted = tuple(sorted(cmp_word))
        if current_word_converted == compare_word_converted:
            return True
        else:
            return False

    def get_word(self, iterable):
        iterator = iter(iterable)
        try:
            # current = next(iterator)
            for next_item in iterator:
                current = next_item
                yield current
                # current = next_item
        except StopIteration as e:
            return e

    def groupAnagrams(self, strs: list) -> list:
        output_list = []
        skip_list = []

        word_tuples = [(x, idx,  y, comp_idx) for idx, x in enumerate(self.get_word(strs)) for comp_idx, y in enumerate(self.get_word(strs))]
        anagram_tuples = [tup for tup in self.get_word(word_tuples) if self.compare_words(tup[0], tup[2])]
        print(anagram_tuples)

        anagram_dict = {}

        seen_tuples = []
        for tup in self.get_word(anagram_tuples):
            if tup[1] not in anagram_dict:
                if (tup[0], tup[1]) not in seen_tuples:
                    anagram_dict[tup[1]] = [(tup[2], tup[3])]
                    seen_tuples.append((tup[2], tup[3]))
            else:
                # check for the second part of the pair in the dict
                if (tup[2], tup[3]) not in anagram_dict[tup[1]]:
                    anagram_dict[tup[1]].append((tup[2], tup[3]))
                    seen_tuples.append((tup[2], tup[3]))

        for key, val in anagram_dict.items():
            output_list.append([tup[0] for tup in val])

        return output_list


# Working solution from discussion
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


if __name__ == '__main__':
    sln = Solution()
    # print(sln.groupAnagrams(["", "", ""]))
    print(sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
