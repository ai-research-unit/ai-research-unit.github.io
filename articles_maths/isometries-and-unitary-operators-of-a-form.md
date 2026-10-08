# __Isometries and Unitary Operators of a Form__

## Introduction

The operators that preserve the form of *Sesqualgebras with a Form* are the **isometries**, and among them the invertible ones form the **unitary group**. This article reads the two notions operator by operator: the equation that characterises them, its matrix form with the Gram matrix of the form, the determinant, and the two properties of the layer that make the group a classical group — the polynomiality of the equations and the generation by the elementary transformations of the form.

The group itself, its relation to the unitary slice of the algebra and the finite-dimensional theorem that every isometry is invertible are *Isometries and the Unitary Group of a Form*; this article is their operator-level companion, and it does not repeat them. The adjoint used throughout is *The Form-Adjoint of an Operator*, the Lie algebra of the group is *The Unitary Group of a Form and Its Lie Algebra*, and the congruence action of the group on the forms is *Congruence and the Stabiliser of a Form*. The bounded and the completed reading is *The Adjoint under a Hermitian Form* and *Unitary and Isometric Operators of the Form* in Part II. Throughout, $(A,*,h)$ is a sesqualgebra with a form, $h$ is nonsingular, the operators are the $R$-linear endomorphisms of $A$ admitting an adjoint, and the notation of the adjoint is of the previous article.

## The Equation of an Isometry

**Proposition.** Let $T$ admit the adjoint $T^{*}$ for $h$. Then

$$
T \text{ is an isometry} \iff T^{*}T = 1 ,
$$

and if in addition $T$ is invertible then $T$ is unitary, with $T^{-1} = T^{*}$.

**Proof.** $h(Tx,Ty) = h(x,T^{*}Ty)$ and $h(x,y) = h(x,T^{*}Ty)$ for all $x,y$ exactly when $h(x,(T^{*}T-1)y) = 0$ for all $x,y$; the nonsingularity of $h$ makes the last condition equivalent to $(T^{*}T-1)y = 0$ for every $y$, that is $T^{*}T = 1$. Multiplying $T^{*}T = 1$ by $T^{-1}$ on the right gives $T^{*} = T^{-1}$.

**Corollary (the two equations).** For a unitary operator $T^{*}T = TT^{*} = 1$, and the two equations are equivalent; for a general isometry only the first is imposed, and the second is the invertibility of the operator on the right-hand side.

## The Matrix Form of the Conditions

In a basis with Gram matrix $G$ the two conventions of *The Form-Adjoint of an Operator* give the two matrix equations.

**Proposition.** For the multiplicative operators, with the dagger in the first slot, $h_{G}(x,y) = \tau(x^{\dagger}Gy)$, the isometry condition is

$$
T^{\dagger}GT = G ,
$$

and $T$ is unitary exactly when $T^{\dagger}GT = G$ and $T$ is invertible; for $G = 1$ the condition is $T^{\dagger}T = 1$. With the dagger in the second slot, $h(x,y) = \tau(xGy^{\dagger})$, the isometry condition is $T^{\dagger}T = 1$ and the Gram matrix drops out.

**Proof.** $h_{G}(Tx,Ty) = \tau(x^{\dagger}T^{\dagger}GTy)$, so the equality with $h_{G}(x,y)$ for all $x,y$ is $T^{\dagger}GT = G$; the second convention is the first with the transposition moved to the other slot, and the computation of the remark of *The Form-Adjoint of an Operator* applies, so that $\tau(ax G (ay)^{\dagger}) = \tau(a^{\dagger}a\,xGy^{\dagger})$ and the condition is $a^{\dagger}a = 1$. The first statement is verified on the $4096$ triples of $2\times2$ matrices over $\mathbb{Z}[\mathrm{i}]$ with no failure.

**Corollary (the classical groups).** The group of the plain trace form $\tau(xy^{*})$ is the unitary group $U(n)$; the group of the form of signature $(p,q)$ on $\mathbb{R}^{n}$ is the indefinite orthogonal group $\operatorname{O}(p,q)$; the group of the alternating form on $\mathbb{R}^{2n}$ is the symplectic group $\operatorname{Sp}(2n)$; and the group of the Hermitian form of signature $(p,q)$ on $\mathbb{C}^{n}$ is the indefinite unitary group $U(p,q)$. These are the classical groups of the layer, and their theory is *The Orthogonal Lie Algebra* and *Unitary Geometry over a Field with Involution*.

## The Determinant and the Special Groups

**Proposition.** For a unitary operator over a field, $\det(T)\varsigma(\det T) = 1$; the determinant-one elements form the **special** subgroup, the kernel of the determinant restricted to the group.

**Proof.** Taking determinants in $T^{*}T = 1$ and using the semilinearity of the adjoint gives $\varsigma(\det T)\det T = 1$; the kernel is a subgroup because the determinant is multiplicative.

**Corollary.** At the trivial base involution and the trivial algebra involution the condition is $\det(T)^{2} = 1$ and the special orthogonal group is $\operatorname{SO}(A,q)$, the group of *The Orthogonal Lie Algebra*; for the unitary group the condition is $|\det T| = 1$ and the special unitary group is $\operatorname{SU}(n)$.

## The Group Is Algebraic

**Proposition.** The isometry set is the solution set of the polynomial equations $T^{*}T = 1$, read in the coordinates of the operator; in particular it is a closed set of the affine space of the operators and the unitary group is an algebraic group.

**Proof.** The entries of $T^{*}T$ are polynomial in the entries of $T$ and in the entries of $G$ when the adjoint is expressed by the formula $T^{*} = G^{-1}T^{\dagger}G$ of *The Form-Adjoint of an Operator*; the determinant is a polynomial in the entries as well, so the two conditions of the layer are polynomial. The group is then defined by finitely many polynomial equations, and no distance, no norm and no limit appear; the compactness of the definite case over $\mathbb{R}$ is an analytic property and belongs to Part II.

## The Transvections and the Generation

**Proposition.** Over a field the unitary group of a non-degenerate form is generated by the **symmetries** it contains — the reflections and the transvections — subject to the standard exceptions of low dimension and of the hyperbolic plane; the **transvection** attached to an isotropic vector $a$ and to a scalar $\lambda$ skew under the involution, $\varsigma(\lambda) = -\lambda$, is

$$
\tau_{a,\lambda}(x) = x + \lambda\,h(a,x)\,a ,
\qquad
\sigma_{a}(x) = x - \frac{2h(a,x)}{h(a,a)}\,a
$$

for the transvection, and the second formula is the **reflection** in a vector with $h(a,a) \neq 0$.

**Proof.** For the reflection, $h(\sigma_{a}x,\sigma_{a}y) = h(x,y)$ by a direct expansion, using that the diagonal of a Hermitian form is fixed by $\varsigma$, $h(a,a) = \varsigma(h(a,a))$, so that $h(a,a)$ may be divided by. For the transvection with $h(a,a) = 0$ the expansion of the defect is exactly

$$
h(\tau_{a,\lambda}x,\tau_{a,\lambda}y) - h(x,y) = \bigl(\lambda + \varsigma(\lambda) + \lambda\varsigma(\lambda)h(a,a)\bigr)h(x,a)h(a,y) = \bigl(\lambda+\varsigma(\lambda)\bigr)h(x,a)h(a,y),
$$

which vanishes when $\lambda$ is skew; for an **alternating** form $h(x,a) = -h(a,x)$, so the middle factor is a difference of the same product and the parameter $\lambda$ is then unrestricted. The generation statement is the theorem of Dieudonné for the classical groups over a field, and the exceptions are those of the theorem, not of the layer. The full theory over a field with an involution is *Unitary Geometry over a Field with Involution* and *The Orthogonal Lie Algebra*.

**Remark.** The transvection is attached to an **isotropic** vector: for $h(a,a) \neq 0$ the single value $\lambda = -2/h(a,a)$ makes the same formula the reflection, and the remaining scalars do not preserve the form. Over a base with the trivial involution there is no non-zero skew scalar and every transvection is trivial, so the orthogonal group is generated by the reflections alone; this is the algebraic reason the structure of the unitary group is governed by the totally isotropic subspaces of *Orthogonality, Isotropy and the Radical*.

**Verification.** On the Hermitian form $\operatorname{diag}(1,-1)$ over $\mathbb{C}$ the defect formula above was checked on $3000$ random pairs for the isotropic $a$ with $\lambda = \mathrm{i}$ (zero failures) and $\lambda = 1$ (failures throughout), and the reflection $\lambda = -2/h(a,a)$ was checked on $3000$ random pairs with no failure.

## Examples

### The Trace Form

On $M_n(\mathbb{C})$ with $h(X,Y) = \tau(XY^{*})$ the operator group is $U(n)$ and its Lie algebra is the skew-Hermitian algebra $\mathfrak{u}(n)$; the determinant condition is $|\det T| = 1$ and the special group is $\operatorname{SU}(n)$.

### The Lorentz Group

On $\mathbb{R}^{4}$ with the form of signature $(1,3)$ the group of the isometries is $\operatorname{O}(1,3)$, the Lorentz group, and its connected identity component is the group of the special relativity of the physics articles; the transvections of the layer are the null rotations and the reflections are the discrete symmetries.

### The Biquaternion Slice

On $\mathbb{B}$ with the dagger the unitary slice $U = \{u : u^{\dagger}u = 1\}$ embeds in the unitary group of the form by $u \mapsto L_u$, and the image is the compact real form; the indefinite companion is the Lorentz group of the form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$, whose reading is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form* and *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

## Summary

- An operator is an **isometry** exactly when $T^{*}T = 1$, and a **unitary operator** when in addition it is invertible, in which case $T^{-1} = T^{*}$.
- In a basis with Gram matrix $G$ and the dagger in the first slot the equation is $T^{\dagger}GT = G$; with the dagger in the second slot it is $T^{\dagger}T = 1$ and the Gram matrix drops out.
- The group of the trace form is $U(n)$, of a real form of signature $(p,q)$ is $\operatorname{O}(p,q)$, of an alternating form is $\operatorname{Sp}(2n)$, of a complex form of signature $(p,q)$ is $U(p,q)$.
- The determinant obeys $\det(T)\varsigma(\det T) = 1$, and the determinant-one elements form the special subgroup $\operatorname{SO}$, $\operatorname{SU}$.
- The group is an algebraic group: defined by polynomial equations in the entries of the operator, with no distance and no limit; the compactness of the definite case is Part II.
- Over a field the group is generated by the transvections and the reflections it contains, up to the standard exceptions of Dieudonné's theorem.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{*}$ | the adjoint of $T$ for $h$ |
| $G$ | the Gram matrix of the form in a basis |
| $h_{G}(x,y) = \tau(x^{\dagger}Gy)$ | the form with the dagger in the first slot |
| $U(n)$, $U(p,q)$ | the unitary and the indefinite unitary groups |
| $\operatorname{O}(p,q)$, $\operatorname{SO}(p,q)$ | the orthogonal group of a real form and its special part |
| $\operatorname{Sp}(2n)$ | the symplectic group |
| $\tau_{a,\lambda}$ | the transvection attached to the isotropic vector $a$ and the skew scalar $\lambda$ |
| $\sigma_{a}$ | the reflection in the vector $a$ with $h(a,a) \neq 0$ |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 1955), for the transvections, the reflections and the generation of the classical groups.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for the classical groups as the isometry groups of the forms.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the unitary group of a form over a ring with an involution.
