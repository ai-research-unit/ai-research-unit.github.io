
# __Real Structures on the Operator Layer__

## Introduction

The **operator layer** of a variety is the sheaf of differential operators $\mathcal{D}_X$ of *The Sheaf of Differential Operators*, an algebra under composition whose elements act on the structure sheaf and on the quasi-coherent modules; a **real structure** on it is an involution of the operator algebra that is semilinear over the structure sheaf, the action of the Galois group by conjugation. The operators split into the **fixed operators**, those commuting with the conjugation, which are exactly the operators defined over the base field, and the **skew operators**, those satisfying the conjugate relation with the sign $-1$; the fixed part is the operator layer of the descended variety, and the descent of the algebra and of its modules is the content of the article. This article fixes the real structure on the operator layer, the conjugation and its two eigenspaces, the descent of the operator algebra, and the distinction between the conjugation and the adjoint, and it is the first article of the `- * Operator Theory` group.

The article reads the real structure of *Real Structures on Varieties and Galois Descent* on the operators, and it prepares *Galois Descent for the Operator Layer*, the second article of the group, which treats the descent data and the effective descent of the operator modules. The operator layer is that of *Operators on a Variety*, *The Pullback Operator of a Morphism* and *The Sheaf of Differential Operators* of this category; the conventions of the conjugation and of the adjoint on the operator layer are those of the written *Involutions on the Operator Layer* of the category *Groups*, where the two operations are separated, and the descent is Part I's *Descent Theory* and *Real Forms and the Descent of an Algebra*. The pairing that defines the adjoint on the operator layer of a variety — the trace form of *The Weil Restriction and the Trace Form* — is used here only for the comparison of the conjugation with the adjoint, and the analytic and smooth operators of Part III are excluded.

Throughout $L/k$ is a finite Galois extension with group $G$, $X$ is a variety over $k$, $X_L$ its base change, and $\mathcal{D} = \mathcal{D}_{X_L}$ the operator layer with the semilinear action of the geometric involution; the general element of $\mathcal{D}$ is written $T$, the conjugation is $\mathrm{ad}_\sigma$, and the two eigenspaces are $\mathcal{D}_+$ and $\mathcal{D}_-$.

## The Operator Layer with a Real Structure

### The Operator Layer

**Definition.** The **operator layer** of $X_L$ is the sheaf of algebras $\mathcal{D}_{X_L}$ of the differential operators of *The Sheaf of Differential Operators*, with the multiplication the composition, the unit the identity, and the order filtration $\mathcal{D}^m$. When only the zeroth order is used it is the structure sheaf $\mathcal{D}^0 = \mathcal{O}_{X_L}$, with the multiplication operators of *Operators on a Variety*; when only the first order is used it is $\mathcal{O}_{X_L}\oplus\mathcal{T}_{X_L}$, with the derivations.

**Proposition (the operator layer of the structure sheaf).** The layer $\mathcal{D}_{X_L}$ is generated over $\mathcal{O}_{X_L}$ by the derivations $\mathcal{T}_{X_L}$, with the relations of *The Sheaf of Differential Operators*; its associated graded is $\operatorname{gr}\mathcal{D}_{X_L}\cong\operatorname{Sym}_{\mathcal{O}_{X_L}}\mathcal{T}_{X_L}$, and the order filtration is preserved by every algebra automorphism that preserves $\mathcal{O}_{X_L}$ and $\mathcal{T}_{X_L}$.

*Proof.* The generation and the isomorphism of the graded algebra are those of *The Sheaf of Differential Operators*; an algebra automorphism preserving the functions and the derivations preserves the order, hence the filtration and the graded algebra.

### The Conjugation of the Operator Layer

**Definition.** A **real structure** on the operator layer $\mathcal{D}_{X_L}$ is a semilinear action of $G$ by algebra automorphisms,
$$
\mathrm{ad}_\sigma : \mathcal{D}_{X_L}\longrightarrow\mathcal{D}_{X_L}, \qquad
\mathrm{ad}_\sigma(ST) = \mathrm{ad}_\sigma(S)\,\mathrm{ad}_\sigma(T), \qquad
\mathrm{ad}_\sigma(fT) = \sigma(f)\,\mathrm{ad}_\sigma(T),
$$
for $\sigma\in G$, $f\in\mathcal{O}_{X_L}$ and $S,T\in\mathcal{D}_{X_L}$, with $\mathrm{ad}_{\sigma\tau} = \mathrm{ad}_\sigma\circ\mathrm{ad}_\tau$; the map $\mathrm{ad}_\sigma$ is the **conjugation** by the geometric involution of $X_L$. It is an algebra automorphism that is semilinear over the structure sheaf, and in the case $G=\mathbb{Z}/2$ it is an involution of the operator layer.

**Proposition (the conjugation is realised by the geometric involution).** For the geometric involution $\sigma$ of $X_L$ the conjugation
$$
\mathrm{ad}_\sigma(T) = \sigma^\sharp\circ T\circ(\sigma^\sharp)^{-1}
$$
is an algebra automorphism of $\mathcal{D}_{X_L}$, semilinear over $\mathcal{O}_{X_L}$, of order two when $\sigma$ is; it preserves the order filtration and the associated graded, and it acts on the functions by $\sigma^\sharp$ and on the derivations by
$$
\mathrm{ad}_\sigma(\partial) = \sigma^\sharp\circ\partial\circ(\sigma^\sharp)^{-1}
$$
for a derivation $\partial$.

*Proof.* The map $\sigma^\sharp\circ(-)\circ(\sigma^\sharp)^{-1}$ is a conjugation by an invertible algebra element, hence an algebra automorphism; the semilinearity is the semilinearity of $\sigma^\sharp$ over $\mathcal{O}_{X_L}$, checked on a function $f$ and an operator $T$: $\sigma^\sharp fT(\sigma^\sharp)^{-1} = \sigma(f)\sigma^\sharp T(\sigma^\sharp)^{-1}$. The order is the order of $\sigma$, and the preservation of the filtration and of the graded algebra is the previous proposition. The action on the derivations is the conjugation of an operator by an algebra automorphism, which is a derivation again.

**Example (the affine line and the Weyl algebra).** For $X = \mathbb{A}^1_k$ with base change $\mathbb{A}^1_L$ and the coordinate $x$, the operator layer is the Weyl algebra $A_1(L) = L\langle x,\partial\rangle$ with $[\partial,x]=1$, and the conjugation of the coefficients $\sigma(\ell x^n) = \sigma(\ell)x^n$ on the functions extends by $\mathrm{ad}_\sigma(\partial) = \partial$ and $\mathrm{ad}_\sigma(x) = x$. The fixed elements are the polynomials in $x,\partial$ with coefficients in $k$, the subalgebra $A_1(k)$, and the operator $i\partial$, for $L=\mathbb{C}$, $k=\mathbb{R}$, is skew: $\mathrm{ad}_\sigma(i\partial) = -i\partial$.

## The Fixed and the Skew Operators

### The Two Eigenspaces

**Definition.** Let $\mathrm{ad}_\sigma$ be the conjugation of the operator layer for a group $G$ generated by a single involution $\sigma$ over $L/k$. The **fixed operators** and the **skew operators** are
$$
\mathcal{D}_+ = \{T : \mathrm{ad}_\sigma(T) = T\}, \qquad \mathcal{D}_- = \{T : \mathrm{ad}_\sigma(T) = -T\},
$$
and the general element with the **conjugation parity** is an element of one of the two eigenspaces.

**Theorem (the decomposition of the operator layer).** When $2$ is invertible in $\mathcal{O}_{X_L}$ the operator layer splits into the two eigenspaces,
$$
\mathcal{D} = \mathcal{D}_+\oplus\mathcal{D}_-, \qquad T = \tfrac12\bigl(T+\mathrm{ad}_\sigma(T)\bigr)+\tfrac12\bigl(T-\mathrm{ad}_\sigma(T)\bigr),
$$
and $\mathcal{D}_+$ is the fixed subalgebra. In characteristic two the decomposition fails and every operator is fixed or nilpotent in the conjugation.

*Proof.* The average of an element with its conjugate is fixed and the difference is skew, so the two either generate or span; their sum is the whole layer by the displayed formula and their intersection is $0$ because an element fixed and skew at once is $T=-T$, so $2T=0$ and $T=0$ when $2$ is invertible. The fixed elements form a subalgebra because the conjugation is an algebra automorphism. In characteristic two the equation $\mathrm{ad}_\sigma(T)=T$ admits the nilpotent solutions $T+\mathrm{ad}_\sigma(T)$ with $T$ skew, and the two eigenspaces coincide with the fixed layer.

**Proposition (the parity of the product).** The eigenspaces multiply by the rule
$$
\mathcal{D}_+\cdot\mathcal{D}_+\subseteq\mathcal{D}_+, \qquad \mathcal{D}_+\cdot\mathcal{D}_-\subseteq\mathcal{D}_-, \qquad \mathcal{D}_-\cdot\mathcal{D}_-\subseteq\mathcal{D}_+ ,
$$
so that $\mathcal{D} = \mathcal{D}_+\oplus\mathcal{D}_-$ is a $\mathbb{Z}/2$-graded algebra with the even part the fixed operators, and the skew part is a module over the fixed part.

*Proof.* The conjugation is an algebra automorphism, so $\mathrm{ad}_\sigma(ST) = \mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T)$, and the signs multiply: the product of two operators of parities $\epsilon$ and $\delta$ has parity $\epsilon\delta$. This is the multiplicative rule of a $\mathbb{Z}/2$-grading.

### The Fixed Operators are the Descended Operators

**Theorem (the fixed algebra is the operator layer of the descended variety).** Let $X$ be a variety over $k$, let $L/k$ be a finite Galois extension with group $G$, and let the operator layer $\mathcal{D}_{X_L}$ carry the conjugation of the geometric involution. Then the fixed algebra is the operator layer of $X$,
$$
\mathcal{D}_{X_L}^{G}\ =\ \mathcal{D}_X .
$$

*Proof.* An operator on $X_L$ that is fixed by every $\sigma\in G$ is an operator whose coefficients are fixed, hence defined over $k$; the sheaf of the fixed operators is the descent of $\mathcal{D}_{X_L}$ along the base change, by the descent of the module category and of the algebra structure of Part I's *Descent Theory* and *Real Forms and the Descent of an Algebra*. On an affine chart the statement is that the $G$-invariants of the Weyl-type algebra $A\otimes_kL$ are $A$, computed from the coefficients by the fixed-point theorem of *The Galois Action as an Operator*.

**Corollary (the fixed derivations and the fixed differential operators).** The fixed derivations are the derivations of $X$, $\mathcal{T}_{X_L}^G = \mathcal{T}_X$, and the fixed differential operators of order at most $m$ are $\mathcal{D}_X^m$; the fixed part of the operator layer is a $\mathcal{D}_X$-algebra, and the associated graded of the fixed part is $\operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X$.

*Proof.* The derivations are the first-order operators and the fixed ones are the derivations defined over $k$ by the theorem; the order filtration restricts to the fixed part because the conjugation preserves it, and the associated graded is computed from the fixed functions and the fixed derivations.

**Example (the Weyl algebra and its fixed subalgebra).** For the affine line and $\mathbb{C}/\mathbb{R}$ the fixed algebra of the Weyl algebra $A_1(\mathbb{C})$ under the conjugation is $A_1(\mathbb{R})$, generated by $x$ and $\partial$ with $[\partial,x]=1$; the operator $x\partial$ is fixed, the operator $i\partial$ is skew, and the skew part is $iA_1(\mathbb{R})$, the module over the fixed algebra generated by $i$.

## The Conjugation and the Adjoint

**Definition.** Let the operator layer carry the **adjoint** operation of the written *Involutions on the Operator Layer* of the category *Groups*: for an operator $T$ the adjoint $T^{*}$ is defined by a nondegenerate bilinear pairing,
$$
\langle Tx,y\rangle = \langle x,T^{*}y\rangle ,
$$
which on a smooth proper variety is the trace pairing of *The Weil Restriction and the Trace Form* and of *The Galois Action on the Cohomology*. The adjoint is an **anti-automorphism** of the operator algebra, $(ST)^{*} = T^{*}S^{*}$, whereas the conjugation $\mathrm{ad}_\sigma$ is an **automorphism**, $\mathrm{ad}_\sigma(ST) = \mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T)$.

**Theorem (the two operations differ, and when they agree).** The conjugation by the geometric involution and the adjoint are distinct operations on the operator layer; they agree on an operator $T$ exactly when $T$ is invariant under the composite, that is when the adjoint of the conjugate equals the conjugate of the adjoint,
$$
\mathrm{ad}_\sigma(T)^{*} = \mathrm{ad}_\sigma(T^{*}) .
$$
When the pairing is invariant under the conjugation, $\langle\sigma x,\sigma y\rangle = \langle x,y\rangle$, the two operations commute on the whole layer, and the fixed operators and the self-adjoint operators are related by the decomposition of the layer.

*Proof.* The conjugation is an automorphism and the adjoint an anti-automorphism, so they cannot be the same operation on a noncommutative layer; on the commutative part they are the identity on the functions only when every function is fixed and self-adjoint. For the commuting identity, let the pairing be invariant, $\langle\sigma x,\sigma y\rangle=\langle x,y\rangle$; then for all $x,y$
$$
\langle \mathrm{ad}_\sigma(T)x,y\rangle = \langle \sigma T\sigma^{-1}x,y\rangle = \langle T\sigma^{-1}x,\sigma^{-1}y\rangle = \langle \sigma^{-1}x,T^{*}\sigma^{-1}y\rangle = \langle x,\sigma T^{*}\sigma^{-1}y\rangle = \langle x,\mathrm{ad}_\sigma(T^{*})y\rangle ,
$$
so $(\mathrm{ad}_\sigma T)^{*} = \mathrm{ad}_\sigma(T^{*})$ by the uniqueness of the adjoint. This is the operator-level instance of the general rule that the involution on the elements and the adjoint on the operators are two structures and not one, and their agreement is proved and never assumed.

**Corollary (the self-adjoint fixed operators).** When the pairing is invariant, an operator $T$ is fixed and self-adjoint exactly when $\mathrm{ad}_\sigma(T) = T = T^{*}$; the self-adjoint fixed operators form a real subspace of the fixed algebra, and the skew fixed operators are the fixed part of the skew-adjoint operators. The unitary operators are the fixed operators with $T^{*}T = TT^{*} = \mathrm{id}$.

*Proof.* The conditions $\mathrm{ad}_\sigma(T)=T$ and $T^{*}=T$ are independent, and their intersection is the fixed self-adjoint part; the fixed skew-adjoint operators are cut out by $T^{*}=-T$ inside the fixed algebra. The unitarity is the condition of the written *Involutions on the Operator Layer*, restricted to the fixed algebra.

## Examples

**Example (the coordinate and the derivative).** On the affine line with the coordinate $x$ and the derivative $\partial$, the conjugation fixes $x$ and $\partial$, so both are fixed operators; the monomial $x^m\partial^n$ is fixed, the operator $i\,x^m\partial^n$ is skew for $L=\mathbb{C}$, $k=\mathbb{R}$, and the fixed part of the Weyl algebra is generated by the fixed monomials. The self-adjoint operators for the trace pairing are those whose coefficients are real, and the two operations $\mathrm{ad}_\sigma$ and $(-)^{*}$ commute on the whole Weyl algebra for the $\mathbb{C}/\mathbb{R}$ example.

**Example (the ring of operators on a vector space with a real structure).** Let $V$ be a $k$-vector space and $V_L = V\otimes_kL$ with the semilinear involution, and let the operator layer be $\operatorname{End}_L(V_L)$ with the conjugation $\mathrm{ad}_\sigma(T) = \Sigma_\sigma T\Sigma_\sigma^{-1}$ of the linear extension $\Sigma_\sigma$ of the involution. The fixed operators are $\operatorname{End}_k(V)$; the skew operators satisfy $T\Sigma_\sigma = -\Sigma_\sigma T$, and the self-adjoint operators for the trace form $\operatorname{Tr}(ST)$ are the operators with $T^{*}=T$ in the sense of the transpose. This is the linear model of the operator layer, and the two operations on it are those of the written *Involutions on the Operator Layer* of the category *Groups*, with the group $\mathbb{Z}/2$ in place of $G$.

**Example (a derivation conjugated to its negative).** On the affine line with the involution $x\mapsto-x$ of the base change, the derivative satisfies $\mathrm{ad}_\sigma(\partial) = -\partial$, since $\partial$ is odd for the inversion of the coordinate: the derivative is a skew operator, the multiplication by $x$ is skew as well, and the product $x\partial$ is fixed. The fixed algebra of the operator layer for this involution is generated by $x^2$, $x\partial$ and $\partial^2$, the even elements of the Weyl algebra under the parity of the total degree.

## Summary

The **operator layer** of $X_L$ is the sheaf of algebras $\mathcal{D}_{X_L}$ of the differential operators, with the order filtration and the associated graded $\operatorname{Sym}_{\mathcal{O}}\mathcal{T}$. A **real structure** on it is a semilinear action of the Galois group by algebra automorphisms, realised by the geometric involution through the conjugation
$$
\mathrm{ad}_\sigma(T) = \sigma^\sharp\circ T\circ(\sigma^\sharp)^{-1},
$$
which is an automorphism of the operator algebra, semilinear over the structure sheaf, preserving the order filtration. For a single involution the layer splits into the **fixed operators** $\mathcal{D}_+ = \{T : \mathrm{ad}_\sigma(T)=T\}$ and the **skew operators** $\mathcal{D}_- = \{T : \mathrm{ad}_\sigma(T)=-T\}$ when $2$ is invertible, with the $\mathbb{Z}/2$-graded multiplication rule; the fixed part is the operator layer of the descended variety,
$$
\mathcal{D}_{X_L}^{G} = \mathcal{D}_X ,
$$
so the fixed derivations are the derivations of $X$. The conjugation is an **automorphism** of the operator layer, whereas the **adjoint** of the written *Involutions on the Operator Layer* is an **anti-automorphism**; the two are different operations, they agree on an operator exactly when the adjoint of the conjugate equals the conjugate of the adjoint, and they commute on the whole layer when the pairing is invariant under the conjugation. The distinction and the agreement are the conventions that the second article of the group, *Galois Descent for the Operator Layer*, uses.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{D}_{X_L}$ | the operator layer: the sheaf of the differential operators |
| $\operatorname{gr}\mathcal{D}\cong\operatorname{Sym}_{\mathcal{O}}\mathcal{T}$ | the associated graded; the symbol |
| $\mathrm{ad}_\sigma(T)=\sigma^\sharp T(\sigma^\sharp)^{-1}$ | the conjugation by the geometric involution |
| $\mathrm{ad}_\sigma(ST)=\mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T)$ | the conjugation is an algebra automorphism |
| $\mathrm{ad}_\sigma(fT)=\sigma(f)\mathrm{ad}_\sigma(T)$ | semilinearity over the structure sheaf |
| $\mathcal{D}_+ = \{T:\mathrm{ad}_\sigma(T)=T\}$ | the fixed operators |
| $\mathcal{D}_- = \{T:\mathrm{ad}_\sigma(T)=-T\}$ | the skew operators |
| $\mathcal{D}=\mathcal{D}_+\oplus\mathcal{D}_-$ | the eigenspace decomposition, when $2$ is invertible |
| $\mathcal{D}_+\mathcal{D}_+\subset\mathcal{D}_+$, $\mathcal{D}_+\mathcal{D}_-\subset\mathcal{D}_-$ | the $\mathbb{Z}/2$-graded multiplication |
| $\mathcal{D}_{X_L}^G=\mathcal{D}_X$ | the fixed algebra is the operator layer of $X$ |
| $\mathcal{T}_{X_L}^G=\mathcal{T}_X$ | the fixed derivations |
| $T^{*}$, $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$ | the adjoint: an anti-automorphism |
| $\mathrm{ad}_\sigma(T)^{*}=\mathrm{ad}_\sigma(T^{*})$ | commuting with the adjoint; the invariant pairing |
| $A_1(k)\subseteq A_1(L)$ | the Weyl algebra and its fixed subalgebra |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the distinction between an involution and an adjoint and the descent of an algebra with an involution.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the descent of the algebras and the modules along a Galois extension.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique IV* (Publications Mathématiques de l'IHÉS 32, 1967), for the descent of the algebras and the effective descent of the modules.
- Armand Borel, Pierre-Paul Grivel, Bernhard Kaup and others, *Algebraic D-Modules* (Perspectives in Mathematics 2, Academic Press, 1987), for the sheaf of the differential operators, its filtration and its modules.
- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the operator layer of a group and the two operations of the written *Involutions on the Operator Layer*, used here for the comparison of the conjugation with the adjoint.
