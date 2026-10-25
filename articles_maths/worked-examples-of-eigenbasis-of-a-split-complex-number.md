# __Worked Examples of Eigenbasis of a Split-Complex Number__

## Introduction

This article computes the eigenvalue decomposition and the eigenbasis of eight split-complex numbers, one after another. The eight elements are those of *Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers*, so that the spectral data and the polar data can be read side by side. The decomposition, the eigenprojections and the eigenbasis are those of *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*; no definition or proof is repeated.

Each case is read from the two real coordinates $q$ and $q'$ of $Q=q+jq'$. The eigenvalues, the eigenprojections, the eigenbasis, the matrix of left multiplication and its diagonal form are computed from them by the formulas of §*The Method*. The eigenbasis is checked by the two identities

$$
Q\Pi_+=\lambda_+\Pi_+,
\qquad
Q\Pi_-=\lambda_-\Pi_-.
$$

The eight cases cover the four open components, the discrete unit, the two scalars and the zero divisor.

| Group | Case | Spectral reading |
|---|---|---|
| Future cone | $5+3j$ | $\lambda_+ = 8$, $\lambda_- = 2$ |
| Right wedge | $3+5j$ | $\lambda_+ = 8$, $\lambda_- = -2$ |
| Past cone | $-5-3j$ | $\lambda_+ = -8$, $\lambda_- = -2$ |
| Left wedge | $1-2j$ | $\lambda_+ = -1$, $\lambda_- = 3$ |
| Discrete unit | $j$ | $\lambda_+ = 1$, $\lambda_- = -1$ |
| Positive scalar | $2$ | $\lambda_+ = \lambda_- = 2$ |
| Negative scalar | $-2$ | $\lambda_+ = \lambda_- = -2$ |
| Null cone | $1+j$ | $\lambda_+ = 2$, $\lambda_- = 0$ |

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its coordinates, its eigenvalues, its eigenprojections, its eigenbasis and its matrix. The summary collects the results in three tables and reads the patterns across the cases (§*Summary*).

## The Method

### The Coordinates and the Spectrum

For $Q=q+jq'$ the two real coordinates are $q$ and $q'$. The two eigenvalues are the idempotent coordinates

$$
\lambda_+=q+q'=Q_+,
\qquad
\lambda_-=q-q'=Q_-.
$$

Their sum and product are

$$
\lambda_++\lambda_-=2q,
\qquad
\lambda_+\lambda_-=q^2-q'^2=\langle Q\rangle_{*}.
$$

The eigenvalues are distinct exactly when $q'\neq0$, because

$$
\lambda_+-\lambda_-=2q'.
$$

The characteristic polynomial is

$$
p_Q(X)=X^2-2qX+(q^2-q'^2)=(X-\lambda_+)(X-\lambda_-),
$$

with discriminant $4q'^2$. The element is a unit exactly when $\lambda_+\lambda_-\neq0$.

### The Eigenprojections

The two eigenprojections are the fixed idempotents

$$
\Pi_+=\frac12(1+j),
\qquad
\Pi_-=\frac12(1-j).
$$

They are idempotent, orthogonal and complete:

$$
\Pi_+^2=\Pi_+,
\qquad
\Pi_-^2=\Pi_-,
\qquad
\Pi_+\Pi_-=\Pi_-\Pi_+=0,
\qquad
\Pi_++\Pi_-=1.
$$

For every $Q$ with $q'\neq0$,

$$
Q\Pi_+=\lambda_+\Pi_+,
\qquad
Q\Pi_-=\lambda_-\Pi_-,
$$

and the eigenvalue decomposition is

$$
Q=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

The Peirce corners relative to $\Pi_+$ are

$$
\mathbb{D}_{++}=\mathbb{R}\Pi_+,
\qquad
\mathbb{D}_{--}=\mathbb{R}\Pi_-,
\qquad
\mathbb{D}_{+-}=\mathbb{D}_{-+}=0.
$$

The two mixed corners vanish because the algebra is commutative. The eigenvalue decomposition is therefore the Peirce decomposition read on the element, and the two Peirce coordinates of $Q$ are its two eigenvalues.

### The Eigenbasis

The pair $(\Pi_+,\Pi_-)$ is a basis of $\mathbb{D}$, and in this basis multiplication by $Q$ is diagonal:

$$
Q\Pi_+=\lambda_+\Pi_+,
\qquad
Q\Pi_-=\lambda_-\Pi_-.
$$

A general element $P=p_0+p_1j$ has eigenbasis coordinates

$$
P=(p_0+p_1)\Pi_++(p_0-p_1)\Pi_-,
$$

so

$$
P\longleftrightarrow(p_0+p_1,\,p_0-p_1).
$$

For $Q$ itself the coordinates are $(\lambda_+,\lambda_-)$. The two spinor spaces are the two coordinate axes,

$$
S_+=\mathbb{R}\Pi_+,
\qquad
S_-=\mathbb{R}\Pi_-,
$$

and a spinor of first chirality is $\xi_+=a_1\Pi_+$, with coordinates $(a_1,0)$, while a spinor of second chirality is $\xi_-=a_2\Pi_-$, with coordinates $(0,a_2)$.

When $q'\neq0$ the eigenvalues are distinct, and every eigenbasis is

$$
(\alpha\Pi_+,\beta\Pi_-),
\qquad
\alpha,\beta\in\mathbb{R}^{\times}.
$$

The pair $(\Pi_+,\Pi_-)$ is the normalised choice $\alpha=\beta=1$.

### The Matrix Picture

In the basis $(1,j)$ the matrix of multiplication by $Q$ is

$$
M_Q=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$

with trace $2q$ and determinant $q^2-q'^2=\lambda_+\lambda_-$. The change to the eigenbasis has columns the coordinate vectors of $\Pi_+$ and $\Pi_-$:

$$
C=\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{pmatrix},
\qquad
C^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

Then

$$
C^{-1}M_QC=\operatorname{diag}(\lambda_+,\lambda_-).
$$

The two columns of $C$ are the two spinor spaces in coordinates.

### Powers, Inverse and Polynomials

The eigenbasis gives every power and every polynomial by the same rule:

$$
Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-,
\qquad
f(Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-.
$$

When $Q$ is a unit,

$$
Q^{-1}=\lambda_+^{-1}\Pi_++\lambda_-^{-1}\Pi_-.
$$

The norm reads $\langle Q\rangle_{*}=\lambda_+\lambda_-$ and the trace reads $2q=\lambda_++\lambda_-$.

### The Three Regimes

The spectral behaviour is fixed by the pair $(q,q')$.

| Regime | Condition | Spectrum | Eigenbasis |
|---|---|---|---|
| Distinct | $q'\neq0$ | $\lambda_+\neq\lambda_-$ | $(\Pi_+,\Pi_-)$, unique up to two scales |
| Scalar | $q'=0$ | $\lambda_+=\lambda_-=q$ | every basis; $(\Pi_+,\Pi_-)$ is a choice |
| Zero divisor | $q'\neq0$, $q^2-q'^2=0$ | $\{2q,0\}$ | $(\Pi_+,\Pi_-)$ still exists |

The scalar regime is the only one in which the eigenbasis fails to be determined by $Q$. The zero-divisor regime is distinct: the two eigenvalues are different, the eigenbasis exists, but one eigenvalue is zero, so $Q$ is not invertible. Case 8 is this regime.

## The Eight Cases

### Case 1: A Generic Element of the Future Cone

**Coordinates.** For $Q=5+3j$,

$$
q=5,
\qquad
q'=3,
\qquad
\lambda_+=8,
\qquad
\lambda_-=2,
\qquad
\langle Q\rangle_{*}=16.
$$

**Eigenprojections.** The projectors are $\Pi_\pm=\tfrac12(1\pm j)$, and

$$
Q\Pi_+=8\Pi_+,
\qquad
Q\Pi_-=2\Pi_-.
$$

Therefore

$$
Q=8\Pi_++2\Pi_-.
$$

**Eigenbasis and matrix.** In the eigenbasis the coordinates of $Q$ are $(8,2)$, and

$$
M_Q=\begin{pmatrix}5&3\\3&5\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}8&0\\0&2\end{pmatrix}.
$$

The trace is $10=8+2$ and the determinant is $16=8\cdot2$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=5+3j$ one has $a_1=\lambda_+=8$ and $a_2=\lambda_-=2$, so
$$
\mathsf M(Q)=\begin{pmatrix}8&0\\0&2\end{pmatrix}=\begin{pmatrix}8&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&2\end{pmatrix}.
$$

**Consequences.** The square is

$$
Q^2=64\Pi_++4\Pi_-=34+30j,
$$

the cube is

$$
Q^3=512\Pi_++8\Pi_-=260+252j,
$$

and the inverse is

$$
Q^{-1}=\frac18\Pi_++\frac12\Pi_-=\frac{5-3j}{16}.
$$

### Case 2: A Generic Element of the Right Wedge

**Coordinates.** For $Q=3+5j$,

$$
q=3,
\qquad
q'=5,
\qquad
\lambda_+=8,
\qquad
\lambda_-=-2,
\qquad
\langle Q\rangle_{*}=-16.
$$

**Eigenprojections.** The same projectors give

$$
Q\Pi_+=8\Pi_+,
\qquad
Q\Pi_-=-2\Pi_-,
$$

hence

$$
Q=8\Pi_+-2\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(8,-2)$, and

$$
M_Q=\begin{pmatrix}3&5\\5&3\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}8&0\\0&-2\end{pmatrix}.
$$

The trace is $6=8-2$ and the determinant is $-16=8\cdot(-2)$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=3+5j$ one has $a_1=\lambda_+=8$ and $a_2=\lambda_-=-2$, so
$$
\mathsf M(Q)=\begin{pmatrix}8&0\\0&-2\end{pmatrix}=\begin{pmatrix}8&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-2\end{pmatrix}.
$$

**Consequences.** The square is again

$$
Q^2=64\Pi_++4\Pi_-=34+30j,
$$

the cube is

$$
Q^3=512\Pi_+-8\Pi_-=252+260j,
$$

and the inverse is

$$
Q^{-1}=\frac18\Pi_+-\frac12\Pi_-=\frac{-3+5j}{16}.
$$

### Case 3: A Generic Element of the Past Cone

**Coordinates.** For $Q=-5-3j$,

$$
q=-5,
\qquad
q'=-3,
\qquad
\lambda_+=-8,
\qquad
\lambda_-=-2,
\qquad
\langle Q\rangle_{*}=16.
$$

**Eigenprojections.** The action is

$$
Q\Pi_+=-8\Pi_+,
\qquad
Q\Pi_-=-2\Pi_-,
$$

so

$$
Q=-8\Pi_+-2\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(-8,-2)$, and

$$
M_Q=\begin{pmatrix}-5&-3\\-3&-5\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}-8&0\\0&-2\end{pmatrix}.
$$

The trace is $-10=-8-2$ and the determinant is $16=(-8)(-2)$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=-5-3j$ one has $a_1=\lambda_+=-8$ and $a_2=\lambda_-=-2$, so
$$
\mathsf M(Q)=\begin{pmatrix}-8&0\\0&-2\end{pmatrix}=\begin{pmatrix}-8&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-2\end{pmatrix}.
$$

**Consequences.** The square is

$$
Q^2=64\Pi_++4\Pi_-=34+30j,
$$

the cube is

$$
Q^3=-512\Pi_+-8\Pi_-=-260-252j,
$$

and the inverse is

$$
Q^{-1}=-\frac18\Pi_+-\frac12\Pi_-=\frac{-5+3j}{16}.
$$

### Case 4: A Generic Element of the Left Wedge

**Coordinates.** For $Q=1-2j$,

$$
q=1,
\qquad
q'=-2,
\qquad
\lambda_+=-1,
\qquad
\lambda_-=3,
\qquad
\langle Q\rangle_{*}=-3.
$$

**Eigenprojections.** The action is

$$
Q\Pi_+=-\Pi_+,
\qquad
Q\Pi_-=3\Pi_-,
$$

so

$$
Q=-\Pi_++3\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(-1,3)$, and

$$
M_Q=\begin{pmatrix}1&-2\\-2&1\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}-1&0\\0&3\end{pmatrix}.
$$

The trace is $2=-1+3$ and the determinant is $-3=(-1)\cdot3$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=1-2j$ one has $a_1=\lambda_+=-1$ and $a_2=\lambda_-=3$, so
$$
\mathsf M(Q)=\begin{pmatrix}-1&0\\0&3\end{pmatrix}=\begin{pmatrix}-1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&3\end{pmatrix}.
$$

**Consequences.** The square is

$$
Q^2=\Pi_++9\Pi_-=5-4j,
$$

the cube is

$$
Q^3=-\Pi_++27\Pi_-=13-14j,
$$

and the inverse is

$$
Q^{-1}=-\Pi_++\frac13\Pi_-=\frac{-1-2j}{3}.
$$

### Case 5: The Discrete Unit

**Coordinates.** For $Q=j$,

$$
q=0,
\qquad
q'=1,
\qquad
\lambda_+=1,
\qquad
\lambda_-=-1,
\qquad
\langle Q\rangle_{*}=-1.
$$

**Eigenprojections.** The action is

$$
Q\Pi_+=\Pi_+,
\qquad
Q\Pi_-=-\Pi_-,
$$

so

$$
Q=\Pi_+-\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(1,-1)$, and

$$
M_Q=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

The trace is $0$ and the determinant is $-1$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=j$ one has $a_1=\lambda_+=1$ and $a_2=\lambda_-=-1$, so
$$
\mathsf M(Q)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
$$

**Consequences.** The element is an involution,

$$
Q^2=\Pi_++\Pi_-=1,
\qquad
Q^{-1}=Q=j.
$$

The eigenbasis is the pair of null lines spanned by $\Pi_+$ and $\Pi_-$, and the two eigenvalues are $+1$ and $-1$.

### Case 6: The Positive Scalar

**Coordinates.** For $Q=2$,

$$
q=2,
\qquad
q'=0,
\qquad
\lambda_+=\lambda_-=2,
\qquad
\langle Q\rangle_{*}=4.
$$

**The scalar regime.** The two eigenvalues coincide. The operator is $L_Q=2\,\mathrm{id}$, every nonzero vector is an eigenvector, and every basis is an eigenbasis. The idempotent basis $(\Pi_+,\Pi_-)$ is a choice, not a consequence of $Q$:

$$
Q=2\Pi_++2\Pi_-=2(\Pi_++\Pi_-).
$$

**Eigenbasis and matrix.** In the chosen eigenbasis the coordinates are $(2,2)$, and

$$
M_Q=2I_2,
\qquad
C^{-1}M_QC=\begin{pmatrix}2&0\\0&2\end{pmatrix}.
$$

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=2$ one has $a_1=\lambda_+=2$ and $a_2=\lambda_-=2$, so
$$
\mathsf M(Q)=\begin{pmatrix}2&0\\0&2\end{pmatrix}=\begin{pmatrix}2&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&2\end{pmatrix}.
$$ The two eigenvalues coincide: the two spinor lines carry the same scale, and the pair $(\Pi_+,\Pi_-)$ is a choice.

**Consequences.** $Q^2=4$ and $Q^{-1}=\tfrac12$. The two spinor spaces are still the two coordinate axes, but $Q$ acts on both by the same scalar.

### Case 7: The Negative Scalar

**Coordinates.** For $Q=-2$,

$$
q=-2,
\qquad
q'=0,
\qquad
\lambda_+=\lambda_-=-2,
\qquad
\langle Q\rangle_{*}=4.
$$

**The scalar regime.** Again every basis is an eigenbasis, and the idempotent pair is a choice:

$$
Q=-2\Pi_+-2\Pi_-=-2(\Pi_++\Pi_-).
$$

**Eigenbasis and matrix.** In the chosen eigenbasis the coordinates are $(-2,-2)$, and

$$
M_Q=-2I_2,
\qquad
C^{-1}M_QC=\begin{pmatrix}-2&0\\0&-2\end{pmatrix}.
$$

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=-2$ one has $a_1=\lambda_+=-2$ and $a_2=\lambda_-=-2$, so
$$
\mathsf M(Q)=\begin{pmatrix}-2&0\\0&-2\end{pmatrix}=\begin{pmatrix}-2&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-2\end{pmatrix}.
$$ The two eigenvalues coincide: the two spinor lines carry the same scale, and the pair $(\Pi_+,\Pi_-)$ is a choice.

**Consequences.** $Q^2=4$ and $Q^{-1}=-\tfrac12$. Cases 6 and 7 have the same square and opposite inverses; the eigenbasis does not distinguish them, because in the scalar regime it is not attached to the element.

### Case 8: The Zero Divisor

**Coordinates.** For $Q=1+j$,

$$
q=1,
\qquad
q'=1,
\qquad
\lambda_+=2,
\qquad
\lambda_-=0,
\qquad
\langle Q\rangle_{*}=0.
$$

**Eigenprojections.** The eigenvalues are distinct, because $q'=1\neq0$, and the fixed projectors are the eigenprojections:

$$
Q\Pi_+=2\Pi_+,
\qquad
Q\Pi_-=0.
$$

Therefore

$$
Q=2\Pi_+.
$$

The element is a zero divisor, yet it has an eigenbasis. The two properties are independent: diagonalisability is not invertibility.

**Eigenbasis and matrix.** The eigenbasis coordinates are $(2,0)$, and

$$
M_Q=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
C^{-1}M_QC=\begin{pmatrix}2&0\\0&0\end{pmatrix}.
$$

The matrix has rank one and determinant zero. Its image is the line of $\Pi_+$ and its kernel is the line of $\Pi_-$.

**Spinors.** A spinor of first chirality is $\xi_+=a_1\Pi_+$ with $a_1\in\mathbb{R}$, and a spinor of second chirality is $\xi_-=a_2\Pi_-$ with $a_2\in\mathbb{R}$. A general element is $Q_{\mathrm{sp}}=a_1\Pi_++a_2\Pi_-$, with matrix
$$
\mathsf M(Q_{\mathrm{sp}})=\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}a_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&a_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(QX)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}a_1&0\\0&a_2\end{pmatrix},
$$
that is $a_1\mapsto\lambda_+a_1$ and $a_2\mapsto\lambda_-a_2$. In the special case $Q=1+j$ one has $a_1=\lambda_+=2$ and $a_2=\lambda_-=0$, so
$$
\mathsf M(Q)=\begin{pmatrix}2&0\\0&0\end{pmatrix}=\begin{pmatrix}2&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$ The second spinor vanishes, its column is zero, and the matrix has rank one.

**Consequences.** The powers are

$$
Q^n=2^n\Pi_+=2^{n-1}Q,
\qquad n\geq1,
$$

and in particular $Q^2=2Q=2+2j$. There is no inverse. The two spinor spaces read the element exactly: $Q$ acts on $S_+$ by the scalar $2$ and kills $S_-$.

## Summary

### Main Results

| Case | $Q$ | $q$ | $q'$ | $\lambda_+$ | $\lambda_-$ | $\langle Q\rangle_{*}$ | Eigenbasis |
|---|---|---|---|---|---|---|---|
| $1$ | $5+3j$ | $5$ | $3$ | $8$ | $2$ | $16$ | yes |
| $2$ | $3+5j$ | $3$ | $5$ | $8$ | $-2$ | $-16$ | yes |
| $3$ | $-5-3j$ | $-5$ | $-3$ | $-8$ | $-2$ | $16$ | yes |
| $4$ | $1-2j$ | $1$ | $-2$ | $-1$ | $3$ | $-3$ | yes |
| $5$ | $j$ | $0$ | $1$ | $1$ | $-1$ | $-1$ | yes |
| $6$ | $2$ | $2$ | $0$ | $2$ | $2$ | $4$ | every basis |
| $7$ | $-2$ | $-2$ | $0$ | $-2$ | $-2$ | $4$ | every basis |
| $8$ | $1+j$ | $1$ | $1$ | $2$ | $0$ | $0$ | yes |

### The Eigenbasis Table

| Case | $\Pi_+$ coordinate | $\Pi_-$ coordinate | $Q\Pi_+$ | $Q\Pi_-$ | Diagonal form |
|---|---|---|---|---|---|
| $1$ | $8$ | $2$ | $8\Pi_+$ | $2\Pi_-$ | $\operatorname{diag}(8,2)$ |
| $2$ | $8$ | $-2$ | $8\Pi_+$ | $-2\Pi_-$ | $\operatorname{diag}(8,-2)$ |
| $3$ | $-8$ | $-2$ | $-8\Pi_+$ | $-2\Pi_-$ | $\operatorname{diag}(-8,-2)$ |
| $4$ | $-1$ | $3$ | $-\Pi_+$ | $3\Pi_-$ | $\operatorname{diag}(-1,3)$ |
| $5$ | $1$ | $-1$ | $\Pi_+$ | $-\Pi_-$ | $\operatorname{diag}(1,-1)$ |
| $6$ | $2$ | $2$ | $2\Pi_+$ | $2\Pi_-$ | $\operatorname{diag}(2,2)$ |
| $7$ | $-2$ | $-2$ | $-2\Pi_+$ | $-2\Pi_-$ | $\operatorname{diag}(-2,-2)$ |
| $8$ | $2$ | $0$ | $2\Pi_+$ | $0$ | $\operatorname{diag}(2,0)$ |

### Powers, Inverses and Matrices

| Case | $Q^2$ | $Q^{-1}$ | $M_Q$ | $\mathrm{tr}\,M_Q$ | $\det M_Q$ |
|---|---|---|---|---|---|
| $1$ | $34+30j$ | $\dfrac{5-3j}{16}$ | $\begin{pmatrix}5&3\\3&5\end{pmatrix}$ | $10$ | $16$ |
| $2$ | $34+30j$ | $\dfrac{-3+5j}{16}$ | $\begin{pmatrix}3&5\\5&3\end{pmatrix}$ | $6$ | $-16$ |
| $3$ | $34+30j$ | $\dfrac{-5+3j}{16}$ | $\begin{pmatrix}-5&-3\\-3&-5\end{pmatrix}$ | $-10$ | $16$ |
| $4$ | $5-4j$ | $\dfrac{-1-2j}{3}$ | $\begin{pmatrix}1&-2\\-2&1\end{pmatrix}$ | $2$ | $-3$ |
| $5$ | $1$ | $j$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $0$ | $-1$ |
| $6$ | $4$ | $\tfrac12$ | $2I_2$ | $4$ | $4$ |
| $7$ | $4$ | $-\tfrac12$ | $-2I_2$ | $-4$ | $4$ |
| $8$ | $2+2j$ | none | $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | $2$ | $0$ |

### What the Cases Show

- Cases 1 to 3 share the square $34+30j$. Their eigenvalues are $(8,2)$, $(8,-2)$ and $(-8,-2)$; the eigenbasis is the same pair of idempotents, and only the two eigenvalues change. The sign pattern of the eigenvalues, not the element, carries the component.
- Case 4 has a negative eigenvalue and a positive one, with a negative norm. Its angle in the polar reading is negative, and its eigenbasis is again the same pair.
- Case 5 is the pure discrete unit. Its eigenvalues are $+1$ and $-1$, and its square is the identity.
- Cases 6 and 7 are the scalar regime. The two eigenvalues coincide, every basis is an eigenbasis, and the idempotent pair is a choice. The spectral data cannot distinguish the two elements beyond the common value of the scalar.
- Case 8 is the zero divisor. The eigenvalues are distinct, the eigenbasis exists, and one eigenvalue is zero. This is the case in which the eigenbasis exists while the polar word of the companion article does not. The element is the projection $2\Pi_+$ onto the first spinor space, with kernel the second.
- The eigenbasis depends only on $j$, not on $Q$, in every non-scalar case. The element enters only through the two eigenvalues. This is the two-dimensional form of the statement that the eigenbasis is attached to the root and not to the scale.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $\lambda_\pm=q\pm q'$ | the two eigenvalues |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two eigenprojections |
| $\mathbb{D}_{\sigma\tau}$ | the Peirce corners |
| $S_\pm=\mathbb{R}\Pi_\pm$ | the two spinor spaces |
| $M_Q$ | the matrix of multiplication by $Q$ in the basis $(1,j)$ |
| $C$ | the change to the eigenbasis |
| $\langle Q\rangle_{*}=q^2-q'^2$ | the split-complex norm |

## Further Reading

- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the eigenvalue decomposition, the Peirce decomposition and the eigenbasis.
- [Eigenbasis of a Split-Complex Number in Matrix Elements Representations](eigenbasis-of-a-split-complex-number-in-matrix-elements-representations.html), for the matrix model, the spectral projectors and the change of basis.
- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the same eight elements read through the polar word.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-split-complex-numbers.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Worked Examples of Eigenbasis a Reduced Biquaternion](worked-examples-of-eigenbasis-a-reduced-biquaternion.html), for the four-dimensional commutative companion.
- [Worked Examples of Eigenbasis of a Biquaternion](worked-examples-of-eigenbasis-of-a-biquaternion.html), for the noncommutative companion with nilpotents.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the ideals and the Peirce corners.
- [Split-Complex Exponential and Lie Group Structure](split-complex-exponential-and-lie-group-structure.html), for the exponential and the logarithm built on the decomposition.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic geometry of the split-complex plane.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation used throughout.
