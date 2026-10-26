# __Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers__

## Introduction

This article collects the eigenbasis, the idempotents and the two spinor spaces of the eight split-complex numbers of *Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers*. The polar decomposition itself, with its coordinates, its word and its check, is in that article; here the same eight elements are read in the eigenbasis $(\Pi_+,\Pi_-)$, with $\Pi_\pm=\tfrac12(1\pm j)$.

The eight elements, in the order of the cases, are collected in the table.

| Case | Element |
|---|---|
| 1 | $5+3j$ |
| 2 | $3+5j$ |
| 3 | $-5-3j$ |
| 4 | $1-2j$ |
| 5 | $j$ |
| 6 | $2$ |
| 7 | $-2$ |
| 8 | $1+j$ |

## The Eigenbasis, the Basis Matrices, and the Spinors

**The basis matrices.** In the eigenbasis $(\Pi_+,\Pi_-)$, with $\Pi_\pm=\tfrac12(1\pm j)$, multiplication by each basis element has the matrix

$$
[L_1]=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
[L_j]=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
[L_{\Pi_+}]=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
[L_{\Pi_-}]=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

In the standard basis $(1,j)$ the first two are $[L_1]=\mathrm I_2$ and $[L_j]=\begin{pmatrix}0&1\\1&0\end{pmatrix}$; the two pairs are conjugate by the change of basis whose columns are the coordinates of $\Pi_+$ and $\Pi_-$. For $Q=q+jq'$,

$$
[L_Q]=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
\qquad
\lambda_\pm=q\pm q',
$$

which is the matrix form of $Q=\lambda_+\Pi_++\lambda_-\Pi_-$.

**The spinor spaces.** The two spinor spaces are the minimal ideals $S_\pm=\mathbb{R}\Pi_\pm$, each a real line; the algebra is commutative, so there are no nilpotents and no mixed part. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with $a_1,a_2\in\mathbb{R}$ and
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}.
$$
Its first column $a_1\Pi_+$ is a spinor of first chirality and its second column $a_2\Pi_-$ a spinor of second chirality. On $S_+$ multiplication by $Q$ is the scalar $\lambda_+$ and on $S_-$ it is the scalar $\lambda_-$. After complexification the same formulas hold with $a_1,a_2\in\mathbb{C}$.

**Case by case.** The two basis matrices $[L_{\Pi_+}]$ and $[L_{\Pi_-}]$ are the same in all eight cases, because the idempotents do not depend on the element. In every case $Q=\lambda_+\Pi_++\lambda_-\Pi_-$, so the Peirce components are $Q\Pi_+=\lambda_+\Pi_+$ and $Q\Pi_-=\lambda_-\Pi_-$, and the matrix is diagonal.

| Case | $Q$ | $\lambda_+$ | $\lambda_-$ | $Q\Pi_+$ | $Q\Pi_-$ | $[L_Q]$ |
|---|---|---|---|---|---|---|
| 1 | $5+3j$ | $8$ | $2$ | $(8)$ | $(2)$ | $\operatorname{diag}(8,2)$ |
| 2 | $3+5j$ | $8$ | $-2$ | $(8)$ | $(-2)$ | $\operatorname{diag}(8,-2)$ |
| 3 | $-5-3j$ | $-8$ | $-2$ | $(-8)$ | $(-2)$ | $\operatorname{diag}(-8,-2)$ |
| 4 | $1-2j$ | $-1$ | $3$ | $(-1)$ | $(3)$ | $\operatorname{diag}(-1,3)$ |
| 5 | $j$ | $1$ | $-1$ | $(1)$ | $(-1)$ | $\operatorname{diag}(1,-1)$ |
| 6 | $2$ | $2$ | $2$ | $(2)$ | $(2)$ | $2\,\mathrm I_2$ |
| 7 | $-2$ | $-2$ | $-2$ | $(-2)$ | $(-2)$ | $-2\,\mathrm I_2$ |
| 8 | $1+j$ | $2$ | $0$ | $(2)$ | $(0)$ | $\operatorname{diag}(2,0)$ |

In case 6 and case 7 the two eigenvalues coincide and the two lines carry the same scale; in case 8 the second eigenvalue is zero and the matrix has rank one.

## The Eight Cases

### Case 1: $5+3j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=5+3j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=8$ and $\lambda_-=2$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 2: $3+5j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=3+5j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=8$ and $\lambda_-=-2$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 3: $-5-3j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=-5-3j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=-8$ and $\lambda_-=-2$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 4: $1-2j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=1-2j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=-1$ and $\lambda_-=3$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 5: $j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=1$ and $\lambda_-=-1$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 6: $2$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=2=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=2$ and $\lambda_-=2$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 7: $-2$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=-2=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=-2$ and $\lambda_-=-2$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

### Case 8: $1+j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $Q=1+j=\lambda_+\Pi_++\lambda_-\Pi_-$, with $\lambda_+=2$ and $\lambda_-=0$, so $[L_{Q}]=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb R\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of first chirality and the second column $a_2\Pi_-$ a spinor of second chirality. For $Q$ itself the coordinates are $(a_1,a_2)=(\lambda_+,\lambda_-)$.

## Summary

- The eigenbasis $(\Pi_+,\Pi_-)$ is the same in all eight cases, because the idempotents do not depend on the element; only the eigenvalues $\lambda_\pm$ change.
- In cases 6 and 7 the two eigenvalues coincide, so the two spinor lines carry the same scale and the matrix is a multiple of the identity.
- In case 8 the second eigenvalue is zero; the component $Q\Pi_-$ vanishes and the matrix has rank one.
- The two Peirce components sum to $[L_Q]$ in every case: $Q\Pi_++Q\Pi_-=\lambda_+\Pi_++\lambda_-\Pi_-$ is the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents |
| $S_\pm=\mathbb{R}\Pi_\pm$ | the two spinor spaces, real lines |
| $\xi_+=a_1\Pi_+$, $\xi_-=a_2\Pi_-$ | the two spinors |
| $a_1,a_2\in\mathbb{R}$ | the spinor coordinates, complex after complexification |
| $\lambda_\pm=q\pm q'$ | the eigenvalues of $Q=q+jq'$ |
| $[L_Q]$ | the matrix of multiplication by $Q$ in the eigenbasis |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the polar decomposition, its word and its check.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the relation between the two decompositions in the real two-dimensional case.
