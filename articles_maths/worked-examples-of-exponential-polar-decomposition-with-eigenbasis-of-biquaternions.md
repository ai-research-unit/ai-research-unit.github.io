# __Worked Examples of Exponential Polar Decomposition with Eigenbasis of Biquaternions__

## Introduction

This article collects the eigenbasis, the four basis elements (two idempotents and two nilpotents) and the two spinor spaces of the eight biquaternions of *Worked Examples of Exponential Polar Decomposition of Biquaternions*. The polar decomposition itself, with its coordinates, its word and its check, is in that article; here the same eight elements are read in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$.

In the three cases with $B=0$, the identity of case 1 and the null-vector elements of cases 6 and 8, there is no eigenbasis singled out by the element. The paragraph of the case reads the element in a fixed Peirce basis $(\tilde\Pi_{+,0},\tilde\Pi_{-,0})$ of *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*; in case 1 the conclusion holds for every pair of complementary idempotents, so the fixed pair is only a choice.

The eight elements, in the order of the cases, are collected in the table.

| Case | Element |
|---|---|
| 1 | $e_t$ |
| 2 | $\vec e_x$ |
| 3 | $\tfrac{1}{\sqrt2}(e_t+\vec e_x)$ |
| 4 | $\sqrt2\,e_t+i\vec e_x$ |
| 5 | $\bigl(1-\tfrac{i}{\sqrt2}\bigr)e_t+\bigl(1+\tfrac{i}{\sqrt2}\bigr)\vec e_x$ |
| 6 | $e_t+\vec e_y+\tfrac{i}{\sqrt2}\vec e_x+\tfrac{i}{\sqrt2}\vec e_z$ |
| 7 | $\bigl(1-\tfrac{i}{2}\bigr)e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z$ |
| 8 | $(1+i)e_t+\vec e_x+i\vec e_y$ |

## The Eigenbasis, the Basis Matrices, and the Spinors

**The basis.** For $\vec Q\neq0$ put $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$, $\vec\Xi=-i\vec Q/B$ and $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$. The two mixed corners are the complex lines
$$
\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
\qquad
\mathbb{B}_{+-}=\tilde\Pi_+\mathbb{B}\tilde\Pi_-,
$$
and $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$ are their generators, normalized by
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_\pm^2=0.
$$
The normalization fixes the pair up to the reciprocal rescaling $\vec\Upsilon_+\mapsto\mu\vec\Upsilon_+$, $\vec\Upsilon_-\mapsto\mu^{-1}\vec\Upsilon_-$. In the eigenbasis order $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the left-regular matrices of the four basis elements are
$$
[L_{\tilde\Pi_+}]=\operatorname{diag}(1,1,0,0),\qquad
[L_{\tilde\Pi_-}]=\operatorname{diag}(0,0,1,1),
$$
$$
[L_{\vec\Upsilon_-}]=
\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
[L_{\vec\Upsilon_+}]=
\begin{pmatrix}0&0&0&0\\0&0&0&0\\1&0&0&0\\0&1&0&0\end{pmatrix},
$$
and
$$
[L_{\tilde Q}]=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
\qquad
\lambda_\pm=Q_t\pm iB.
$$
In the $2\times2$ model $\mathsf M_2^{Q}$ the same elements are
$$
\mathsf M_2^{Q}(\tilde\Pi_+)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\mathsf M_2^{Q}(\vec\Upsilon_-)=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\mathsf M_2^{Q}(\vec\Upsilon_+)=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\mathsf M_2^{Q}(\tilde\Pi_-)=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$
$$
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
When $\vec Q\parallel\vec e_z$ the eigenbasis is the standard Peirce basis of *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*, §*The Biquaternion Case*, with the two labels exchanged according to the sign of $B$; the four matrices above are then the matrices of $\tilde\Pi_+$, $\vec\Upsilon_-$, $\vec\Upsilon_+$, $\tilde\Pi_-$ in that basis.

**The spinor spaces.** The two spinor spaces are the minimal left ideals
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-.
$$
Each is two-dimensional over $\mathbb{C}$. A spinor is an element of one of them, so it has two complex coordinates, not one. A spinor of first chirality is
$$
\xi_+=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+,
\qquad (Q_{2,11},Q_{2,21})\in\mathbb{C}^2,
$$
the first column of the matrix; a spinor of second chirality is
$$
\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-,
\qquad (Q_{2,12},Q_{2,22})\in\mathbb{C}^2,
$$
the second column. The four coordinates together belong to a general element of the algebra,
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^{Q}(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix},
$$
which is the pair $(\xi_+,\xi_-)$ and is not itself a spinor. The matrices of the two spinors are
$$
\mathsf M_2^{Q}(\xi_+)=\begin{pmatrix}Q_{2,11}&0\\Q_{2,21}&0\end{pmatrix},
\qquad
\mathsf M_2^{Q}(\xi_-)=\begin{pmatrix}0&Q_{2,12}\\0&Q_{2,22}\end{pmatrix}.
$$
Under multiplication by $\tilde Q$,
$$
(Q_{2,11},Q_{2,21})\longmapsto(\lambda_+Q_{2,11},\;\lambda_-Q_{2,21}),
\qquad
(Q_{2,12},Q_{2,22})\longmapsto(\lambda_+Q_{2,12},\;\lambda_-Q_{2,22}).
$$

**The Peirce coordinates of $\tilde Q_2=\tilde Q$.** For the element $\tilde Q_2=\tilde Q$ of the decomposition the nilpotent coordinates vanish, $Q_{2,21}=Q_{2,12}=0$, and $Q_{2,11}=\lambda_+$, $Q_{2,22}=\lambda_-$. Its Peirce components are therefore
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+\longleftrightarrow\begin{pmatrix}\lambda_+\\0\end{pmatrix},
\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-\longleftrightarrow\begin{pmatrix}0\\\lambda_-\end{pmatrix},
$$
with matrices $\operatorname{diag}(\lambda_+,0)$ and $\operatorname{diag}(0,\lambda_-)$, and their sum is $\operatorname{diag}(\lambda_+,\lambda_-)$. The zero entries are the vanishing nilpotent coordinates of this particular element, not a missing dimension: a general element in the same basis can have both coordinates nonzero in each column. For example, $\tilde Q+\vec\Upsilon_++\vec\Upsilon_-$ has the matrix
$$
\mathsf M_2^{Q}(\tilde Q+\vec\Upsilon_++\vec\Upsilon_-)=\begin{pmatrix}\lambda_+&1\\1&\lambda_-\end{pmatrix},
$$
first-chirality spinor $\xi_+=( \lambda_+,1)$ and second-chirality spinor $\xi_-=(1,\lambda_-)$.

**Case by case.** In every case with $B\neq0$ the eigenvalues are $\lambda_\pm=Q_t\pm iB$, the
Peirce components of $\tilde Q$ are $\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+$ and $\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-$; these are the columns $(\lambda_+,0)$ and $(0,\lambda_-)$ of the diagonal matrix, the nilpotent coordinates being zero because the element of the case is $\tilde Q$ itself. For cases 2 to 5 the vector part is $Q_x\vec e_x$ and $B=Q_x$, so $\vec\Xi=-i\vec e_x$ and $\tilde\Pi_\pm=\tfrac12(e_t\mp i\vec e_x)$; case 7 has a genuine three-dimensional vector part.

| Case | $\tilde Q$ | $B$ | $\lambda_+$ | $\lambda_-$ | $\tilde Q\tilde\Pi_+$ | $\tilde Q\tilde\Pi_-$ | $\mathsf M_2^{Q}(\tilde Q)$ |
|---|---|---|---|---|---|---|---|
| 1 | $e_t$ | $0$ | $1$ | $1$ | any $\tilde\Pi_+$ | any $\tilde\Pi_-$ | $\mathrm I_2$ |
| 2 | $\vec e_x$ | $1$ | $i$ | $-i$ | $(i,0)$ | $(0,-i)$ | $\operatorname{diag}(i,-i)$ |
| 3 | $\tfrac{1}{\sqrt2}(e_t+\vec e_x)$ | $\tfrac{1}{\sqrt2}$ | $\tfrac{1+i}{\sqrt2}$ | $\tfrac{1-i}{\sqrt2}$ | $(\lambda_+,0)$ | $(0,\lambda_-)$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ |
| 4 | $\sqrt2\,e_t+i\vec e_x$ | $i$ | $\sqrt2-1$ | $\sqrt2+1$ | $(\lambda_+,0)$ | $(0,\lambda_-)$ | $\operatorname{diag}(\sqrt2-1,\sqrt2+1)$ |
| 5 | $\bigl(1-\tfrac{i}{\sqrt2}\bigr)e_t+\bigl(1+\tfrac{i}{\sqrt2}\bigr)\vec e_x$ | $1+\tfrac{i}{\sqrt2}$ | $\bigl(1-\tfrac{1}{\sqrt2}\bigr)(1+i)$ | $\bigl(1+\tfrac{1}{\sqrt2}\bigr)(1-i)$ | $(\lambda_+,0)$ | $(0,\lambda_-)$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ |
| 6 | $e_t+\vec e_y+\tfrac{i}{\sqrt2}\vec e_x+\tfrac{i}{\sqrt2}\vec e_z$ | $0$ | $1$ | $1$ | — | — | — (Jordan block) |
| 7 | $\bigl(1-\tfrac{i}{2}\bigr)e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z$ | $\sqrt{i+\tfrac14}$ | $1-\tfrac{i}{2}+iB$ | $1-\tfrac{i}{2}-iB$ | $(\lambda_+,0)$ | $(0,\lambda_-)$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ |
| 8 | $(1+i)e_t+\vec e_x+i\vec e_y$ | $0$ | $1+i$ | $1+i$ | — | — | — (Jordan block) |

In case 1 the element is the identity and every pair of complementary idempotents is an eigenbasis: the two spinor spaces can be any pair of minimal ideals, and both eigenvalues are $1$. In cases 6 and 8 the vector part is null, $B=0$, so there is no eigenbasis, no normalized nilpotent pair and no spinor decomposition attached to $\tilde Q$; the multiplication is a single Jordan block with the repeated eigenvalue $1$, respectively $1+i$, and the matrix is not diagonalisable.

## The Eight Cases

### Case 1: $e_t$

**The four basis elements.** $B=0$, so there is no eigenbasis. The fixed Peirce basis of the algebra is
$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),\quad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=e_t=\tilde\Pi_++\tilde\Pi_-$, so $\lambda_+=\lambda_-=1$ and $\mathsf M_2^Q(\tilde Q)=\mathrm I_2$; every complementary pair of idempotents gives the same decomposition.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(1,0,0,1)$.

### Case 2: $\vec e_x$

**The four basis elements.** $\vec Q=\vec e_x$ and $B=1$, so $\vec\Xi=-i\vec e_x$ and
$$
\tilde\Pi_+=\tfrac12(e_t-i\vec e_x),\quad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_x),\quad
\vec\Upsilon_+=\tfrac12(\vec e_y+i\vec e_z),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_z-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=i\tilde\Pi_+-i\tilde\Pi_-$, so $\lambda_+=i$, $\lambda_-=-i$ and $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(i,-i)$.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(i,0,0,-i)$.

### Case 3: $\tfrac{1}{\sqrt2}(e_t+\vec e_x)$

**The four basis elements.** The vector part is again along $\vec e_x$, so $\vec\Xi=-i\vec e_x$ and the four basis elements are those of Case 2:
$$
\tilde\Pi_+=\tfrac12(e_t-i\vec e_x),\quad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_x),\quad
\vec\Upsilon_+=\tfrac12(\vec e_y+i\vec e_z),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_z-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=\tfrac{1}{\sqrt2}(e_t+\vec e_x)=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, with $\lambda_+=\tfrac{1+i}{\sqrt2}$ and $\lambda_-=\tfrac{1-i}{\sqrt2}$, so $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(\lambda_+,0,0,\lambda_-)$.

### Case 4: $\sqrt2\,e_t+i\vec e_x$

**The four basis elements.** The vector part is again along $\vec e_x$, so $\vec\Xi=-i\vec e_x$ and the four basis elements are those of Case 2:
$$
\tilde\Pi_+=\tfrac12(e_t-i\vec e_x),\quad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_x),\quad
\vec\Upsilon_+=\tfrac12(\vec e_y+i\vec e_z),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_z-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=\sqrt2\,e_t+i\vec e_x=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, with $\lambda_+=\sqrt2-1$ and $\lambda_-=\sqrt2+1$, so $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(\lambda_+,0,0,\lambda_-)$.

### Case 5: $\bigl(1-\tfrac{i}{\sqrt2}\bigr)e_t+\bigl(1+\tfrac{i}{\sqrt2}\bigr)\vec e_x$

**The four basis elements.** The vector part is again along $\vec e_x$, so $\vec\Xi=-i\vec e_x$ and the four basis elements are those of Case 2:
$$
\tilde\Pi_+=\tfrac12(e_t-i\vec e_x),\quad
\tilde\Pi_-=\tfrac12(e_t+i\vec e_x),\quad
\vec\Upsilon_+=\tfrac12(\vec e_y+i\vec e_z),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_z-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=\bigl(1-\tfrac{i}{\sqrt2}\bigr)e_t+\bigl(1+\tfrac{i}{\sqrt2}\bigr)\vec e_x=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, with $\lambda_+=\bigl(1-\tfrac{1}{\sqrt2}\bigr)(1+i)$ and $\lambda_-=\bigl(1+\tfrac{1}{\sqrt2}\bigr)(1-i)$, so $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(\lambda_+,0,0,\lambda_-)$.

### Case 6: $e_t+\vec e_y+\tfrac{i}{\sqrt2}\vec e_x+\tfrac{i}{\sqrt2}\vec e_z$

**The four basis elements.** $B=0$, so there is no eigenbasis. The fixed Peirce basis of the algebra is
$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),\quad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** The eigenvalue is $\lambda_+=1$, double, and
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}1+\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}-1\\[2pt]1+\tfrac{1}{\sqrt2}&1-\tfrac{1}{\sqrt2}\end{pmatrix}=\mathrm I_2+\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}-1\\[2pt]1+\tfrac{1}{\sqrt2}&-\tfrac{1}{\sqrt2}\end{pmatrix},
$$
and the second matrix is square-zero. The element is unipotent: it is not diagonalisable and no eigenbasis exists.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q$ itself the two columns are $(1+\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$ and $(\tfrac{1}{\sqrt2}-1,1-\tfrac{1}{\sqrt2})$; left multiplication by $\tilde Q$ acts on them by $\mathsf M_2^Q(\tilde Q)$, not diagonally.

### Case 7: $\bigl(1-\tfrac{i}{2}\bigr)e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z$

**The four basis elements.** $B=\sqrt{i+\tfrac14}$ and $\vec\Xi=-i\vec Q/B$, so
$$
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\vec W=\frac{\vec Q\times\vec e_x}{|\vec Q\times\vec e_x|}=i\vec e_y-\sqrt2\,\vec e_z,\qquad
\vec\Upsilon_\pm=-i\,\vec W\tilde\Pi_\pm,
$$
where $\vec W\cdot\vec Q=0$ and $\vec W\cdot\vec W=1$; then $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** $\tilde Q=\bigl(1-\tfrac{i}{2}\bigr)e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ with $\lambda_\pm=1-\tfrac{i}{2}\pm iB$, so $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q_2=\tilde Q$ the coordinates are $(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22})=(\lambda_+,0,0,\lambda_-)$.

### Case 8: $(1+i)e_t+\vec e_x+i\vec e_y$

**The four basis elements.** $B=0$, so there is no eigenbasis. The fixed Peirce basis of the algebra is
$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),\quad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),
$$
with $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\vec\Upsilon_\pm^2=0$,
$\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$.

**The eigenvalue decomposition.** The eigenvalue is $\lambda_+=1+i$, double, and
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}1+i&-2i\\0&1+i\end{pmatrix}=(1+i)\mathrm I_2+\begin{pmatrix}0&-2i\\0&0\end{pmatrix},
$$
and the second matrix is square-zero. The element is not diagonalisable and no eigenbasis exists.

**The spinor spaces and a general element.** $S_+=\mathbb B\tilde\Pi_+=\mathbb C\tilde\Pi_+\oplus\mathbb C\vec\Upsilon_+$
and $S_-=\mathbb B\tilde\Pi_-=\mathbb C\vec\Upsilon_-\oplus\mathbb C\tilde\Pi_-$,
and a general element of $\mathbb B$ is
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad
\mathsf M_2^Q(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The first column $(Q_{2,11},Q_{2,21})$ is a spinor of first chirality,
$Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$; the second column
$(Q_{2,12},Q_{2,22})$ is a spinor of second chirality,
$Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$.
For $\tilde Q$ itself the two columns are $(1+i,0)$ and $(-2i,1+i)$; left multiplication by $\tilde Q$ acts on them by $\mathsf M_2^Q(\tilde Q)$, not diagonally.

## Summary

- The eigenbasis depends on the element through its root $\vec\Xi$; the two idempotents change from case to case, unlike the fixed idempotents of the split-complex and reduced-biquaternion layers.
- In every case with $B\neq0$ the eigenvalues are $\lambda_\pm=Q_t\pm iB$, the Peirce components of $\tilde Q$ are $\lambda_+\tilde\Pi_+$ and $\lambda_-\tilde\Pi_-$; these are the two columns of the diagonal matrix.
- In case 1 the element is the identity, every pair of complementary idempotents is an eigenbasis, and the two spinor spaces can be any pair of minimal ideals.
- In cases 6 and 8 the vector part is null, $B=0$: there is no eigenbasis, no normalized nilpotent pair and no spinor decomposition attached to $\tilde Q$, and the multiplication is a single Jordan block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\vec\Xi=-i\vec Q/B$ | the two idempotents |
| $\vec\Upsilon_\pm$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ | the normalized nilpotents |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor spaces, minimal left ideals |
| $\xi_+=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$, $\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$ | the two spinors, elements of $S_+$ and $S_-$ |
| $\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-$ | the general element; its two columns are the two spinors |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mathsf M_2^{Q}$ | the $2\times2$ model in the eigenbasis |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Biquaternions](worked-examples-of-exponential-polar-decomposition-of-biquaternions.html), for the polar decomposition, its word and its check.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the relation between the two decompositions in the noncommutative case.
