# __The Fundamental Symmetry of the Form__

## Introduction

An indefinite Hermitian form is not a norm: its diagonal takes both signs, and the Cauchy–Schwarz inequality and the theory of *The Norm Defined by a Form* apply to the definite forms alone. The defect is repaired by a single device. As soon as the space is written as the orthogonal sum of a part on which the form is positive definite and a part on which it is negative definite, the operator that acts as $+\mathrm{id}$ on the first part and as $-\mathrm{id}$ on the second turns the indefinite form into a definite one, and every definite statement is read in the indefinite case by conjugating each occurrence of the form by that operator. This operator is the **fundamental symmetry** $J$ of the form, and the article develops it for the forms of *Topological Sesquialgebras with a Form*: the standard form of the layer is Hermitian but need not be definite, and the decomposition that makes it definite is the datum that brings it back to the definite theory.

Three facts organise the article. The **fundamental symmetry** built from a fundamental decomposition has square one, is self-adjoint for the definite companion form, and is an isometry of the indefinite form; it is the bridge, $h(x,y) = \langle Jx,y\rangle$ and $\langle x,y\rangle = h(Jx,y)$, between the given form and the definite one, so that each of the two is recovered from the other and from $J$. The **adjoints under the two forms** differ by conjugation by $J$: if $T^{\dagger}$ is the adjoint of an operator for $h$ and $T^{*}$ its adjoint for the companion, then $T^{\dagger} = J T^{*} J$, so the indefinite operator theory is the definite one with $J$ inserted, and the $h$-self-adjoint operators are the operators $T$ with $JT$ self-adjoint. And the symmetry is **not determined by the form**: the fundamental decompositions form a family, and on the plane of signature $(1,1)$ a one-parameter family, so the choice of $J$ is a choice of decomposition; when the form is nondegenerate a distinguished choice is available, the symmetry $J$ determined by $J^{T} = H(H^{2})^{-1/2}$ from the Gram operator, which is $J = H(H^{2})^{-1/2}$ when the Gram matrix is symmetric and carries the transpose otherwise; it is the one that makes the companion form a function of the given one.

The article defines the fundamental decomposition and the symmetry, proves the bridge and the eigenspace properties, relates the two adjoints, treats the non-uniqueness and the canonical choice, and works the signature $(1,1)$ plane, a Pontryagin space and the indefinite biquaternion form. The definite norm and the collapse are *The Norm Defined by a Form*; the signature and the inertia are *The Indefinite Case and the Signature*; the bilinear counterpart is *The Fundamental Symmetry* and the space it produces is a Krein space; the operator theory of the indefinite case is *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*. Throughout, $A$ is a sesquialgebra with a form in the sense of *Topological Sesquialgebras with a Form* over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$, and $R$ complete when a norm or a completion is in question; the given form $h$ is Hermitian, compatible with the product, and **indefinite** — not assumed positive definite.

## The Fundamental Decomposition

### The Definite Subspaces

**Definition.** Let $h$ be a Hermitian form on $A$. A submodule $W \subseteq A$ is **positive definite** when $h(x,x) > 0$ for every nonzero $x \in W$, **negative definite** when $h(x,x) < 0$ for every nonzero $x$, and **definite** when it is one of the two. Two submodules $W, W'$ are **$h$-orthogonal**, written $W \perp W'$, when $h(x,y) = 0$ for all $x \in W$, $y \in W'$; the orthogonal of a set is $W^{\perp} = \{x : h(x,y) = 0 \ \forall y \in W\}$, the radical of the form being $A^{\perp}$.

**Definition.** A **fundamental decomposition** of $(A,h)$ is an $h$-orthogonal direct sum

$$
A = A^{+} \oplus A^{-} , \qquad A^{+} \perp A^{-} ,
$$

with $A^{+}$ positive definite and $A^{-}$ negative definite. An indefinite form that admits a fundamental decomposition is **decomposable**; the rank of $A^{-}$ is the **negative index** of the form.

**Remark (existence is a hypothesis).** A nondegenerate Hermitian form over an ordered field admits a fundamental decomposition when it is orthogonally diagonalisable — in particular always in finite dimension over $\mathbb{R}$ or $\mathbb{C}$, by the principal-axis theorem, and, in the complete indefinite case, when the space is a Krein space. The layer takes decomposability as part of the datum of the indefinite object; the definite form is the case $A^{-} = 0$, and the examples below all exhibit the decomposition explicitly.

**Proposition (the decomposition computes the signature).** Let $A = A^{+}\oplus A^{-}$ be a fundamental decomposition of finite rank. Then every orthogonal basis of $A^{+}$ is positive and every orthogonal basis of $A^{-}$ is negative, and the pair $(\dim A^{+}, \dim A^{-})$ over $\mathbb{R}$ is the **signature** of the form, independent of the decomposition by *The Indefinite Case and the Signature*.

*Proof.* The assertion on the bases is definiteness on the summands; the invariance of the signature under a change of fundamental decomposition is Sylvester's law of inertia, the content of *The Indefinite Case and the Signature*. $\square$

## The Fundamental Symmetry

### The Definition

**Definition.** Let $A = A^{+}\oplus A^{-}$ be a fundamental decomposition, and let $P^{+}, P^{-}$ be the projections onto the two summands along the decomposition. The **fundamental symmetry** of the decomposition is

$$
J = P^{+} - P^{-} .
$$

The **companion form** of the decomposition is

$$
\langle x, y \rangle = h(x^{+}, y^{+}) - h(x^{-}, y^{-}) , \qquad x = x^{+}+x^{-}, \quad y = y^{+}+y^{-} .
$$

Equivalently, since $A^{+}\perp A^{-}$, the companion is $\langle x,y\rangle = h(Jx,y)$.

### The Properties

**Theorem (the symmetry is an involution and a bridge).** Let $A = A^{+}\oplus A^{-}$ be a fundamental decomposition with symmetry $J$ and companion form $\langle\cdot,\cdot\rangle$. Then

$$
J^{2} = \mathrm{id}, \qquad J = 2P^{+}-\mathrm{id} = \mathrm{id}-2P^{-} ,
$$

the subspaces $A^{+}, A^{-}$ are the eigenspaces of $J$ for the eigenvalues $+1$ and $-1$, the companion form is positive definite and Hermitian, $J$ is self-adjoint for the companion, $\langle Jx,y\rangle = \langle x,Jy\rangle$, and

$$
h(x,y) = \langle Jx,y \rangle , \qquad \langle x,y \rangle = h(Jx,y) \qquad \text{for all } x, y \in A .
$$

Moreover $J$ is an isometry of both forms,

$$
h(Jx,Jy) = h(x,y) , \qquad \langle Jx,Jy \rangle = \langle x,y \rangle ,
$$

and it is $h$-self-adjoint, $h(Jx,y) = h(x,Jy)$.

*Proof.* The projections satisfy $P^{+}+P^{-}=\mathrm{id}$, $P^{+}P^{-}=0$ and $(P^{\pm})^{2}=P^{\pm}$, so $J^{2}=P^{+}+P^{-}=\mathrm{id}$ and the eigenvector assertions are the definition of the projections. The companion is positive definite because on the summands it is $\pm h$, which is positive there, and the summands are orthogonal; it is Hermitian because $h$ is and the sign is entrywise real. For the bridge, $Jx = x^{+}-x^{-}$, so $\langle Jx,y\rangle = h(x^{+},y^{+}) - h(-x^{-},y^{-}) = h(x^{+},y^{+})+h(x^{-},y^{-}) = h(x,y)$ by the orthogonality of the summands; the second identity is the first read at $J$ in the first slot. Self-adjointness of $J$ for the companion is $\langle Jx,y\rangle = h(x,y) = \langle x,Jy\rangle$ by the bridge twice, and the isometry of $h$ is $h(Jx,Jy) = \langle J^{2}x,Jy\rangle = \langle x,Jy\rangle = h(x,y)$, with the companion case identical. Finally $h(Jx,y) = \langle J^{2}x,y\rangle = \langle x,y\rangle = h(x,Jy)$. $\square$

**Corollary (the pair of forms determines $J$).** The companion is the unique positive definite form $\langle\cdot,\cdot\rangle$ with $h(x,y) = \langle Jx,y\rangle$ for $J = P^{+}-P^{-}$; conversely, given $h$ and a positive definite companion $\langle\cdot,\cdot\rangle$ whose associated operator $J$ defined by $h(x,y) = \langle Jx,y\rangle$ satisfies $J^{2} = \mathrm{id}$, the pair is a fundamental decomposition with that symmetry.

*Proof.* The first clause is the bridge. For the second, the operator $J$ is self-adjoint for the companion, $\langle Jx,y\rangle = h(x,y) = \varsigma(h(y,x)) = \varsigma(\langle Jy,x\rangle) = \langle x,Jy\rangle$ by the Hermitian property of the two forms, so its eigenspaces $A^{\pm} = \ker(J\mp\mathrm{id})$ are companion-orthogonal and $h$ equals $\pm\langle\cdot,\cdot\rangle$ on them, whence they are definite and the pair is a fundamental decomposition with symmetry $J$. $\square$

**Remark (the companion is not the given form).** For a definite form the companion and the form agree and $J = \mathrm{id}$; for an indefinite one they differ by the sign on $A^{-}$, and it is the companion, not $h$, that carries the norm, the Cauchy–Schwarz inequality and the positivity of *Positivity and the Positive Cone of a Hermitian Form*. The whole point of $J$ is that it lets the definite theory of that article be read on an indefinite object.

## The Eigenspaces and the Definite Companion

### The Projections

**Proposition (the projections from $J$).** With $J$ as above,

$$
P^{+} = \tfrac{1}{2}(\mathrm{id}+J) , \qquad P^{-} = \tfrac{1}{2}(\mathrm{id}-J) ,
$$

the companion reads $\langle x,y\rangle = h(P^{+}x,y) - h(P^{-}x,y)$, and in the notation of the eigenspaces $A^{\pm} = \ker(J \mp \mathrm{id})$ one has $A = A^{+}\oplus A^{-}$ with $(A^{+})^{\perp} = A^{-}$ and $(A^{-})^{\perp} = A^{+}$, each part being definite and hence nondegenerate for the restriction of $h$.

*Proof.* The formulas for the projections solve $J = P^{+}-P^{-}$ together with $P^{+}+P^{-} = \mathrm{id}$, and the orthogonality of the eigenspaces is the orthogonality of the summands, which is part of the definition of the decomposition. $\square$

**Remark (definiteness is carried by the eigenspaces).** The proposition is the reason the eigenspaces, and not the original summands of some other decomposition, are intrinsic to $J$: two fundamental decompositions with the same symmetry have the same eigenspaces, and the symmetry is exactly the determination of the pair of complementary definite subspaces. Changing $J$ is changing the decomposition, and the next but one section shows that this is a genuine freedom.

### The Gram Operators

**Definition.** Let $A$ be free of finite rank over a field with the form $h$ and the companion $\langle\cdot,\cdot\rangle$ of a decomposition, and let $H$ and $G$ be their **Gram matrices** in a common basis, $H_{ij} = h(e_{i},e_{j})$, $G_{ij} = \langle e_{i},e_{j}\rangle$. The **Gram operators** are the multiplications by $H$ and by $G$.

**Proposition (the Gram relation).** In every basis, $H = J^{T}G$, where $J$ is the matrix of the fundamental symmetry and $J^{T}$ is its transpose; if the companion form is the standard one, $G = I$, then $J = H^{T} = \varsigma(H)$, and this is $J = H$ exactly when $H$ is symmetric, that is when its entries lie in the fixed field $k$. The companion is recovered from the given form by $G = J^{T}H$, so the two Gram matrices determine the symmetry and conversely.

*Proof.* The bridge $h(x,y) = \langle Jx,y\rangle$ in matrix form is $x^{T}H\varsigma(y) = (Jx)^{T}G\varsigma(y) = x^{T}J^{T}G\varsigma(y)$ for all $x,y$, whence $H = J^{T}G$; the case $G=I$ gives $J=H^{T}=\varsigma(H)$, which is $H$ when $H$ is symmetric. $\square$

**Theorem (the canonical symmetry).** Let the form be nondegenerate with Gram matrix $H$ Hermitian and invertible over $R$, and let the companion be the one whose Gram matrix is the **modulus** $|H| = (H^{2})^{1/2}$, the positive definite square root of $H^{2}$. Then the companion has the fundamental symmetry $J$ determined by

$$
J^{T} = H\,|H|^{-1} = H\,(H^{2})^{-1/2} , \qquad \text{that is} \qquad J = \varsigma\bigl(H(H^{2})^{-1/2}\bigr) ,
$$

which satisfies $J^{2} = \mathrm{id}$, $J^{T} = \varsigma(J)$, and $h(x,y) = \langle Jx,y\rangle$ for the companion of Gram matrix $|H|$. When $H$ is symmetric — in particular in the bilinear layer, where $\varsigma = \mathrm{id}$ — its transpose is itself and the formula is the classical $J = H(H^{2})^{-1/2} = \operatorname{sign}(H)$; in the general sesquilinear case the transpose on the left is essential, because the bridge reads $H = J^{T}|H|$ in the Gram matrices.

*Proof.* The matrix $H$ is Hermitian, so $H^{2}$ is Hermitian positive definite and $|H| = (H^{2})^{1/2}$ is Hermitian positive definite and a function of $H$; the product $H|H|^{-1}$ commutes with $|H|$ and has square $\mathrm{id}$, so the matrix $J$ with $J^{T} = H|H|^{-1}$ satisfies $J^{2} = \mathrm{id}$ after transposing, and it is Hermitian, $J^{T} = \varsigma(J)$, because $H|H|^{-1}$ is. The bridge is the identity $H = J^{T}|H|$ read on the vectors, $\langle Jx,y\rangle = x^{T}J^{T}|H|\varsigma(y) = x^{T}H\varsigma(y) = h(x,y)$, by the definition of $J^{T}$. $\square$

**Remark (the canonical symmetry is the one the form carries).** The significance of this $J$ is that the companion it produces, of Gram matrix $|H|$, is a function of the given form, so no further choice is made: among all fundamental symmetries of a nondegenerate form this is the distinguished one, and on the models of the article, whose Gram matrices are symmetric, it is the sign $\operatorname{sign}(H) = H(H^{2})^{-1/2}$ computed by the functional calculus on $H$. The other symmetries come from the other choices of companion, and the freedom is genuine, as the next section shows.

## The Adjoints under the Two Forms

**Theorem (the adjoints differ by $J$).** Let $\langle\cdot,\cdot\rangle$ be the companion of a fundamental decomposition with symmetry $J$, and for a bounded operator $T$ let $T^{*}$ be its adjoint for the companion and $T^{\dagger}$ its adjoint for $h$,

$$
\langle Tx,y\rangle = \langle x,T^{*}y\rangle , \qquad h(Tx,y) = h(x,T^{\dagger}y) .
$$

Then

$$
T^{\dagger} = J\,T^{*}\,J ,
$$

and consequently $T$ is $h$-self-adjoint, $T^{\dagger}=T$, if and only if $JT$ is self-adjoint for the companion; $T$ is $h$-unitary, $T^{\dagger}T=TT^{\dagger}=\mathrm{id}$, if and only if $T$ is a $J$-unitary operator, $T^{*}JT = J$; and $T$ is an $h$-isometry, $T^{\dagger}T=\mathrm{id}$, if and only if $T^{*}JT = J$.

*Proof.* For the first identity, $h(Tx,y) = \langle JTx,y\rangle = \langle x,(JT)^{*}y\rangle$ and $h(x,T^{\dagger}y) = \langle Jx,T^{\dagger}y\rangle = \langle x,JT^{\dagger}y\rangle$, the last step by the self-adjointness of $J$ for the companion; the two are equal for all $x$ when $(JT)^{*} = JT^{\dagger}$, that is $T^{\dagger} = J T^{*} J$, since $J^{*}=J$ and $J^{2}=\mathrm{id}$. For the criteria, $T^{\dagger}T = \mathrm{id}$ reads $JT^{*}JT=\mathrm{id}$, that is $T^{*}JT=J$ after applying $J$ on the left; the unitary case is the same identity together with its companion $TT^{\dagger}=\mathrm{id}$, and the self-adjoint case is $T=JT^{*}J$, that is $(JT)^{*}=JT$. $\square$

**Remark (the operator theory of the indefinite case).** The theorem is the precise sense in which the indefinite operator theory is the definite one with $J$ inserted: $h$-self-adjoint becomes $J$-self-adjoint, $h$-unitary becomes $J$-unitary, and the spectral theory becomes the indefinite spectral theory of *The General Spectral Theorem on a Krein Space*. It is the form-layer counterpart of the identity $T^{\dagger} = J T^{*}J$ of the bilinear layer, and the concrete case of the operators of the biquaternion algebra is *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

## Non-Uniqueness and the Canonical Choice

### A One-Parameter Family

**Example (the indefinite plane).** Let $A = \mathbb{R}^{2}$ with the form $h(x,y) = x_{1}y_{1} - x_{2}y_{2}$ of signature $(1,1)$. For every real $t$ put

$$
u_{t} = (\cosh t, \sinh t) , \qquad v_{t} = (\sinh t, \cosh t) .
$$

Then $h(u_{t},u_{t}) = 1$, $h(v_{t},v_{t}) = -1$ and $h(u_{t},v_{t}) = 0$, so $A = \mathbb{R}u_{t}\oplus\mathbb{R}v_{t}$ is a fundamental decomposition, and the symmetry of the decomposition is

$$
J_{t} = \begin{pmatrix} \cosh 2t & -\sinh 2t \\ \sinh 2t & -\cosh 2t \end{pmatrix} .
$$

Each $J_{t}$ has $J_{t}^{2} = \mathrm{id}$, fixes $u_{t}$ and negates $v_{t}$, and is self-adjoint for the companion $\langle x,y\rangle_{t} = h(J_{t}x,y)$, whose Gram matrix is $\begin{pmatrix}\cosh 2t & -\sinh 2t \\ -\sinh 2t & \cosh 2t\end{pmatrix}$, positive definite with determinant one. The fundamental symmetries therefore form a one-parameter family, so the symmetry of an indefinite form is not determined by the form. At $t = 0$ the symmetry is $\mathrm{diag}(1,-1)$ and the companion is the Euclidean form, the canonical choice of the next proposition.

**Remark (the geometry of the family).** The positive lines $\mathbb{R}u_{t}$ are exactly the lines on which $h$ is positive definite, that is the lines inside the light cone $x_{1}^{2} > x_{2}^{2}$; the family in the example is that of the positive lines, and the freedom in $J$ is the freedom in choosing the positive part of a decomposition. In higher signature the set of fundamental symmetries is the set of pairs of complementary maximal definite subspaces, and it is parametrised by the contractions between two fixed such subspaces, the **angular operators** of the Krein-space theory.

### The Distinguished Choice

**Theorem (the canonical symmetry is well defined).** Let the form be nondegenerate and let a definite companion be fixed, with $J$ defined by $h(x,y) = \langle Jx,y\rangle$ and $J^{2}=\mathrm{id}$. Then $J$ is the unique fundamental symmetry of the form whose companion is the fixed one; and among all fundamental symmetries of a form given by a Hermitian invertible Gram matrix $H$, the symmetry determined by $J^{T} = H(H^{2})^{-1/2}$ is the unique one whose companion is the modulus $|H|$.

*Proof.* The first clause is the corollary of the bridge. For the second, diagonalise: by the principal-axis theorem there is a basis in which $H = \operatorname{diag}(\lambda_1,\dots,\lambda_m)$ is real and the companion is $G = \lvert H\rvert = \operatorname{diag}(\lvert\lambda_1\rvert,\dots,\lvert\lambda_m\rvert)$, and in that basis the symmetry of the companion is $\operatorname{diag}(f(\lambda_1),\dots,f(\lambda_m))$ with $f(\lambda)^{2} = 1$. If $f(\lambda_i) = -1$ for some $i$ with $\lambda_i > 0$, the basis vector $e_i$ lies in the negative part $A^{-}$ while $h(e_i,e_i) = \lambda_i > 0$, contrary to the negative definiteness of $A^{-}$, and symmetrically if $f(\lambda_i) = +1$ for some $\lambda_i < 0$; hence $f(\lambda_i) = \operatorname{sign}(\lambda_i)$ for every $i$. In a basis diagonalising $H$ the matrix $H$ is real and symmetric, so the symmetry is $\operatorname{sign}(H) = H\lvert H\rvert^{-1}$ there, and in the original basis it is the matrix $J$ with $J^{T} = H\lvert H\rvert^{-1}$. $\square$

**Remark (the choice made in the layer).** The layer with a form, *Topological Sesquialgebras with a Form*, takes the form as given and does not prescribe a decomposition; the operator theory of the indefinite case, *The Adjoint under a Hermitian Form*, uses a chosen fundamental symmetry, and the statements are invariant under the change of the choice in the sense that the definite statements transported by two different symmetries are related by the angular operator. The canonical symmetry is the convention that removes the choice when the form is nondegenerate and complete.

## Worked Cases

### The Plane

**Example (the plane, continued).** On $\mathbb{R}^{1,1}$ the canonical symmetry relative to the standard basis is $J = \operatorname{diag}(1,-1) = J_{0}$, with the Euclidean companion; the companion of $J_{t}$ is the form of Gram matrix $\begin{pmatrix}\cosh2t&-\sinh2t\\-\sinh2t&\cosh2t\end{pmatrix}$; and the $\langle\cdot,\cdot\rangle_{t}$-adjoint and the $h$-adjoint of an operator differ by conjugation by $J_{t}$. The example is the smallest in which all the statements of the article are visible, and it is the one in which the non-uniqueness of $J$ is exact.

### A Pontryagin Space

**Example (the Pontryagin space $\Pi_{1}$).** Let $H$ be a Hilbert space and let $A = H\oplus\mathbb{R}$ carry the form $h((x,s),(y,t)) = \langle x,y\rangle_{H} - st$, of negative index one. The decomposition $A^{+} = H\oplus 0$, $A^{-} = 0\oplus\mathbb{R}$ is fundamental, the symmetry is $J = \mathrm{id}_{H}\oplus(-\mathrm{id})$, the companion is the Hilbert form on the sum, and $A$ is a **Pontryagin space** of index one. The canonical symmetry relative to the Hilbert form is again $J$, and the $h$-unitary operators are the $J$-unitary ones, the structure studied for the bilinear layer in *Krein Spaces* and *The Krein Isometry Group and Its $J$-Contractions*. The example shows that the indefinite index one case is not exotic: it is the Hilbert space to which a single negative direction has been adjoined.

### The Biquaternion Algebra

**Example (the indefinite biquaternion form).** On $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the coefficient vector $\tilde Q = \sum_{\mu}Q_{\mu}e_{\mu}$ and the sign vector $\varepsilon = (1,-1,-1,-1)$, the **quaternion sesquilinear form** of *The Four Pairings of the Biquaternion Algebra*, §*The Four Pairings*,

$$
h_{\natural*}(P,Q) = \operatorname{Sc}(P^{\natural}Q^{*}) = \sum_{\mu}\varepsilon_{\mu}P_{\mu}\overline{Q_{\mu}} ,
$$

is Hermitian and of signature $(2,6)$ over $\mathbb{R}$, by *The Indefinite Case and the Signature*. Against the definite companion $\langle P,Q\rangle_{*} = \sum_{\mu}P_{\mu}\overline{Q_{\mu}}$, the complex sesquilinear form of the same article, the bridge is $h_{\natural*}(P,Q) = \langle JP,Q\rangle_{*}$ with

$$
J = \operatorname{diag}(1,-1,-1,-1) ,
$$

acting on the complex coefficient vector; $J$ squares to $\mathrm{id}$ and is self-adjoint, the positive eigenspace is the complex line spanned by $e_{0}$ — two real dimensions — and the negative eigenspace is the span of $e_{1}, e_{2}, e_{3}$ — six real dimensions, which is the signature $(2,6)$. The form $h_{*}$ is itself definite and is its own companion, of symmetry $\mathrm{id}$. The example is the finite-dimensional model in which the two signs and the operator $J$ are read on the four complex coordinates, and it is the form-layer reading of the indefinite biquaternion form whose operators are *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

## The Definite Case and the Collapse

**Theorem (the definite case).** Let $h$ be positive definite. Then the only fundamental decomposition is $A = A\oplus 0$, the companion is $h$ itself, $J = \mathrm{id}$, the bridge is trivial, and the adjoint identity $T^{\dagger} = J T^{*} J$ reduces to $T^{\dagger} = T^{*}$: the theory of the article is the theory of *The Norm Defined by a Form* and *The Adjoint under a Hermitian Form*, with no $J$ to insert.

*Proof.* A positive definite space has no nonzero negative definite subspace, so $A^{-} = 0$; the remaining statements are the definitions at $J=\mathrm{id}$. $\square$

**Theorem (the collapse at the trivial involution).** Let $\varsigma = \mathrm{id}$. Then the form is symmetric and bilinear, the canonical symmetry is the sign of the Gram matrix relative to a symmetric definite form, and the construction is that of *The Fundamental Symmetry* of the bilinear layer: $h(x,y) = \langle Jx,y\rangle$ with $J^{2}=\mathrm{id}$ and $J$ self-adjoint for the symmetric companion. The Krein space that the completed companion produces is *Krein Spaces*, named here and developed in the bilinear degree-2 form category.

*Proof.* At $\varsigma=\mathrm{id}$ the Hermitian property is symmetry and the semilinear slots are linear, so each statement is the corresponding statement above read for a symmetric bilinear form; the identification with *The Fundamental Symmetry* and *Krein Spaces* is the collapse theorem of *Topological Sesquialgebras with a Form*, §*The Collapse at the Trivial Involution*. $\square$

**Remark (what the collapse preserves).** The collapse preserves the operator $J$ and the bridge and changes only the two forms from Hermitian to symmetric; the sesquilinear content of the article is the presence of two involutions, the base $\varsigma$ and the algebra $*$, in the slot rules of the forms that $J$ bridges, and it disappears when $\varsigma=\mathrm{id}$ and the forms become bilinear.

## Summary

A **fundamental decomposition** of an indefinite Hermitian form is an $h$-orthogonal splitting $A = A^{+}\oplus A^{-}$ into a positive definite and a negative definite part, and its **fundamental symmetry** is $J = P^{+}-P^{-}$. The symmetry satisfies $J^{2} = \mathrm{id}$, has the summands for eigenspaces, is self-adjoint and isometric for both the form and the **companion form** $\langle x,y\rangle = h(x^{+},y^{+}) - h(x^{-},y^{-})$, which is positive definite, and it is the **bridge** $h(x,y) = \langle Jx,y\rangle$, $\langle x,y\rangle = h(Jx,y)$ between the indefinite form and the definite one. The **adjoints** under the two forms differ by conjugation by $J$, $T^{\dagger} = JT^{*}J$, so the $h$-self-adjoint, $h$-unitary and $h$-isometric operators are the $J$-self-adjoint, $J$-unitary and $J$-isometric ones, and the indefinite operator theory is the definite one with $J$ inserted. The symmetry is **not determined** by the form — on the plane of signature $(1,1)$ it is the one-parameter family $J_{t}$ — but a distinguished choice is available when the form is nondegenerate, the **canonical symmetry** $J$ with $J^{T} = H(H^{2})^{-1/2}$ built from the Gram matrix, which is $J = H(H^{2})^{-1/2}$ when $H$ is symmetric and is the unique symmetry whose companion has Gram matrix $\lvert H\rvert$. The worked cases are the indefinite plane, the Pontryagin space of index one and the indefinite biquaternion form of signature $(2,6)$; at $\varsigma = \mathrm{id}$ the construction is that of the **bilinear** layer, whose completed object is a Krein space.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A^{+}$, $A^{-}$ | the positive definite and negative definite parts of a fundamental decomposition |
| $A^{+}\perp A^{-}$ | $h$-orthogonality of the two parts |
| $J = P^{+}-P^{-}$ | the fundamental symmetry of the decomposition |
| $J^{2} = \mathrm{id}$ | the symmetry is an involution with eigenspaces $A^{\pm}$ |
| $\langle x,y\rangle = h(Jx,y)$ | the companion form, positive definite |
| $h(x,y) = \langle Jx,y\rangle$ | the bridge between the two forms |
| $P^{\pm} = \tfrac{1}{2}(\mathrm{id}\pm J)$ | the projections of the decomposition |
| $H$, $G$, $H = J^{T}G$ | the Gram matrices of the form and the companion in a basis |
| $J^{T} = H(H^{2})^{-1/2}$ | the canonical symmetry of a nondegenerate form; $J = H(H^{2})^{-1/2}$ when $H$ is symmetric |
| $T^{\dagger} = JT^{*}J$ | the $h$-adjoint in terms of the companion adjoint |
| $T^{*}JT = J$ | the criterion that $T$ be $h$-isometric, that is $J$-unitary |
| $(1,1)$, $(2,6)$, $\Pi_{1}$ | the signatures of the worked examples |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the fundamental decomposition, the fundamental symmetry and the companion form.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the Gram operators, the canonical symmetry and the $J$-self-adjoint and $J$-unitary operators.
- Thomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the angular operators, the non-uniqueness of the fundamental symmetry and the Pontryagin spaces.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the signature, the inertia and the Hermitian forms over a field with involution.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the bounded operators, adjoints and the positive square root of a positive operator.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the Hermitian matrices, their modulus $(H^{2})^{1/2}$ and the principal-axis theorem.
