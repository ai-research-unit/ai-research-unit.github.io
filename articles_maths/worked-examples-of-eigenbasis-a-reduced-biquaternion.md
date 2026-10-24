# __Worked Examples of Eigenbasis a Reduced Biquaternion__

## Introduction

This article computes the eigenvalue decomposition and the eigenbasis of eight reduced biquaternions, one after another. The eight elements are those of *Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions*, so that the spectral data and the polar data can be read side by side. The decomposition, the eigenprojections and the eigenbasis are those of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*; no definition or proof is repeated.

Each case is read from the two complex coordinates $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$ of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$. The eigenvalues, the eigenprojections, the eigenbasis, the matrix of multiplication and its diagonal form are computed from them by the formulas of §*The Method*. The eigenbasis is checked by the two identities

$$
\breve Q\Pi_+=\lambda_+\Pi_+,
\qquad
\breve Q\Pi_-=\lambda_-\Pi_-.
$$

The eight cases cover the generic element, the complex scalar, the two pure phases, the boundary of the principal diamond, the hyperbolic line, the central discrete element and the zero divisor.

| Group | Case | Spectral reading |
|---|---|---|
| Generic | $3+4i+j(1-i)$ | $\lambda_+=4+3i$, $\lambda_-=2+5i$ |
| Complex scalar | $1+i$ | $\lambda_+= \lambda_-=1+i$ |
| Central phase | $i$ | $\lambda_+=\lambda_-=i$ |
| Split phase | $ij$ | $\lambda_+=i$, $\lambda_-=-i$ |
| Boundary of the diamond | $j$ | $\lambda_+=1$, $\lambda_-=-1$ |
| Hyperbolic line | $\exp(j\ln2)=\tfrac54+\tfrac34j$ | $\lambda_+=2$, $\lambda_-=\tfrac12$ |
| Central discrete | $-1$ | $\lambda_+=\lambda_-=-1$ |
| Zero divisor | $1+j$ | $\lambda_+=2$, $\lambda_-=0$ |

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its components, its eigenvalues, its eigenprojections, its eigenbasis and its matrix. The summary collects the results in three tables and reads the patterns across the cases (§*Summary*).

## The Method

### The Coordinates and the Spectrum

For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ the two complex coordinates are

$$
Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},
\qquad
Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}.
$$

The two eigenvalues are the idempotent coordinates

$$
\lambda_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\qquad
\lambda_-=Q_{\blacktriangle}-Q_{\blacktriangledown}.
$$

Their sum and product are

$$
\lambda_++\lambda_-=2Q_{\blacktriangle},
\qquad
\lambda_+\lambda_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2
=\langle\breve Q\rangle_{\mathrm{ts}}.
$$

The eigenvalues are distinct exactly when $Q_{\blacktriangledown}\neq0$, because

$$
\lambda_+-\lambda_-=2Q_{\blacktriangledown}.
$$

The characteristic polynomial is

$$
p_{\breve Q}(X)=X^2-2Q_{\blacktriangle}X+(Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2)
=(X-\lambda_+)(X-\lambda_-),
$$

with discriminant $4Q_{\blacktriangledown}^2$. The element is a unit exactly when $\lambda_+\lambda_-\neq0$.

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

For every $\breve Q$ with $Q_{\blacktriangledown}\neq0$,

$$
\breve Q\Pi_+=\lambda_+\Pi_+,
\qquad
\breve Q\Pi_-=\lambda_-\Pi_-,
$$

and the eigenvalue decomposition is

$$
\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

The Peirce corners relative to $\Pi_+$ are

$$
\mathbb{B}_{\mathrm{r},++}=\mathbb{C}\Pi_+,
\qquad
\mathbb{B}_{\mathrm{r},--}=\mathbb{C}\Pi_-,
\qquad
\mathbb{B}_{\mathrm{r},+-}=\mathbb{B}_{\mathrm{r},-+}=0.
$$

The mixed corners vanish because the idempotents are central. The eigenvalue decomposition is the Peirce decomposition read on the element, and the two Peirce coordinates of $\breve Q$ are its two eigenvalues.

### The Eigenbasis

The pair $(\Pi_+,\Pi_-)$ is a $\mathbb{C}$-basis of $\mathbb{B}_{\mathrm{r}}$, and in this basis multiplication by $\breve Q$ is diagonal:

$$
\breve Q\Pi_+=\lambda_+\Pi_+,
\qquad
\breve Q\Pi_-=\lambda_-\Pi_-.
$$

A general element $\breve P=P_{\blacktriangle}+jP_{\blacktriangledown}$ has eigenbasis coordinates

$$
\breve P=(P_{\blacktriangle}+P_{\blacktriangledown})\Pi_++(P_{\blacktriangle}-P_{\blacktriangledown})\Pi_-,
$$

so

$$
\breve P\longleftrightarrow(P_{\blacktriangle}+P_{\blacktriangledown},\,P_{\blacktriangle}-P_{\blacktriangledown}).
$$

For $\breve Q$ itself the coordinates are $(\lambda_+,\lambda_-)$. The two spinor spaces are the two complex lines

$$
S_+=\mathbb{C}\Pi_+,
\qquad
S_-=\mathbb{C}\Pi_-,
$$

and a spinor of first chirality is $\xi_+=A_1\Pi_+$, with coordinates $(A_1,0)$, while a spinor of second chirality is $\xi_-=A_2\Pi_-$, with coordinates $(0,A_2)$, with $A_1,A_2\in\mathbb{C}$.

When $Q_{\blacktriangledown}\neq0$ the eigenvalues are distinct, and every eigenbasis is

$$
(\alpha\Pi_+,\beta\Pi_-),
\qquad
\alpha,\beta\in\mathbb{C}^{\times}.
$$

The pair $(\Pi_+,\Pi_-)$ is the normalised choice $\alpha=\beta=1$.

### The Matrix Picture

In the basis $(1,j)$ the matrix of multiplication by $\breve Q$ is

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
Q_{\blacktriangle}&Q_{\blacktriangledown}\\
Q_{\blacktriangledown}&Q_{\blacktriangle}
\end{pmatrix},
$$

with trace $2Q_{\blacktriangle}$ and determinant $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=\lambda_+\lambda_-$. The change to the eigenbasis is the same fixed matrix as in the split-complex case:

$$
C=\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{pmatrix},
\qquad
C^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

Then

$$
C^{-1}\mathsf M(\breve Q)C=\operatorname{diag}(\lambda_+,\lambda_-).
$$

The two columns of $C$ are the two spinor spaces in coordinates.

### Powers, Inverse and Polynomials

The eigenbasis gives every power and every polynomial by the same rule:

$$
\breve Q^n=\lambda_+^n\Pi_++\lambda_-^n\Pi_-,
\qquad
f(\breve Q)=f(\lambda_+)\Pi_++f(\lambda_-)\Pi_-.
$$

When $\breve Q$ is a unit,

$$
\breve Q^{-1}=\lambda_+^{-1}\Pi_++\lambda_-^{-1}\Pi_-.
$$

The reduced norm reads $\langle\breve Q\rangle_{\mathrm{ts}}=\lambda_+\lambda_-$ and the trace reads $2Q_{\blacktriangle}=\lambda_++\lambda_-$.

### The Three Regimes

| Regime | Condition | Spectrum | Eigenbasis |
|---|---|---|---|
| Distinct | $Q_{\blacktriangledown}\neq0$ | $\lambda_+\neq\lambda_-$ | $(\Pi_+,\Pi_-)$, unique up to two scales |
| Scalar | $Q_{\blacktriangledown}=0$ | $\lambda_+=\lambda_-=Q_{\blacktriangle}$ | every basis; $(\Pi_+,\Pi_-)$ is a choice |
| Zero divisor | $Q_{\blacktriangledown}\neq0$, $Q_{\blacktriangle}^2=Q_{\blacktriangledown}^2$ | $\{2Q_{\blacktriangle},0\}$ | $(\Pi_+,\Pi_-)$ still exists |

The scalar regime is the only one in which the eigenbasis fails to be determined by $\breve Q$. The zero-divisor regime is distinct: the two eigenvalues are different, the eigenbasis exists, but one eigenvalue is zero, so $\breve Q$ is not invertible. Case 8 is this regime.

## The Eight Cases

### Case 1: A Generic Element

**Components.** For $\breve Q=3+4i+j(1-i)$,

$$
Q_{\blacktriangle}=3+4i,
\qquad
Q_{\blacktriangledown}=1-i,
\qquad
\lambda_+=4+3i,
\qquad
\lambda_-=2+5i,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=-7+26i.
$$

**Eigenprojections.** The projectors are $\Pi_\pm=\tfrac12(1\pm j)$, and

$$
\breve Q\Pi_+=(4+3i)\Pi_+,
\qquad
\breve Q\Pi_-=(2+5i)\Pi_-.
$$

Therefore

$$
\breve Q=(4+3i)\Pi_++(2+5i)\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(4+3i,\,2+5i)$, and

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
3+4i&1-i\\
1-i&3+4i
\end{pmatrix},
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
4+3i&0\\
0&2+5i
\end{pmatrix}.
$$

The trace is $6+8i=2Q_{\blacktriangle}$ and the determinant is $-7+26i=(4+3i)(2+5i)$.

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=3+4i+j(1-i)$ one has $A_1=\lambda_+=4+3i$ and $A_2=\lambda_-=2+5i$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}4+3i&0\\0&2+5i\end{pmatrix}=\begin{pmatrix}4+3i&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&2+5i\end{pmatrix}.
$$

**Consequences.** The square is

$$
\breve Q^2=(4+3i)^2\Pi_++(2+5i)^2\Pi_-
=-7+22i+j(14+2i),
$$

and the inverse is

$$
\breve Q^{-1}=\frac{\Pi_+}{4+3i}+\frac{\Pi_-}{2+5i}
=\frac{83-106i+j(33+19i)}{725}.
$$

### Case 2: A Complex Scalar

**Components.** For $\breve Q=1+i$,

$$
Q_{\blacktriangle}=1+i,
\qquad
Q_{\blacktriangledown}=0,
\qquad
\lambda_+=\lambda_-=1+i,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=2i.
$$

**The scalar regime.** The two eigenvalues coincide. The operator is $L_{\breve Q}=(1+i)\,\mathrm{id}$, every nonzero vector is an eigenvector, and every complex basis is an eigenbasis. The idempotent basis is a choice:

$$
\breve Q=(1+i)\Pi_++(1+i)\Pi_-=(1+i)(\Pi_++\Pi_-).
$$

**Eigenbasis and matrix.** In the chosen eigenbasis the coordinates are $(1+i,\,1+i)$, and

$$
\mathsf M(\breve Q)=(1+i)I_2,
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
1+i&0\\
0&1+i
\end{pmatrix}.
$$

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=1+i$ one has $A_1=\lambda_+=1+i$ and $A_2=\lambda_-=1+i$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}1+i&0\\0&1+i\end{pmatrix}=\begin{pmatrix}1+i&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1+i\end{pmatrix}.
$$ The two eigenvalues coincide: the two spinor lines carry the same scale, and the pair $(\Pi_+,\Pi_-)$ is a choice.

**Consequences.** $\breve Q^2=2i$ and $\breve Q^{-1}=\tfrac{1-i}{2}$. The two spinor spaces are the two coordinate lines, and $\breve Q$ acts on both by the same complex scalar.

### Case 3: The Central Phase

**Components.** For $\breve Q=i$,

$$
Q_{\blacktriangle}=i,
\qquad
Q_{\blacktriangledown}=0,
\qquad
\lambda_+=\lambda_-=i,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=-1.
$$

**The scalar regime.** Again every basis is an eigenbasis, and the idempotent pair is a choice:

$$
\breve Q=i\Pi_++i\Pi_-=i(\Pi_++\Pi_-).
$$

**Eigenbasis and matrix.** In the chosen eigenbasis the coordinates are $(i,i)$, and

$$
\mathsf M(\breve Q)=iI_2,
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
i&0\\
0&i
\end{pmatrix}.
$$

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=i$ one has $A_1=\lambda_+=i$ and $A_2=\lambda_-=i$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}i&0\\0&i\end{pmatrix}=\begin{pmatrix}i&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&i\end{pmatrix}.
$$ The two eigenvalues coincide: the two spinor lines carry the same scale, and the pair $(\Pi_+,\Pi_-)$ is a choice.

**Consequences.** $\breve Q^2=-1$ and $\breve Q^{-1}=-i$. The element is the central complex phase of angle $\pi/2$.

### Case 4: The Split Phase

**Components.** For $\breve Q=ij$,

$$
Q_{\blacktriangle}=0,
\qquad
Q_{\blacktriangledown}=i,
\qquad
\lambda_+=i,
\qquad
\lambda_-=-i,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=1.
$$

**Eigenprojections.** The action is

$$
\breve Q\Pi_+=i\Pi_+,
\qquad
\breve Q\Pi_-=-i\Pi_-,
$$

so

$$
\breve Q=i\Pi_+-i\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(i,-i)$, and

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
0&i\\
i&0
\end{pmatrix},
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
i&0\\
0&-i
\end{pmatrix}.
$$

The trace is $0=i-i$ and the determinant is $1=i(-i)$.

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=ij$ one has $A_1=\lambda_+=i$ and $A_2=\lambda_-=-i$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=\begin{pmatrix}i&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-i\end{pmatrix}.
$$

**Consequences.** The element is a square root of $-1$:

$$
\breve Q^2=-1,
\qquad
\breve Q^{-1}=-\breve Q=-ij.
$$

The eigenvalues are the two imaginary units, and the eigenbasis separates them.

### Case 5: The Boundary of the Diamond

**Components.** For $\breve Q=j$,

$$
Q_{\blacktriangle}=0,
\qquad
Q_{\blacktriangledown}=1,
\qquad
\lambda_+=1,
\qquad
\lambda_-=-1,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=-1.
$$

**Eigenprojections.** The action is

$$
\breve Q\Pi_+=\Pi_+,
\qquad
\breve Q\Pi_-=-\Pi_-,
$$

so

$$
\breve Q=\Pi_+-\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(1,-1)$, and

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$

The trace is $0$ and the determinant is $-1$.

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=j$ one has $A_1=\lambda_+=1$ and $A_2=\lambda_-=-1$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
$$

**Consequences.** The element is an involution,

$$
\breve Q^2=\Pi_++\Pi_-=1,
\qquad
\breve Q^{-1}=\breve Q=j.
$$

The eigenbasis is the pair of null lines spanned by $\Pi_+$ and $\Pi_-$.

### Case 6: The Hyperbolic Line

**Components.** For $\breve Q=\exp(j\ln2)=\tfrac54+\tfrac34j$,

$$
Q_{\blacktriangle}=\tfrac54,
\qquad
Q_{\blacktriangledown}=\tfrac34,
\qquad
\lambda_+=2,
\qquad
\lambda_-=\tfrac12,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=1.
$$

**Eigenprojections.** The action is

$$
\breve Q\Pi_+=2\Pi_+,
\qquad
\breve Q\Pi_-=\tfrac12\Pi_-,
$$

so

$$
\breve Q=2\Pi_++\tfrac12\Pi_-.
$$

**Eigenbasis and matrix.** The eigenbasis coordinates are $(2,\tfrac12)$, and

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
\tfrac54&\tfrac34\\
\tfrac34&\tfrac54
\end{pmatrix},
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
2&0\\
0&\tfrac12
\end{pmatrix}.
$$

The trace is $\tfrac52=2+\tfrac12$ and the determinant is $1=2\cdot\tfrac12$.

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=\exp(j\ln2)=\tfrac54+\tfrac34j$ one has $A_1=\lambda_+=2$ and $A_2=\lambda_-=\tfrac12$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}2&0\\0&\tfrac12\end{pmatrix}=\begin{pmatrix}2&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&\tfrac12\end{pmatrix}.
$$

**Consequences.** The square is

$$
\breve Q^2=4\Pi_++\tfrac14\Pi_-=\tfrac{17}{8}+\tfrac{15}{8}j,
$$

and the inverse is

$$
\breve Q^{-1}=\tfrac12\Pi_++2\Pi_-=\tfrac54-\tfrac34j.
$$

### Case 7: The Central Discrete Element

**Components.** For $\breve Q=-1$,

$$
Q_{\blacktriangle}=-1,
\qquad
Q_{\blacktriangledown}=0,
\qquad
\lambda_+=\lambda_-=-1,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=1.
$$

**The scalar regime.** Every basis is an eigenbasis, and the idempotent pair is a choice:

$$
\breve Q=-\Pi_+-\Pi_-=-(\Pi_++\Pi_-).
$$

**Eigenbasis and matrix.** In the chosen eigenbasis the coordinates are $(-1,-1)$, and

$$
\mathsf M(\breve Q)=-I_2,
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
-1&0\\
0&-1
\end{pmatrix}.
$$

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=-1$ one has $A_1=\lambda_+=-1$ and $A_2=\lambda_-=-1$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=\begin{pmatrix}-1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&-1\end{pmatrix}.
$$ The two eigenvalues coincide: the two spinor lines carry the same scale, and the pair $(\Pi_+,\Pi_-)$ is a choice.

**Consequences.** $\breve Q^2=1$ and $\breve Q^{-1}=-1$. The element is the central discrete element of order two.

### Case 8: The Zero Divisor

**Components.** For $\breve Q=1+j$,

$$
Q_{\blacktriangle}=1,
\qquad
Q_{\blacktriangledown}=1,
\qquad
\lambda_+=2,
\qquad
\lambda_-=0,
\qquad
\langle\breve Q\rangle_{\mathrm{ts}}=0.
$$

**Eigenprojections.** The eigenvalues are distinct, because $Q_{\blacktriangledown}=1\neq0$, and the fixed projectors are the eigenprojections:

$$
\breve Q\Pi_+=2\Pi_+,
\qquad
\breve Q\Pi_-=0.
$$

Therefore

$$
\breve Q=2\Pi_+.
$$

The element is a zero divisor, yet it has an eigenbasis. The two properties are independent: diagonalisability is not invertibility.

**Eigenbasis and matrix.** The eigenbasis coordinates are $(2,0)$, and

$$
\mathsf M(\breve Q)=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
C^{-1}\mathsf M(\breve Q)C=
\begin{pmatrix}
2&0\\
0&0
\end{pmatrix}.
$$

The matrix has rank one and determinant zero. Its image is the line of $\Pi_+$ and its kernel is the line of $\Pi_-$.

**Spinors.** A spinor of first chirality is $\xi_+=A_1\Pi_+$ with $A_1\in\mathbb{C}$, and a spinor of second chirality is $\xi_-=A_2\Pi_-$ with $A_2\in\mathbb{C}$. A general element is $\breve Q_{\mathrm{sp}}=A_1\Pi_++A_2\Pi_-$, with matrix
$$
\mathsf M(\breve Q_{\mathrm{sp}})=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}
$$
in the eigenbasis $(\Pi_+,\Pi_-)$, so the two spinors have the matrices
$$
\mathsf M(\xi_+)=\begin{pmatrix}A_1&0\\0&0\end{pmatrix},
\qquad
\mathsf M(\xi_-)=\begin{pmatrix}0&0\\0&A_2\end{pmatrix};
$$
the first column is $\xi_+$ and the second is $\xi_-$. Multiplication by $\breve Q=\lambda_+\Pi_++\lambda_-\Pi_-$ acts on the two columns by
$$
\mathsf M(\breve Q\breve Q_{\mathrm{sp}})=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix},
$$
that is $A_1\mapsto\lambda_+A_1$ and $A_2\mapsto\lambda_-A_2$. In the special case $\breve Q=1+j$ one has $A_1=\lambda_+=2$ and $A_2=\lambda_-=0$, so
$$
\mathsf M(\breve Q)=\begin{pmatrix}2&0\\0&0\end{pmatrix}=\begin{pmatrix}2&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$ The second spinor vanishes, its column is zero, and the matrix has rank one.

**Consequences.** The powers are

$$
\breve Q^n=2^n\Pi_+=2^{n-1}\breve Q,
\qquad n\geq1,
$$

and in particular $\breve Q^2=2\breve Q=2+2j$. There is no inverse. The two spinor spaces read the element exactly: $\breve Q$ acts on $S_+$ by the scalar $2$ and kills $S_-$.

## Summary

### Main Results

| Case | $\breve Q$ | $Q_{\blacktriangle}$ | $Q_{\blacktriangledown}$ | $\lambda_+$ | $\lambda_-$ | $\langle\breve Q\rangle_{\mathrm{ts}}$ | Eigenbasis |
|---|---|---|---|---|---|---|---|
| $1$ | $3+4i+j(1-i)$ | $3+4i$ | $1-i$ | $4+3i$ | $2+5i$ | $-7+26i$ | yes |
| $2$ | $1+i$ | $1+i$ | $0$ | $1+i$ | $1+i$ | $2i$ | every basis |
| $3$ | $i$ | $i$ | $0$ | $i$ | $i$ | $-1$ | every basis |
| $4$ | $ij$ | $0$ | $i$ | $i$ | $-i$ | $1$ | yes |
| $5$ | $j$ | $0$ | $1$ | $1$ | $-1$ | $-1$ | yes |
| $6$ | $\tfrac54+\tfrac34j$ | $\tfrac54$ | $\tfrac34$ | $2$ | $\tfrac12$ | $1$ | yes |
| $7$ | $-1$ | $-1$ | $0$ | $-1$ | $-1$ | $1$ | every basis |
| $8$ | $1+j$ | $1$ | $1$ | $2$ | $0$ | $0$ | yes |

### The Eigenbasis Table

| Case | $\Pi_+$ coordinate | $\Pi_-$ coordinate | $\breve Q\Pi_+$ | $\breve Q\Pi_-$ | Diagonal form |
|---|---|---|---|---|---|
| $1$ | $4+3i$ | $2+5i$ | $(4+3i)\Pi_+$ | $(2+5i)\Pi_-$ | $\operatorname{diag}(4+3i,2+5i)$ |
| $2$ | $1+i$ | $1+i$ | $(1+i)\Pi_+$ | $(1+i)\Pi_-$ | $\operatorname{diag}(1+i,1+i)$ |
| $3$ | $i$ | $i$ | $i\Pi_+$ | $i\Pi_-$ | $\operatorname{diag}(i,i)$ |
| $4$ | $i$ | $-i$ | $i\Pi_+$ | $-i\Pi_-$ | $\operatorname{diag}(i,-i)$ |
| $5$ | $1$ | $-1$ | $\Pi_+$ | $-\Pi_-$ | $\operatorname{diag}(1,-1)$ |
| $6$ | $2$ | $\tfrac12$ | $2\Pi_+$ | $\tfrac12\Pi_-$ | $\operatorname{diag}(2,\tfrac12)$ |
| $7$ | $-1$ | $-1$ | $-\Pi_+$ | $-\Pi_-$ | $\operatorname{diag}(-1,-1)$ |
| $8$ | $2$ | $0$ | $2\Pi_+$ | $0$ | $\operatorname{diag}(2,0)$ |

### Powers, Inverses and Matrices

| Case | $\breve Q^2$ | $\breve Q^{-1}$ | $\mathsf M(\breve Q)$ | $\mathrm{tr}$ | $\det$ |
|---|---|---|---|---|---|
| $1$ | $-7+22i+j(14+2i)$ | $\dfrac{83-106i+j(33+19i)}{725}$ | $\begin{pmatrix}3+4i&1-i\\1-i&3+4i\end{pmatrix}$ | $6+8i$ | $-7+26i$ |
| $2$ | $2i$ | $\dfrac{1-i}{2}$ | $(1+i)I_2$ | $2+2i$ | $2i$ |
| $3$ | $-1$ | $-i$ | $iI_2$ | $2i$ | $-1$ |
| $4$ | $-1$ | $-ij$ | $\begin{pmatrix}0&i\\i&0\end{pmatrix}$ | $0$ | $1$ |
| $5$ | $1$ | $j$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $0$ | $-1$ |
| $6$ | $\tfrac{17}{8}+\tfrac{15}{8}j$ | $\tfrac54-\tfrac34j$ | $\begin{pmatrix}\tfrac54&\tfrac34\\\tfrac34&\tfrac54\end{pmatrix}$ | $\tfrac52$ | $1$ |
| $7$ | $1$ | $-1$ | $-I_2$ | $-2$ | $1$ |
| $8$ | $2+2j$ | none | $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | $2$ | $0$ |

### What the Cases Show

- Case 1 is the generic element. Its two eigenvalues are distinct complex numbers, and the eigenbasis is the fixed pair $(\Pi_+,\Pi_-)$. The matrix is symmetric in the complex sense, and its two eigenvalues are the diagonal entries of the diagonal form.
- Cases 2, 3 and 7 are the scalar regime. The two eigenvalues coincide, every complex basis is an eigenbasis, and the idempotent pair is a choice. The spectral data carry only the common scalar.
- Cases 4 and 5 are the two pure phases. Their eigenvalues are $(\pm i)$ and $(\pm1)$, and both are square roots of $\pm1$, with squares $-1$ and $+1$. The eigenbasis separates the two signs.
- Case 6 is the hyperbolic line. Its eigenvalues are $2$ and $\tfrac12$, reciprocal to each other, and the element is the exponential of $j\ln2$. The product of the eigenvalues is $1$, so the element is a unit of reduced norm one.
- Case 8 is the zero divisor. The eigenvalues are distinct, the eigenbasis exists, and one eigenvalue is zero. This is the case in which the eigenbasis exists while the polar word of the companion article does not. The element is the projection $2\Pi_+$ onto the first spinor space, with kernel the second.
- The eigenbasis depends only on $j$, not on $\breve Q$, in every non-scalar case. The element enters only through the two eigenvalues.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | the reduced biquaternion algebra, $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a reduced biquaternion |
| $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the two eigenvalues |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two eigenprojections |
| $\mathbb{B}_{\mathrm{r},\sigma\tau}$ | the Peirce corners |
| $S_\pm=\mathbb{C}\Pi_\pm$ | the two spinor spaces |
| $\mathsf M(\breve Q)$ | the matrix of multiplication by $\breve Q$ in the basis $(1,j)$ |
| $C$ | the change to the eigenbasis |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | the reduced norm |

## Further Reading

- [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html), for the eigenvalue decomposition, the Peirce decomposition and the eigenbasis.
- [Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations](eigenbasis-of-a-reduced-biquaternion-in-matrix-elements-representations.html), for the matrix models, the spectral projectors and the change of basis.
- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the same eight elements read through the polar word.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-reduced-biquaternions.html), for the same eight cases read in the eigenbasis, with the idempotents and the spinors.
- [Worked Examples of Eigenbasis of a Split-Complex Number](worked-examples-of-eigenbasis-of-a-split-complex-number.html), for the two-dimensional commutative companion.
- [Worked Examples of Eigenbasis a Biquaternion](worked-examples-of-eigenbasis-a-biquaternion.html), for the noncommutative companion with nilpotents.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the ideals and the Peirce corners.
- [Reduced Biquaternion Elementary Functions](reduced-biquaternion-elementary-functions.html), for the exponential and the logarithm built on the decomposition.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the idempotent decomposition and the coordinatewise product.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation used throughout.
