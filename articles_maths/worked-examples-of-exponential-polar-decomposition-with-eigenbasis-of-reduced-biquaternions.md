# __Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions__

## Introduction

This article collects the eigenbasis, the idempotents and the two spinor spaces of the eight reduced biquaternions of *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*. The polar decomposition itself, with its two components, its word and its check, is in that article; here the same eight elements are read in the eigenbasis $(\Pi_+,\Pi_-)$, with $\Pi_\pm=\tfrac12(1\pm j)$.

The eight elements, in the order of the cases, are collected in the table.

| Case | Element |
|---|---|
| 1 | $3+4i+j(1-i)$ |
| 2 | $1+i$ |
| 3 | $i$ |
| 4 | $ij$ |
| 5 | $j$ |
| 6 | $\tfrac54+\tfrac34j$ |
| 7 | $-1$ |
| 8 | $1+j$ |

## The Eigenbasis, the Basis Matrices, and the Spinors

**The basis matrices.** In the eigenbasis $(\Pi_+,\Pi_-)$, with $\Pi_\pm=\tfrac12(1\pm j)$, multiplication by each basis element has the matrix

$$
[L_1]=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
[L_j]=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
[L_i]=\begin{pmatrix}i&0\\0&i\end{pmatrix},\quad
[L_{ij}]=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
$$
$$
[L_{\Pi_+}]=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
[L_{\Pi_-}]=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

In the standard basis $(1,j)$ the first four are $[L_1]=\mathrm I_2$, $[L_j]=\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $[L_i]=i\mathrm I_2$ and $[L_{ij}]=i\sigma_x$; the matrix picture $\mathsf M(\breve Q)$ is the matrix in that basis, and the diagonal form below is its conjugate. For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$,

$$
[L_{\breve Q}]=\begin{pmatrix}C_+&0\\0&C_-\end{pmatrix},
\qquad
C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown},
$$

which is the matrix form of $\breve Q=C_+\Pi_++C_-\Pi_-$.

**The spinor spaces.** The two spinor spaces are the minimal ideals $S_\pm=\mathbb{C}\Pi_\pm$, each a complex line; the algebra is commutative, so there are no nilpotents and no mixed part. A general element is $\breve Q_2=A_1\Pi_++A_2\Pi_-$, with $A_1,A_2\in\mathbb{C}$ and
$$
[L_{\breve Q_2}]=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}.
$$
Its first column $A_1\Pi_+$ is a spinor of the first Peirce copy and its second column $A_2\Pi_-$ a spinor of the second Peirce copy. On $S_+$ multiplication by $\breve Q$ is the scalar $C_+$ and on $S_-$ it is the scalar $C_-$.

**Case by case.** The two basis matrices $[L_{\Pi_+}]$ and $[L_{\Pi_-}]$ are the same in all eight cases, because the idempotents do not depend on the element. In every case $\breve Q=C_+\Pi_++C_-\Pi_-$, so the Peirce components are $\breve Q\Pi_+=C_+\Pi_+$ and $\breve Q\Pi_-=C_-\Pi_-$, and the matrix is diagonal.

| Case | $\breve Q$ | $C_+$ | $C_-$ | $\breve Q\Pi_+$ | $\breve Q\Pi_-$ | $[L_{\breve Q}]$ |
|---|---|---|---|---|---|---|
| 1 | $3+4i+j(1-i)$ | $4+3i$ | $2+5i$ | $(4+3i)$ | $(2+5i)$ | $\operatorname{diag}(4+3i,2+5i)$ |
| 2 | $1+i$ | $1+i$ | $1+i$ | $(1+i)$ | $(1+i)$ | $(1+i)\mathrm I_2$ |
| 3 | $i$ | $i$ | $i$ | $(i)$ | $(i)$ | $i\,\mathrm I_2$ |
| 4 | $ij$ | $i$ | $-i$ | $(i)$ | $(-i)$ | $\operatorname{diag}(i,-i)$ |
| 5 | $j$ | $1$ | $-1$ | $(1)$ | $(-1)$ | $\operatorname{diag}(1,-1)$ |
| 6 | $\tfrac54+\tfrac34j$ | $2$ | $\tfrac12$ | $(2)$ | $(\tfrac12)$ | $\operatorname{diag}(2,\tfrac12)$ |
| 7 | $-1$ | $-1$ | $-1$ | $(-1)$ | $(-1)$ | $-\mathrm I_2$ |
| 8 | $1+j$ | $2$ | $0$ | $(2)$ | $(0)$ | $\operatorname{diag}(2,0)$ |

In cases 2, 3 and 7 the two eigenvalues coincide, so the element is a complex scalar and the matrix is a multiple of the identity; the two lines carry the same scale. In case 8 the second eigenvalue is zero and the matrix has rank one.

## The Eight Cases

### Case 1: $3+4i+j(1-i)$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=3+4i+j(1-i)=C_+\Pi_++C_-\Pi_-$, with $C_+=4+3i$ and $C_-=2+5i$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 2: $1+i$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=1+i=C_+\Pi_++C_-\Pi_-$, with $C_+=1+i$ and $C_-=1+i$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 3: $i$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=i=C_+\Pi_++C_-\Pi_-$, with $C_+=i$ and $C_-=i$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 4: $ij$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=ij=C_+\Pi_++C_-\Pi_-$, with $C_+=i$ and $C_-=-i$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 5: $j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=j=C_+\Pi_++C_-\Pi_-$, with $C_+=1$ and $C_-=-1$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 6: $\tfrac54+\tfrac34j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=\tfrac54+\tfrac34j=C_+\Pi_++C_-\Pi_-$, with $C_+=2$ and $C_-=\tfrac12$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 7: $-1$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=-1=C_+\Pi_++C_-\Pi_-$, with $C_+=-1$ and $C_-=-1$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

### Case 8: $1+j$

**The two idempotents.** $\Pi_\pm=\tfrac12(1\pm j)$. The algebra is commutative, so the mixed Peirce corners vanish: there are no nilpotents, and the Peirce basis has two elements, not four.

**The eigenvalue decomposition.** $\breve Q=1+j=C_+\Pi_++C_-\Pi_-$, with $C_+=2$ and $C_-=0$, so $[L_{\breve Q}]=\operatorname{diag}(C_+,C_-)$.

**The spinor spaces and a general element.** $S_\pm=\mathbb C\Pi_\pm$, one line each, and the algebra is $S_+\oplus S_-$. A general element is $\breve Q_2=a_1\Pi_++a_2\Pi_-$, with
$$
[L_{\breve Q_2}]=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix};
$$
the first column $a_1\Pi_+$ is a spinor of the first Peirce copy and the second column $a_2\Pi_-$ a spinor of the second Peirce copy. For $\breve Q$ itself the coordinates are $(a_1,a_2)=(C_+,C_-)$.

## Summary

- The eigenbasis $(\Pi_+,\Pi_-)$ is the same in all eight cases, because the idempotents do not depend on the element; only the eigenvalues $C_\pm$ change.
- In cases 2, 3 and 7 the two eigenvalues coincide, so the element is a complex scalar, the two spinor lines carry the same scale and the matrix is a multiple of the identity.
- In case 8 the second eigenvalue is zero; the component $\breve Q\Pi_-$ vanishes and the matrix has rank one.
- The two Peirce components sum to $[L_{\breve Q}]$ in every case: $\breve Q\Pi_++\breve Q\Pi_-=C_+\Pi_++C_-\Pi_-$ is the diagonal matrix $\operatorname{diag}(C_+,C_-)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents |
| $S_\pm=\mathbb{C}\Pi_\pm$ | the two spinor spaces, complex lines |
| $\xi_+=A_1\Pi_+$, $\xi_-=A_2\Pi_-$ | the two spinors |
| $A_1,A_2\in\mathbb{C}$ | the spinor coordinates |
| $C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the eigenvalues of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ |
| $[L_{\breve Q}]$ | the matrix of multiplication by $\breve Q$ in the eigenbasis |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the polar decomposition, its word and its check.
- [Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-a-reduced-biquaternion.html), for the relation between the two decompositions in the commutative four-dimensional case.
