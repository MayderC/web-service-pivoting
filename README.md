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

### Json response para pivoteo parcial y escalonado

```json
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
                [3, 1, -1, 1],
                [2, 3, 1, 1],
                [0, -2, -1, -14]
              ],
              [
                [3, 1, -1, 1],
                [
                  0, 2.3333333333333335, 1.6666666666666665, 0.33333333333333337
                ],
                [0, -2, -1, -14]
              ]
            ],
            "elemental_operation": ["2.0/3.0"],
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
                [3, 1, -1, 1],
                [
                  0, 2.3333333333333335, 1.6666666666666665, 0.33333333333333337
                ],
                [0, -2, -1, -14]
              ]
            ],
            "elemental_operation": ["0.0/3.0"],
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
              [0, -2, -1, -14],
              [2, 3, 1, 1],
              [3, 1, -1, 1]
            ],
            [
              [3, 1, -1, 1],
              [2, 3, 1, 1],
              [0, -2, -1, -14]
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
                [3, 1, -1, 1],
                [
                  0, 2.3333333333333335, 1.6666666666666665, 0.33333333333333337
                ],
                [0, -2, -1, -14]
              ],
              [
                [3, 1, -1, 1],
                [
                  0, 2.3333333333333335, 1.6666666666666665, 0.33333333333333337
                ],
                [0, 0, 0.4285714285714284, -13.714285714285714]
              ]
            ],
            "elemental_operation": ["-2.0/2.3333333333333335"],
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
              [3, 1, -1, 1],
              [0, 2.3333333333333335, 1.6666666666666665, 0.33333333333333337],
              [0, -2, -1, -14]
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

## Json response para pivoteo total

```json
{
  "solution": {
    "x": 3,
    "z": 1,
    "y": 2
  },
  "steps": {
    "firts_operation": [
      {
        "matrices": [
          [
            [3, -6, 7, 4],
            [8, 0, -5, 19],
            [1, -2, 6, 5]
          ],
          [
            [8, 0, -5, 19],
            [3, -6, 7, 4],
            [1, -2, 6, 5]
          ]
        ],
        "unknowns": [["x", "y", "z"]],
        "one_operation": {
          "operations": [
            {
              "operation": "1.0 * 1 / 8.0",
              "row": 0,
              "col": 0,
              "result": 1
            },
            {
              "operation": "0.0 * 1 / 8.0",
              "row": 0,
              "col": 1,
              "result": 0
            },
            {
              "operation": "-0.625 * 1 / 8.0",
              "row": 0,
              "col": 2,
              "result": -0.625
            },
            {
              "operation": "2.375 * 1 / 8.0",
              "row": 0,
              "col": 3,
              "result": 2.375
            }
          ],
          "matrices": [
            [
              [8, 0, -5, 19],
              [3, -6, 7, 4],
              [1, -2, 6, 5]
            ],
            [
              [1, 0, -0.625, 2.375],
              [3, -6, 7, 4],
              [1, -2, 6, 5]
            ]
          ]
        },
        "zero_operation": {
          "operations": [
            {
              "operation": "1.0 * 3.0 * -1 + 0.0",
              "row": 0,
              "col": 1,
              "result": 0
            },
            {
              "operation": "0.0 * 3.0 * -1 + -6.0",
              "row": 0,
              "col": 1,
              "result": -6
            },
            {
              "operation": "-0.625 * 3.0 * -1 + 8.875",
              "row": 0,
              "col": 1,
              "result": 8.875
            },
            {
              "operation": "2.375 * 3.0 * -1 + -3.125",
              "row": 0,
              "col": 1,
              "result": -3.125
            },
            {
              "operation": "1.0 * 1.0 * -1 + 0.0",
              "row": 0,
              "col": 2,
              "result": 0
            },
            {
              "operation": "0.0 * 1.0 * -1 + -2.0",
              "row": 0,
              "col": 2,
              "result": -2
            },
            {
              "operation": "-0.625 * 1.0 * -1 + 6.625",
              "row": 0,
              "col": 2,
              "result": 6.625
            },
            {
              "operation": "2.375 * 1.0 * -1 + 2.625",
              "row": 0,
              "col": 2,
              "result": 2.625
            }
          ],
          "matrices": [
            [
              [1, 0, -0.625, 2.375],
              [3, -6, 7, 4],
              [1, -2, 6, 5]
            ],
            [
              [1, 0, -0.625, 2.375],
              [0, -6, 8.875, -3.125],
              [0, -2, 6.625, 2.625]
            ]
          ]
        },
        "sorted_pivot": false,
        "pivot_value": 8,
        "pivot_positions": {
          "row": 1,
          "column": 0
        },
        "description_row": "Se cambia la fila 2 por la fila 1",
        "description_col": "No hay cambio de columnas",
        "description_unk": "No hay cambio de posicion en las incognitas"
      },
      {
        "matrices": [
          [
            [1, 0, -0.625, 2.375],
            [0, -6, 8.875, -3.125],
            [0, -2, 6.625, 2.625]
          ],
          [
            [1, -0.625, 0, 2.375],
            [0, 8.875, -6, -3.125],
            [0, 6.625, -2, 2.625]
          ]
        ],
        "unknowns": [
          ["x", "y", "z"],
          ["x", "z", "y"]
        ],
        "one_operation": {
          "operations": [
            {
              "operation": "1.0 * 1 / 8.875",
              "row": 1,
              "col": 1,
              "result": 1
            },
            {
              "operation": "-0.676056338028169 * 1 / 8.875",
              "row": 1,
              "col": 2,
              "result": -0.676056338028169
            },
            {
              "operation": "-0.35211267605633806 * 1 / 8.875",
              "row": 1,
              "col": 3,
              "result": -0.35211267605633806
            }
          ],
          "matrices": [
            [
              [1, -0.625, 0, 2.375],
              [0, 8.875, -6, -3.125],
              [0, 6.625, -2, 2.625]
            ],
            [
              [1, -0.625, 0, 2.375],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 6.625, -2, 2.625]
            ]
          ]
        },
        "zero_operation": {
          "operations": [
            {
              "operation": "1.0 * -0.625 * -1 + 0.0",
              "row": 1,
              "col": 0,
              "result": 0
            },
            {
              "operation": "-0.676056338028169 * -0.625 * -1 + -0.4225352112676056",
              "row": 1,
              "col": 0,
              "result": -0.4225352112676056
            },
            {
              "operation": "-0.35211267605633806 * -0.625 * -1 + 2.1549295774647885",
              "row": 1,
              "col": 0,
              "result": 2.1549295774647885
            },
            {
              "operation": "1.0 * 6.625 * -1 + 0.0",
              "row": 1,
              "col": 2,
              "result": 0
            },
            {
              "operation": "-0.676056338028169 * 6.625 * -1 + 2.47887323943662",
              "row": 1,
              "col": 2,
              "result": 2.47887323943662
            },
            {
              "operation": "-0.35211267605633806 * 6.625 * -1 + 4.95774647887324",
              "row": 1,
              "col": 2,
              "result": 4.95774647887324
            }
          ],
          "matrices": [
            [
              [1, -0.625, 0, 2.375],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 6.625, -2, 2.625]
            ],
            [
              [1, 0, -0.4225352112676056, 2.1549295774647885],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 0, 2.47887323943662, 4.95774647887324]
            ]
          ]
        },
        "sorted_pivot": false,
        "pivot_value": 8.875,
        "pivot_positions": {
          "row": 1,
          "column": 2
        },
        "description_row": "No hay cambio de filas",
        "description_col": "Se cambia la columna 3 por la columna 2",
        "description_unk": "Se cambia la columna 3 por la columna 2 del vector de incognitas"
      },
      {
        "matrices": [
          [
            [1, 0, -0.4225352112676056, 2.1549295774647885],
            [0, 1, -0.676056338028169, -0.35211267605633806],
            [0, 0, 2.47887323943662, 4.95774647887324]
          ]
        ],
        "unknowns": [["x", "z", "y"]],
        "one_operation": {
          "operations": [
            {
              "operation": "1.0 * 1 / 2.47887323943662",
              "row": 2,
              "col": 2,
              "result": 1
            },
            {
              "operation": "2.0 * 1 / 2.47887323943662",
              "row": 2,
              "col": 3,
              "result": 2
            }
          ],
          "matrices": [
            [
              [1, 0, -0.4225352112676056, 2.1549295774647885],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 0, 2.47887323943662, 4.95774647887324]
            ],
            [
              [1, 0, -0.4225352112676056, 2.1549295774647885],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 0, 1, 2]
            ]
          ]
        },
        "zero_operation": {
          "operations": [
            {
              "operation": "1.0 * -0.4225352112676056 * -1 + 0.0",
              "row": 2,
              "col": 0,
              "result": 0
            },
            {
              "operation": "2.0 * -0.4225352112676056 * -1 + 3.0",
              "row": 2,
              "col": 0,
              "result": 3
            },
            {
              "operation": "1.0 * -0.676056338028169 * -1 + 0.0",
              "row": 2,
              "col": 1,
              "result": 0
            },
            {
              "operation": "2.0 * -0.676056338028169 * -1 + 1.0",
              "row": 2,
              "col": 1,
              "result": 1
            }
          ],
          "matrices": [
            [
              [1, 0, -0.4225352112676056, 2.1549295774647885],
              [0, 1, -0.676056338028169, -0.35211267605633806],
              [0, 0, 1, 2]
            ],
            [
              [1, 0, 0, 3],
              [0, 1, 0, 1],
              [0, 0, 1, 2]
            ]
          ]
        },
        "sorted_pivot": true,
        "pivot_value": 2.47887323943662,
        "pivot_positions": {
          "row": 2,
          "column": 2
        },
        "description_row": "No hay cambio de filas",
        "description_col": "No hay cambio de columnas",
        "description_unk": "No hay cambio de posición en las incógnitas"
      }
    ],
    "sort_unknowns": []
  }
}
```

### data properties

```js

export interface Response {
  solution: Solution
  steps: {
    first_operation : Step[],
    sort_unknowns : string[]
  }
}

Solution {
  x: number
  z: number
  y: number
}

Step {
  matrices: number[][][]
  unknowns: string[][]
  one_operation: OneOperation
  zero_operation: ZeroOperation
  sorted_pivot: boolean
  pivot_value: number
  pivot_positions: PivotPositions
  description_row: string
  description_col: string
  description_unk: string
}

OneOperation {
  operations: Operation[]
  matrices: number[][][]
}


ZeroOperation {
  operations: Operation[]
  matrices: number[][][]
}

Operation {
  operation: string
  row: number
  col: number
  result: number
}

PivotPositions {
  row: number
  column: number
}

```

#### Orden

- Pivote
- Cambio de filas o columnas o ambas
- hacer uno, antes y despues
- hacer cero antes y despues
  solucion ultima columna de la matriz
- ultimo array de string: Pendiente.
