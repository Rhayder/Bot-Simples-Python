{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "bb0ae933",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyautogui\n",
    "\n",
    "pyautogui.PAUSE = 2\n",
    "# abrir ferramenta/sistemas\n",
    "pyautogui.press(\"win\")\n",
    "pyautogui.write(\"Login.xlsx\")\n",
    "pyautogui.press(\"backspace\")\n",
    "pyautogui.press(\"enter\")\n",
    "# preencher login\n",
    "pyautogui.click(x=498, y=281)\n",
    "pyautogui.write(\"Rhayder\")\n",
    "# preencher senha\n",
    "pyautogui.click(x=493, y=340)\n",
    "pyautogui.write(\"teste@teste123789\")\n",
    "# clicar em logar\n",
    "pyautogui.click(x=347, y=435)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a2a77b44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Point(x=1241, y=15)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ac15b1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
