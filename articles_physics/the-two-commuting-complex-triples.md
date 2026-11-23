# __The Two Commuting Complex Triples__

## Introduction

The Lorentz algebra looks like two rotation algebras wearing each other's clothes. Change basis to

$$
\vec J_{\pm}=\tfrac12\bigl(\vec J\pm i\vec K\bigr),
$$

and the six-generator table becomes two three-generator tables that do not talk to each other: each triple closes as a rotation algebra, and every bracket between the two triples vanishes. The complexified algebra is therefore a direct sum of two copies of $\mathfrak{sl}(2,\mathbb{C})$, and the representation theory of the Lorentz group is the representation theory of that sum.

The change of basis costs complex coefficients, and the coefficients are the whole difficulty. The two triples are not the real $\mathfrak{su}(2)$ inside the Lorentz algebra; they are the two halves of its complexification. This article makes the change, proves the closure and the commutation, identifies the two triples geometrically as the self-dual and anti-self-dual bivectors, reads the adjoint representation as $(1,0)\oplus(0,1)$, and states why the real form decides unitarity.

The article assumes *The Six Generators and Their Commutators* for the table and the generators, and *The Isomorphisms and Their Dimensions* for the dimensions. It hands the eigenvalues to *The Two Casimirs of the Lorentz Algebra* and the representation theory to *The Finite-Dimensional Representations and Their Unitarity Defect*.

## The Change of Basis

### The Definition

$$
\vec J_{+}=\tfrac12\bigl(\vec J+i\vec K\bigr),\qquad \vec J_{-}=\tfrac12\bigl(\vec J-i\vec K\bigr),
$$

component by component: $J_{+k}=\tfrac12(J_\imath+iK_\imath)$ and $J_{-k}=\tfrac12(J_\imath-iK_\imath)$.

### The Complex Number in the Definition

The symbol $i$ in that display is the **scalar of the complexification**, not the central element of the algebra, and the difference is not pedantic. With the central element the combination vanishes identically, because $iK_\imath=i\cdot\tfrac12 i\vec e_\imath=-\tfrac12\vec e_\imath=-J_\imath$ and therefore

$$
J_\imath+iK_\imath=0 .
$$

That identity is correct, and it is the reason the two triples have no meaning inside the real algebra, and none inside the algebra read with its own complex structure either.

The complexification is the space of formal complex combinations,

$$
\mathfrak{so}(1,3)_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{so}(1,3),
$$

in which the scalar multiplies a real basis without being an element of the algebra. In that space $J_\imath+iK_\imath$ is a nonzero vector, and the two triples live there.

### The Two Must Not Be Identified

There is a natural map from the complexification into the algebra, $\digamma_{\mathrm{scl}}\otimes x\mapsto\digamma_{\mathrm{scl}} x$, and it is not injective. The element

$$
i\otimes\vec e_x-1\otimes i\vec e_x
$$

is nonzero in the complexification and maps to $i\vec e_x-i\vec e_x=0$ in the algebra. So $\mathbb{B}$ is a **quotient** of the complexification and the complexification is not a subalgebra of $\mathbb{B}$. This is the precise sense in which *The Isomorphisms and Their Dimensions* says that the complexification is a different object again:

$$
\mathfrak{so}(1,3)_{\mathbb{C}}\ \text{is not a subalgebra of}\ \mathbb{B},
\qquad
\mathfrak{so}(1,3)_{\mathbb{R}}\cong\mathfrak{sl}(2,\mathbb{C})\ \text{is}.
$$

A reader who tries to compute the two triples as biquaternions will get zero, and the zero is not an error of arithmetic; it is the identity above. The triples are objects of the complexification, and every formula in this article is a formula there.

### How the Checks Are Done

The numerical checks are performed on the real four-dimensional congruence matrices of the generators, in which $J_\imath$ and $K_\imath$ are real and the complexification unit $i$ is an external scalar, so the combinations $\tfrac12(\rho(J_\imath)\pm i\rho(K_\imath))$ are nonzero and the brackets below hold for them. The $2\times2$ image cannot serve for this purpose: there the central scalar is already inside the entries, $\mathsf{M}_2(K_\imath)=i\,\mathsf{M}_2(J_\imath)$, and the combination collapses to zero, as the identity above requires. This is the operational meaning of "the coefficient field's $i$": it is an operation on the array, and it is distinguishable from the central scalar because the central scalar is already inside the array.

## Each Triple Closes

### The Three Brackets

With the table $[J_i,J_j]=\epsilon_{\imath\jmath\ell}J_\imath$, $[J_i,K_j]=\epsilon_{\imath\jmath\ell}K_\imath$, $[K_i,K_j]=-\epsilon_{\imath\jmath\ell}J_\imath$,

$$
[J_{+i},J_{+j}]=\tfrac14\Bigl([J_i,J_j]+i[J_i,K_j]+i[K_i,J_j]-[K_i,K_j]\Bigr)
=\tfrac14\bigl(2\epsilon_{\imath\jmath\ell}J_\imath+2i\epsilon_{\imath\jmath\ell}K_\imath\bigr)=\epsilon_{\imath\jmath\ell}J_{+k}.
$$

The same computation with $i\to-i$ gives

$$
[J_{-i},J_{-j}]=\epsilon_{\imath\jmath\ell}J_{-k}.
$$

So each triple closes with the structure constants of a rotation algebra, and the factor $\tfrac12$ is exactly what makes the constant $\epsilon$ rather than $2\epsilon$.

### The Cross Brackets

$$
[J_{+i},J_{-j}]=\tfrac14\Bigl([J_i,J_j]-i[J_i,K_j]+i[K_i,J_j]+[K_i,K_j]\Bigr)
=\tfrac14\bigl(\epsilon_{\imath\jmath\ell}J_\imath-i\epsilon_{\imath\jmath\ell}K_\imath+i\epsilon_{\imath\jmath\ell}K_\imath-\epsilon_{\imath\jmath\ell}J_\imath\bigr)=0 .
$$

Every cross bracket vanishes. This is the whole content of the change of basis: the six-generator table, which has three non-trivial blocks, becomes two three-generator tables and a block of zeros.

### The Verification

Both statements are checked on the four-vector representation: the closure holds on all six ordered pairs of each triple with structure constants $\epsilon_{\imath\jmath\ell}$, and all nine cross brackets vanish to machine precision. The check is done with complex $4\times4$ matrices obtained from the congruence representation of *The Two Actions of One Group: Adjoint and Congruence*, which is the representation in which the two triples are most easily written.

## The Two Triples Commute

### The Consequence

A Lie algebra that is the span of two subalgebras with vanishing cross brackets is their direct sum. So

$$
\mathfrak{so}(1,3)_{\mathbb{C}}\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),
$$

and each summand is spanned by one triple.

The dimension count agrees: $3+3=6$ over $\mathbb{C}$, which is $12$ over $\mathbb{R}$, the dimension of the complexification of a six-dimensional real algebra.

### What Direct Sum Means for Representations

An irreducible representation of a direct sum is a tensor product of one irreducible representation of each summand. Each summand is $\mathfrak{sl}(2,\mathbb{C})$, whose irreducible representations are labelled by a half-integer $j$ and have dimension $2j+1$. So the irreducible representations of the complexified Lorentz algebra are labelled by a pair

$$
(m,n),\qquad \dim=(2m+1)(2n+1),
$$

and that pair is the entire classification. *The Finite-Dimensional Representations and Their Unitarity Defect* tabulates the first few.

### What It Does Not Mean

The direct sum is a statement about the **complexified** algebra. The real Lorentz algebra is not a direct sum of two real algebras, and no real subalgebra of it is a copy of $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. This is the subject of the section on the real form, and it is the point at which a reader is most likely to draw a false conclusion.

## The Self-Dual and Anti-Self-Dual Projections

### Bivectors

A Lorentz transformation's infinitesimal generator is a bivector $M_{\imath\jmath}=-M_{\jmath\imath}$, with six independent components: three $M_{0i}$ and three $M_{ij}$. The dictionary to the generators of this block is

$$
M_{0i}\longleftrightarrow K_i,\qquad M_{ij}\longleftrightarrow\epsilon_{\imath\jmath\ell}J_\imath,
$$

so a boost is a timelike-spacelike bivector and a rotation is a spacelike-spacelike one.

### The Hodge Star

On bivectors the Hodge star is

$$
\star M_{0i}=\tfrac12\epsilon_{\imath\jmath\ell}M_{j\imath},\qquad \star M_{j\imath}=-\epsilon_{j\imathi}M_{0i},
$$

which satisfies $\star^{2}=-1$ on real bivectors. The sign of the square is the Lorentzian sign pattern's: in the Euclidean case the star squares to $+1$ and there is no splitting, which is why the self-dual decomposition is a Lorentzian phenomenon and why *The SO(4) Route to the Euclidean Frame* has to say what replaces it.

### The Projections

With $\star^{2}=-1$ the operators

$$
\Pi_{\pm}=\tfrac12\bigl(1\mp i\star\bigr)
$$

are complementary projectors, and they split the complexified bivector space into the $\pm i$ eigenspaces of the star. Applied to the generators:

$$
\star J_\imath=-K_\imath,\qquad \star K_\imath=J_\imath,
$$

so

$$
\star\bigl(J_\imath+iK_\imath\bigr)=-K_\imath+iJ_\imath=i\bigl(J_\imath+iK_\imath\bigr),
\qquad
\star\bigl(J_\imath-iK_\imath\bigr)=-i\bigl(J_\imath-iK_\imath\bigr).
$$

Hence $\vec J_+$ spans the self-dual bivectors and $\vec J_-$ the anti-self-dual ones, and the two triples are the two eigenspaces. The factor $\tfrac12$ in the definition of the triples is the normalisation that makes the projector formula come out with unit coefficient.

### Why the Names Are the Right Ones

A bivector is self-dual when $\star F=iF$ and anti-self-dual when $\star F=-iF$. Those are the two eigenspaces just computed. On the field strength the same split is the subject of *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane*, and on the algebra it is the split of this section; the two are one statement seen in two carriers.

## The Adjoint as $(1,0)\oplus(0,1)$

### The Eight-Dimensional Adjoint

The adjoint action of the algebra on itself is eight-dimensional over $\mathbb{R}$. Its complexification splits as the two central directions plus the scalar-free part, and the scalar-free part splits into the two triples. So

$$
\mathbb{B}\ \text{under }[-,-]\ \cong\ (0,0)\oplus(0,0)\oplus(1,0)\oplus(0,1),
$$

where the two $(0,0)$ are the central directions $e_t$ and $ie_t$.

### The Weights

That the traceless part is $(1,0)\oplus(0,1)$ and not, say, $(\tfrac12,\tfrac12)$ is read from the Casimirs, and the numbers are these. On the eight-dimensional adjoint:

- the first Casimir takes the value $0$ on the two central directions and $\pm2$ on the traceless part, in the two summands with opposite signs of the second Casimir;
- the second Casimir takes the values $+2$ on the self-dual triple and $-2$ on the anti-self-dual one;
- and $2=j(j+1)$ at $j=1$, so each triple carries spin one under its own $\mathfrak{sl}(2,\mathbb{C})$.

The signs of the two Casimirs are a convention of the generators, and *The Two Casimirs of the Lorentz Algebra* fixes them once for all; the magnitudes $2$ and the splitting are not conventional.

### Why the Adjoint Is Not the Vector

A frequent error is to identify the adjoint with the four-vector $(\tfrac12,\tfrac12)$ because both have "four" or "six" in them. The adjoint is six-dimensional and scalar-free, and it is $(1,0)\oplus(0,1)$; the four-vector is four-dimensional and is $(\tfrac12,\tfrac12)$, and it is the module $\mathbb{B}_\Phi$ under the congruence. The two representations are different, and the numbers $1+1$ and $\tfrac12+\tfrac12$ are what tell them apart.

## Why the Real Form Decides Unitarity

### The Trap

The complexified algebra has two summands, each a copy of $\mathfrak{sl}(2,\mathbb{C})$, and $\mathfrak{sl}(2,\mathbb{C})$ has a compact real form, namely $\mathfrak{su}(2)$. A reader may conclude that the Lorentz algebra is a sum of two copies of $\mathfrak{su}(2)$, and therefore compact, and therefore that its finite-dimensional representations are unitary. The conclusion is false and the reasoning is the trap.

### Why It Is False

Two facts, each decisive.

- **The two triples are not the compact real form.** In the compact real form $\mathfrak{su}(2)$ the generators are anti-Hermitian and satisfy $[T_i,T_j]=\epsilon_{\imath\jmath\ell}T_\imath$ with all three directions equivalent. In the Lorentz algebra the three $J$ are anti-Hermitian and the three $K$ are Hermitian; the triple $\vec J_+$ contains $i\vec K$, which is anti-Hermitian only if $K$ is Hermitian *and* the $i$ is the coefficient field's, so the triple as a whole is in the complexification and has no Hermiticity property of its own. A complex basis element cannot be tested for Hermiticity without a real form to test against.
- **The compact real form is a different real slice.** The algebra $\mathfrak{so}(4)$ has generators with $[K_i,K_j]=+J_\imath$ and is a sum of two copies of $\mathfrak{su}(2)$; the algebra $\mathfrak{so}(1,3)$ has the minus sign and is not. The two are different real forms of the same complex algebra, and the sign of one block of the table is what separates them.

### What Unitarity Needs

A unitary representation needs an inner product preserved by the representation, and that needs a real form on which the star is positive definite. On a non-compact real form no such form exists for a nontrivial finite-dimensional representation: the boosts are Hermitian generators with real eigenvalues, and a Hermitian operator with a nonzero real eigenvalue cannot be unitary in a finite-dimensional space. This is the argument of *The Finite-Dimensional Representations and Their Unitarity Defect*, and the present article supplies its algebraic premise.

### The Rule for This Block

The two triples are a computational device and not a statement of compactness. They are used to label representations, to compute Casimirs and to split bivectors. They are never used to conclude that a representation is unitary, and any sentence of the form "the Lorentz group is $SU(2)\times SU(2)$" is wrong in this block and is corrected in *The Cartan Subalgebra, the Roots and the Three Real Forms*.

## Summary

The two triples $\vec J_\pm=\tfrac12(\vec J\pm i\vec K)$ each close with structure constants $\epsilon_{\imath\jmath\ell}$ and commute with each other, so the complexified Lorentz algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$. The $i$ in their definition is the coefficient field's, not the algebra's central scalar; with the central scalar the combination vanishes. The triples are the self-dual and anti-self-dual eigenspaces of the Hodge star, whose square is $-1$ in Lorentzian sign pattern. The adjoint representation is the two central directions plus $(1,0)\oplus(0,1)$, each triple carrying spin one. The triples are not the real $\mathfrak{su}(2)$ inside the Lorentz algebra but its complexification, and the real form decides unitarity: the compact real form is $\mathfrak{so}(4)$ and the Lorentz algebra is not it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\vec J_\pm=\tfrac12(\vec J\pm i\vec K)$ | the two complex triples |
| $J_{+k}$, $J_{-k}$ | their components |
| $M_{\imath\jmath}$ | the bivector generators, $M_{0i}=K_i$, $M_{ij}=\epsilon_{\imath\jmath\ell}J_\imath$ |
| $\star$ | the Hodge star on bivectors, $\star^{2}=-1$ |
| $\Pi_\pm=\tfrac12(1\mp i\star)$ | the self-dual and anti-self-dual projectors |
| $(m,n)$ | the pair of half-integers labelling a representation |
| $\mathfrak{so}(4)$, $\mathfrak{so}(2,2)$ | the compact and split real forms of the same complex algebra |

## Further Reading

- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — $\mathfrak{sl}(2,\mathbb{C})$ and $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, the direct sum and the pair of highest weights.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §5.6 — the two commuting triples $\vec A$ and $\vec B$, the $(A,B)$ labelling and the warning about compactness.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984 — the self-dual and anti-self-dual decomposition of bivectors and the $\star^{2}=-1$ convention.
- M. Carmeli, *Group Theory and General Relativity*, McGraw-Hill, 1977 — the complexification of the Lorentz algebra and its two ideals.
- *The Six Generators and Their Commutators* — the table rewritten here.
- *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane* — the same split on the field strength, in the corpus's own notation.
