# __Unitary Equivalence and Congruence of Operators of the Form__

## Introduction

The operator theory of a form has two equivalence relations and two complete invariants, and the contrast between them is the subject of this article. **Unitary equivalence** is the conjugation of an operator by the unitary group, $T \mapsto UTU^{\dagger}$; it preserves the form, hence the adjoint, hence self-adjointness and normality, and it classifies the normal operators of a fixed form up to their **spectrum**. **Congruence** is the change of coordinates of the form itself, $h \mapsto h \circ (C \times C)$, $C$ invertible; it forgets the form, preserves the **inertia** by Sylvester's law, and classifies the Hermitian forms on the underlying module up to their signature. The first relation acts on the operators and its invariant is a set of numbers attached to the operator; the second acts on the forms and its invariant is a set of numbers attached to the form; and the layer uses the second to normalise the form and the first to normalise the operator.

The relation between them is the following. A congruence of the form by $C$ transports the operator theory: the operator $T$ on $(A,h)$ corresponds to the operator $C^{-1}TC$ on the congruent form, a **similarity**, so the spectrum is preserved while the form and the adjoint are not. The intersection of the two relations is the case in which the congruence is by an element of the **unitary group**, and the article proves that the unitary group is exactly the **stabiliser** of the form for the congruence action: the congruences that leave the form fixed are the isometries, and the invertible isometries are the unitary operators. That identity is what makes the layer's classification of the forms by their inertia the correct normal form for the spectral theory: after the form is reduced to its diagonal model, the operators on it are classified by the spectrum and by nothing else.

The article develops the unitary equivalence and its invariants, the congruence of the Hermitian forms with the Gram matrix transformation and Sylvester's law of inertia, the comparison of the two classifications and the transport of the operator theory, and it works the matrices and the hyperbolic plane. The unitary group is *Unitary and Isometric Operators of the Form*; the adjoint is *The Adjoint under a Hermitian Form*; the spectrum and its completeness for normal operators are *The Spectra of Self-Adjoint Operators of the Form*; the inertia and Sylvester's law are *The Indefinite Case and the Signature*; the cone of the positive forms is *Positivity and the Positive Cone of a Hermitian Form*, §*The Cone of Positive Forms*; the polar factors transported by the unitary group are *The Polar Decomposition of an Operator of the Form*; the bilinear counterpart is *Unitary Equivalence and Congruence of Operators with Hermitian Adjoint*. Throughout, $A$ is a sesquialgebra with a form over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$, $h$ is Hermitian, compatible and nonsingular, and in the definite finite-dimensional sections $A$ is free of finite rank over $k$ or $k(\mathrm{i})$ and $h$ is positive definite.

## Unitary Equivalence

### The Action of the Unitary Group

**Theorem (the action).** For a unitary operator $U$ and an operator $T$, let

$$
U \cdot T = UTU^{\dagger} .
$$

Then $\cdot$ is a left action of the unitary group $U(A,h)$ on $B(A)$: $1 \cdot T = T$ and $(UV)\cdot T = U\cdot(V\cdot T)$. The action preserves the adjoint, $(U\cdot T)^{\dagger} = U\cdot T^{\dagger}$, and it therefore preserves self-adjointness, skew-adjointness, normality and unitarity.

*Proof.* The unit acts by $1T1 = T$, and $(UV)T(UV)^{\dagger} = U(VTV^{\dagger})U^{\dagger}$ by the anti-multiplicativity and the identity $(UV)^{\dagger} = V^{\dagger}U^{\dagger} = V^{-1}U^{-1}$. For the adjoint, $(UTU^{\dagger})^{\dagger} = (U^{\dagger})^{\dagger}T^{\dagger}U^{\dagger} = UT^{\dagger}U^{\dagger}$, using the order two of the adjoint operation. The preservation of the four properties is immediate from the preservation of the adjoint. $\square$

**Proposition (the covariance of the matrix elements).** For a unitary $U$ and an operator $T$,

$$
h(Tx,y) = h\bigl((UTU^{\dagger})(Ux), Uy\bigr) \qquad \text{for all } x, y .
$$

*Proof.* The right side is $h(UTU^{\dagger}Ux, Uy) = h(UTx, Uy) = h(Tx, U^{\dagger}Uy) = h(Tx,y)$, using $U^{\dagger}U = 1$. $\square$

### The Invariants

**Theorem (the invariants of unitary equivalence).** Unitary equivalence preserves the spectrum, the modulus and the polar factors: $\sigma(UTU^{\dagger}) = \sigma(T)$ and $\lvert UTU^{\dagger}\rvert = U\lvert T\rvert U^{\dagger}$; if $T = U_{T}\lvert T\rvert$ is the polar decomposition of $T$, then $UTU^{\dagger} = (U U_{T}U^{\dagger})\,\lvert UTU^{\dagger}\rvert$ is the polar decomposition of $UTU^{\dagger}$.

*Proof.* The conjugation is a similarity by an invertible operator, so the spectrum is unchanged. For the modulus, $(UTU^{\dagger})^{\dagger}(UTU^{\dagger}) = UT^{\dagger}U^{\dagger}UTU^{\dagger} = U(T^{\dagger}T)U^{\dagger}$, and $U\lvert T\rvert U^{\dagger}$ is self-adjoint, positive and of square $U(T^{\dagger}T)U^{\dagger}$, so it is the modulus by the uniqueness of the positive square root. The polar statement is the same computation read on the pair. $\square$

**Theorem (completeness for normal operators).** Let the form be definite and finite dimensional over the sesquilinear base $R = k(\mathrm{i})$. Then two normal operators are unitarily equivalent if and only if they have the same spectrum.

*Proof.* Unitary equivalence preserves the spectrum by the theorem above. Conversely, by *The Spectra of Self-Adjoint Operators of the Form*, a normal operator over the sesquilinear base is diagonalisable in an $h$-orthonormal basis with its spectrum on the diagonal, and the multiplicities are determined by the spectrum; a unitary sending the eigenbasis of the first operator to the eigenbasis of the second, matching the eigenvalues, conjugates one into the other. $\square$

**Remark (the invariant is not complete for general operators).** Beyond the normal operators the spectrum is only a partial invariant, and two operators with the same spectrum need not be unitarily equivalent: the Jordan structure is an additional invariant, which the definite layer does not develop. The comparison with the congruence is sharp: the *whole* of the spectral data, including the multiplicities, is invariant under unitary equivalence, whereas a general congruence preserves only what the similarity $C^{-1}TC$ preserves and moves everything that refers to the form — the adjoint, the self-adjointness, the modulus and the polar factors.

## Congruence

### The Relation on the Forms

**Definition.** Two Hermitian forms $h$ and $k$ on $A$ are **congruent** when there is an invertible $R$-linear map $C$ with

$$
k(x,y) = h(Cx, Cy) \qquad \text{for all } x, y ,
$$

written $k = h_{C}$.

**Proposition (the congruent form is Hermitian and nonsingular).** If $h$ is Hermitian and $C$ invertible, then $h_{C}$ is Hermitian; $h_{C}$ is nonsingular exactly when $h$ is; and if $h$ is positive definite then $h_{C}$ is positive definite.

*Proof.* Hermitian: $h_{C}(y,x) = h(Cy,Cx) = \varsigma(h(Cx,Cy)) = \varsigma(h_{C}(x,y))$. Nonsingularity: the radical of $h_{C}$ is $C^{-1}(A^{\perp})$, so it vanishes exactly when $A^{\perp}$ does. Definiteness: $h_{C}(x,x) = h(Cx,Cx) > 0$ for $x \neq 0$ because $C$ is injective and $h$ is definite. $\square$

**Theorem (the Gram matrix transformation).** Let $H$ and $K$ be the Gram matrices of $h$ and $k$ in a basis, and let $C$ have matrix $\Gamma$ in the same basis. Then $k = h_{C}$ if and only if

$$
K = \Gamma^{T} H\, \varsigma(\Gamma) .
$$

*Proof.* The value $k(x,y) = h(Cx,Cy)$ is the quadratic form of the matrix $\Gamma^{T}H\varsigma(\Gamma)$ evaluated at the coordinate vectors of $x$ and $y$, and the two forms have the same Gram matrix exactly when they agree, by the reconstruction of a form from its Gram matrix of *The Sesquilinear Form and the Conjugation*, §*The Reconstruction*. $\square$

### Sylvester's Law of Inertia

**Theorem (Sylvester's law).** Let the base be one of the two classical kinds, and let $h$ be a Hermitian form on a free module of finite rank with Gram matrix $H$. Then $h$ is congruent to the diagonal form with $r$ entries $+1$, $s$ entries $-1$ and $t$ entries $0$, where $(r,s,t)$ is the inertia of $H$; the inertia is invariant under congruence; over $k$ the inertia is the complete invariant of congruence, and over $k(\mathrm{i})$ the rank $r+s$ is.

*Proof.* The reduction by simultaneous row and column operations to the diagonal form and the invariance of the inertia are *The Indefinite Case and the Signature*, §*Sylvester's Law*; the completeness is the Lagrange reduction of the form to a sum of squares and the classification of the nonzero squares by their sign over the ordered field $k$. $\square$

### The Cone and the Tolerance under Congruence

**Proposition (the cone and the tolerance under congruence).** Every congruence carries a positive semi-definite form to a positive semi-definite form, so it is an automorphism of the cone of *Positivity and the Positive Cone of a Hermitian Form*, §*The Cone of Positive Forms*; the definite forms are carried to definite forms; and the tolerance $x \succeq_{h} y \iff h(x-y,x-y) \geq 0$ of *Positivity and the Positive Cone of a Hermitian Form*, §*The Tolerance*, is transformed by

$$
x \succeq_{h_{C}} y \iff Cx \succeq_{h} Cy .
$$

*Proof.* The diagonal of the congruent form is $h_{C}(x,x) = h(Cx,Cx)$, which is nonnegative for every $x$ exactly when $h$ is positive semi-definite on the range of $C$, that is on all of $A$; the definiteness is the proposition above. For the tolerance, $h_{C}(x-y,x-y) = h(C(x-y),C(x-y)) = h(Cx-Cy,Cx-Cy)$ by the linearity of $C$, which is the assertion. $\square$

### The Stabiliser of the Form

**Theorem (the unitary group is the stabiliser).** For an invertible $C$, the congruence $h_{C}$ equals $h$ if and only if $C$ is an isometry of $h$; the invertible isometries are the unitary operators, so the unitary group is the stabiliser of $h$ in the congruence action on the Hermitian forms.

*Proof.* The equality $h(Cx,Cy) = h(x,y)$ for all $x,y$ is the isometry condition of *Unitary and Isometric Operators of the Form*, §*The Definitions*, and by *Unitary and Isometric Operators of the Form*, §*The Equivalences*, an invertible isometry is unitary. $\square$

**Remark (the compatibility under a congruence).** A congruence does not preserve the *compatibility* with the product in general: the congruent form $h_{C}$ need not be compatible for the involution $*$, and the adjoint operation is transported rather than preserved — the $h_{C}$-adjoint of the transported operator $T^{C} = C^{-1}TC$ is the conjugate $C^{-1}T^{\dagger}C$ of the $h$-adjoint of $T$, and not $T^{\dagger}$ itself. What is preserved is the involution itself in the multiplicative case: if $C$ is a $*$-automorphism of the algebra — multiplicative and commuting with $*$ — then

$$
h_{C}(xy,z) = h(Cx\,Cy, Cz) = h(Cy, (Cx)^{*}Cz) = h(Cy, C(x^{*})Cz) = h_{C}(y, x^{*}z) ,
$$

so $h_{C}$ is again compatible for $*$. The compatible forms of the layer are therefore singled out by a congruence orbit together with an involution, and this is the reason the layer's forms are attached to the algebra and to its involution, not to the module alone.

## The Two Classifications Compared

### Spectrum and Inertia

**Theorem (the comparison).** The two relations are the two halves of one normal form. Unitary equivalence is the orbit relation of the unitary group on the operators of a fixed form, and its complete invariant for the normal operators over the sesquilinear base is the spectrum. Congruence is the orbit relation of the general linear group on the Hermitian forms of a fixed module, and its complete invariant is the inertia. The layer first brings the form to the diagonal model $\operatorname{diag}(1_{r},-1_{s},0_{t})$ by a congruence, and then classifies the operators on the model up to unitary equivalence by their spectra.

*Proof.* The two orbit statements are the definition of the two actions; the invariants are the completeness theorems quoted above. The last clause is the combination: the congruence normalises the form and the unitary equivalence normalises the operator. $\square$

### The Transport of the Operator Theory

**Theorem (the transport).** Let $k = h_{C}$ and let $T$ be an operator on $(A,h)$. Then the operator $T^{C} = C^{-1}TC$ on $(A,k)$ is $k$-self-adjoint if and only if $T$ is $h$-self-adjoint; the two adjoints are related by $(T^{C})^{\dagger_{k}} = C^{-1}T^{\dagger}C$; $T^{C}$ is similar to $T$, so the two have the same spectrum; and the transport is a left action of the general linear group, $(T^{C})^{D} = T^{CD}$.

*Proof.* The map $C : (A,k) \to (A,h)$ is an isometry by the definition of $k$, so it carries the adjoint of the one form to the adjoint of the other: $k(T^{C}x,y) = h(TCx,Cy) = h(Cx,T^{\dagger}Cy) = k(x,C^{-1}T^{\dagger}Cy)$, whence $(T^{C})^{\dagger_{k}} = C^{-1}T^{\dagger}C$, and $T^{C}$ is $k$-self-adjoint exactly when $T$ is $h$-self-adjoint. The similarity statement is that $C$ conjugates $T^{C}$ back to $T$, $C\,T^{C}\,C^{-1} = T$, so the two operators are similar, and the action law is the computation $(T^{C})^{D} = D^{-1}C^{-1}TCD = (CD)^{-1}T(CD)$. $\square$

**Remark (what congruence forgets and what it keeps).** A congruence of the form keeps the spectrum, because the transport is a similarity; it forgets self-adjointness, because the conjugate of a self-adjoint operator of $h$ is self-adjoint for the congruent form and not for $h$ unless the congruence is an isometry. This is the precise sense in which the layer's operator theory lives on the pair (algebra, form) and not on the algebra alone: the form is exactly the datum that selects the unitary group inside the general linear group, and with it the self-adjoint operators and the spectral theory.

## Worked Cases

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, whose Gram matrix in the standard basis is the identity of size $n^{2}$. A congruent form has Gram matrix $\Gamma^{T}\varsigma(\Gamma)$, which is positive definite for every invertible $\Gamma$; the inertia of the identity is $(n^{2},0,0)$, so every congruent form is positive definite by Sylvester's law, and over $k(\mathrm{i}) = \mathbb{C}$ the rank $n^{2}$ is the complete invariant. The unitary group of $h$ is $U(n^{2})$ by *Unitary and Isometric Operators of the Form*, §*The Matrices*, and it is the stabiliser of the form; the unitary equivalence of the operators is the conjugation $T \mapsto UTU^{\dagger}$ by a unitary of $M_{n^{2}}(\mathbb{C})$. The example is the model in which both relations are visible on the same object, the congruence acting on the Gram matrix and the unitary equivalence on the operator.

### The Hyperbolic Plane

**Example (the hyperbolic plane).** On $A = \mathbb{R}^{2}$ with the form of signature $(1,1)$ of Gram matrix $H = \operatorname{diag}(1,-1)$, the congruence class is the set of the forms with inertia $(1,1,0)$, and it is the whole of the indefinite forms on $\mathbb{R}^{2}$ by Sylvester's law. The hyperbolic rotation $C_{t} = \begin{pmatrix}\cosh t & \sinh t \\ \sinh t & \cosh t\end{pmatrix}$ satisfies $C_{t}^{T}HC_{t} = H$, so it lies in the unitary group of the form and the congruence by $C_{t}$ fixes the form; the operator $T = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ of *The Spectra of Self-Adjoint Operators of the Form* is $h$-self-adjoint, and its transport by $C_{t}$ is $C_{t}^{-1}TC_{t}$, a similar matrix with the same spectrum $\{\mathrm{i},-\mathrm{i}\}$ that is self-adjoint for the same form because $C_{t}$ is an isometry. The example is the smallest in which the unitary group is not trivial, the stabiliser is a one-parameter group and the transport is visible.

## Summary

**Unitary equivalence**, $T \mapsto UTU^{\dagger}$, is the action of the **unitary group** on the operators of a fixed form; it preserves the adjoint, hence self-adjointness, skew-adjointness, normality and unitarity, and it preserves the spectrum, the modulus and the polar factors; for **normal** operators over the sesquilinear base the **spectrum** is the complete invariant. **Congruence**, $h \mapsto h_{C}$ with $h_{C}(x,y) = h(Cx,Cy)$, is the change of coordinates of the form; its Gram matrix transforms as $K = \Gamma^{T}H\varsigma(\Gamma)$, it preserves the **inertia** by **Sylvester's law**, and over $k$ the inertia is the complete invariant while over $k(\mathrm{i})$ the rank is. The **unitary group is the stabiliser** of the form in the congruence action. A congruence transports the operator theory by the **similarity** $T \mapsto C^{-1}TC$, which preserves the spectrum and moves the form and the adjoint; the layer uses the congruence to bring the form to its diagonal model and the unitary equivalence to classify the operators on that model by their spectra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $U \cdot T = UTU^{\dagger}$ | the action of the unitary group, the unitary equivalence |
| $(U\cdot T)^{\dagger} = U\cdot T^{\dagger}$ | the action preserves the adjoint |
| $h(Tx,y) = h((UTU^{\dagger})(Ux),Uy)$ | the covariance of the matrix elements |
| $\sigma(UTU^{\dagger}) = \sigma(T)$ | the spectrum is an invariant of unitary equivalence |
| $\lvert UTU^{\dagger}\rvert = U\lvert T\rvert U^{\dagger}$ | the transport of the modulus |
| $h_{C}(x,y) = h(Cx,Cy)$ | the congruence of a form by an invertible $C$ |
| $K = \Gamma^{T}H\varsigma(\Gamma)$ | the transformation of the Gram matrix |
| $(r,s,t)$ | the inertia, invariant under congruence |
| $h_{C} = h \iff C$ unitary | the unitary group is the stabiliser of the form |
| $(T^{C})^{\dagger_{k}} = C^{-1}T^{\dagger}C$ | the transport of the adjoint under a congruence |
| $T^{C} = C^{-1}TC$ | the transport of an operator under a congruence |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the congruence of matrices, Sylvester's law of inertia and the unitary equivalence of normal matrices.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the congruence of indefinite forms and the classification by the inertia.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the isometry group of an indefinite inner product and its action.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the unitary group of an algebra with involution and its action on the operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the congruences of Hermitian forms over a ring with involution and the Witt classification.
- Rudolf Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the congruence classes, the Witt group and the inertia over an ordered field.
