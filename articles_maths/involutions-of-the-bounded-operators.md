
# __Involutions of the Bounded Operators__

## Introduction

The algebra $B(H)$ of bounded operators on a Hilbert space carries a canonical involution, the adjoint, and every non-degenerate bounded form on $H$ defines a second one: the form-adjoint $T \mapsto T^{\dagger}$, given by $B(Tx, y) = B(x, T^{\dagger}y)$, is the conjugate $\Phi^{-1}T^{*}\Phi$ of the canonical adjoint by the operator $\Phi$ of the form, and it is again an involutive anti-automorphism of $B(H)$. Each involution singles out its own **unitary group**, the operators satisfying $T^{\dagger}T = TT^{\dagger} = \mathrm{id}$, and these are the classical groups: the unitary group of the inner product, the orthogonal and the symplectic groups of the symmetric and the alternating forms, and the indefinite unitary groups of the indefinite Hermitian forms. The involutions differ from one another by conjugation, the form-adjoint being conjugate to the canonical one, and in finite dimension every involution of the algebra that is compatible with the operator norm is of this kind.

This article develops the involutions of $B(H)$ and the groups they define. The canonical adjoint and its properties are *The Adjoint of a Bounded Operator*; the abstract involutive Banach algebras and the $\ast$-automorphisms are *Involutive Banach Algebras and the Gelfand–Naimark Theorem* and *Operator Algebras*; the forms that induce the involutions are *Banach and Hilbert Spaces*, and the indefinite hermitian forms and their geometry are Part III, named and not used; the finite-dimensional forms and their classical groups are *Hilbert Algebras*. The adjoint defined by an abstract dual pairing is *The Dual Pairing and the Adjoint*. No analysis and no spectral theory is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $H$ is a Hilbert space over $\mathbb{K}$ with inner product $\langle\cdot,\cdot\rangle$, $B(H)$ is its algebra of bounded operators, $T^{*}$ is the canonical adjoint, and $B$ is a non-degenerate bounded sesquilinear form on $H$ with induced operator $\Phi \in B(H)$, $B(x,y) = \langle x, \Phi y\rangle$, assumed invertible with bounded inverse; the **form-adjoint** is $T^{\dagger}$. The forms are owned by the form theory of this Part and are used here only through the operator $\Phi$.

## The Involutions of B(H)

**Definition.** An **involution** of $B(H)$ is a map $T \mapsto T^{\sharp}$ that is conjugate-linear, reverses products, $(ST)^{\sharp} = T^{\sharp}S^{\sharp}$, is its own inverse, $T^{\sharp\sharp} = T$, and fixes the identity. The canonical adjoint $T \mapsto T^{*}$ is one; the form-adjoint $T \mapsto T^{\dagger}$ of a non-degenerate bounded form is another.

**Theorem (existence of the form-adjoint).** Let $B$ be a non-degenerate bounded sesquilinear form with induced operator $\Phi$, $B(x,y) = \langle x, \Phi y\rangle$, and suppose $\Phi$ is invertible with bounded inverse. Then for every $T \in B(H)$ there is a unique $T^{\dagger} \in B(H)$ with

$$
B(Tx, y) = B(x, T^{\dagger}y) \qquad (x, y \in H),
$$

and

$$
T^{\dagger} = \Phi^{-1}\,T^{*}\,\Phi .
$$

The map $T \mapsto T^{\dagger}$ is an involution of $B(H)$, and it fixes the identity; it is the canonical adjoint exactly when $\Phi$ is a scalar multiple of the identity.

**Proof.** $B(Tx,y) = \langle Tx,\Phi y\rangle = \langle x, T^{*}\Phi y\rangle = B(x, \Phi^{-1}T^{*}\Phi y)$, so $T^{\dagger} = \Phi^{-1}T^{*}\Phi$ is a solution, and it is unique because $B$ is non-degenerate. The map is conjugate-linear and reverses products as a composite of the canonical adjoint with the conjugation by the invertible $\Phi$, and $(\Phi^{-1}T^{*}\Phi)^{*}$-computation gives $T^{\dagger\dagger} = \Phi^{-1}T\Phi = T$. It equals the canonical adjoint iff $\Phi^{-1}T^{*}\Phi = T^{*}$ for all $T$, that is iff $\Phi$ is central in $B(H)$, i.e. a scalar.

**Proposition (the involutions are conjugate).** The form-adjoint is the canonical adjoint transported by the similarity $\Phi$,

$$
T^{\dagger} = \Phi^{-1}\,T^{*}\,\Phi ,
$$

so it is an involution of $B(H)$ of the same kind as the canonical one, and the map $T \mapsto \Phi T$ is an isomorphism of $B(H)$ with the canonical involution onto $B(H)$ with the form involution. In particular the two involutions have the same structural properties: both reverse products, both are isometric for the operator norm, and both are homeomorphisms for the weak, strong and weak-star topologies.

**Proof.** The displayed identity is the theorem; the transport of the involution is the definition of an isomorphism of involutive algebras, and the structural properties are inherited because the similarity by $\Phi$ is a bounded isomorphism with bounded inverse and preserves the operator topologies.

**Proposition (the $\ast$-automorphisms and the inner case).** An **$\ast$-automorphism** of $B(H)$ is an algebra automorphism commuting with the canonical involution. In finite dimension every $\ast$-automorphism of $B(H)$ is $\mathrm{Ad}_{U}(T) = UTU^{*}$ for a unitary $U$, so the group of $\ast$-automorphisms is the projective unitary group $U(H)/\{\lambda\mathrm{id}\}$; the form-adjoint of a form with Hermitian operator $\Phi = \Phi^{*}$ is the canonical adjoint of the similar algebra $\Phi^{1/2}B(H)\Phi^{-1/2}$.

**Proof.** Finite-dimensional $\ast$-automorphisms are inner by the classification of the $\ast$-automorphisms of a finite-dimensional $C^{*}$-algebra, owned by *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the unitary can be normalised modulo the scalars, and the second statement is the transport by $\Phi^{1/2}$ when $\Phi$ is positive invertible Hermitian.

## The Classical Groups

**Definition.** For an involution $T \mapsto T^{\sharp}$ of $B(H)$ the **unitary group** is

$$
U(H, \sharp) = \{T \in B(H) : T^{\sharp}T = TT^{\sharp} = \mathrm{id}\} ,
$$

a group under multiplication; for the canonical involution it is the unitary group $U(H)$, and for the form-adjoint of $B$ it is the group of $B$-isometries.

**Theorem (the unitary group of a form).** For the form-adjoint of a non-degenerate bounded form $B$ with induced operator $\Phi$,

$$
T^{\dagger}T = \mathrm{id} \iff T^{*}\Phi T = \Phi \iff B(Tx, Ty) = B(x, y) \ \text{for all } x, y ,
$$

so the unitary group of the form is the group of bounded operators preserving $B$; it is a closed subgroup of $B(H)$ for the norm topology, hence a topological group, and it contains the identity and is closed under inverses by the involution.

**Proof.** $T^{\dagger}T = \Phi^{-1}T^{*}\Phi T = \mathrm{id}$ iff $T^{*}\Phi T = \Phi$; evaluating gives $B(Tx,Ty) = \langle Tx,\Phi Ty\rangle = \langle x, T^{*}\Phi Ty\rangle = \langle x,\Phi y\rangle = B(x,y)$. The group is closed because it is the common zero set of the continuous maps $T \mapsto T^{*}\Phi T - \Phi$ and $T \mapsto TT^{\dagger}-\mathrm{id}$; it is a topological group with the induced topology.

**Theorem (the classical cases).** The unitary group of the form $B$ takes the classical values:

1. for $B$ the inner product on a complex Hilbert space, $U(H)$, the unitary group, and on a real Hilbert space $O(H)$, the orthogonal group;
2. for $B$ a non-degenerate symmetric bilinear form on a real space, the orthogonal group of $B$;
3. for $B$ a non-degenerate alternating (skew-symmetric) form, the symplectic group $Sp(H,B)$;
4. for $B$ an indefinite non-degenerate Hermitian form of signature $(p,q)$ on $\mathbb{K}^{n}$, the indefinite unitary group $U(p,q)$.

**Proof.** These are the definitions read through the theorem: the preservation of the form is the defining condition in each case, the group being unitary, orthogonal or symplectic according to the symmetry type of $B$. The indefinite Hermitian forms and their geometry are Part III, named here and not developed; the finite-dimensional forms and the groups are *Hilbert Algebras*.

**Proposition (the groups under conjugation).** Two forms that are equivalent, $B' = B \circ (\Phi^{-1}\times\Phi^{-1})$ with $\Phi$ invertible, define conjugate involutions and conjugate unitary groups, $U(H,B') = \Phi\,U(H,B)\,\Phi^{-1}$; the classification of the classical groups is therefore the classification of the forms up to equivalence, which is *Hilbert Algebras*, in the finite-dimensional case, and Part III in general.

**Proof.** If $B(x,y) = B'(\Phi x, \Phi y)$ then $T$ preserves $B$ iff $\Phi T \Phi^{-1}$ preserves $B'$, giving the conjugation of the groups; the classification statement is the cited one.

## Examples

**Example (the self-adjoint and skew parts of an involution).** For each involution $T \mapsto T^{\sharp}$ of $B(H)$ the algebra splits over $\mathbb{R}$ into the $\sharp$-self-adjoint operators $T = T^{\sharp}$ and the $\sharp$-skew operators $T = -T^{\sharp}$, with $T = \frac12(T+T^{\sharp}) + \frac12(T-T^{\sharp})$; for the canonical involution these are the self-adjoint and skew-adjoint operators of *The Adjoint of a Bounded Operator*, and for the form-adjoint they are the operators self-adjoint or skew with respect to $B$.

**Example (the Minkowski form).** On $\mathbb{C}^{n}$ with the form $B(x,y) = \sum_{i=1}^{p}x_{i}\overline{y_{i}} - \sum_{i=p+1}^{n}x_{i}\overline{y_{i}}$ of signature $(p,q)$, the induced operator is $\Phi = \mathrm{diag}(1,\dots,1,-1,\dots,-1)$, the form-adjoint is $T^{\dagger} = \Phi T^{*}\Phi$, and the unitary group is the indefinite unitary group $U(p,q)$; its self-adjoint part contains the operators that are $\Phi$-self-adjoint, and the indefinite geometry is Part III.

**Example (the real orthogonal and the symplectic cases).** On $\mathbb{R}^{n}$ with the standard symmetric form the form-adjoint is the transpose, $T^{\dagger} = T^{\mathsf{T}}$, and the unitary group is the orthogonal group $O(n)$; on $\mathbb{R}^{2m}$ with the standard alternating form $B(x,y) = \sum_{i}(x_{2i-1}y_{2i} - x_{2i}y_{2i-1})$ the form-adjoint is the symplectic transpose and the unitary group is the symplectic group $Sp(2m,\mathbb{R})$.

## Summary

The algebra $B(H)$ of bounded operators on a Hilbert space carries the canonical involution $T \mapsto T^{*}$, the adjoint, and every non-degenerate bounded form $B$ with induced invertible operator $\Phi$, $B(x,y) = \langle x,\Phi y\rangle$, defines the form-adjoint $T^{\dagger} = \Phi^{-1}T^{*}\Phi$, which is again an involutive anti-automorphism of $B(H)$ and is the canonical adjoint transported by the similarity $\Phi$; the two involutions therefore have the same structural properties, and they coincide only for a central $\Phi$. The unitary group of an involution is the group of operators satisfying $T^{\sharp}T = TT^{\sharp} = \mathrm{id}$; for the form-adjoint it is the group of operators preserving $B$, closed in $B(H)$ and hence a topological group, and it takes the classical values: the unitary and orthogonal groups of the inner product, the orthogonal group of a symmetric bilinear form, the symplectic group of an alternating form, and the indefinite unitary groups $U(p,q)$ of the indefinite Hermitian forms. The involutions of equivalent forms are conjugate, so the classification of the groups reduces to the classification of the forms, which is *Hilbert Algebras* in finite dimension and Part III in general. The adjoint defined by an abstract dual pairing is *The Dual Pairing and the Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$, $\langle\cdot,\cdot\rangle$ | Hilbert space and its inner product |
| $B(H)$ | bounded operators |
| $T^{*}$ | canonical adjoint |
| $B$, $\Phi$ | non-degenerate bounded form and its induced operator, $B(x,y) = \langle x,\Phi y\rangle$ |
| $T^{\dagger} = \Phi^{-1}T^{*}\Phi$ | form-adjoint, an involution of $B(H)$ |
| $T^{\sharp}$ | a general involution of $B(H)$ |
| $U(H,\sharp)$ | unitary group of an involution |
| $U(H)$, $O(H)$, $Sp(H,B)$, $U(p,q)$ | the classical groups |

## Further Reading

- Paul R. Halmos, *Linear Algebra Problem Book* (Mathematical Association of America, 1995), for the classical groups and the forms that define them.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the involutions of $B(H)$, the $\ast$-automorphisms and the unitaries.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the adjoint, the operator topologies and the unitary group.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the sesquilinear forms, the classical groups and the Witt theory.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (AMS, 2002), for the orthogonal, unitary and symplectic groups and the forms that define them.
