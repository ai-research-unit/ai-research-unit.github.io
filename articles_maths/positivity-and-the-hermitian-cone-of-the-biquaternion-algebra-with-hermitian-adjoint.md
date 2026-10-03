# __Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

An involution orders an algebra. Once an element $\tilde T$ has a conjugate $\tilde{T}^{*}$, the fixed elements play the role of the real numbers, the elements $\tilde{T}^{*}\tilde T$ the role of squares of lengths, and the question whether those squares are "positive" is the question whether the dagger is a **positive involution**. On the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with the Hermitian conjugation whose fixed space is the Hermitian sector $\mathbb{M}_+$ and whose anti-fixed space is the anti-Hermitian sector $\mathbb{M}_-$ (*Biquaternion Algebra*, *Biquaternion Involution Lattice*), all three notions are available, and this article treats them: the two sectors and their splitting of the algebra, the cone of elements $\tilde{Q}\tilde{Q}^{*}$, the positivity of the involution, the polar decomposition it induces, and the Cartan involution of the group of units with its Lie-algebra decomposition.

The result that organises the article is that, in the biquaternion algebra, **positivity holds** — and the reason is a change of Clifford structure, not a change of the algebra. The scalar form of the dagger is $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$, strictly positive off zero; so the dagger is positive, the cone of squares is the cone of the positive semidefinite Hermitian elements, and every element has a polar decomposition $\tilde{Q}=U\lvert\tilde{Q}\rvert$ with $U$ unitary. But the biquaternion norm $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, the interval of the corpus, is a *complex, indefinite* form that vanishes on the null cone, and the temptation is to conclude that no positivity can hold. The general theorem, that the dagger of a real Clifford algebra is positive exactly when the quadratic form is negative definite (*Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*), seems to forbid it outright, since $N$ is not negative definite. The resolution is the one that article itself records under the exchange of sides: a positive definite quadratic form does not fail to give a cone, it gives the cone of the **other** involution, and the involution to use is reversion rather than Clifford conjugation. The dagger of $\mathbb{B}$ is exactly that reversion, the reversion of the positive definite Clifford structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ (*The Clifford Structure of the Biquaternion Algebra*, *Biquaternion Versors and the Orthogonal Group*), so its positivity and the indefiniteness of $N$ are statements about two different structures on one algebra, and they are compatible.

Positivity is not only consistent here, it is simple, and that simplicity is the second theme. Because the form $\mathrm{Sc}(\tilde{T}^{*}\tilde W)$ is positive definite, every subspace of $\mathbb{B}$ inherits a positive definite restriction, so no subspace is isotropic and the module theory of the companion article needs no correction (*Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*). And because the algebra is a full complex matrix algebra, the cone is a **symmetric cone**: self-dual for the scalar form, with the positive definite elements as interior, and the group of units decomposing as $U(2)\cdot\exp(\mathbb{M}_+)$ along the Cartan involution.

The cone of the two-sided operators is described in *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, §*The Image of the Identity and the Cone*, where $\{\Theta_{\tilde{Q}}(e_0)\}=\{\tilde{Q}\tilde{Q}^{*}\}$ is read as the image of the identity; the present article is its dedicated counterpart, and it does not repeat the operator statements. The scalar and the algebra-valued forms are *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*; the Jordan structure of $\mathbb{M}_+$ and its isotropic cone are *Biquaternion Hermitian Subspace*; the symmetric space is cited from *Symmetric Spaces*; and the general theory, with the exchange of sides and the Cartan involution, is *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*.

## Self-Adjoint and Skew Elements

**Definition.** An element $\tilde{Q}$ is **Hermitian**, or self-adjoint, if $\tilde{Q}^{*}=\tilde{Q}$, and **skew-adjoint** if $\tilde{Q}^{*}=-\tilde{Q}$. Write

$$
\mathrm{Herm}=\{\tilde{Q}:\tilde{Q}^{*}=\tilde{Q}\}=\mathbb{M}_+,
\qquad
\mathrm{Skew}=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\}=\mathbb{M}_-.
$$

**Proposition (the splitting).** The dagger is an anti-involution of order two, so $\mathrm{Herm}$ and $\mathrm{Skew}$ are real subspaces and

$$
\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-,
\qquad
\tilde{Q}=\tfrac12\bigl(\tilde{Q}+\tilde{Q}^{*}\bigr)+\tfrac12\bigl(\tilde{Q}-\tilde{Q}^{*}\bigr),
$$

the splitting being the eigen-decomposition of the involution.

*Proof.* $(\tilde{Q}^{*})^{\dagger}=\tilde{Q}$ gives $\mathrm{Herm}\cap\mathrm{Skew}=0$, and the displayed formula exhibits the sum, its first term fixed by the dagger and its second negated, because $2$ is invertible in $\mathbb{C}$ (the base field of the algebra, with the identity involution).

**Proposition (squares are Hermitian).** For every $\tilde{Q}$ the element $\tilde{Q}^{*}\tilde{Q}$ is Hermitian, and so is $\tilde{Q}\tilde{Q}^{*}$.

*Proof.* $(\tilde{Q}^{*}\tilde{Q})^{\dagger}=\tilde{Q}^{*}(\tilde{Q}^{*})^{\dagger}=\tilde{Q}^{*}\tilde{Q}$, and the second statement is the first with $\tilde{Q}$ replaced by $\tilde{Q}^{*}$.

**Remark (the two sectors in matrix form).** Under the isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_k)=-i\sigma_k$, the Hermitian sector maps onto the Hermitian matrices, $\Phi(\mathbb{M}_+)=H_2(\mathbb{C})$, and the anti-Hermitian sector onto the skew-Hermitian ones, $\Phi(\mathbb{M}_-)=u(2)$; both are real four-dimensional subspaces, and the splitting of the proposition is the decomposition of a matrix into its Hermitian and skew-Hermitian parts (*Biquaternion 2×2 Matrix Element Representation*, *Biquaternion Hermitian Subspace*). This is the reason the two sectors behave so differently under every formula of the article: one is the observable side, the other the generator side.

## Positivity of the Involution

**Definition.** The dagger is **positive** if

$$
\mathrm{Sc}\bigl(\tilde{Q}^{*}\tilde{Q}\bigr)>0\qquad\text{for every }\tilde{Q}\neq0 .
$$

**Theorem (the biquaternion dagger is positive).** For every biquaternion,

$$
\mathrm{Sc}\bigl(\tilde{Q}^{*}\tilde{Q}\bigr)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\ \ge 0 ,
$$

with equality if and only if $\tilde{Q}=0$. Hence the dagger of $\mathbb{B}$ is a positive involution and the scalar form $(\tilde{Q},\tilde{R})=\mathrm{Sc}(\tilde{Q}^{*}\tilde{R})$ is positive definite.

*Proof.* Write $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. By *The Hermitian Form on the Biquaternion Algebra* the diagonal of the Hermitian form is $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$, and $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$ by the same computation applied to $\tilde{Q}^{*}$, whose coefficients are the conjugates $Q_{\bar{\mu}}$ of those of $\tilde{Q}$. A sum of non-negative reals vanishes only if each term does, so the form vanishes only at $\tilde{Q}=0$; and the same computation with $\tilde{R}$ in place of $\tilde{Q}^{*}$ makes the sesquilinear form positive definite in the basis $e_0,e_1,e_2,e_3$, where its Gram matrix is the identity.

**Remark (why no contradiction with the general theorem).** The general article proves that the dagger of a real Clifford algebra is positive exactly when the quadratic form is negative definite, and it adds the correction that a positive definite form gives the cone of the *other* involution, the two statements being exchanged by $e_i\mapsto ie_i$ (*Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*, §*Remark (the exchange of sides)*). The biquaternion algebra is that exchange in force. Its dagger is not the Clifford conjugation of the Minkowski structure $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$; it is the **reversion** of the positive definite structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, in which the vectors are the imaginary quaternions $ie_k$ and reversion fixes them, which is why $ie_3$ is Hermitian while $e_3$ is not (*Biquaternion Versors and the Orthogonal Group*, §*The Two Involutions*). The scalar form it licenses is the Euclidean form $\sum_\mu\lvert Q_\mu\rvert^{2}$, not the quaternion norm. The two structures on the one algebra carry two forms:

| structure | quadratic form | on the vectors | involution | definite? |
|---|---|---|---|---|
| $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ | $\sum_\mu\lvert Q_\mu\rvert^{2}$, positive definite | $ie_k$ | reversion $={}^{*}$ | positive |
| $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ | $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, indefinite | Minkowski $V$ | Clifford conjugation | indefinite |

**Corollary ($C^{*}$-structure).** With the dagger, $\mathbb{B}\cong M_2(\mathbb{C})$ is a finite-dimensional $C^{*}$-algebra — the algebra of bounded operators on the two-dimensional Hilbert space $S$ of *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* — and the scalar form is its Hilbert–Schmidt inner product, $\mathrm{Sc}(\tilde{T}^{*}\tilde W)=\tfrac12\operatorname{Tr}(\Phi(\tilde T)^{\dagger}\Phi(\tilde W))$ (*Biquaternion 2×2 Matrix Element Representation*). Every theorem of the $C^{*}$-theory of the positive cone applies, and the next two sections read three of them in biquaternion terms.

## The Hermitian Cone

**Definition.** The **Hermitian cone** of the algebra is the image of the squaring map,

$$
P=\bigl\{\tilde{Q}^{*}\tilde{Q}:\tilde{Q}\in\mathbb{B}\bigr\}.
$$

Its elements are Hermitian by the proposition above, and it contains $0$ and $e_0$.

**Theorem (the cone in matrix form).** The cone is the set of positive semidefinite Hermitian elements,

$$
P=\bigl\{H\in\mathbb{M}_+:\Phi(H)\succeq0\bigr\}=\bigl\{\tilde{Q}\tilde{Q}^{*}:\tilde{Q}\in\mathbb{B}\bigr\},
$$

and it is a closed convex cone of real dimension four, pointed, generating the Hermitian sector. It is **self-dual** for the scalar form: $H\in P$ if and only if $(H,K)\ge0$ for every $K\in P$.

*Proof.* $\Phi(\tilde{Q}^{*}\tilde{Q})=\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q})\succeq0$ is the standard form of a positive semidefinite matrix, so $P$ is contained in the positive semidefinite Hermitian elements; conversely a positive semidefinite Hermitian $H$ has a positive semidefinite Hermitian square root $H^{1/2}$, and $H=H^{1/2}(H^{1/2})^{\dagger}=\tilde{Q}^{*}\tilde{Q}$ with $\tilde{Q}=H^{1/2}$, which is Hermitian and so satisfies $\tilde{Q}^{*}=\tilde{Q}$. The second description follows because $\tilde{Q}\mapsto\tilde{Q}^{*}$ is a bijection. Closedness, convexity and the four real dimensions are those of the positive semidefinite cone $H_2(\mathbb{C})_{\succeq0}$, which has real dimension four. Pointedness: $H\in P\cap(-P)$ means $H\succeq0$ and $-H\succeq0$, so $H=0$. Generation: the spectral decomposition writes any Hermitian $H$ as $H_+-H_-$ with $H_\pm\succeq0$. Self-duality: if $H\succeq0$ and $K\succeq0$ then $(H,K)=\mathrm{Sc}(HK)=\tfrac12\operatorname{Tr}(HK)=\tfrac12\operatorname{Tr}(H^{1/2}KH^{1/2})\ge0$, so $P\subseteq \bar{P}$; conversely if $(H,K)\ge0$ for every $K\in P$, testing against the rank-one elements $K=\tilde E\tilde{E}^{*}$ gives $\tilde{E}^{*}\Phi(H)\tilde E\ge0$ for every $\tilde E\in\mathbb{C}^2$, which is $H\succeq0$.

**Corollary (the interior is the image of the units).** The interior of the cone is the set of positive definite Hermitian elements, and

$$
P^{\circ}=\bigl\{\tilde{Q}^{*}\tilde{Q}:N(\tilde{Q})\neq0\bigr\}=\bigl\{\tilde{Q}\tilde{Q}^{*}:\tilde{Q}\in\mathbb{B}^{\times}\bigr\},
$$

singled out by any of the equivalent conditions $N(\tilde{Q})\neq0$, $\tilde{Q}$ invertible, $\tilde{Q}^{*}\tilde{Q}\succ0$. The boundary consists of the nonzero singular squares, of rank one.

*Proof.* $\det\Phi(\tilde{Q}^{*}\tilde{Q})=\lvert\det\Phi(\tilde{Q})\rvert^{2}=\lvert N(\tilde{Q})\rvert^{2}$ by the multiplicativity of the determinant and $N=\det\Phi$ (*Biquaternion Norm and Invertibility*, *Biquaternion 2×2 Matrix Element Representation*), and a positive semidefinite matrix is positive definite exactly when its determinant is nonzero. The equivalence of $N(\tilde{Q})\neq0$ with invertibility is the invertibility criterion of *Biquaternion Norm and Invertibility*.

**Remark (the two cones of the Hermitian sector).** The word "cone" is already used in the algebra for a different set, and the two must not be confused. The **isotropic cone** of $\mathbb{M}_+$ is the null set of the biquaternion norm there, $q_0^{2}=(\mathbf{q}',\mathbf{q}')$, the part of the zero-divisor locus that lies in the sector (*Biquaternion Hermitian Subspace*, *Biquaternion Zero Divisors*); it is a cone of real dimension three, and it is indefinite — it contains the nonzero null elements. The **Hermitian cone** $P$ of this article is the cone of squares, of real dimension four; it meets the null set only along its boundary, where it is the forward half of the isotropic cone. The isotropic cone is the **boundary** of $P$ together with the boundary of $-P$, and the two statements are related by the interval form of the next section.

## The Cone, the Interval Form and the Isotropic Cone

**Setting.** The Hermitian sector is a real four-dimensional space on which the biquaternion norm restricts to a quadratic form of signature $(1,3)$: for $H=t e_0+i\mathbf{u}$ with $t\in\mathbb{R}$ and $\mathbf{u}\in\mathbb{R}^{3}$, $N(H)=t^{2}-\lvert\mathbf{u}\rvert^{2}$ (*Biquaternion Versors and the Orthogonal Group*, §*The Form and its Isometries*). In the matrix model $\Phi(H)=t I+\mathbf{u}\cdot\boldsymbol{\sigma}$, whose eigenvalues are $t\pm\lvert\mathbf{u}\rvert$.

**Theorem (the cone is the forward cone of the interval form).** For $H\in\mathbb{M}_+$, the following are equivalent: $H\in P$; the two eigenvalues of $\Phi(H)$ are non-negative; $t\ge\lvert\mathbf{u}\rvert$. Hence

$$
P=\bigl\{t e_0+i\mathbf{u}:t\ge\lvert\mathbf{u}\rvert\bigr\},
$$

the closed **forward light cone** of the interval form $N$ on $\mathbb{M}_+$; its interior is $t>\lvert\mathbf{u}\rvert$, the positive definite elements; and its boundary is the forward half $t=\lvert\mathbf{u}\rvert$ of the isotropic cone, that is the nonzero null elements of $\mathbb{M}_+$ with non-negative time component.

*Proof.* A Hermitian matrix is positive semidefinite exactly when its eigenvalues are non-negative, and the eigenvalues of $tI+\mathbf{u}\cdot\boldsymbol{\sigma}$ are $t\pm\lvert\mathbf{u}\rvert$, both non-negative exactly when $t\ge\lvert\mathbf{u}\rvert$. On $t=\lvert\mathbf{u}\rvert$ one eigenvalue vanishes, so $\det\Phi(H)=N(H)=0$ by $N=\det\Phi$, and for $t>\lvert\mathbf{u}\rvert$ both are positive.

**Corollary (the extreme rays and the projective line).** The extreme rays of $P$ are the nonzero rank-one squares, and in the matrix model they are the outer products

$$
\tilde{Q}\tilde{Q}^{*}\longleftrightarrow \tilde E\tilde{E}^{*},
\qquad \tilde E\in\mathbb{C}^{2},\ \tilde E\neq0,
$$

the pair $(\tilde E)$ being determined up to a nonzero complex scalar; so the extreme rays are parametrised by the projective line $\mathbb{P}^{1}(\mathbb{C})$. On the boundary each element is a product $\pm \tilde E\tilde{E}^{*}$ of a spinor and its conjugate, which is the factorisation of a null element, and the parametrisation is the projective form of the two rulings of the null quadric (*Biquaternion Spin Geometry*, *Biquaternion 2×2 Matrix Element Representation*).

**Remark (the cone and the two-sided operators).** The cone appeared in the operator family as the image of the identity, $\Theta_{\tilde{Q}}(e_0)=\tilde{Q}\tilde{Q}^{*}$ (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, §*The Image of the Identity and the Cone*), and as the positive cone over which the completely positive maps are defined (*Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*). What is added here is the intrinsic description: $P$ is the cone of squares of the involution, the forward cone of the interval form, and the symmetric cone of the Jordan algebra $\mathbb{M}_+$ (*Biquaternion Hermitian Subspace*), the three being one object read three ways.

## The Polar Decomposition

**Theorem (the dagger polar decomposition).** Every biquaternion has a decomposition

$$
\tilde{Q}=U\,\lvert\tilde{Q}\rvert,
\qquad
\lvert\tilde{Q}\rvert=\bigl(\tilde{Q}^{*}\tilde{Q}\bigr)^{1/2}\in P,
\qquad
U^{\dagger}U=e_0,
$$

with $\lvert\tilde{Q}\rvert$ the positive square root in the cone and $U$ in the unitary slice. The decomposition is unique exactly when $\tilde{Q}$ is invertible, that is exactly outside the null cone.

*Proof.* The element $\tilde{Q}^{*}\tilde{Q}$ is Hermitian and in the cone, so in the matrix algebra it has a unique positive semidefinite square root $\lvert\tilde{Q}\rvert$, and $\Phi(\lvert\tilde{Q}\rvert)=\lvert\Phi(\tilde{Q})\rvert$ in the sense of the positive square root of a positive semidefinite matrix. For invertible $\tilde{Q}$ set $U=\tilde{Q}\lvert\tilde{Q}\rvert^{-1}$; then $U^{\dagger}U=\lvert\tilde{Q}\rvert^{-1}\tilde{Q}^{*}\tilde{Q}\lvert\tilde{Q}\rvert^{-1}=\lvert\tilde{Q}\rvert^{-1}\lvert\tilde{Q}\rvert^{2}\lvert\tilde{Q}\rvert^{-1}=e_0$, and the uniqueness of the positive square root makes the pair unique. For singular $\tilde{Q}$ the element $\lvert\tilde{Q}\rvert$ is a nonzero singular positive element and the unitary factor is not unique; the decomposition still exists by the matrix statement.

**Corollary (the absolute value and the norm).** $\lvert\tilde{Q}\rvert$ is Hermitian, positive semidefinite, and

$$
N\bigl(\lvert\tilde{Q}\rvert\bigr)=\lvert N(\tilde{Q})\rvert\ \ge 0 ,
$$

so the absolute value lands in the Hermitian sector with a *non-negative* norm there, and $\tilde{Q}$ is invertible if and only if $\lvert\tilde{Q}\rvert$ lies in the interior of the cone.

*Proof.* $N(\lvert\tilde{Q}\rvert)=\det\Phi(\lvert\tilde{Q}\rvert)=\det\lvert\Phi(\tilde{Q})\rvert=\lvert\det\Phi(\tilde{Q})\rvert=\lvert N(\tilde{Q})\rvert$, the third equality being the product of the non-negative eigenvalues of the positive semidefinite matrix $\lvert\Phi(\tilde{Q})\rvert$. The invertibility statement is the corollary of the previous section.

**Remark (the two polar decompositions of the algebra).** This decomposition is not the polar element representation $\tilde{Q}=r e^{i\alpha}B\hat{q}$ of *Biquaternion Polar Element Representation*. The dagger decomposition separates a **unitary** factor from a **positive** one, exists for every element, and is unique off the null cone; the polar element representation separates a scale, a central phase, a Hermitian positive boost and a unit real quaternion, exists on the same set off the null cone. The two agree in domain and differ in factors: the dagger decomposition absorbs the scale and the phase into the unitary factor, while the polar word exhibits them. Their common failure set is the null cone, and for the same reason: it is where the modulus ceases to be invertible, so that the decomposition loses its uniqueness while the factors that remain are those of the boundary.

**Corollary (the real-quaternion slice).** On the slice $\mathbb{H}_{\mathbb{B}}$ of real coefficients the dagger is the quaternion conjugation, $\tilde{Q}^{*}=\tilde{Q}^{\natural}$, so

$$
\tilde{Q}^{*}\tilde{Q}=N(\tilde{Q})e_0 ,
$$

a real scalar, and $\lvert\tilde{Q}\rvert=\lvert N(\tilde{Q})\rvert^{1/2}e_0$ with $U=\tilde{Q}/\lvert N(\tilde{Q})\rvert^{1/2}$ for $N(\tilde{Q})>0$. The cone therefore meets that slice in the ray $\mathbb{R}_{\ge0}e_0$, and on it the decomposition reduces to the polar decomposition of a quaternion, as the general article records for its quaternion example: $\tilde{Q}^{*}\tilde{Q}$ is a non-negative real scalar and $U$ lies in the unit sphere $SU(2)=\mathrm{Spin}(3)$.

*Proof.* On the slice the coefficient conjugation is the identity, so $\tilde{Q}^{*}=\tilde{Q}^{\natural}$, and $\tilde{Q}^{\natural}\tilde{Q}=N(\tilde{Q})e_0$ by the defining identity of the quaternion norm (*Biquaternion Norm and Invertibility*). The rest is the theorem with a scalar absolute value.

## The Cartan Involution

**Definition.** On the group of units $\mathbb{B}^{\times}=GL(2,\mathbb{C})$ put

$$
\theta(\tilde{Q})=\bigl(\tilde{Q}^{*}\bigr)^{-1}.
$$

**Proposition (an automorphism of order two).** $\theta$ is an automorphism of the group of units of order two, its fixed set is exactly the unitary slice,

$$
\theta(\tilde{Q})=\tilde{Q}\iff\tilde{Q}^{*}\tilde{Q}=e_0\iff\tilde{Q}\in U=U(2),
$$

and its differential at the identity is $\mathrm{d}\theta=-{}^{*}$, which is $+1$ on the anti-Hermitian sector and $-1$ on the Hermitian sector.

*Proof.* $\theta(\tilde{Q}\tilde{R})=((\tilde{Q}\tilde{R})^{\dagger})^{-1}=(\tilde{R}^{*}\tilde{Q}^{*})^{-1}=(\tilde{Q}^{*})^{-1}(\tilde{R}^{*})^{-1}=\theta(\tilde{Q})\theta(\tilde{R})$, so $\theta$ is an automorphism; $\theta^{2}(\tilde{Q})=(((\tilde{Q}^{*})^{-1})^{\dagger})^{-1}=(\tilde{Q}^{-1})^{-1}=\tilde{Q}$, so it has order two. Its fixed set is $\{\tilde{Q}:(\tilde{Q}^{*})^{-1}=\tilde{Q}\}=\{\tilde{Q}:\tilde{Q}^{*}\tilde{Q}=e_0\}$, the slice. For the differential, $\theta(e_0+t \tilde A)\equiv e_0-t \tilde{A}^{*}$ to first order, so $\mathrm{d}\theta(\tilde A)=-\tilde{A}^{*}$, which is $\tilde A$ on $\mathbb{M}_-$ and $-\tilde A$ on $\mathbb{M}_+$.

**Theorem (Cartan decomposition).** With the commutator bracket $[\tilde A,\tilde D]=\tilde A\tilde D-\tilde D\tilde A$,

$$
[\mathbb{M}_-,\mathbb{M}_-]\subseteq\mathbb{M}_-,
\qquad
[\mathbb{M}_-,\mathbb{M}_+]\subseteq\mathbb{M}_+,
\qquad
[\mathbb{M}_+,\mathbb{M}_+]\subseteq\mathbb{M}_- .
$$

*Proof.* For $\tilde{A}^{*}=-\tilde A$ and $\tilde{D}^{*}=-\tilde D$, $[\tilde A,\tilde D]^{\dagger}=(\tilde A\tilde D-\tilde D\tilde A)^{\dagger}=\tilde{D}^{*}\tilde{A}^{*}-\tilde{A}^{*}\tilde{D}^{*}=\tilde D\tilde A-\tilde A\tilde D=-[\tilde A,\tilde D]$, giving the first inclusion; the other two are the same computation with the signs of one or both arguments changed.

**Corollary (the group decomposition and the symmetric space).** The anticommuting eigenspaces of $\mathrm{d}\theta$ give the Cartan decomposition of the Lie algebra,

$$
\mathfrak{gl}(2,\mathbb{C})=\mathbb{M}_-\oplus\mathbb{M}_+\cong u(2)\oplus H_2(\mathbb{C}),
$$

with $\mathbb{M}_-$ the Lie algebra of the slice $U(2)$ and $\mathbb{M}_+$ the tangent space of the symmetric space; at the group level,

$$
\mathbb{B}^{\times}=U\cdot\exp(\mathbb{M}_+),
\qquad
\mathbb{B}^{\times}/U\cong P^{\circ},
$$

every invertible element being uniquely a unitary times the exponential of a Hermitian element, and the quotient being the interior of the cone, the positive definite Hermitian elements. This is the Cartan decomposition of a reductive group, read in the algebra; the general theory is *Symmetric Spaces* and the Lie-theoretic part of it in *Biquaternion Lie Group and Exponential Structure*.

*Proof.* The exponential of a Hermitian element is positive definite, the exponential of the whole sector $\mathbb{M}_+$ is the whole interior of the cone, and the decomposition $\tilde{Q}=U\exp(H)$ is the polar decomposition, since $\lvert\tilde{Q}\rvert=\exp(H)$ for a unique Hermitian $H$; that the stabiliser of the quotient is exactly $U$ is the proposition above, so the quotient is the interior of the cone.

**Remark (the trap of the real-quaternion slice).** On $\mathbb{H}_{\mathbb{B}}$ the involution ${}^{*}$ is the quaternion conjugation and $\theta(\tilde{Q})=(\tilde{Q}^{\natural})^{-1}=\tilde{Q}/N(\tilde{Q})$, which is not the identity and not the conjugation of the slice; the automorphism of the slice given by the conjugation is a different map. The Cartan involution is an operation of the full complexification, and restricting it to the real-quaternion slice changes what it is.

## Summary

The dagger of the biquaternion algebra is a **positive involution**: $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$, strictly positive off zero, so $\mathbb{B}\cong M_2(\mathbb{C})$ with the dagger is a finite-dimensional $C^{*}$-algebra and the scalar form is its Hilbert–Schmidt form. This is not in tension with the general theorem that positivity requires a negative definite quadratic form, because the dagger of $\mathbb{B}$ is not the Clifford conjugation of the Minkowski structure $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ but the **reversion** of the positive definite structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$; the indefiniteness of the biquaternion norm $N$ belongs to the other structure, the exchange of sides being $e_i\mapsto ie_i$. The algebra splits as $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, the Hermitian and the anti-Hermitian sector, which are $H_2(\mathbb{C})$ and $u(2)$ in the matrix model, and $\tilde{Q}^{*}\tilde{Q}$ is Hermitian for every $\tilde{Q}$.

The **Hermitian cone** $P=\{\tilde{Q}^{*}\tilde{Q}\}=\{\tilde{Q}\tilde{Q}^{*}\}$ is the positive semidefinite Hermitian cone $H_2(\mathbb{C})_{\succeq0}$: closed, convex, pointed, of real dimension four, generating $\mathbb{M}_+$, and **self-dual** for the scalar form. Its interior is the image of the units, $P^{\circ}=\{\tilde{Q}^{*}\tilde{Q}:N(\tilde{Q})\neq0\}$, and in the interval form $N=t^{2}-\lvert\mathbf{u}\rvert^{2}$ on $\mathbb{M}_+$ it is the **forward light cone** $t\ge\lvert\mathbf{u}\rvert$, whose boundary is the forward part of the isotropic cone and whose extreme rays are the rank-one squares $\tilde E\tilde{E}^{*}$, parametrised by $\mathbb{P}^{1}(\mathbb{C})$. The word is not the older one of the series: the *isotropic cone* of $\mathbb{M}_+$ is the null set of $N$ there, the boundary of $P$ together with the boundary of $-P$, and it is indefinite; $P$ meets the null set only along its own boundary, the forward half.

Every element has a **polar decomposition** $\tilde{Q}=U\lvert\tilde{Q}\rvert$ with $\lvert\tilde{Q}\rvert=(\tilde{Q}^{*}\tilde{Q})^{1/2}\in P$ and $U\in U(2)$, unique exactly off the null cone, and distinct from the polar element representation although defined on the same set; $N(\lvert\tilde{Q}\rvert)=\lvert N(\tilde{Q})\rvert$, and on the real-quaternion slice it reduces to the quaternion polar decomposition, the cone meeting the slice in the ray $\mathbb{R}_{\ge0}e_0$. The **Cartan involution** $\theta(\tilde{Q})=(\tilde{Q}^{*})^{-1}$ is an automorphism of the group of units of order two with fixed set the unitary slice $U(2)$ and differential $-{}^{*}$, and its eigen-decomposition is the Cartan decomposition $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_2(\mathbb{C})$ with $[\mathbb{M}_-,\mathbb{M}_-]\subseteq\mathbb{M}_-$, $[\mathbb{M}_-,\mathbb{M}_+]\subseteq\mathbb{M}_+$, $[\mathbb{M}_+,\mathbb{M}_+]\subseteq\mathbb{M}_-$; at the group level $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_+)$ and $\mathbb{B}^{\times}/U(2)\cong P^{\circ}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+,\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors; $H_2(\mathbb{C})$ and $u(2)$ |
| $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$ | The dagger is positive; the scalar form is positive definite |
| $P=\{\tilde{Q}^{*}\tilde{Q}\}=\{\tilde{Q}\tilde{Q}^{*}\}$ | Hermitian cone; positive semidefinite Hermitian elements |
| $P^{\circ}=\{N(\tilde{Q})\neq0\}$ | Interior; image of the units; positive definite elements |
| $t\ge\lvert\mathbf{u}\rvert$ in $H=te_0+i\mathbf{u}$ | $P$ as the forward cone of the interval form on $\mathbb{M}_+$ |
| $\tilde E\tilde{E}^{*}$, $\tilde E\neq0$, up to scalar | Extreme rays; parametrised by $\mathbb{P}^{1}(\mathbb{C})$ |
| $\lvert\tilde{Q}\rvert=(\tilde{Q}^{*}\tilde{Q})^{1/2}$, $\tilde{Q}=U\lvert\tilde{Q}\rvert$ | Polar decomposition; unique off the null cone |
| $\theta(\tilde{Q})=(\tilde{Q}^{*})^{-1}$ | Cartan involution; fixed set $U=U(2)$ |
| $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_2(\mathbb{C})$ | Cartan decomposition; $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_+)$ |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the algebra and the four conjugations
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the Hermitian form and the inner product
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the bilinear form
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the scalar form
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions and their fixed spaces.
- *Biquaternion Hermitian Subspace* (`articles_maths/biquaternion-hermitian-subspace.md`), for $\mathbb{M}_+$, its Jordan structure, its norm and its isotropic cone.
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for $\Phi(e_k)=-i\sigma_k$, the Hermitian matrices, the determinant and the absolute determinant.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for $N$, the polar form, the invertibility criterion and the real forms.
- *Biquaternion Versors and the Orthogonal Group* (`articles_maths/biquaternion-versors-and-the-orthogonal-group.md`), for the signature $(1,3)$ of $\mathbb{M}_+$ and the identification of the dagger with the Euclidean reversion.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the cone as the image of the identity under the sandwich.
- *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/hermitian-modules-over-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the use of positivity in the module theory, where it makes every restriction positive definite.
- *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positive cone over which the maps are defined.
- *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-a-clifford-algebra-with-hermitian-adjoint.md`), for the general theory, the exchange of sides and the Cartan involution.
