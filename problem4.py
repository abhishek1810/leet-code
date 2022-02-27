# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        median_position = (len(nums1) + len(nums2)) // 2

        i = 0
        j = 0
        joined_array = []
        while i < len(nums1) or j < len(nums2):

            if i == len(nums1) and j != len(nums2):
                joined_array.extend(nums2[j:])
                j+=(len(nums2)-j)
            elif i != len(nums1) and j == len(nums2):
                joined_array.extend(nums1[i:])
                i += (len(nums1) - i)
            else:
                if nums1[i] < nums2[j]:
                    joined_array.append(nums1[i])
                    i+=1
                elif nums1[i] > nums2[j]:
                    joined_array.append(nums2[j])
                    j+=1
                else:
                    joined_array.append(nums1[i])
                    i+=1
                    joined_array.append(nums2[j])
                    j+=1

            if i + j  >= median_position :
                if (len(nums1) + len(nums2)) % 2 == 0 :
                    return (joined_array[median_position] + joined_array[median_position-1]) / 2
                else:
                    return joined_array[median_position]


print( Solution().findMedianSortedArrays([1,2],[]) )