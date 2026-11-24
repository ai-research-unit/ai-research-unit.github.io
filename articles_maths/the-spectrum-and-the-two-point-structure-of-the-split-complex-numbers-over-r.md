# __The Spectrum and the Two-Point Structure of $\mathbb{C}^{\mathrm{spl}}$ over $\mathbb{R}$__

## Introduction

The split-complex ring is the product of two copies of its base, and its spectrum is therefore a set of two points. This article reads the algebra through that set: the two characters, which are the two idempotent coordinates; the spectrum with its topology; the étale structure of rank two that makes the algebra a product and not a field; the exchange of the two points, which is the only automorphism; and the form the Galois correspondence takes when the base is not extended but split.

The algebra is $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}[j]$, $j^2=1$, with $\Pi_\pm=\tfrac12(1\pm j)$ and the idempotent coordinates $Q_\pm=q\pm q'$. The algebra and the idempotents are *Split-Complex Algebra* and *Square Roots of One and the Idempotents of the Split-Complex Algebra*; the involution is *The Involutions, the Subspaces and the Idempotent Lines of the Split-Complex Space*; the ideals are *Ideals and Peirce Decomposition of the Split-Complex Algebra*. The comparison throughout is with *Galois Theory of $\mathbb{C}/\mathbb{R}$*, of which this article is the split counterpart.

## The Characters

**Definition.** A **character** of $\mathbb{C}_{\mathrm{spl}}$ is a non-zero $\mathbb{R}$-algebra homomorphism into $\mathbb{R}$.

**Theorem (the two characters).** The characters are the two coordinate maps

$$
\digamma_{\mathrm{map},+} : Q=q+jq'\mapsto q+q' , \qquad \digamma_{\mathrm{map},-} : Q=q+jq'\mapsto q-q' ,
$$

with kernels $\ker\digamma_{\mathrm{map},\pm}=\mathbb{R}\Pi_\mp$.

**Proof.** A character fixes $\mathbb{R}$ and sends $j$ to an element $\xi$ with $\xi^2=1$, hence to $\xi=\pm1$. For $\xi=1$ the value on $Q$ is $q+q'$ and for $\xi=-1$ it is $q-q'$; each is additive, multiplicative and unital, since $(q+q')(c+c')$ and $(q-q')(c-c')$ are the two coordinates of the product. The kernel of $\digamma_{\mathrm{map},+}$ is the set $q'=-q$, that is $\mathbb{R}\Pi_-$, and the kernel of $\digamma_{\mathrm{map},-}$ is $\mathbb{R}\Pi_+$.

The characters are the two idempotent coordinates, so the algebra is recovered from its characters: the map $Q\mapsto(\digamma_{\mathrm{map},+}(Q),\digamma_{\mathrm{map},-}(Q))$ is the isomorphism $\mathbb{C}_{\mathrm{spl}}\cong\mathbb{R}\times\mathbb{R}$. Two characters, two coordinates, one isomorphism.

### The Values on the Idempotents

The characters read the idempotents as the two coordinate projectors,

$$
\digamma_{\mathrm{map},+}(\Pi_+)=1,\quad \digamma_{\mathrm{map},+}(\Pi_-)=0, \qquad \digamma_{\mathrm{map},-}(\Pi_+)=0,\quad \digamma_{\mathrm{map},-}(\Pi_-)=1 ,
$$

so each character is the evaluation of the Peirce coordinate it names and vanishes on the other idempotent. The two values on an element are its two Peirce coordinates, which is the reason the idempotent coordinates are also called the spectral coordinates (*Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*).

### Why There Are Exactly Two

The count is forced twice over. An $\mathbb{R}$-algebra map is determined by the image of $j$, and that image must satisfy $\xi^2=1$; over any field of characteristic other than two the equation has the two solutions $\pm1$, so there are two characters into any field extension of the base, and no more. The same computation over an ordered field gives the same answer, because $1$ has exactly the two square roots $\pm1$ there.

## The Spectrum

### The Spectrum as a Set

The prime ideals are the kernels of the characters, $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$, and there is no other: the two-sided ideals are $\{0\}$, the two lines and the ring (*Ideals and Peirce Decomposition of the Split-Complex Algebra*), the zero ideal is not prime because $\Pi_+\Pi_-=0$ with both factors non-zero, and the ring is excluded. So

$$
\operatorname{Spec}\mathbb{C}_{\mathrm{spl}}=\{\mathfrak p_+,\mathfrak p_-\}, \qquad \mathfrak p_+=\mathbb{R}\Pi_+,\quad \mathfrak p_-=\mathbb{R}\Pi_- ,
$$

a set of two points.

### The Zariski Topology

Both primes are maximal, so both points are closed, and a finite space in which every point is closed is discrete: every subset is closed, and also open. The spectrum is the discrete two-point space, and its topology carries no information beyond the count.

### The Residue Fields

Each quotient is the base, $\mathbb{C}_{\mathrm{spl}}/\mathfrak p_\pm\cong\mathbb{R}$, and the two isomorphisms are the characters. The residue field of each point is therefore $\mathbb{R}$ itself, of degree one over the base.

### The Algebra as the Functions on the Spectrum

A function on two points with real values is a pair of reals, and the pair is an element. The global sections of the structure sheaf are the algebra,

$$
\Gamma(\operatorname{Spec}\mathbb{C}_{\mathrm{spl}},\mathcal{O})=\mathbb{C}_{\mathrm{spl}} ,
$$

so the algebra is exactly the ring of all real-valued functions on its spectrum, and the two characters are the two evaluations.

## The Étale Structure

### Rank Two and Split

The base map $\mathbb{R}\to\mathbb{C}_{\mathrm{spl}}$ is finite and flat, the algebra being free of rank two on $\{1,j\}$, and it is unramified: the defining polynomial $X^2-1$ is separable over $\mathbb{R}$, its derivative $2X$ being invertible at both roots. A finite flat unramified map is étale, so the extension is finite étale of rank two. It is also split: the algebra is a product of two copies of the base, and the two copies are the two points.

### The Two-Point Cover

The geometric picture is a cover of one point by two points. Over the base the fibre of the spectrum is the two-point set, the cover is the trivial one, and the two sheets are the two idempotent lines. A cover of rank two over a one-point base is either trivial or connected, and the split algebra is the trivial case by construction.

### Against the Degree-Two Extension

Over $\mathbb{R}$ there are exactly two finite étale algebras of rank two up to isomorphism: the split one, $\mathbb{R}\times\mathbb{R}$, and the field $\mathbb{C}$. The two are the two classes of the rank-two cover. The field is connected, its spectrum is one point with residue field $\mathbb{C}$, and its two characters into $\mathbb{C}$ are the identity and the conjugation, exchanged by the Galois action. The split algebra is disconnected, its spectrum is two points with residue field $\mathbb{R}$, and its two characters are already defined over the base. The count of characters is two in both cases; what changes is whether the two points are one point with a degree-two residue field or two points with residue field the base.

## The Exchange and the Only Automorphism

### The Exchange Acts by Transposition

The conjugation $\bar\cdot$, $j\mapsto-j$, sends $\digamma_{\mathrm{map},+}$ to $\digamma_{\mathrm{map},-}$ and $\digamma_{\mathrm{map},-}$ to $\digamma_{\mathrm{map},+}$, since $\digamma_{\mathrm{map},\pm}(\bar Q)=\digamma_{\mathrm{map},\mp}(Q)$. On the spectrum it acts as the transposition of the two points, freely and transitively: one orbit of size two.

### Why It Is the Only One

The automorphisms of the algebra are the identity and the conjugation (*The Involutions, the Subspaces and the Idempotent Lines of the Split-Complex Space*), so the automorphism group is $\mathbb{Z}/2\mathbb{Z}$ and its action on the two points is the full symmetric group of the set. The group is the same as the Galois group of $\mathbb{C}/\mathbb{R}$ and its action is not: there the single point is fixed and the residue field is moved, here the two points are moved and each residue field is fixed.

## The Galois Correspondence Here

### The Two Intermediate Subalgebras

A subalgebra of $\mathbb{C}_{\mathrm{spl}}$ containing $\mathbb{R}$ is either $\mathbb{R}$ or the whole algebra: it contains $1$, and an element $q+jq'$ with $q'\neq0$ together with $1$ spans the plane. So the intermediate subalgebras are two, and they correspond to the two subgroups of $\mathbb{Z}/2\mathbb{Z}$: the whole group to the base, the trivial subgroup to the algebra. The reversal is exact.

### The Invariant Partitions

The correspondence has a second reading, and it is the one that shows what "split" means. A subalgebra of the functions on two points is the set of functions constant on each block of a partition of the two-point set. There are two partitions, one block and two blocks, and the exchange leaves both invariant. So the subalgebras correspond to the invariant partitions, hence to the subgroups, and the correspondence is a bijection of two-element sets.

### The Fixed Ring

The fixed ring of the exchange is the set of functions with equal values at the two points, that is the real line. The invariants of the action are the base, exactly as for $\mathbb{C}/\mathbb{R}$, where the invariants of the conjugation are the real field. The two extensions agree on the invariant and differ on everything else.

### The Opposite Conclusion

The fundamental theorem of Galois theory asks for a normal separable extension and reads the intermediate fields off the subgroups of the group. Here the group is the same $\mathbb{Z}/2\mathbb{Z}$, the rank is the same two, and the invariants are the same base, but the extension is not a field: the algebra splits, the two points are rational, and the correspondence is the trivial one between two two-element sets. This is the split counterpart of *Galois Theory of $\mathbb{C}/\mathbb{R}$*, and it reaches the opposite conclusion at the one place that matters: there the degree-two extension is a field and the Galois action is transitive on the two embeddings of its residue field, while here the extension is a product and the action is a transposition of two points of the base.

## Summary

The characters of $\mathbb{C}_{\mathrm{spl}}$ are the two idempotent coordinates $\digamma_{\mathrm{map},\pm}(Q)=q\pm q'$, with kernels the two idempotent lines, and an $\mathbb{R}$-algebra map is fixed by the image of $j$, which satisfies $\xi^2=1$, so there are exactly two. The spectrum is the discrete two-point space $\{\mathbb{R}\Pi_+,\mathbb{R}\Pi_-\}$, each point has residue field $\mathbb{R}$, and the algebra is the ring of all real-valued functions on the two points.

The base map is finite étale of rank two and split, so the algebra is a product of two copies of the base and not a field. Up to isomorphism there are two such algebras over $\mathbb{R}$, this one and the field $\mathbb{C}$: the field has one point with a degree-two residue field, the split algebra two points with residue field the base. The conjugation acts on the two points as the transposition, and it is the only automorphism.

The Galois correspondence holds with two intermediate subalgebras against two subgroups, and it also reads as the correspondence between subalgebras and invariant partitions of the two-point set. The invariants are the base in both the split and the field case; the difference is that the split extension is a product, so the action moves the points instead of the residue field, which is the opposite conclusion to the one drawn for $\mathbb{C}/\mathbb{R}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\digamma_{\mathrm{map},\pm}(Q)=q\pm q'$ | The two characters, the two idempotent coordinates |
| $\ker\digamma_{\mathrm{map},\pm}=\mathbb{R}\Pi_\mp$ | The kernel of each character, a minimal ideal |
| $\operatorname{Spec}\mathbb{C}_{\mathrm{spl}}=\{\mathfrak p_+,\mathfrak p_-\}$ | The spectrum, two points |
| $\mathbb{C}_{\mathrm{spl}}\cong\mathbb{R}\times\mathbb{R}$ | The algebra as the functions on the two points |
| $\bar\cdot$ | The exchange of the two points, the only automorphism |
| $V_2=\{\mathrm{id},\bar\cdot\}$ | The automorphism group, $\mathbb{Z}/2\mathbb{Z}$ |
| $\mathbb{R}_{\mathbb{C}_{\mathrm{spl}}}=\mathbb{C}_{\mathrm{spl}}^{\bar\cdot}$ | The fixed ring, the base |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, Graduate Texts in Mathematics 52, 1977), for the spectrum, the residue field at a point and the sections of the structure sheaf.
- Michel Raynaud, *Anneaux locaux henséliens* (Springer, Lecture Notes in Mathematics 169, 1970), for finite étale algebras of a field as products of separable extensions.
- Pierre Antoine Grillet, *Abstract Algebra* (Springer, 2nd ed. 2007), for the product of rings, its prime ideals and the Chinese remainder theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the correspondence between central idempotents and product decompositions.
- Nathan Jacobson, *Lectures in Abstract Algebra III* (Van Nostrand, 1964), for the Galois theory of a finite commutative algebra over a field.
