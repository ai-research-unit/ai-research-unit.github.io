# __Worked Examples of Eigenbasis a Biquaternion__

## Introduction

This article computes the eigenvalue decomposition, the $Q$-adapted Peirce basis, the nilpotents and the eigenbasis of eight biquaternions, one after another. The eight elements are those of *Worked Examples of Exponential Polar Decomposition of Biquaternions*, so that the spectral data and the polar data can be read side by side. The decomposition, the eigenprojections, the $Q$-adapted basis and the nilpotents are those of *Eigenvalue Decomposition and Eigenbasis of a Biquaternion*; no definition or proof is repeated.

Each case is read from the four complex coordinates $Q_t,Q_x,Q_y,Q_z$ of $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. Write

$$
B^2=Q_x^2+Q_y^2+Q_z^2,
\qquad
B=\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2},
$$

and fix one square root $B$. The eigenvalues, the eigenprojections, the nilpotents and the matrices are computed from them by the formulas of §*The Method*. The eigenbasis is checked by the four identities

$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,
\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,
\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,
\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$

The eight cases cover five elements with $B\neq0$, one scalar and two elements with $B=0$ and $\vec Q\neq0$. In the Q-adapted basis a general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with the matrix $\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}$; its two columns are the two spinors.

| Regime | Case | Spectral reading |
|---|---|---|
| Distinct, vector part along $\vec e_x$ | $\vec e_x$ | $B=1$, $\lambda_\pm=\pm i$ |
| Distinct, same direction | $\frac{1}{\sqrt2}(e_t+\vec e_x)$ | $B=\frac{1}{\sqrt2}$, $\lambda_\pm=\frac{1\pm i}{\sqrt2}$ |
| Distinct, real eigenvalues | $\sqrt2\,e_t+i\vec e_x$ | $B=i$, $\lambda_+=\sqrt2-1$, $\lambda_-=\sqrt2+1$ |
| Distinct, same direction | $\bigl(1-\frac{i}{\sqrt2}\bigr)e_t+\bigl(1+\frac{i}{\sqrt2}\bigr)\vec e_x$ | $B=1+\frac{i}{\sqrt2}$, $\lambda_+=a(1+i)$, $\lambda_-=b(1-i)$ |
| Distinct, generic direction | $\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $B=\sqrt{\frac14+i}$, $\lambda_\pm=1-\frac{i}{2}\pm iB$ |
| Scalar | $e_t$ | $B=0$, $\lambda_\pm=1$ |
| Jordan | $e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$ | $B=0$, $\lambda_\pm=1$ |
| Jordan | $(1+i)e_t+\vec e_x+i\vec e_y$ | $B=0$, $\lambda_\pm=1+i$ |

Here $a=1-\frac{1}{\sqrt2}$ and $b=1+\frac{1}{\sqrt2}$.

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its coordinates, its spectrum, its eigenprojections, its nilpotents when they exist, its eigenbasis and its matrix. The summary collects the results in three tables and reads the patterns across the cases (§*Summary*).

## The Method

### The Coordinates and the Spectrum

For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ the four complex coordinates are $Q_t,Q_x,Q_y,Q_z$, and the vector part is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with square

$$
\vec Q^2=-(Q_x^2+Q_y^2+Q_z^2)e_t=-B^2e_t.
$$

The two eigenvalues are

$$
\lambda_+=Q_t+iB,
\qquad
\lambda_-=Q_t-iB.
$$

Their sum and product are

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=Q_t^2+B^2=\langle\tilde Q\rangle_{\natural}.
$$

The eigenvalues are distinct exactly when $B\neq0$, because

$$
\lambda_+-\lambda_-=2iB.
$$

The characteristic polynomial is

$$
p_{\tilde Q}(X)=(X-Q_t)^2+B^2=(X-\lambda_+)(X-\lambda_-),
$$

with discriminant $-4B^2$. The element is a unit exactly when $Q_t^2+B^2\neq0$.

### The Eigenprojections

Put

$$
\vec U=\frac{\vec Q}{B},
\qquad
\vec\Xi=-i\vec U=-\frac{i\vec Q}{B}.
$$

Then $\vec\Xi^2=e_t$, and the two eigenprojections are

$$
\tilde\Pi_+=\frac12(e_t+\vec\Xi),
\qquad
\tilde\Pi_-=\frac12(e_t-\vec\Xi).
$$

They are idempotent, orthogonal and complete:

$$
\tilde\Pi_+^2=\tilde\Pi_+,
\qquad
\tilde\Pi_-^2=\tilde\Pi_-,
\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t.
$$

For every $\tilde Q$ with $B\neq0$,

$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,
\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-,
$$

and the eigenvalue decomposition is

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

The swap $B\mapsto-B$ exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$ and the two eigenvalues. The decomposition is unique up to this exchange.

### The Peirce Corners and the Nilpotents

The Peirce corners relative to $\tilde\Pi_+$ are

$$
\mathbb{B}_{++}=\tilde\Pi_+\mathbb{B}\tilde\Pi_+,
\qquad
\mathbb{B}_{+-}=\tilde\Pi_+\mathbb{B}\tilde\Pi_-,
\qquad
\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
\qquad
\mathbb{B}_{--}=\tilde\Pi_-\mathbb{B}\tilde\Pi_-.
$$

The two diagonal corners are the complex lines of the idempotents:

$$
\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+,
\qquad
\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-.
$$

The two mixed corners are one-dimensional over $\mathbb{C}$. The convention is:

$$
\vec\Upsilon_+\in\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
\qquad
\vec\Upsilon_-\in\mathbb{B}_{+-}=\tilde\Pi_+\mathbb{B}\tilde\Pi_-.
$$

The indexing is by the left ideal, not by the corner.

**Construction.** Choose a pure element $\tilde Q_1$ with

$$
(\tilde Q_1,\tilde Q_1)+\frac{(\tilde Q_1,\vec Q)^2}{B^2}\neq0,
\qquad
(\tilde Q_1,\vec Q)=\operatorname{Sc}(\tilde Q_1\vec Q).
$$

Put

$$
u=\tilde\Pi_-\tilde Q_1\tilde\Pi_+,
\qquad
v=\tilde\Pi_+\tilde Q_1\tilde\Pi_-.
$$

Then

$$
uv=c\,\tilde\Pi_-,
\qquad
vu=c\,\tilde\Pi_+,
\qquad
c=(\tilde Q_1,\tilde Q_1)+\frac{(\tilde Q_1,\vec Q)^2}{B^2},
$$

and

$$
u^2=v^2=0.
$$

Choose a square root $\alpha$ of $c$ and set

$$
\vec\Upsilon_+=\frac{u}{\alpha},
\qquad
\vec\Upsilon_-=\frac{v}{\alpha}.
$$

Then

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.
$$

The normalisation fixes the products, not the individual generators: it leaves the reciprocal rescaling

$$
\vec\Upsilon_+\longmapsto\mu\vec\Upsilon_+,
\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,
\qquad
\mu\in\mathbb{C}^{\times}.
$$

**The shared solution for $\vec Q=Q_x\vec e_x$.** For cases 2 to 5 the vector part is along $\vec e_x$, so

$$
\vec\Xi=-i\vec e_x,
\qquad
\tilde\Pi_+=\frac12(e_t-i\vec e_x),
\qquad
\tilde\Pi_-=\frac12(e_t+i\vec e_x).
$$

Choose $\tilde Q_1=\vec e_y$. Then

$$
u=\frac12(\vec e_y+i\vec e_z),
\qquad
v=\frac12(\vec e_y-i\vec e_z),
\qquad
uv=-\tilde\Pi_-,
\qquad
vu=-\tilde\Pi_+.
$$

Thus $c=-1$, and the choice $\alpha=i$ gives

$$
\boxed{\;
\vec\Upsilon_+=\frac12(\vec e_z-i\vec e_y),
\qquad
\vec\Upsilon_-=\frac12(-\vec e_z-i\vec e_y).
\;}
$$

The pair is the same for the four elements, because it depends only on $\vec\Xi$, not on the eigenvalues.

### The Q-Adapted Peirce Basis

The four elements

$$
\tilde\Pi_+,
\qquad
\vec\Upsilon_-,
\qquad
\vec\Upsilon_+,
\qquad
\tilde\Pi_-
$$

form a $\mathbb{C}$-basis of $\mathbb{B}$. It is the **$Q$-adapted Peirce basis**. Write $L_{\tilde Q}(\tilde P)=\tilde Q\tilde P$ and $R_{\tilde Q}(\tilde P)=\tilde P\tilde Q$ for left and right multiplication. In this basis multiplication by $\tilde Q$ is diagonal:

$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,
\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,
\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,
\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$

Thus the matrix of left multiplication $L_{\tilde Q}$ in the $Q$-adapted basis is

$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$

Because each eigenvalue occurs twice, the eigenbasis is not unique: any basis of the $\lambda_+$-eigenspace together with any basis of the $\lambda_-$-eigenspace is an eigenbasis. The $Q$-adapted basis is the choice singled out by the Peirce structure.

The two minimal left ideals are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$

and

$$
\mathbb{B}=S_+\oplus S_-.
$$

On $S_+$ the eigenbasis is $(\tilde\Pi_+,\vec\Upsilon_+)$, with eigenvalues $\lambda_+$ and $\lambda_-$; on $S_-$ it is $(\vec\Upsilon_-,\tilde\Pi_-)$, with eigenvalues $\lambda_+$ and $\lambda_-$. Each is an eigenbasis with distinct eigenvalues, because $B\neq0$.

The spaces $S_\pm$ are the spinor spaces, the minimal left ideals. They are not the eigenspaces of $L_{\tilde Q}$: the $\lambda_+$-eigenspace is the right ideal $\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-$, and the $\lambda_-$-eigenspace is $\tilde\Pi_-\mathbb{B}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-$. The spaces $S_\pm$ are the eigenspaces of right multiplication $R_{\tilde Q}$. The $Q$-adapted basis is an eigenbasis of $L_{\tilde Q}$; on each $S_\pm$, $L_{\tilde Q}$ carries both eigenvalues, while $R_{\tilde Q}$ is scalar. The side of the multiplication is the whole difference. The labels first and second are fixed by the convention $\tilde\Pi_+=(e_t+\vec\Xi)/2$; replacing $B$ by $-B$ exchanges them.

### Spinors and the $2\times2$ Model

A spinor of first chirality is an element of $S_+$,

$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+,
\qquad
Q_{\mathrm{sp},11},Q_{\mathrm{sp},21}\in\mathbb{C},
$$

with coordinates $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$, the first column of the matrix. Under multiplication by $\tilde Q$,

$$
\tilde Q\xi_+=\lambda_+Q_{\mathrm{sp},11}\tilde\Pi_++\lambda_-Q_{\mathrm{sp},21}\vec\Upsilon_+.
$$

A spinor of second chirality is an element of $S_-$,

$$
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-,
\qquad
Q_{\mathrm{sp},12},Q_{\mathrm{sp},22}\in\mathbb{C},
$$

with coordinates $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$, the second column, and

$$
\tilde Q\xi_-=\lambda_+Q_{\mathrm{sp},12}\vec\Upsilon_-+\lambda_-Q_{\mathrm{sp},22}\tilde\Pi_-.
$$

The same diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ acts on the coordinates of both spinor spaces.

Every element of $\mathbb{B}$ splits as $\tilde P=\tilde P\tilde\Pi_++\tilde P\tilde\Pi_-$, a spinor of first chirality plus a spinor of second chirality. A general element is therefore a pair of spinors, not a spinor.

The assignment

$$
\tilde\Pi_+\longmapsto E_{11},
\qquad
\vec\Upsilon_-\longmapsto E_{12},
\qquad
\vec\Upsilon_+\longmapsto E_{21},
\qquad
\tilde\Pi_-\longmapsto E_{22}
$$

gives the $Q$-adapted model $\mathsf M_2^Q$. For a general element

$$
\tilde P=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
$$

the matrix is

$$
\mathsf M_2^Q(\tilde P)=
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix},
$$

and for $\tilde Q$ itself

$$
\mathsf M_2^Q(\tilde Q)=
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}.
$$

The first column is $S_+$ and the second column is $S_-$.

### The Fixed Matrix Model

The fixed model sends

$$
\mathsf M_2(e_t)=I_2,
\qquad
\mathsf M_2(\vec e_x)=
\begin{pmatrix}0&-i\\-i&0\end{pmatrix},
\qquad
\mathsf M_2(\vec e_y)=
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\mathsf M_2(\vec e_z)=
\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

For a general element,

$$
\mathsf M_2(\tilde Q_{\mathrm{sp}})=
\begin{pmatrix}
Q_{\mathrm{sp},t}-iQ_{\mathrm{sp},z}&-iQ_{\mathrm{sp},x}-Q_{\mathrm{sp},y}\\
-iQ_{\mathrm{sp},x}+Q_{\mathrm{sp},y}&Q_{\mathrm{sp},t}+iQ_{\mathrm{sp},z}
\end{pmatrix},
$$

with trace $2Q_{\mathrm{sp},t}$ and determinant $Q_{\mathrm{sp},t}^2+Q_{\mathrm{sp},x}^2+Q_{\mathrm{sp},y}^2+Q_{\mathrm{sp},z}^2$.

The spectral projectors are

$$
\rho_\pm=\mathsf M_2(\tilde\Pi_\pm)
=\frac12\left(I_2\pm\mathsf M_2(\vec\Xi)\right),
$$

and they satisfy

$$
\rho_\pm^2=\rho_\pm,
\qquad
\rho_+\rho_-=\rho_-\rho_+=0,
\qquad
\rho_++\rho_-=I_2,
\qquad
\mathsf M_2(\tilde Q)=\lambda_+\rho_++\lambda_-\rho_-.
$$

### The Regimes

| Regime | Condition | Spectrum | Eigenbasis |
|---|---|---|---|
| Distinct | $B\neq0$ | $\lambda_+\neq\lambda_-$ | the $Q$-adapted basis; unique up to the reciprocal rescaling of $\vec\Upsilon_\pm$ and the exchange from $B\mapsto-B$ |
| Jordan | $B=0$, $\vec Q\neq0$ | $\lambda_+= \lambda_-=Q_t$ | none: the eigenspace is two-dimensional |
| Scalar | $\vec Q=0$ | $\lambda_+= \lambda_-=Q_t$ | every basis |

In the Jordan regime, write $\tilde Q=Q_te_t+\vec N$ with $\vec N=\vec Q$ and $\vec N^2=0$. The minimal polynomial is $(X-Q_t)^2$. When $Q_t\neq0$ the element is unipotent up to the scalar $Q_t$; when $Q_t=0$ it is nilpotent. In both subcases the eigenspace is $\ker L_{\vec N}$, of dimension two. A two-dimensional eigenspace in a four-dimensional algebra is not a basis of eigenvectors, so there is no eigenbasis. In the scalar regime the operator is $Q_t\,\mathrm{id}$, every nonzero vector is an eigenvector, and every basis is an eigenbasis; the $Q$-adapted construction does not apply because $\vec\Xi$ is undefined.

## The Eight Cases

### Case 1: The Identity

**Coordinates.** For $\tilde Q=e_t$,

$$
Q_t=1,
\qquad
Q_x=Q_y=Q_z=0,
\qquad
B=0,
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**The scalar regime.** The vector part vanishes, so the element is the scalar $1$. The two eigenvalues coincide, $\lambda_\pm=1$, and the left multiplication is the identity:

$$
L_{\tilde Q}=\mathrm{id}.
$$

Every nonzero vector is an eigenvector, every basis is an eigenbasis, and the eigenspace is the whole algebra, of dimension four. There is no $Q$-adapted Peirce basis attached to $\tilde Q$, because the root $\vec\Xi=-i\vec Q/B$ is undefined. The standard Peirce pair $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ is a choice; in it the matrix of $L_{\tilde Q}$ is the identity.

**Spinors.** There is no Q-adapted spinor pair: $B=0$, the two eigenvalues coincide, and the eigenspace is two-dimensional, so $\tilde Q$ selects no pair of complementary minimal left ideals. A general element still has two spinor components in the fixed Peirce basis. With
$$
\mathsf M_2(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix},
$$
the first column $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ is the spinor in the first minimal left ideal and the second column $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ is the spinor in the second. Their matrices are
$$
\mathsf M_2(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$ In the special case
$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}1&0\\0&1\end{pmatrix},
$$
the two columns are $(1,0)$ and $(0,1)$. Both columns are eigenvectors with eigenvalue $1$: every idempotent is an eigenprojection, so every pair of complementary minimal left ideals is a pair of spinor spaces.

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=I_2,
\qquad
\mathrm{tr}=2,
\qquad
\det=1.
$$

The eigenprojections of the matrix are not unique: the spectral projector of the only eigenvalue is $I_2$, and every decomposition of $I_2$ into two complementary idempotents is a choice.

**Consequences.** $\tilde Q^2=e_t$ and $\tilde Q^{-1}=e_t$. The case is the trivial eigenbasis: the algebra is already diagonal, and the element does not select a basis.

### Case 2: A Pure Vector of the Unit Sphere

**Coordinates.** For $\tilde Q=\vec e_x$,

$$
Q_t=0,
\qquad
Q_x=1,
\qquad
Q_y=Q_z=0,
\qquad
B=1,
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**Spectrum.** The eigenvalues are

$$
\lambda_+=i,
\qquad
\lambda_-=-i.
$$

**Eigenprojections.** With $\vec\Xi=-i\vec e_x$,

$$
\tilde\Pi_+=\frac12(e_t-i\vec e_x),
\qquad
\tilde\Pi_-=\frac12(e_t+i\vec e_x),
$$

and

$$
\tilde Q\tilde\Pi_+=i\tilde\Pi_+,
\qquad
\tilde Q\tilde\Pi_-=-i\tilde\Pi_-,
\qquad
\tilde Q=i\tilde\Pi_+-i\tilde\Pi_-.
$$

**Nilpotents.** The shared solution of §*The Method* gives

$$
\vec\Upsilon_+=\frac12(\vec e_z-i\vec e_y),
\qquad
\vec\Upsilon_-=\frac12(-\vec e_z-i\vec e_y).
$$

The checks are

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.
$$

**The eigenbasis.** The $Q$-adapted basis is

$$
\tilde\Pi_+,
\qquad
\vec\Upsilon_-,
\qquad
\vec\Upsilon_+,
\qquad
\tilde\Pi_-,
$$

with the diagonal action

$$
\tilde Q\tilde\Pi_+=i\tilde\Pi_+,
\qquad
\tilde Q\vec\Upsilon_-=i\vec\Upsilon_-,
\qquad
\tilde Q\vec\Upsilon_+=-i\vec\Upsilon_+,
\qquad
\tilde Q\tilde\Pi_-=-i\tilde\Pi_-.
$$

Thus $L_{\tilde Q}$ has the diagonal form

$$
\operatorname{diag}(i,i,-i,-i),
$$

and the $2\times2$ model is

$$
\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(i,-i).
$$

**Spinors.** A general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with matrix
$$
\mathsf M_2^Q(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}
$$
in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. Its two columns are the two spinors:
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},11}\\Q_{\mathrm{sp},21}\end{pmatrix},
\qquad
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},22}\end{pmatrix},
$$
with matrices
$$
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$
Left multiplication by $\tilde Q$ multiplies both columns by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\lambda_-Q_{\mathrm{sp},21}),
\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\lambda_-Q_{\mathrm{sp},22}).
$$
In the special case $\tilde Q=\vec e_x$ one has $Q_{\mathrm{sp},11}=\lambda_+=i$, $Q_{\mathrm{sp},21}=0$, $Q_{\mathrm{sp},12}=0$, $Q_{\mathrm{sp},22}=\lambda_-=-i$, so
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}i&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&0\\0&-i\end{pmatrix}.
$$

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
0&-i\\
-i&0
\end{pmatrix},
\qquad
\mathrm{tr}=0,
\qquad
\det=1.
$$

The spectral projectors are

$$
\rho_+=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
\rho_-=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
$$

and indeed

$$
i\rho_+-i\rho_-=
\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
$$

**Consequences.** The element is a square root of $-e_t$:

$$
\tilde Q^2=-e_t,
\qquad
\tilde Q^{-1}=-\tilde Q=-\vec e_x,
\qquad
\tilde Q^3=-\vec e_x,
\qquad
\tilde Q^4=e_t.
$$

### Case 3: A Sum of the Identity and a Pure Vector

**Coordinates.** For $\tilde Q=\frac{1}{\sqrt2}(e_t+\vec e_x)$,

$$
Q_t=\frac{1}{\sqrt2},
\qquad
Q_x=\frac{1}{\sqrt2},
\qquad
Q_y=Q_z=0,
\qquad
B=\frac{1}{\sqrt2},
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**Spectrum.** The eigenvalues are

$$
\lambda_+=\frac{1+i}{\sqrt2},
\qquad
\lambda_-=\frac{1-i}{\sqrt2}.
$$

**Eigenprojections.** The vector part is again along $\vec e_x$, so the projectors and the nilpotents are those of case 2:

$$
\tilde\Pi_+=\frac12(e_t-i\vec e_x),
\qquad
\tilde\Pi_-=\frac12(e_t+i\vec e_x),
\qquad
\vec\Upsilon_\pm=\frac12(\pm\vec e_z-i\vec e_y).
$$

Therefore

$$
\tilde Q=\frac{1+i}{\sqrt2}\tilde\Pi_++\frac{1-i}{\sqrt2}\tilde\Pi_-.
$$

**The eigenbasis.** The $Q$-adapted basis is again

$$
(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-),
$$

with the diagonal action

$$
\operatorname{diag}\left(\frac{1+i}{\sqrt2},\frac{1+i}{\sqrt2},\frac{1-i}{\sqrt2},\frac{1-i}{\sqrt2}\right).
$$

The $2\times2$ model is

$$
\mathsf M_2^Q(\tilde Q)=
\operatorname{diag}\left(\frac{1+i}{\sqrt2},\frac{1-i}{\sqrt2}\right).
$$

**Spinors.** A general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with matrix
$$
\mathsf M_2^Q(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}
$$
in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. Its two columns are the two spinors:
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},11}\\Q_{\mathrm{sp},21}\end{pmatrix},
\qquad
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},22}\end{pmatrix},
$$
with matrices
$$
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$
Left multiplication by $\tilde Q$ multiplies both columns by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\lambda_-Q_{\mathrm{sp},21}),
\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\lambda_-Q_{\mathrm{sp},22}).
$$
In the special case $\tilde Q=\tfrac{1}{\sqrt2}(e_t+\vec e_x)$ one has $Q_{\mathrm{sp},11}=\lambda_+=\tfrac{1+i}{\sqrt2}$, $Q_{\mathrm{sp},21}=0$, $Q_{\mathrm{sp},12}=0$, $Q_{\mathrm{sp},22}=\lambda_-=\tfrac{1-i}{\sqrt2}$, so
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}\tfrac{1+i}{\sqrt2}&0\\0&\tfrac{1-i}{\sqrt2}\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}\tfrac{1+i}{\sqrt2}&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&0\\0&\tfrac{1-i}{\sqrt2}\end{pmatrix}.
$$

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&-i\\
-i&1
\end{pmatrix},
\qquad
\mathrm{tr}=\sqrt2,
\qquad
\det=1.
$$

Its spectral projectors are the same $\rho_\pm$ as in case 2, and

$$
\lambda_+\rho_++\lambda_-\rho_-=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&-i\\
-i&1
\end{pmatrix}.
$$

**Consequences.** The square is

$$
\tilde Q^2=\vec e_x,
$$

the cube is

$$
\tilde Q^3=\frac{\vec e_x-e_t}{\sqrt2}=-\tilde Q^{-1},
$$

and the inverse is

$$
\tilde Q^{-1}=\frac{e_t-\vec e_x}{\sqrt2}.
$$

The fourth power is $-e_t$. The element is a square root of $\vec e_x$.

### Case 4: A Real Spectrum from an Imaginary Root

**Coordinates.** For $\tilde Q=\sqrt2\,e_t+i\vec e_x$,

$$
Q_t=\sqrt2,
\qquad
Q_x=i,
\qquad
Q_y=Q_z=0,
\qquad
B=i,
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**Spectrum.** With the root $B=i$,

$$
\lambda_+=\sqrt2-1,
\qquad
\lambda_-=\sqrt2+1.
$$

The two eigenvalues are real and distinct, although $B$ is imaginary. The other root $-i$ exchanges them.

**Eigenprojections.** The vector part is along $\vec e_x$, so

$$
\tilde\Pi_+=\frac12(e_t-i\vec e_x),
\qquad
\tilde\Pi_-=\frac12(e_t+i\vec e_x),
$$

and

$$
\tilde Q=(\sqrt2-1)\tilde\Pi_++(\sqrt2+1)\tilde\Pi_-.
$$

**Nilpotents.** The nilpotents are the shared pair

$$
\vec\Upsilon_+=\frac12(\vec e_z-i\vec e_y),
\qquad
\vec\Upsilon_-=\frac12(-\vec e_z-i\vec e_y).
$$

**The eigenbasis.** The diagonal action is

$$
\operatorname{diag}(\sqrt2-1,\sqrt2-1,\sqrt2+1,\sqrt2+1),
$$

and the $2\times2$ model is

$$
\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\sqrt2-1,\sqrt2+1).
$$

**Spinors.** A general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with matrix
$$
\mathsf M_2^Q(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}
$$
in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. Its two columns are the two spinors:
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},11}\\Q_{\mathrm{sp},21}\end{pmatrix},
\qquad
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},22}\end{pmatrix},
$$
with matrices
$$
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$
Left multiplication by $\tilde Q$ multiplies both columns by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\lambda_-Q_{\mathrm{sp},21}),
\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\lambda_-Q_{\mathrm{sp},22}).
$$
In the special case $\tilde Q=\sqrt2\,e_t+i\vec e_x$ one has $Q_{\mathrm{sp},11}=\lambda_+=\sqrt2-1$, $Q_{\mathrm{sp},21}=0$, $Q_{\mathrm{sp},12}=0$, $Q_{\mathrm{sp},22}=\lambda_-=\sqrt2+1$, so
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}\sqrt2-1&0\\0&\sqrt2+1\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}\sqrt2-1&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&0\\0&\sqrt2+1\end{pmatrix}.
$$

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
\sqrt2&1\\
1&\sqrt2
\end{pmatrix},
\qquad
\mathrm{tr}=2\sqrt2,
\qquad
\det=1.
$$

This is a real symmetric matrix with eigenvectors $(1,-1)$ and $(1,1)$, which are the columns of the projectors up to scale.

**Consequences.** The square is

$$
\tilde Q^2=3+2\sqrt2\,i\vec e_x,
$$

the cube is

$$
\tilde Q^3=5\sqrt2+7i\vec e_x,
$$

and the inverse is

$$
\tilde Q^{-1}=\sqrt2-i\vec e_x.
$$

### Case 5: A Generic Element on the Same Axis

**Coordinates.** For

$$
\tilde Q=\left(1-\frac{i}{\sqrt2}\right)e_t+\left(1+\frac{i}{\sqrt2}\right)\vec e_x,
$$

the coordinates are

$$
Q_t=1-\frac{i}{\sqrt2},
\qquad
Q_x=1+\frac{i}{\sqrt2},
\qquad
Q_y=Q_z=0,
\qquad
B=1+\frac{i}{\sqrt2},
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**Spectrum.** Put $a=1-\frac{1}{\sqrt2}$ and $b=1+\frac{1}{\sqrt2}$. Then

$$
\lambda_+=a(1+i),
\qquad
\lambda_-=b(1-i).
$$

Numerically,

$$
\lambda_+\approx 0.2928932188+0.2928932188\,i,
\qquad
\lambda_-\approx 1.7071067812-1.7071067812\,i.
$$

**Eigenprojections.** The vector part is along $\vec e_x$, so

$$
\tilde\Pi_+=\frac12(e_t-i\vec e_x),
\qquad
\tilde\Pi_-=\frac12(e_t+i\vec e_x),
$$

and

$$
\tilde Q=a(1+i)\tilde\Pi_++b(1-i)\tilde\Pi_-.
$$

**Nilpotents.** The shared pair is

$$
\vec\Upsilon_+=\frac12(\vec e_z-i\vec e_y),
\qquad
\vec\Upsilon_-=\frac12(-\vec e_z-i\vec e_y).
$$

**The eigenbasis.** The diagonal action is

$$
\operatorname{diag}\bigl(a(1+i),a(1+i),b(1-i),b(1-i)\bigr),
$$

and the $2\times2$ model is

$$
\mathsf M_2^Q(\tilde Q)=\operatorname{diag}\bigl(a(1+i),b(1-i)\bigr).
$$

**Spinors.** A general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with matrix
$$
\mathsf M_2^Q(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}
$$
in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. Its two columns are the two spinors:
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},11}\\Q_{\mathrm{sp},21}\end{pmatrix},
\qquad
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},22}\end{pmatrix},
$$
with matrices
$$
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$
Left multiplication by $\tilde Q$ multiplies both columns by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\lambda_-Q_{\mathrm{sp},21}),
\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\lambda_-Q_{\mathrm{sp},22}).
$$
In the special case $\tilde Q=(1-\tfrac{i}{\sqrt2})e_t+(1+\tfrac{i}{\sqrt2})\vec e_x$ one has $Q_{\mathrm{sp},11}=\lambda_+=a(1+i)$, $Q_{\mathrm{sp},21}=0$, $Q_{\mathrm{sp},12}=0$, $Q_{\mathrm{sp},22}=\lambda_-=b(1-i)$, so
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}a(1+i)&0\\0&b(1-i)\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}a(1+i)&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&0\\0&b(1-i)\end{pmatrix}.
$$

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
1-\frac{i}{\sqrt2}&\frac{1}{\sqrt2}-i\\
\frac{1}{\sqrt2}-i&1-\frac{i}{\sqrt2}
\end{pmatrix},
\qquad
\mathrm{tr}=2-i\sqrt2,
\qquad
\det=1.
$$

**Consequences.** The square is

$$
\tilde Q^2=3\vec e_x-2\sqrt2\,i\,e_t,
$$

and the inverse is

$$
\tilde Q^{-1}=\left(1-\frac{i}{\sqrt2}\right)-\left(1+\frac{i}{\sqrt2}\right)\vec e_x.
$$

### Case 6: Orthogonal Axes and a Unipotent Element

**Coordinates.** For

$$
\tilde Q=e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z,
$$

the coordinates are

$$
Q_t=1,
\qquad
Q_x=\frac{i}{\sqrt2},
\qquad
Q_y=1,
\qquad
Q_z=\frac{i}{\sqrt2},
\qquad
B=0,
\qquad
\langle\tilde Q\rangle_{\natural}=1.
$$

**The Jordan regime.** The vector part is nonzero and null:

$$
Q_x^2+Q_y^2+Q_z^2=-\frac12+1-\frac12=0.
$$

Write

$$
\tilde N=\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z.
$$

Then

$$
\tilde N^2=-\frac12+1-\frac12=0,
\qquad
\tilde Q=e_t+\tilde N.
$$

The minimal polynomial is $(X-1)^2$, the only eigenvalue is $1$, and the eigenspace is

$$
\ker L_{\tilde N}=\{\tilde P:\tilde N\tilde P=0\},
$$

of dimension two. A two-dimensional eigenspace does not span the four-dimensional algebra, so there is no eigenbasis. The element is unipotent: it is a unit, with inverse

$$
\tilde Q^{-1}=e_t-\tilde N
=e_t-\frac{i}{\sqrt2}\vec e_x-\vec e_y-\frac{i}{\sqrt2}\vec e_z.
$$

**Spinors.** There is no Q-adapted spinor pair: $B=0$, the two eigenvalues coincide, and the eigenspace is two-dimensional, so $\tilde Q$ selects no pair of complementary minimal left ideals. A general element still has two spinor components in the fixed Peirce basis. With
$$
\mathsf M_2(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix},
$$
the first column $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ is the spinor in the first minimal left ideal and the second column $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ is the spinor in the second. Their matrices are
$$
\mathsf M_2(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$ In the special case
$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}1+\frac{1}{\sqrt2}&\frac{1}{\sqrt2}-1\\[2pt]1+\frac{1}{\sqrt2}&1-\frac{1}{\sqrt2}\end{pmatrix},
$$
the two columns are $(1+\frac{1}{\sqrt2},\,1+\frac{1}{\sqrt2})$ and $(\frac{1}{\sqrt2}-1,\,1-\frac{1}{\sqrt2})$. The first column is an eigenvector with eigenvalue $1$; the second is not. The eigenspace is one line, so there is one eigenspinor and no second one, and no spinor decomposition of $\tilde Q$.

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
1+\frac{1}{\sqrt2}&\frac{1}{\sqrt2}-1\\
1+\frac{1}{\sqrt2}&1-\frac{1}{\sqrt2}
\end{pmatrix}
=I_2+\mathsf N,
\qquad
\mathsf N=
\begin{pmatrix}
\frac{1}{\sqrt2}&\frac{1}{\sqrt2}-1\\
1+\frac{1}{\sqrt2}&-\frac{1}{\sqrt2}
\end{pmatrix},
$$

with $\mathsf N^2=0$. The kernel of $\mathsf N$ is the line spanned by $(1,1+\sqrt2)$, and the eigenspace of $\mathsf M_2(\tilde Q)$ is the two-dimensional space of matrices whose two columns lie on that line.

**Consequences.** The powers are

$$
\tilde Q^n=e_t+n\tilde N,
$$

so

$$
\tilde Q^2=e_t+2\tilde N
=e_t+i\sqrt2\,\vec e_x+2\vec e_y+i\sqrt2\,\vec e_z.
$$

The element is a unit of norm one, not a zero divisor, although its vector part is null.

### Case 7: A Generic Direction

**Coordinates.** For

$$
\tilde Q=\left(1-\frac{i}{2}\right)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z,
$$

the coordinates are

$$
Q_t=1-\frac{i}{2},
\qquad
Q_x=\frac{1+i}{\sqrt2},
\qquad
Q_y=\frac{1}{\sqrt2},
\qquad
Q_z=\frac{i}{2}.
$$

The vector part has square

$$
B^2=\frac{(1+i)^2}{2}+\frac12+\frac{i^2}{4}
=i+\frac12-\frac14=\frac14+i,
$$

so

$$
B=\sqrt{\frac14+i}\approx 0.8002425902+0.6248105338\,i.
$$

**Spectrum.** The eigenvalues are

$$
\lambda_+=1-\frac{i}{2}+iB\approx 0.3751894662+0.3002425902\,i,
$$

$$
\lambda_-=1-\frac{i}{2}-iB\approx 1.6248105338-1.3002425902\,i.
$$

Their product is $1$. The element is a unit.

**Eigenprojections.** With $\vec\Xi=-i\vec Q/B$,

$$
\vec\Xi=\frac{1-i}{\sqrt2\,B}\vec e_x-\frac{i}{\sqrt2\,B}\vec e_y+\frac{1}{2B}\vec e_z,
$$

and $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$. Numerically,

$$
\tilde\Pi_+\approx \frac12e_t+(0.0601727-0.4887892\,i)\vec e_x+(-0.2143082-0.2744809\,i)\vec e_y+(0.1940873-0.1515388\,i)\vec e_z,
$$

$$
\tilde\Pi_-\approx \frac12e_t+(-0.0601727+0.4887892\,i)\vec e_x+(0.2143082+0.2744809\,i)\vec e_y+(-0.1940873+0.1515388\,i)\vec e_z.
$$

The decomposition is

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

**Nilpotents.** Choose the transverse pure element

$$
\tilde Q_1=i\vec e_y-\sqrt2\,\vec e_z,
\qquad
\tilde Q_1^2=-e_t.
$$

The construction gives

$$
u=\tilde\Pi_-\tilde Q_1\tilde\Pi_+,
\qquad
v=\tilde\Pi_+\tilde Q_1\tilde\Pi_-,
\qquad
uv=-\tilde\Pi_-,
\qquad
vu=-\tilde\Pi_+.
$$

With $\alpha=i$,

$$
\vec\Upsilon_+=\frac{u}{i}
\approx (-0.1940873+0.1515388\,i)\vec e_x+(1.1912523+0.0850970\,i)\vec e_y+(-0.0601727+1.1958960\,i)\vec e_z,
$$

$$
\vec\Upsilon_-=\frac{v}{i}
\approx (0.1940873-0.1515388\,i)\vec e_x+(-0.1912523-0.0850970\,i)\vec e_y+(0.0601727+0.2183176\,i)\vec e_z.
$$

The checks hold for the computed values to machine precision:

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.
$$

The nilpotents are not simple coordinate expressions, because the direction of $\vec Q$ is not aligned with an axis. They are computed from the projection formula, which is the general construction.

**The eigenbasis.** The $Q$-adapted basis is

$$
(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-),
$$

with the diagonal action

$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$

and the $2\times2$ model is

$$
\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-).
$$

**Spinors.** A general element is $\tilde Q_{\mathrm{sp}}=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},21}\vec\Upsilon_++Q_{\mathrm{sp},22}\tilde\Pi_-$, with matrix
$$
\mathsf M_2^Q(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix}
$$
in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. Its two columns are the two spinors:
$$
\xi_+=Q_{\mathrm{sp},11}\tilde\Pi_++Q_{\mathrm{sp},21}\vec\Upsilon_+\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},11}\\Q_{\mathrm{sp},21}\end{pmatrix},
\qquad
\xi_-=Q_{\mathrm{sp},12}\vec\Upsilon_-+Q_{\mathrm{sp},22}\tilde\Pi_-\longleftrightarrow\begin{pmatrix}Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},22}\end{pmatrix},
$$
with matrices
$$
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$
Left multiplication by $\tilde Q$ multiplies both columns by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})\longmapsto(\lambda_+Q_{\mathrm{sp},11},\lambda_-Q_{\mathrm{sp},21}),
\qquad
(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})\longmapsto(\lambda_+Q_{\mathrm{sp},12},\lambda_-Q_{\mathrm{sp},22}).
$$
In the special case $\tilde Q=(1-\tfrac{i}{2})e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z$ one has $Q_{\mathrm{sp},11}=\lambda_+=1-\tfrac{i}{2}+iB$, $Q_{\mathrm{sp},21}=0$, $Q_{\mathrm{sp},12}=0$, $Q_{\mathrm{sp},22}=\lambda_-=1-\tfrac{i}{2}-iB$, so
$$
\mathsf M_2^Q(\tilde Q)=\begin{pmatrix}1-\tfrac{i}{2}+iB&0\\0&1-\tfrac{i}{2}-iB\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_+)=\begin{pmatrix}1-\tfrac{i}{2}+iB&0\\0&0\end{pmatrix},
\qquad
\mathsf M_2^Q(\xi_-)=\begin{pmatrix}0&0\\0&1-\tfrac{i}{2}-iB\end{pmatrix}.
$$

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
\frac32-\frac{i}{2}&-\frac{i}{\sqrt2}\\
\frac{2-i}{\sqrt2}&\frac12-\frac{i}{2}
\end{pmatrix},
\qquad
\mathrm{tr}=2-i,
\qquad
\det=1.
$$

The spectral projectors are

$$
\rho_+=\frac{1}{2B}
\begin{pmatrix}
B-\frac{i}{2}&-\frac{1}{\sqrt2}\\
-\frac{1+2i}{\sqrt2}&B+\frac{i}{2}
\end{pmatrix},
\qquad
\rho_-=I_2-\rho_+,
$$

and $\mathsf M_2(\tilde Q)=\lambda_+\rho_++\lambda_-\rho_-$.

**Consequences.** The square is

$$
\tilde Q^2=\left(\frac12-2i\right)e_t+\frac{3+i}{\sqrt2}\vec e_x+\frac{2-i}{\sqrt2}\vec e_y+\left(\frac12+i\right)\vec e_z,
$$

and the inverse is the conjugate, because the norm is one:

$$
\tilde Q^{-1}=\left(1-\frac{i}{2}\right)e_t-\frac{1+i}{\sqrt2}\vec e_x-\frac{1}{\sqrt2}\vec e_y-\frac{i}{2}\vec e_z.
$$

### Case 8: A Null Vector Part and a Unipotent Unit

**Coordinates.** For

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y,
$$

the coordinates are

$$
Q_t=1+i,
\qquad
Q_x=1,
\qquad
Q_y=i,
\qquad
Q_z=0,
\qquad
B=0,
\qquad
\langle\tilde Q\rangle_{\natural}=2i.
$$

**The Jordan regime.** The vector part is nonzero and null:

$$
Q_x^2+Q_y^2=1+i^2=0.
$$

Write

$$
\tilde N=\vec e_x+i\vec e_y.
$$

Then

$$
\tilde N^2=-e_t+0+e_t=0,
\qquad
\tilde Q=(1+i)e_t+\tilde N.
$$

The only eigenvalue is $1+i$, the minimal polynomial is $(X-(1+i))^2$, and the eigenspace is $\ker L_{\tilde N}$, of dimension two. There is no eigenbasis. The element is a unit, with inverse

$$
\tilde Q^{-1}=\frac{1-i}{2}e_t+\frac{i}{2}\vec e_x-\frac12\vec e_y.
$$

**Spinors.** There is no Q-adapted spinor pair: $B=0$, the two eigenvalues coincide, and the eigenspace is two-dimensional, so $\tilde Q$ selects no pair of complementary minimal left ideals. A general element still has two spinor components in the fixed Peirce basis. With
$$
\mathsf M_2(\tilde Q_{\mathrm{sp}})=\begin{pmatrix}Q_{\mathrm{sp},11}&Q_{\mathrm{sp},12}\\Q_{\mathrm{sp},21}&Q_{\mathrm{sp},22}\end{pmatrix},
$$
the first column $(Q_{\mathrm{sp},11},Q_{\mathrm{sp},21})$ is the spinor in the first minimal left ideal and the second column $(Q_{\mathrm{sp},12},Q_{\mathrm{sp},22})$ is the spinor in the second. Their matrices are
$$
\mathsf M_2(\xi_+)=\begin{pmatrix}Q_{\mathrm{sp},11}&0\\Q_{\mathrm{sp},21}&0\end{pmatrix},
\qquad
\mathsf M_2(\xi_-)=\begin{pmatrix}0&Q_{\mathrm{sp},12}\\0&Q_{\mathrm{sp},22}\end{pmatrix}.
$$ In the special case
$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}1+i&-2i\\0&1+i\end{pmatrix},
$$
the two columns are $(1+i,\,0)$ and $(-2i,\,1+i)$. The first column is an eigenvector with eigenvalue $1+i$; the second is not. The eigenspace is one line, so there is one eigenspinor and no second one, and no spinor decomposition of $\tilde Q$.

**Matrix.** In the fixed model,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
1+i&-2i\\
0&1+i
\end{pmatrix}
=(1+i)I_2+\mathsf N,
\qquad
\mathsf N=
\begin{pmatrix}
0&-2i\\
0&0
\end{pmatrix},
\qquad
\mathsf N^2=0.
$$

The matrix is a single Jordan block. The kernel of $\mathsf N$ is the line spanned by $(1,0)$, and the eigenspace of $\mathsf M_2(\tilde Q)$ under left multiplication is the two-dimensional space of matrices whose two columns lie on that line, that is, whose second row is zero.

**Consequences.** The square is

$$
\tilde Q^2=2i\,e_t+2(1+i)\vec e_x+2(i-1)\vec e_y,
$$

and the general power is

$$
\tilde Q^n=(1+i)^n\left(e_t+\frac{n}{1+i}\tilde N\right).
$$

The vector part is null, but the norm is $2i\neq0$: the element is not a zero divisor. A null vector part is not a null element.

## Summary

### Main Results

| Case | $\tilde Q$ | $B$ | $\lambda_+$ | $\lambda_-$ | $\langle\tilde Q\rangle_{\natural}$ | Regime | Eigenbasis |
|---|---|---|---|---|---|---|---|
| $1$ | $e_t$ | $0$ | $1$ | $1$ | $1$ | scalar | every basis |
| $2$ | $\vec e_x$ | $1$ | $i$ | $-i$ | $1$ | distinct | yes |
| $3$ | $\frac{1}{\sqrt2}(e_t+\vec e_x)$ | $\frac{1}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $1$ | distinct | yes |
| $4$ | $\sqrt2\,e_t+i\vec e_x$ | $i$ | $\sqrt2-1$ | $\sqrt2+1$ | $1$ | distinct | yes |
| $5$ | $\bigl(1-\frac{i}{\sqrt2}\bigr)e_t+\bigl(1+\frac{i}{\sqrt2}\bigr)\vec e_x$ | $1+\frac{i}{\sqrt2}$ | $a(1+i)$ | $b(1-i)$ | $1$ | distinct | yes |
| $6$ | $e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$ | $0$ | $1$ | $1$ | $1$ | Jordan | none |
| $7$ | $\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $\sqrt{\frac14+i}$ | $1-\frac{i}{2}+iB$ | $1-\frac{i}{2}-iB$ | $1$ | distinct | yes |
| $8$ | $(1+i)e_t+\vec e_x+i\vec e_y$ | $0$ | $1+i$ | $1+i$ | $2i$ | Jordan | none |

### The Eigenbasis Table

For the five distinct cases the $Q$-adapted basis is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ and the diagonal values are $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

| Case | $\tilde\Pi_+$ | $\vec\Upsilon_\pm$ | $\operatorname{diag}$ |
|---|---|---|---|
| $2$ | $\frac12(e_t-i\vec e_x)$ | $\vec\Upsilon_\pm=\frac12(\pm\vec e_z-i\vec e_y)$ | $(i,i,-i,-i)$ |
| $3$ | $\frac12(e_t-i\vec e_x)$ | $\vec\Upsilon_\pm=\frac12(\pm\vec e_z-i\vec e_y)$ | $\bigl(\frac{1+i}{\sqrt2},\frac{1+i}{\sqrt2},\frac{1-i}{\sqrt2},\frac{1-i}{\sqrt2}\bigr)$ |
| $4$ | $\frac12(e_t-i\vec e_x)$ | $\vec\Upsilon_\pm=\frac12(\pm\vec e_z-i\vec e_y)$ | $(\sqrt2-1,\sqrt2-1,\sqrt2+1,\sqrt2+1)$ |
| $5$ | $\frac12(e_t-i\vec e_x)$ | $\vec\Upsilon_\pm=\frac12(\pm\vec e_z-i\vec e_y)$ | $(a(1+i),a(1+i),b(1-i),b(1-i))$ |
| $7$ | $\frac12(e_t+\vec\Xi)$ | computed from $\tilde Q_1=i\vec e_y-\sqrt2\vec e_z$ | $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ |

For cases 1, 6 and 8 there is no $Q$-adapted basis: case 1 is scalar, and cases 6 and 8 are Jordan.

### The Matrices

| Case | $\mathsf M_2(\tilde Q)$ | $\mathrm{tr}$ | $\det$ |
|---|---|---|---|
| $1$ | $I_2$ | $2$ | $1$ |
| $2$ | $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$ | $0$ | $1$ |
| $3$ | $\frac{1}{\sqrt2}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$ | $\sqrt2$ | $1$ |
| $4$ | $\begin{pmatrix}\sqrt2&1\\1&\sqrt2\end{pmatrix}$ | $2\sqrt2$ | $1$ |
| $5$ | $\begin{pmatrix}1-\frac{i}{\sqrt2}&\frac{1}{\sqrt2}-i\\\frac{1}{\sqrt2}-i&1-\frac{i}{\sqrt2}\end{pmatrix}$ | $2-i\sqrt2$ | $1$ |
| $6$ | $\begin{pmatrix}1+\frac{1}{\sqrt2}&\frac{1}{\sqrt2}-1\\1+\frac{1}{\sqrt2}&1-\frac{1}{\sqrt2}\end{pmatrix}$ | $2$ | $1$ |
| $7$ | $\begin{pmatrix}\frac32-\frac{i}{2}&-\frac{i}{\sqrt2}\\\frac{2-i}{\sqrt2}&\frac12-\frac{i}{2}\end{pmatrix}$ | $2-i$ | $1$ |
| $8$ | $\begin{pmatrix}1+i&-2i\\0&1+i\end{pmatrix}$ | $2+2i$ | $2i$ |

### What the Cases Show

- Cases 2 to 5 have the same vector direction $\vec e_x$. They therefore have the same root $\vec\Xi=-i\vec e_x$, the same eigenprojections $\tilde\Pi_\pm$, and the same nilpotents $\vec\Upsilon_\pm$. Only the two eigenvalues change. The eigenbasis is attached to the direction of the vector part, not to its magnitude or to the scalar part. This is the biquaternion form of the statement that the eigenbasis is attached to the root.
- Case 4 has $B=i$ and real eigenvalues. The root need not be real for the spectrum to be real. The sign of the root exchanges the two eigenvalues and the two projectors.
- Case 6 is the unipotent case with a real scalar part. The vector part is null, $B=0$, and the element is $e_t$ plus a square-zero element. The eigenspace has dimension two, so there is no eigenbasis.
- Case 8 is the unipotent case with a complex scalar part. The vector part is again null, the norm is $2i\neq0$, and the element is a unit. A null vector part does not imply a zero divisor.
- None of the eight is a zero divisor. The zero-divisor regime with $B\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$ is not represented, and neither is the nilpotent subcase $Q_t=0$, $B=0$. Case 8 is the closest miss: its vector part is null, but its scalar part keeps the norm nonzero.
- Case 1 is the scalar regime. Every basis is an eigenbasis, and the $Q$-adapted construction does not apply.
- Case 7 is the generic direction. The nilpotents are not aligned with the axes, and they are computed from the projection formula. The symmetric closed form of *Eigenvalue Decomposition and Eigenbasis of a Biquaternion* gives the same pair up to the reciprocal rescaling when the direction is off the exceptional cone; the projection formula is the construction used here.
- In the distinct regime the eigenvalues repeat twice in the four-dimensional eigenbasis, and they are distinct on each two-dimensional spinor space. The $2\times2$ model records the two values once, one for each column.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | a biquaternion |
| $B=\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ | a fixed square root of the vector part |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\vec\Xi=-i\vec Q/B$ | the pure root of $+1$ attached to $\tilde Q$ |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ | the two eigenprojections |
| $\vec\Upsilon_\pm$ | the normalised nilpotents of the mixed Peirce corners |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two minimal left ideals, the spinor spaces |
| $\mathsf M_2$ | the fixed $2\times2$ matrix model |
| $\mathsf M_2^Q$ | the $Q$-adapted matrix model |
| $\rho_\pm=\mathsf M_2(\tilde\Pi_\pm)$ | the spectral projectors |
| $L_{\tilde Q},R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the norm |

## Further Reading

- [Eigenvalue Decomposition and Eigenbasis of a Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-biquaternion.html), for the eigenvalue decomposition, the Peirce decomposition, the nilpotents and the eigenbasis.
- [Eigenbasis of a Biquaternion in Matrix Elements Representations](eigenbasis-of-a-biquaternion-in-matrix-elements-representations.html), for the fixed model, the $Q$-adapted model and the diagonalising matrix.
- [Worked Examples of Exponential Polar Decomposition of Biquaternions](worked-examples-of-exponential-polar-decomposition-of-biquaternions.html), for the same eight elements read through the polar word.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-biquaternions.html), for the same eight cases read in the Q-adapted basis, with the nilpotents and the spinors.
- [Worked Examples of Eigenbasis of a Split-Complex Number](worked-examples-of-eigenbasis-of-a-split-complex-number.html), for the two-dimensional commutative companion.
- [Worked Examples of Eigenbasis a Reduced Biquaternion](worked-examples-of-eigenbasis-a-reduced-biquaternion.html), for the four-dimensional commutative companion.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce corners and the minimal left ideals.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and the logarithm built on the decomposition.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the Jordan and nilpotent regimes.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebraic structure of the biquaternion algebra.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation used throughout.
