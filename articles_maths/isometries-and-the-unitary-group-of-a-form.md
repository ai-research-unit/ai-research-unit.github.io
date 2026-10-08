# __Isometries and the Unitary Group of a Form__

## Introduction

An operator preserves the form of the layer when it preserves every pairing, $h(Tx,Ty) = h(x,y)$, and the collection of such operators is the **isometry group** of the form: the unitary group $U(A,h)$ of the sesquilinear layer. This article defines it, proves its two equivalent descriptions, and identifies the algebraic conditions under which the two descriptions separate.

Two facts organise the article. The condition $h(Tx,Ty) = h(x,y)$ is equivalent, for a nonsingular form and an operator admitting an adjoint, to the single algebraic equation $T^{*}T = 1$ in the adjoint of *The Form-Adjoint of an Operator*: on a nonsingular module the form is recovered from the adjoint, so the geometric hypothesis becomes an equation in the algebra of operators. And the adjoint operation restricted to the group is **inversion**, $T^{-1} = T^{*}$: the involution of the operator algebra is the group-theoretic inverse, which is why the form's group is an algebraic group with a prescribed involution and not a metric object.

The group is the stabiliser of the form under congruence (*Congruence and the Stabiliser of a Form*), its elements are the operators whose adjoint is their inverse, and its Lie algebra is the space of the skew operators (*The Unitary Group of a Form and Its Lie Algebra*). The elements of the algebra whose dagger is their inverse act by isometries by left multiplication, and the unitary slice of *Hermitian Algebras* is the bridge between the group of the form and the group of the algebra. The metric aspects — boundedness, completeness, compactness of the group for a definite form — are Part II and *Unitary and Isometric Operators of the Form*. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$, $h$ is nonsingular, the operators are the $R$-linear endomorphisms of $A$ admitting an adjoint, and $T^{*}$ denotes that adjoint.

## The Isometry Group

**Definition.** An operator $T$ is an **isometry** of $h$ when $h(Tx,Ty) = h(x,y)$ for all $x, y \in A$. The isometries form the **isometry set** $\operatorname{Iso}(A,h)$, and the **unitary group** $U(A,h)$ is the group of the invertible isometries.

**Proposition.** The isometry set is a monoid under composition, and the unitary group is its group of units.

**Proof.** The identity is an isometry, the composite of two isometries is an isometry, and $U(A,h)$ is by definition the set of the isometries invertible in the monoid. The group law is the composition, the inverse of an isometry is an isometry because $h(T^{-1}x, T^{-1}y) = h(TT^{-1}x, TT^{-1}y) = h(x,y)$ applying the isometry to the pair $(T^{-1}x, T^{-1}y)$.

**Proposition (the equation of an isometry).** Let $T$ admit the adjoint $T^{*}$. Then

$$
T \in \operatorname{Iso}(A,h) \iff T^{*}T = 1 .
$$

**Proof.** $h(Tx, Ty) = h(x, T^{*}Ty)$ for every pair by the definition of the adjoint, and $h(x,y) = h(x, T^{*}Ty)$ for every pair iff $h(x, (T^{*}T - 1)y) = 0$ for every $x, y$; the nonsingularity of $h$ makes this equivalent to $T^{*}T = 1$.

**Corollary (the finite-dimensional case).** Over a field and in finite dimension with $h$ non-degenerate, every isometry is invertible: if $Tx = 0$ then $h(x,y) = h(Tx,Ty) = 0$ for every $y$, and non-degeneracy gives $x = 0$, so $T$ is injective and hence bijective. Then

$$
U(A,h) = \{T : T^{*}T = 1\} = \{T : TT^{*} = 1\} .
$$

Over a general ring the implication fails — an injective endomorphism of a free module of finite rank need not be surjective — and the group is the set of the invertible isometries, which is the reading of the topological article *Unitary and Isometric Operators of the Form* in the complete case, where the unilateral shift is isometric without being unitary.

## Inversion Is the Adjoint

**Proposition.** On $U(A,h)$ the adjoint is the inverse:

$$
T^{-1} = T^{*} \qquad \text{for every } T \in U(A,h) .
$$

**Proof.** $T^{*}T = 1$ and $T$ is invertible, so $T^{*} = T^{-1}$ multiplying on the right by $T^{-1}$; taking adjoints in $TT^{*} = 1$ gives the same relation in the other order.

**Corollary.** The adjoint operation is an anti-automorphism of order two of the algebra of operators, $(ST)^{*} = T^{*}S^{*}$, and its restriction to $U(A,h)$ is the group inverse; on the group it therefore satisfies $(ST)^{*} = T^{*}S^{*}$ and $(T^{*})^{*} = T$, which is the group-theoretic statement that inversion reverses the product.

**Proposition (the determinant).** Over a field, for $T \in U(A,h)$ the determinant satisfies

$$
\det(T)\,\varsigma(\det(T)) = 1 .
$$

**Proof.** Taking determinants in $T^{*}T = 1$ and using that the adjoint is $\varsigma$-semilinear, $\det(T^{*}) = \varsigma(\det(T))$; the determinant of the identity is $1$.

At the trivial base involution this reads $\det(T)^{2} = 1$, the classical statement for the orthogonal group; the determinant-one part is the kernel of the determinant map, and it is the group of the layer in the classical theory, *The Orthogonal Lie Algebra*.

## The Operators of the Elements

**Definition.** An element $u \in A$ is **left-unitary** when $u^{*}u = 1$ and **unitary** when $u^{*}u = uu^{*} = 1$; the unitaries are the **unitary slice** $U(A)$ of *Hermitian Algebras*.

**Proposition.** Let $L_u$ be the left multiplication by $u$. Then

- $L_u$ is an isometry of $h$ exactly when $u$ is left-unitary;
- $L_u$ is a unitary operator exactly when $u$ is unitary.

**Proof.** $h(ux, uy) = h(x, u^{*}uy)$ by the compatibility of *Sesqualgebras with a Form*, so the left side equals $h(x,y)$ for all $x,y$ iff $h(x, (u^{*}u - 1)y) = 0$ for all $x,y$, which is $u^{*}u = 1$ by nonsingularity. Invertibility of $L_u$ is invertibility of $u$ in $A$, and for a unitary element $u^{-1} = u^{*}$ gives the second clause.

The assignment $u \mapsto L_u$ is an injective $R$-algebra homomorphism on a unital algebra, so the unitary slice embeds in the unitary group of the form, and the elements of the slice act on $A$ by form-preserving transformations. This is the bridge between the algebra and the group: the group of the form contains the group of the algebra, and the two agree for the forms whose isometries are all of the shape $L_u$, which is a property of the algebra and not a theorem of the layer.

## Examples

### The Trace Form

On $M_n(\mathbb{C})$ with $h(X,Y) = \tau(XY^{*})$ the adjoint is given by the dagger, $T^{*}(X) = T^{\dagger}X$ read in the basis of the matrices, so the isometry equation $T^{*}T = 1$ is $T^{\dagger}T = 1$, the unitary group $U(n)$: the group of the form is the classical unitary group.

### The Orthogonal Case

At the trivial base involution and $* = \mathrm{id}$ the formula reads $T^{\mathrm{t}}T = 1$ and the group is the orthogonal group of the symmetric form, $\operatorname{O}(A,q)$, with determinant-one part $\operatorname{SO}(A,q)$ of *The Orthogonal Lie Algebra*.

### The Biquaternion Slice

On $\mathbb{B}$ with the dagger of *Hermitian Algebras*, the unitary slice $U = \{u : u^{\dagger}u = uu^{\dagger} = 1\}$ is the compact real form of the algebra of the biquaternions, and the isometries of the Lorentzian form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ form the indefinite group of the layer; the two are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* and *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## Summary

- An **isometry** of $h$ is an operator with $h(Tx,Ty) = h(x,y)$; the isometries form a monoid and the **unitary group** $U(A,h)$ is its group of units.
- For a nonsingular form and an operator with an adjoint, $T$ is an isometry exactly when $T^{*}T = 1$.
- Over a field and in finite dimension with $h$ non-degenerate every isometry is invertible, so the equation alone defines the group; over a general ring the injectivity does not give the surjectivity and the two notions separate.
- On the group the adjoint is the inverse, $T^{-1} = T^{*}$, so the involution of the operators is the group inverse; the determinant obeys $\det(T)\varsigma(\det(T)) = 1$.
- The left multiplication $L_u$ is an isometry exactly when $u^{*}u = 1$ and is a unitary operator exactly when $u$ is unitary, which embeds the unitary slice in the unitary group of the form.
- The definitions are polynomial, so the group is algebraic; the boundedness and the compactness of the definite case are Part II.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\operatorname{Iso}(A,h)$ | the isometry monoid of the form |
| $U(A,h)$ | the unitary group of the form |
| $T^{*}$ | the adjoint of $T$ for $h$ |
| $L_u$ | the left multiplication by $u$ |
| $U(A)$ | the unitary slice $\{u : u^{*}u = uu^{*} = 1\}$ |
| $\operatorname{O}(A,q)$, $\operatorname{SO}(A,q)$ | the orthogonal group and its determinant-one part |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the unitary group of a form over a ring with an involution.
- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 1955), for the classical groups attached to a form and their generation.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for the orthogonal and unitary groups as isometry groups.
