{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "lesson.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNSpFErJgJsO0km1ukhBSRD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HusanJalilov/AI_Jpyuter_/blob/main/lesson_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OF7CmlteLLQl"
      },
      "source": [
        "import pandas as pd\n"
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "OGA76k7zLwI8",
        "outputId": "4293bfd0-1518-4669-84db-7a197b762424"
      },
      "source": [
        "data={\n",
        "    'Yil':[2010,2016,2017,2018,2019,2020,2021],\n",
        "    'Detilar':[230,124,678,89,45,890,345],\n",
        "    'Kadetlar':[230,321,333,567,345,876,348],\n",
        "    'Yunyorlar':[100,32,144,788,334,80,567],\n",
        "    'Vuzroznilar':[12,44,76,34,99,46,9]\n",
        "}\n",
        "df=pd.DataFrame(data)\n",
        "df"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Yil</th>\n",
              "      <th>Detilar</th>\n",
              "      <th>Kadetlar</th>\n",
              "      <th>Yunyorlar</th>\n",
              "      <th>Vuzroznilar</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2010</td>\n",
              "      <td>230</td>\n",
              "      <td>230</td>\n",
              "      <td>100</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2016</td>\n",
              "      <td>124</td>\n",
              "      <td>321</td>\n",
              "      <td>32</td>\n",
              "      <td>44</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2017</td>\n",
              "      <td>678</td>\n",
              "      <td>333</td>\n",
              "      <td>144</td>\n",
              "      <td>76</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2018</td>\n",
              "      <td>89</td>\n",
              "      <td>567</td>\n",
              "      <td>788</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2019</td>\n",
              "      <td>45</td>\n",
              "      <td>345</td>\n",
              "      <td>334</td>\n",
              "      <td>99</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>2020</td>\n",
              "      <td>890</td>\n",
              "      <td>876</td>\n",
              "      <td>80</td>\n",
              "      <td>46</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>2021</td>\n",
              "      <td>345</td>\n",
              "      <td>348</td>\n",
              "      <td>567</td>\n",
              "      <td>9</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Yil  Detilar  Kadetlar  Yunyorlar  Vuzroznilar\n",
              "0  2010      230       230        100           12\n",
              "1  2016      124       321         32           44\n",
              "2  2017      678       333        144           76\n",
              "3  2018       89       567        788           34\n",
              "4  2019       45       345        334           99\n",
              "5  2020      890       876         80           46\n",
              "6  2021      345       348        567            9"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0T64Z1ESL9z1",
        "outputId": "8d7e44a6-fd3e-4fce-96bc-8a7a63ed46bb"
      },
      "source": [
        "dew=df['Yil']\n",
        "dew"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    2010\n",
              "1    2016\n",
              "2    2017\n",
              "3    2018\n",
              "4    2019\n",
              "5    2020\n",
              "6    2021\n",
              "Name: Yil, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-xBaCfhGN860",
        "outputId": "3c2d97a7-1f1d-4276-d715-bd90daf2501e"
      },
      "source": [
        "type(dew)"
      ],
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.series.Series"
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i8YV9ou3OAGO",
        "outputId": "9b69724a-071d-42e2-83ed-3c8dfe87c8b9"
      },
      "source": [
        "dew1=df[['Yil','Kadetlar']]\n",
        "type(dew1)"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PR7pCZrxOmae",
        "outputId": "e8ec32b6-e4c7-42b6-bf85-71085d4f45ad"
      },
      "source": [
        "dew"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    2010\n",
              "1    2016\n",
              "2    2017\n",
              "3    2018\n",
              "4    2019\n",
              "5    2020\n",
              "6    2021\n",
              "Name: Yil, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ShwmILkEPgZw"
      },
      "source": [
        "dew.index=[12,13,55,77,34,56,78]"
      ],
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ftAwYyDPmZe",
        "outputId": "f73de5c1-2768-40aa-bec6-18ace1eb6210"
      },
      "source": [
        "dew"
      ],
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12    2010\n",
              "13    2016\n",
              "55    2017\n",
              "77    2018\n",
              "34    2019\n",
              "56    2020\n",
              "78    2021\n",
              "Name: Yil, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DZm_RxYVPnoH",
        "outputId": "63a1f789-b834-4c64-f0fb-f9f49a4ee3b9"
      },
      "source": [
        "dew[2:4]"
      ],
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "55    2017\n",
              "77    2018\n",
              "Name: Yil, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pR3DWEOUPq78"
      },
      "source": [
        "import numpy as np\n",
        "abj=pd.Series(np.arange(5), index=['a','s','d','f','g'])"
      ],
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "raEf4SGhSPlT",
        "outputId": "fbba4b16-9e43-489c-cf47-9d3afe285bbe"
      },
      "source": [
        "abj"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a     0\n",
              "s,    1\n",
              "d     2\n",
              "f     3\n",
              "g     4\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sHNlNK9BSV7J",
        "outputId": "0ad7fb5e-5b5a-49f0-9080-f0bd417f12b3"
      },
      "source": [
        "abj['a']"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GQkgfXQxSbcM",
        "outputId": "d03fb1b0-34db-4020-b333-f70f2c297bc1"
      },
      "source": [
        "abj[['a']]"
      ],
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 64
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gTku0l_bSd9_",
        "outputId": "c8ce4a61-a386-408e-916b-52ff8d1b4576"
      },
      "source": [
        "abj[0:3]"
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a    0\n",
              "s    1\n",
              "d    2\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Pv1IKrYySk4a",
        "outputId": "d6947d69-1e22-4063-efaf-f0c905c1d5c0"
      },
      "source": [
        "abj[abj<3]"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a    0\n",
              "s    1\n",
              "d    2\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4gi9F1uSS5oM"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}