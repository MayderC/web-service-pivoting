# web-service-pivoting

- install dependencies

```sh
  pip install -r requirements.txt
```

- run proyect

```sh
  uvicorn --app-dir src main:app --reload
```

API DEPLOY

- https://web-production-0127.up.railway.app/docs
- https://metodos.onrender.com/docs

TODO:

- implement the diferents tecniques of pivoting

### Json response

```js

{
  "solution": {
    "x": -18,
    "y": 23,
    "z": -32
  },
  "steps": {
    "first_operation": [
      {
        "zero_operations": [
          {
            "matrices": [
              [
                [3,1,-1,1],
                [2,3,1,1],
                [0,-2,-1,-14]
              ],
              [
                [3,1,-1,1],
                [0,2.3333333333333335,1.6666666666666665,0.33333333333333337],
                [0,-2,-1,-14]
              ]
            ],
            "elemental_operation": [
              "2.0/3.0"
            ],
            "row": 1,
            "operations": {
              "operation": [
                "2.0 - 2.0/3.0 * 3.0 = 0.0",
                "3.0 - 2.0/3.0 * 1.0 = 2.3333333333333335",
                "1.0 - 2.0/3.0 * -1.0 = 1.6666666666666665",
                "1.0 - 2.0/3.0 * 1.0 = 0.33333333333333337"
              ]
            },
            "is_zero": false,
            "helping_msg_dev": "The index of each element in the array named 'operation', represents an index of the column of the currently matrix"
          },
          {
            "matrices": [
              [
                [3,1,-1,1],
                [0,2.3333333333333335,1.6666666666666665,0.33333333333333337],
                [0,-2,-1,-14]
              ]
            ],
            "elemental_operation": [
              "0.0/3.0"
            ],
            "row": 2,
            "operations": {
              "operation": []
            },
            "is_zero": true
          }
        ],
        "pivot_swap": {
          "description": "Se cambia la fila 1 por la fila 3",
          "sorted_pivot": false,
          "matrices": [
            [
              [0,-2,-1,-14],
              [2,3,1,1],
              [3,1, -1,1]
            ],
            [
              [3,1,-1,1],
              [2,3,1,1],
              [0,-2,-1,-14]
            ]
          ],
          "helping_msg_dev": "matrices[0] = before swaping row, matriz[1] = after swaping row",
          "step": 1
        }
      },
      {
        "zero_operations": [
          {
            "matrices": [
              [
                [3,1,-1,1],
                [0,2.3333333333333335,1.6666666666666665,0.33333333333333337],
                [0,-2, -1,-14]
              ],
              [
                [3,1,-1,1],
                [0,2.3333333333333335,1.6666666666666665,0.33333333333333337],
                [0,0,0.4285714285714284, -13.714285714285714]
              ]
            ],
            "elemental_operation": [
              "-2.0/2.3333333333333335"
            ],
            "row": 2,
            "operations": {
              "operation": [
                "-2.0 - -2.0/2.3333333333333335 * 2.3333333333333335 = 0.0",
                "-1.0 - -2.0/2.3333333333333335 * 1.6666666666666665 = 0.4285714285714284",
                "-14.0 - -2.0/2.3333333333333335 * 0.33333333333333337 = -13.714285714285714"
              ]
            },
            "is_zero": false,
            "helping_msg_dev": "The index of each element in the array named 'operation', represents an index of the column of the currently matrix"
          }
        ],
        "pivot_swap": {
          "description": "Pivote ordenado, la matriz queda igual",
          "sorted_pivot": true,
          "matrices": [
            [
              [3,1,-1,1],
              [0,2.3333333333333335,1.6666666666666665,0.33333333333333337],
              [0,-2,-1,-14 ]
            ]
          ],
          "helping_msg_dev": "matrices[0] is the same, because it was not changed",
          "step": 2
        }
      }
    ],
    "reversal": [
      {
        "equation": "0.4285714285714284 * z + 13.714285714285714 = 0",
        "result": -32,
        "unknown": "z"
      },
      {
        "equation": "2.3333333333333335 * y + 1.6666666666666665 * -32.0 + -0.33333333333333337 = 0",
        "result": 23,
        "unknown": "y"
      },
      {
        "equation": "3.0 * x + 1.0 * 23.0 + -1.0 * -32.0 + -1.0 = 0",
        "result": -18,
        "unknown": "x"
      }
    ]
  }
}

```

### data properties

- matrices en todos los casos representa la matriz antes y despues, si solo hay una es porque no hubo ningun cambio.

```ts
Response {
  solution: Solution;
  steps: Steps;
}

Solution {
  x: number;
  y: number;
  z: number;
}

Steps {
  first_operation: FirstOperation[]; //Array de FirstOperation
  reversal: Reversal[]; //Array de Reversal
}

FirstOperation {
  zero_operations: ZeroOperation[]; //Array de ZeroOperation
  pivot_swap: PivotSwap;
}

ZeroOperation {
  matrices: number[][][]; //Array de matrices
  elemental_operation: string[]; //Array de string
  row: number;
  operations: Operations;
  is_zero: boolean;
  helping_msg_dev?: string;
}

/*
  el indice de operations representa la columa de la fila(row) donde se aplica la formula,

  si is_zero es true, es porque ya hay un (cero) debajo de la diagonal entonces se omite realizar operaciones sobre esa columna

*/

Operations {
  operation: string[]; //Array de string
}

PivotSwap {
  description: string;
  sorted_pivot: boolean;
  matrices: number[][][]; //Array de matrices
  helping_msg_dev: string;
  step: number;
}

Reversal {
  equation: string;
  result: number;
  unknown: string;
}
```

Orden para mostrar resultado,

- 1 FirstOperation

  - 1.1 PivotSwap

    - 1.1.1 step
    - 1.1.2 description
    - 1.1.3 matrices
    - 1.1.4 sorted

  - 1.2 ZeroOperation
    - 1.2.1 is_zero
    - 1.2.2 operations
    - 1.2.3 matrices

- 2 Reversal
  - 2.1 ecuacion
  - 2.2 resultado
  - 2.3 incognita
