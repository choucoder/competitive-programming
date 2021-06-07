#include <bits/stdc++.h>
#define PB push_back

using namespace std;

typedef vector<int> vi;

void mergeSort(int arr[], int l, int r);
void merge(int arr[], int l, int m, int r);
void printArray(int arr[], int l, int r);


int main(int argc, char *argv[]) {
    int arr[] = {5, 4, 1, 8, 7, 2, 6, 3};
    int n = sizeof(arr) / sizeof(int);

    cout << "Numero de elementos: " << n << "\n";
    mergeSort(arr, 0, n);
    printArray(arr, 0, n);
    return 0;
}

void mergeSort(int arr[], int l, int r) {
    if ((r - l) > 1) {
        int m = ((r - l) / 2) + l;
        mergeSort(arr, l, m);
        mergeSort(arr, m, r);
        merge(arr, l, m, r);
    }
}

void merge(int arr[], int l, int m, int r) {
    int i = l;
    int j = m;
    int k = l;
    vi c;

    while(i <  m && j < r) {
        if (arr[i] < arr[j]) {
            c.PB(arr[i]);
            i += 1;
        }
        else {
            c.PB((arr[j]));
            j += 1;
        }
    }

    while(i < m) {
        c.PB(arr[i]);
        i += 1;
    }

    while (j < r) {
        c.PB(arr[j]);
        j += 1;
    }
    for (int i=l, j=0; i < r; i++, j++) {
        arr[i] = c.at(j);
    }
    cout << "Subarray ordenado: ";
    printArray(arr, l, r);
}

void printArray(int arr[], int l, int r) {
    for (int i=l; i < r; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}