# __The Hermitian Sandwich on a Krein Space__

## Introduction

On a Krein space $K$ with fundamental symmetry $J$ and indefinite adjoint $\dagger$, the **Hermitian sandwich** of a bounded operator $T$ by an operator $Q$ is

$$
H_{Q}(T) = Q\,T\,Q^{\dagger} ,
$$

the two-sided operator built from $Q$ and its indefinite adjoint. It is the indefinite counterpart of the sandwich $\Theta_x$ of a Hilbert algebra, and it is the operation that transports operators along the symmetry group of the form: for a $J$-unitary $Q$ the sandwich is the inner automorphism $\mathrm{Ad}_Q$, it preserves the indefinite form and the $J$-positivity, and it acts on self-adjointness and on the kernel and the image in a way that can be computed exactly.

The contrast with the Hilbert case is the interesting part. In Hilbert space the sandwich by a unitary $U$ is a unitary equivalence, so it preserves the Hilbert norm, the spectrum, the positive cone and every spectral subspace. In a Krein space the sandwich by a $J$-unitary $Q$ preserves the indefinite form but not the Hilbert inner product, because a $J$-unitary operator need not be Hilbert-unitary: it is a form-isometry of the indefinite geometry, and the Hilbert norm of the sandwich generally changes. What is preserved is the indefinite geometry — the form, the $J$-positivity, the $J$-self-adjointness, the $J$-unitarity — and what is not preserved is the Hilbert metric; the sandwich therefore fails to transport the spectrum, and this failure is the reason the indefinite theory needs the modular and spectral tools of *Spectral Theory on Krein Spaces* rather than the Hilbert spectral theorem.

This article fixes the dagger sandwich, its adjoint and composition laws, the preservation of the form and of $J$-positivity, the kernel and the image, the automorphism statement on the unitary slice, and the contrast with the Hilbert case.

The indefinite adjoint is *J-Self-Adjoint and J-Unitary Operators*; the fundamental symmetry and the form are *The Fundamental Symmetry* and *Krein Spaces*; the $J$-positive cone and the order are *The J-Positive Cone and the J-Order* and *Krein Algebras*; the Hilbert-algebra sandwich is *The Adjoint of the Sandwich on a Hermitian Algebra* and *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*; the spectral consequences are *Spectral Theory on Krein Spaces*. Those are cited. The space is $K$ with form $[\cdot,\cdot]$, fundamental symmetry $J$, Hilbert adjoint $*$ and indefinite adjoint $\dagger$.

## The Dagger Sandwich

**Definition.** For bounded operators $Q, T$ the **Hermitian sandwich** (or **dagger sandwich**) is

$$
H_{Q}(T) = Q\,T\,Q^{\dagger} , \qquad Q^{\dagger} = JQ^{*}J .
$$

**Proposition (adjoint and composition laws).** For all bounded $Q, S, T$,

$$
H_{Q}(T)^{\dagger} = H_{Q}(T^{\dagger}) , \qquad H_{Q}(H_{S}(T)) = H_{QS}(T) , \qquad H_{Q}(ST) = H_{Q}(S)H_{Q}(T) \text{ if } Q^{\dagger}Q = 1 .
$$

**Proof.** $(QTQ^{\dagger})^{\dagger} = Q^{\dagger\dagger}T^{\dagger}Q^{\dagger} = QT^{\dagger}Q^{\dagger}$; the composition is associativity; the multiplicativity uses $Q^{\dagger}Q = 1$ to cancel the middle pair.

**Proposition (the parameter rule).** For a scalar $\alpha$ one has $H_{\alpha Q}(T) = |\alpha|^{2}H_{Q}(T)$; the sandwich is a semilinear, homogeneous quadratic operation in the parameter and linear in the argument.

**Proof.** $(\alpha Q)^{\dagger} = \bar\alpha Q^{\dagger}$ and $(\alpha Q)T(\bar\alpha Q^{\dagger}) = |\alpha|^{2}QTQ^{\dagger}$.

**Remark (the Hilbert-algebra sandwich is the definite case).** When $J = \mathrm{id}$ the indefinite adjoint is the Hilbert adjoint, the dagger sandwich is the sandwich $\Theta_Q(T) = QTQ^{*}$ of a Hilbert algebra, and every statement below reduces to the Hilbert one; the indefinite theory is the same family of operations read with a form of nonzero rank.

## Preservation of the Form and of J-Positivity

**Theorem (form preservation by $J$-unitary parameters).** Let $Q$ be $J$-unitary, $Q^{\dagger}Q = QQ^{\dagger} = 1$. Then for every $T$ and all $x, y$

$$
[H_{Q}(T)x, H_{Q}(T)y] = [TQ^{\dagger}x, TQ^{\dagger}y] , \qquad [H_{Q}(T)x,y] = [TQ^{\dagger}x, Q^{\dagger}y] ,
$$

and $H_{Q}(T)$ is $J$-isometric whenever $T$ is; in particular the $J$-unitary group acts on the operators by sandwiches preserving the indefinite geometry.

**Proof.** The elementary rule is $[Qx,y] = [x,Q^{\dagger}y]$, which follows from $[x,y] = \langle Jx,y\rangle$ and $(Qx,y) = (x,Q^{*}y)$. With $x$ replaced by $TQ^{\dagger}x$ it gives $[QTQ^{\dagger}x,y] = [TQ^{\dagger}x,Q^{\dagger}y]$, the second identity; the first follows by applying the rule once more with $y$ replaced by $H_{Q}(T)y$. If $T$ is $J$-isometric then $[TQ^{\dagger}x,TQ^{\dagger}y] = [Q^{\dagger}x,Q^{\dagger}y]$, and $Q^{\dagger}$ is $J$-unitary with $Q$, so this is $[x,y]$.

**Proposition (preservation of $J$-self-adjointness and $J$-positivity).** If $T$ is $J$-self-adjoint then $H_{Q}(T)$ is $J$-self-adjoint; if $T$ is $J$-positive and $Q$ is $J$-unitary then $H_{Q}(T)$ is $J$-positive; and if $T$ is $J$-unitary then $H_{Q}(T)$ is $J$-unitary.

**Proof.** The first statement is $H_Q(T)^{\dagger} = H_Q(T^\dagger) = H_Q(T)$ for $J$-self-adjoint $T$; for the second, $[H_Q(T)x,x] = [TQ^{\dagger}x,Q^{\dagger}x]\geq0$ by the second identity of the theorem and the $J$-positivity of $T$; the third is the isometry statement applied twice.

**Proposition (the $J$-adjoint sandwich).** With $Q = J$ one has $J^{\dagger} = J$ and $H_{J}(T) = JTJ$; this sandwich is the dictionary between the Hilbert data and the indefinite ones: $H_{J}(T)$ is Hilbert-self-adjoint exactly when $T$ is, and $H_{J}(T)\geq0$ in the Hilbert sense exactly when $T\geq0$. The link with the indefinite notions is the dictionary $T$ is $J$-self-adjoint $\iff$ $JT$ is Hilbert-self-adjoint, and in that case $H_{J}(T) = JTJ = T^{*}$.

**Proof.** $H_J(T) = JTJ$ and $(JTJ)^{*} = JT^{*}J$, so $H_J(T)$ is Hilbert-self-adjoint iff $T^{*}=T$; further $\langle JTJx,x\rangle = \langle T(Jx),Jx\rangle$ and $J$ is surjective, so $H_J(T)\geq0$ iff $T\geq0$. Finally $T$ is $J$-self-adjoint iff $JT^{*}J=T$, i.e. $T^{*}=JTJ=H_J(T)$, iff $JT^{*} = TJ$, which says $JT$ is Hilbert-self-adjoint.

## The Kernel and the Image

**Theorem (kernel and image for invertible parameters).** Let $Q$ be invertible. Then for every $T$

$$
\ker H_{Q}(T) = Q^{\dagger-1}\bigl(\ker T\bigr) = (Q^{\dagger})^{-1}\ker T , \qquad \mathrm{im}\,H_{Q}(T) = Q\bigl(\mathrm{im}\,T\bigr) ,
$$

and for $J$-unitary $Q$ these read $\ker H_{Q}(T) = Q\ker T$ and $\mathrm{im}\,H_{Q}(T) = Q\,\mathrm{im}\,T$.

**Proof.** $QTQ^{\dagger}x = 0 \iff TQ^{\dagger}x = 0$, so $x\in\ker H_Q(T) \iff Q^{\dagger}x\in\ker T$; the image statement is the same computation with the roles reversed, and $Q$ maps the image of $T$ onto the image of the sandwich.

**Corollary (rank and index).** For $J$-unitary $Q$ the sandwich preserves the dimension of the kernel, the codimension of the image and hence the Fredholm index of $T$; it does not preserve the Hilbert-orthogonal complement of the image, only the $J$-orthogonal one.

**Proof.** $Q$ is an isomorphism of the vector space $K$ and an isometry of the indefinite form; the kernel and image statements are the theorem, and the orthogonality statement is that $Q$ preserves $[\cdot,\cdot]$ but not $\langle\cdot,\cdot\rangle$.

**Remark (what is preserved and what is not).** The sandwich by a $J$-unitary $Q$ preserves the kernel dimension, the range and its codimension, and the indefinite geometry; it does not preserve the Hilbert norm, the Hilbert-orthogonal complements, the spectrum or the Hilbert positive cone. This is the exact sense in which the indefinite sandwich is a symmetry of the form and not of the metric.

## The Unitary Slice and Automorphisms

**Theorem (the sandwich is the inner automorphism on the $J$-unitary group).** For $J$-unitary $Q$ the map $T\mapsto H_{Q}(T) = QTQ^{\dagger}$ is an algebra automorphism of $B(K)$ preserving the $J$-adjoint operation, with inverse $H_{Q^{\dagger}}$; the assignment $Q\mapsto H_{Q}$ is a group homomorphism from the $J$-unitary group $\mathcal{U}_{J}(K)$ into $\mathrm{Aut}(B(K))$ with kernel the scalars of modulus one.

**Proof.** Multiplicativity and preservation of the $J$-adjoint are the laws of the first section with $Q^{\dagger}Q = 1$; the inverse statement is $H_{Q}H_{Q^{\dagger}} = H_{QQ^{\dagger}} = \mathrm{id}$; the kernel statement is that $QTQ^{\dagger} = T$ for all $T$ forces $Q$ to be a scalar.

**Proposition (what the automorphism does to the $J$-self-adjoint part).** The automorphism $H_{Q}$ maps the real space of $J$-self-adjoint operators onto itself and the $J$-positive cone onto itself; on the $J$-unitary group it is the conjugation $U\mapsto QUQ^{\dagger}$, which is the defining action of $\mathcal{U}_{J}(K)$ on itself.

**Proof.** Preservation of $J$-self-adjointness and of $J$-positivity is the theorem of the previous section; the action on the unitary group is multiplicativity.

**Remark (the sandwich generates the inner symmetries).** Every $J$-unitary equivalence of operators is a sandwich, and every sandwich by a $J$-unitary element is a symmetry of the indefinite geometry. The inner symmetries of the theory are therefore exactly the sandwiches, and the outer ones — the modular and spectral operations that do not come from an element — are what the theory cannot express as a sandwich; this is the same dichotomy as in the Hilbert-algebra case, where the sandwiches give the inner automorphisms and the modular flow is generally outer.

## Contrast with the Hilbert Case

**Proposition (Hilbert space).** If $J = \mathrm{id}$ then $K$ is a Hilbert space, every $Q$ with $Q^{*}Q = QQ^{*} = 1$ is unitary and $H_{Q}(T) = QTQ^{*}$; the sandwich is a unitary equivalence, so it preserves the Hilbert norm, the spectrum, the Hilbert positive cone, the Hilbert-orthogonal complements and the whole Hilbert spectral theory.

**Proof.** With $J = \mathrm{id}$ the indefinite adjoint is the Hilbert adjoint and the statements are the definitions of unitary equivalence.

**Theorem (Krein space: the failures).** For a $J$-unitary $Q$ that is not Hilbert-unitary, the sandwich $H_{Q}$ does not preserve the Hilbert norm, the Hilbert-orthogonal direct sum decompositions, the Hilbert positive cone or the spectrum; it preserves the indefinite form, the $J$-self-adjointness, the $J$-positivity, the $J$-unitarity and the kernel and image of every operator.

**Proof.** A $J$-unitary $Q$ satisfies $Q^{*}JQ = J$ and is Hilbert-unitary only if moreover $Q^{*}Q = 1$; when it is not, the sandwich changes the Hilbert norm, and the spectrum is not preserved because a $J$-self-adjoint operator has conjugate-symmetric spectrum while its sandwich by a merely form-preserving $Q$ need not; the positive statements are the theorems above.

**Remark (why the contrast matters).** The Hilbert sandwich is the natural notion of equivalence in Hilbert space, and it preserves everything. The indefinite sandwich is the natural notion of equivalence in a Krein space, and it preserves only the indefinite structure; the resulting equivalence relation on $J$-self-adjoint operators is coarser than similarity, and the classification of $J$-self-adjoint operators up to it is the classification of their invariants under form-preserving change of basis. This is why the spectral theory of *Spectral Theory on Krein Spaces* cannot be imported from the Hilbert theory by transport along a sandwich.

## Worked Cases

### The Fundamental Symmetry

For $Q = J$ the sandwich is $H_{J}(T) = JTJ$; it is Hilbert-self-adjoint exactly when $T$ is and Hilbert-positive exactly when $T$ is, $H_{J}$ is an involution on the space of operators, and for $T$ $J$-self-adjoint the sandwich is the Hilbert adjoint, $H_{J}(T)=T^{*}$. This is the translation dictionary between the indefinite and the Hilbert descriptions, read as a sandwich.

### Matrices

For $K = \mathbb{C}^{1,1}$ with $J = \mathrm{diag}(1,-1)$ and $Q = \left(\begin{smallmatrix}\cosh t & \sinh t\\ \sinh t & \cosh t\end{smallmatrix}\right)$, the operator $Q$ is $J$-unitary but not unitary; the sandwich $H_{Q}(J)$ is a $J$-self-adjoint operator with Hilbert norm different from that of $J$, and its Hilbert spectrum differs from $\{-1,+1\}$ while its indefinite spectrum is the same.

### The Definite Case

For $J = \mathrm{id}$ the sandwich by a unitary $Q$ is conjugation by a unitary, and kernel, image, spectrum, norm and positive cone are all preserved; the contrast of the previous section collapses.

## Summary

The **Hermitian sandwich** on a Krein space is $H_{Q}(T) = QTQ^{\dagger}$, with $Q^{\dagger} = JQ^{*}J$; it satisfies $H_Q(T^{\dagger}) = H_Q(T)^{\dagger}$, $H_Q(H_S(T)) = H_{QS}(T)$, and it is multiplicative in the argument exactly when $Q$ is $J$-isometric. For $J$-**unitary** $Q$ the sandwich **preserves the indefinite form** in the twisted sense $[H_Q(T)x,H_Q(T)y] = [TQ^{\dagger}x,TQ^{\dagger}y]$, it preserves **$J$-self-adjointness**, **$J$-positivity** and **$J$-unitarity**, and it is an algebra automorphism of $B(K)$; the **kernel and the image** are transported exactly, $\ker H_Q(T) = Q\ker T$ and $\mathrm{im}\,H_Q(T) = Q\,\mathrm{im}\,T$, so the kernel dimension, the range and the index are preserved. The **contrast with the Hilbert case** is that a $J$-unitary operator need not be Hilbert-unitary: the sandwich preserves the indefinite geometry — form, positivity, self-adjointness, kernel and image — but not the Hilbert norm, the Hilbert-orthogonal decompositions, the Hilbert positive cone or the spectrum, so the indefinite sandwich is a symmetry of the form rather than of the metric and cannot transport the Hilbert spectral theory. The indefinite adjoint is *J-Self-Adjoint and J-Unitary Operators*, the form and the symmetry are *Krein Spaces* and *The Fundamental Symmetry*, the positivity is *Krein Algebras* and *The J-Positive Cone and the J-Order*, the Hilbert-algebra sandwich is *The Adjoint of the Sandwich on a Hermitian Algebra*, and the spectral consequences are *Spectral Theory on Krein Spaces*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H_{Q}(T) = QTQ^{\dagger}$ | The Hermitian sandwich |
| $Q^{\dagger} = JQ^{*}J$ | The indefinite adjoint of the parameter |
| $H_{Q}(T^{\dagger}) = H_{Q}(T)^{\dagger}$ | The sandwich commutes with adjunction |
| $[H_{Q}(T)x,y] = [TQ^{\dagger}x,Q^{\dagger}y]$ | Form preservation for $J$-unitary $Q$ |
| $J$-positivity preserved | $[H_Q(T)x,x] = [TQ^{\dagger}x,Q^{\dagger}x]$ |
| $\ker H_{Q}(T) = Q\ker T$ | Kernel for $J$-unitary $Q$ |
| $\mathrm{im}\,H_{Q}(T) = Q\,\mathrm{im}\,T$ | Image for $J$-unitary $Q$ |
| $J = \mathrm{id}$ | Hilbert case, where the sandwich is unitary equivalence |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the form-preserving transformations of a Krein space.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the unitary group of a Krein space and its action.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the matrix form of the sandwich and its invariants.
- Peter Jonas, "On the spectral theory of operators on Krein spaces", in *Operator Theory: Advances and Applications* (Birkhäuser), for the limits of form-preserving equivalence.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the Hilbert-algebra sandwich $\Theta_x(y) = xyx^{\dagger}$ in the definite case.
