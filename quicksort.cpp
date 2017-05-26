#include <iostream>

using namespace std;

void quickSort(int*, int, int);
void printArray(int*, int);

int main() {
    int arr[10] = {5,9,8,3,7,4,1,6,2,0};
    printArray(arr, 10);
    quickSort(arr, 0, 10);
    printArray(arr, 10);
    return 0;
}

void quickSort(int* arr, int left, int right) {
    int size = right - left;
//    char c;
    if (size <= 1) return;
//    cout << "Left: " << left << endl;
//    cout << "Right: " << right << endl;
    int pivot = left;
    int low = left;
    int high = right - 1;
    swap(arr[pivot], arr[high]);
    pivot = high;
    --high;

    while (low < high) {
        if (arr[low] > arr[pivot]) {
            while (low < high && arr[high] > arr[pivot]) --high;
            swap(arr[low], arr[high]);
        }
        ++low;
    }
//    printArray(arr, 10);
    if (arr[high] > arr[pivot])
        swap(arr[pivot], arr[high]);
//    printArray(arr, 10);
//    cin >> c;
    quickSort(arr, left, high);
    quickSort(arr, high + 1, right);
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << ' ';
    }
    cout << endl;
}
    
