# __The Peirce Decomposition__

## Introduction

An idempotent cuts the algebra into four corners. This article states the cut, the multiplication rule between the corners, the coordinates it gives, and the real structure that the cut respects. It is the frame in which the element is read in *Spectral Algebra*.

The article assumes the classification of the idempotents of *Idempotents*: the trivial pair $0,e_t$, the non-trivial idempotents $\tfrac12(e_t+\tilde\Xi)$ over the roots of $+1$, the complete orthogonal pairs, primitivity and the Hermitian subfamily. It assumes the product and the conjugations, and nothing else.

The frame is one object read four ways: the decomposition of the algebra, the coordinates of an element, the matrix model of the four corners, and the real structure. The spinor spaces built on the frame are *The Spinor Spaces*; the modules built on it are *The Regular Module* and *The Minimal Left Ideals*. No form is used. The frame itself is built in §*Three Constructions of the Peirce Frame* from roots, from idempotents and from nilpotents.

## Idempotents and Orthogonal Idempotents

**The idempotents of $\mathbb{B}$ are $0$, $e_t$ and the nontrivial idempotents; every nontrivial idempotent is primitive, and each root of $+1$ carries a complete orthogonal pair.**

**Definition.** Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** when $e^2 = e$. Two idempotents $e, f$ are **orthogonal** when $ef = fe = 0$; a family is **pairwise orthogonal** when its members are pairwise orthogonal and **complete** when in addition their sum is $1$; a nonzero idempotent is **primitive** when it is not a sum of two nonzero orthogonal idempotents.

**The pair of a root of $+1$.** Over $\mathbb{C}$ every idempotent of this article comes from a root of $+1$. Let $\tilde\Xi$ be a root of $+1$, $\tilde\Xi^2=e_t$. Its **two idempotents** are

$$
\tilde\Pi_+=\tilde\Pi_+(\tilde\Xi)=\frac{e_t+\tilde\Xi}{2}, \qquad \tilde\Pi_-=\tilde\Pi_-(\tilde\Xi)=\frac{e_t-\tilde\Xi}{2},
$$

the subscript $+$ naming the member attached to $+1$ and the subscript $-$ the member attached to $-1$ (§*The Idempotent Convention* of *Conventions in Mathematics*). Each is idempotent by the same computation, $\tilde\Pi_+^2=\tfrac14(e_t+\tilde\Xi)^2=\tfrac14(e_t+2\tilde\Xi+e_t)=\tilde\Pi_+$ and $\tilde\Pi_-^2=\tfrac14(e_t-\tilde\Xi)^2=\tfrac14(e_t-2\tilde\Xi+e_t)=\tilde\Pi_-$; the two are orthogonal, $\tilde\Pi_+\tilde\Pi_-=\tfrac14(e_t-\tilde\Xi^2)=0=\tilde\Pi_-\tilde\Pi_+$; and they are **complete**, $\tilde\Pi_+ + \tilde\Pi_-=e_t$. The root is their difference, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, and the two members are the two values of multiplication by the root,

$$
\tilde\Xi\tilde\Pi_+=\tilde\Pi_+\tilde\Xi=\tilde\Pi_+, \qquad \tilde\Xi\tilde\Pi_-=\tilde\Pi_-\tilde\Xi=-\tilde\Pi_- .
$$

The construction inverts: a nontrivial idempotent $\tilde\Pi$ gives the root $2\tilde\Pi-e_t$, since $(2\tilde\Pi-e_t)^2=4\tilde\Pi^2-4\tilde\Pi+e_t=e_t$, and the root returns $\tilde\Pi$ as $\tilde\Pi_+(2\tilde\Pi-e_t)=\tilde\Pi$. So the complete orthogonal pairs of idempotents of $\mathbb{B}$ are exactly the pairs of the roots of $+1$, and a root and its opposite give the same pair. The computation and the classification of the roots are *Idempotents*, §*The Two Idempotents of a Root* and §*The Correspondence with the Roots of One*.

The **standard pair** is the pair of the root $i\vec e_z$, for which $(i\vec e_z)^2=i^2\vec e_z^2=e_t$:

$$
\tilde\Pi_+=\tilde\Pi_+(i\vec e_z)=\frac{e_t+i \vec e_z}{2}, \qquad \tilde\Pi_-=\tilde\Pi_-(i\vec e_z)=\frac{e_t-i \vec e_z}{2}.
$$

The two are orthogonal, sum to $e_t$, are Hermitian, $\tilde\Pi_+^{*}=\tilde\Pi_+$ and $\tilde\Pi_-^{*}=\tilde\Pi_-$, and are primitive; they generate the off-diagonal elements of the next section.

In the matrix model the primitive idempotents are exactly the nontrivial ones. An idempotent of $M_2(\mathbb{C})$ is conjugate to a diagonal matrix with entries in $\{0,1\}$, hence of rank $0$, $1$ or $2$: the two extremes are the trivial idempotents $0$ and $e_t$, and a rank-one idempotent is primitive, because a sum of two nonzero orthogonal idempotents would have image of dimension at least two. So the nontrivial idempotents of $\mathbb{B}$ and its primitive idempotents are the same set, and each nontrivial idempotent $\tilde\Pi$ comes with the complementary primitive idempotent $e_t - \tilde\Pi$.

| Idempotent | Form | Complement | Central | Primitive | Matrix model |
|---|---|---|---|---|---|
| $0$ | $0$ | $e_t$ | yes | no | $0$ |
| $e_t$ | $e_t$ | $0$ | yes | no | $\mathrm I_{2}$ |
| Hermitian family | $\tfrac12(e_t+i\vec u)$, $\vec u^2=-e_t$ | $\tfrac12(e_t-i\vec u)$ | no | yes | rank-one projector |
| Non-Hermitian family | $\tfrac12(e_t+\vec\xi+i\vec\xi')$, $\vec\xi\neq0$ and the two real conditions | $\tfrac12(e_t-\vec\xi-i\vec\xi')$ | no | yes | rank-one projector |

The classification of the idempotents of $\mathbb{B}$ — the trivial idempotents, the halving map on the roots of $+1$, the Hermitian idempotents and the dimension of the idempotent set — is the subject of *Idempotents*.

## The Peirce Decompositions

**A complete orthogonal pair of idempotents gives four one-dimensional corners, and every root of $+1$ gives one such pair; the diagonal corners are copies of $\mathbb{C}$ and the off-diagonal corners are nilpotent.**

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix. In $\mathbb{B}$ the family is the pair of a root of $+1$: the nontrivial idempotents are the rank-one projectors of $M_2(\mathbb{C})$ (§*Idempotents and Orthogonal Idempotents*), so a complete orthogonal family has at most two members and the two-member case is the only one that occurs. The decomposition is therefore attached to a root of $+1$, and the roots modulo the sign change count the decompositions (§*As Many Decompositions as Roots of One*).

### One Idempotent

Let $\tilde\Pi$ be an idempotent of $\mathbb{B}$ and write $\tilde\Pi'=e_t-\tilde\Pi$ for its complement. The sign $+$ names $\tilde\Pi$ and the sign $-$ names $\tilde\Pi'$. Every element expands as

$$
\tilde Q=\tilde\Pi\tilde Q\tilde\Pi+\tilde\Pi\tilde Q\tilde\Pi'+\tilde\Pi'\tilde Q\tilde\Pi+\tilde\Pi'\tilde Q\tilde\Pi',
$$

so the algebra splits into the four **Peirce spaces**

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--},
\qquad
\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau,
$$

with $\tilde\Pi_+=\tilde\Pi$ and $\tilde\Pi_-=\tilde\Pi'$. This is the **Peirce decomposition** of $\mathbb{B}$ with respect to $\tilde\Pi$. It refines the two-term decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}\tilde\Pi'$.

The corner $\tilde\Pi\mathbb{B}\tilde\Pi$ is a subalgebra with identity $\tilde\Pi$; the off-diagonal corners carry the left action of one diagonal corner and the right action of the other, and carry no identity. The expansion, the directness of the four terms and the product rule below are proved in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, where the case of a **central** idempotent is also separated: for a central $\tilde\Pi$ the off-diagonal corners vanish and the sum is a product of algebras. That special case does not arise here, since no nontrivial idempotent of $\mathbb{B}$ is central. A nontrivial idempotent $\tilde\Pi$ is the member attached to $+1$ of the pair of the root $\tilde\Xi=2\tilde\Pi-e_t$, so the decomposition written here is the one attached to that root (§*From One Idempotent to Its Complement*).

**Proposition (the Peirce multiplication).** For $\sigma,\tau,\mu,\nu\in\{+,-\}$,

$$
\mathbb{B}_{\sigma\tau}\mathbb{B}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}.
$$

**Proof.** An element of $\mathbb{B}_{\sigma\tau}$ is $\tilde\Pi_\sigma\tilde Q\tilde\Pi_\tau$ and an element of $\mathbb{B}_{\mu\nu}$ is $\tilde\Pi_\mu\tilde B\tilde\Pi_\nu$. The product is $\tilde\Pi_\sigma\tilde Q\tilde\Pi_\tau\tilde\Pi_\mu\tilde B\tilde\Pi_\nu$; the middle factor is $\tilde\Pi_\tau\tilde\Pi_\mu=\delta_{\tau\mu}\tilde\Pi_\tau$. The result is $\delta_{\tau\mu}\tilde\Pi_\sigma(\tilde Q\tilde\Pi_\tau\tilde B)\tilde\Pi_\nu\in\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}$.

### A Complete Orthogonal Family

For a finite complete orthogonal family $\tilde\Pi_1,\dots,\tilde\Pi_n$ the same expansion gives

$$
\mathbb{B}=\bigoplus_{i,j=1}^{n}\tilde\Pi_i\mathbb{B}\tilde\Pi_j,
\qquad
(\tilde\Pi_i\mathbb{B}\tilde\Pi_j)(\tilde\Pi_k\mathbb{B}\tilde\Pi_l)\subseteq\delta_{jk}\,\tilde\Pi_i\mathbb{B}\tilde\Pi_l.
$$

Each diagonal corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_i$ is an algebra with identity $\tilde\Pi_i$, and each off-diagonal piece carries the left action of one corner and the right action of the other. In $\mathbb{B}$ the nontrivial idempotents are primitive, so a complete orthogonal family has at most two nontrivial members, and the pair $\tilde\Pi_+,\tilde\Pi_-$ of a root of $+1$ is the case that occurs.

**The mixed spaces are square-zero subalgebras.** For the mixed space $\tilde\Pi\mathbb{B}\tilde\Pi'$ and $a,a'\in\mathbb{B}$ one has $(\tilde\Pi a\tilde\Pi')(\tilde\Pi a'\tilde\Pi')=\tilde\Pi a(\tilde\Pi'\tilde\Pi)a'\tilde\Pi'=0$, since $\tilde\Pi'\tilde\Pi=0$; so $\tilde\Pi\mathbb{B}\tilde\Pi'\cdot\tilde\Pi\mathbb{B}\tilde\Pi'=0$, and likewise $\tilde\Pi'\mathbb{B}\tilde\Pi\cdot\tilde\Pi'\mathbb{B}\tilde\Pi=0$. A mixed Peirce space is therefore closed under the product, but with the identically zero product: it is a subalgebra without a unit, and it carries no algebra structure that could enter a decomposition of $\mathbb{B}$ as a product. In the biquaternion case this is the nilpotence of the two mixed basis elements, $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$ (§*The Biquaternion Case*).

### The Biquaternion Case

**The four Peirce spaces are four one-dimensional lines, the two diagonal ones spanned by the idempotents and the two mixed ones by the nilpotents.**

Take the complete orthogonal family $\tilde\Pi_+,\tilde\Pi_-$ of §*Idempotents and Orthogonal Idempotents*, the pair of the root $\tilde\Xi$ of $+1$. The two off-diagonal corners are spanned by the elements

$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}.
$$

Then $\{\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$; the element $\vec\Upsilon_x$ spans the corner $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ and $\vec\Upsilon_y$ the corner $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$, and the multiplication is

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x=\vec\Upsilon_x\tilde\Pi_-,\qquad
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_+,\qquad
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
$$

together with $\vec\Upsilon_x\tilde\Pi_+=\tilde\Pi_-\vec\Upsilon_x=\tilde\Pi_+\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_-=0$ and $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$.

Write $\mathbb{B}_{st}$ for the corner $\tilde\Pi_s\mathbb{B}\tilde\Pi_t$, with $s,t\in\{+,-\}$. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--},\qquad
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,
$$

and by the multiplication table just given each corner is one-dimensional over $\mathbb{C}$:

$$
\boxed{\;
\mathbb{B}_{++}=\mathbb{C}\tilde\Pi_+,\qquad
\mathbb{B}_{+-}=\mathbb{C}\vec\Upsilon_x,\qquad
\mathbb{B}_{-+}=\mathbb{C}\vec\Upsilon_y,\qquad
\mathbb{B}_{--}=\mathbb{C}\tilde\Pi_-
\;},
$$

so the Peirce decomposition reads

$$
\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_x\oplus\mathbb{C}\vec\Upsilon_y\oplus\mathbb{C}\tilde\Pi_-.
$$

| Corner | Definition | Basis | Dimension over $\mathbb{C}$ | Matrix unit |
|---|---|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ | $\tilde\Pi_+$ | $1$ | $E_{11}$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ | $\vec\Upsilon_x$ | $1$ | $E_{12}$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ | $\vec\Upsilon_y$ | $1$ | $E_{21}$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_-$ | $\tilde\Pi_-$ | $1$ | $E_{22}$ |

**Normalised pairs.** For any complete pair, the two mixed corners are one-dimensional. Choose nonzero $u\in\mathbb{B}_{-+}$ and $v\in\mathbb{B}_{+-}$. Then $uv=c\tilde\Pi_-$ and $vu=c\tilde\Pi_+$ for the same nonzero scalar $c$. Choose $\alpha$ with $\alpha^2=c$ and set $\vec\Upsilon_+=u/\alpha$ and $\vec\Upsilon_-=v/\alpha$. Then
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0.
$$
The normalisation fixes the products, not the individual generators: it is invariant under the reciprocal rescaling $\vec\Upsilon_-\mapsto\mu\vec\Upsilon_-$, $\vec\Upsilon_+\mapsto\mu^{-1}\vec\Upsilon_+$ with $\mu\in\mathbb{C}^{\times}$. The standard pair above is the case $\mu=1$ of this construction. The general construction from a transverse vector is in *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*.

**The root on the corners.** The two signs of the pair are the two values of multiplication by the root, and each corner collects one sign on the left and one on the right:

$$
x\in\mathbb{B}_{st} \iff \tilde\Xi x = s\,x \ \text{ and } \ x\tilde\Xi = t\,x ,
$$

so $\mathbb{B}_{st}$ is the subspace on which left multiplication by $\tilde\Xi$ acts by $s$ and right multiplication by $\tilde\Xi$ acts by $t$. The root splits the algebra twice, once by each multiplication, and the diagonal corners $\mathbb{B}_{++}$ and $\mathbb{B}_{--}$ are the components on which the two signs agree.

**The corners multiply by their signs.** For $x\in\mathbb{B}_{st}$ and $y\in\mathbb{B}_{uv}$ one has $\tilde\Xi(xy)=(\tilde\Xi x)y=s\,xy$ and $(xy)\tilde\Xi=x(y\tilde\Xi)=v\,xy$, and the product vanishes unless the inner signs agree,

$$
\mathbb{B}_{st}\mathbb{B}_{uv} \subseteq \delta_{tu}\,\mathbb{B}_{sv}.
$$

This is the rule of §*A Complete Orthogonal Family* read on the signs: a product of two corners survives exactly when the two inner signs match, and it lies in the corner carrying the two outer signs. It makes the parity grading of §*The Decomposition as a Grading* the grading by the product of the two signs, the even part $\mathbb{B}_{++}\oplus\mathbb{B}_{--}$ against the odd part $\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}$.

### As Many Decompositions as Roots of One

**The Peirce decompositions of $\mathbb{B}$ relative to a complete orthogonal pair of idempotents are in bijection with the roots of $+1$ modulo the sign change $\tilde\Xi\sim-\tilde\Xi$: a root and its opposite give the same decomposition, and no two other roots give the same one.**

The map of §*Idempotents and Orthogonal Idempotents* sends a root $\tilde\Xi$ to the pair $\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi)$, hence to its decomposition. It is surjective, because a complete orthogonal pair $(\tilde\Pi,\tilde\Pi')$ gives the root $\tilde\Xi=\tilde\Pi-\tilde\Pi'$, whose square is

$$
\tilde\Xi^2 = \tilde\Pi^2-\tilde\Pi\tilde\Pi'-\tilde\Pi'\tilde\Pi+(\tilde\Pi')^2 = \tilde\Pi+\tilde\Pi' = e_t ,
$$

so the pair is the pair of a root and its decomposition is the one of that root. It is injective on the classes, because the root is read back from the pair, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, so a pair determines the root up to the interchange of its two members; and the interchange is exactly the replacement of the root by its opposite, $\tilde\Pi_+(-\tilde\Xi)=\tilde\Pi_-(\tilde\Xi)$ and $\tilde\Pi_-(-\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)$. So the classes $\{\tilde\Xi,-\tilde\Xi\}$, the unordered pairs of idempotents and the decompositions correspond one to one.

Read on the three families of the roots of $+1$ (§*Statement of the Theorem* of *Idempotents*), the count is:

- the trivial class $\{\pm e_t\}$ gives the pair $(e_t,0)$ and the **degenerate decomposition**, whose corners are $\mathbb{B}$ and $0$ rather than four lines;
- the purely imaginary class $\{\pm i\vec u\}$, over the real vectors $\vec u$ with $\vec u^2=-e_t$, is a two-real-parameter family; the change $\vec u\mapsto-\vec u$ leaves the class unchanged, so the classes form a real projective plane, and the two idempotents are Hermitian, the members of the second family of §*The Families of Idempotents* of the companion article, lying in $\mathbb{M}_+$;
- the nontrivial class, the roots $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions of §*The Non-Hermitian Roots* of the companion article, is a four-real-parameter family.

So the Peirce decompositions of $\mathbb{B}$ form a two-real-parameter family of Hermitian decompositions and a four-real-parameter family, together with the one degenerate decomposition. Each of them carries the reciprocal $\mathbb{C}^\times$ of normalised mixed bases of §*Systems of Matrix Units*, and all of them are conjugate by an inner automorphism, by the rigidity proved there.

### From One Idempotent to Its Complement

**The decomposition depends on the unordered pair of complementary idempotents, not on which member carries the sign $+$.**

Over $\mathbb{B}$ the decomposition relative to a pair of idempotents is forced by a single idempotent, equivalently by a single root. Let $\tilde\Pi \in \mathbb{B}$ be nontrivial and put $\tilde\Pi' = e_t - \tilde\Pi$; then

$$
\tilde\Xi = \tilde\Pi - \tilde\Pi' = 2\tilde\Pi - e_t
$$

is a root of $+1$, since $\tilde\Xi^2 = \tilde\Pi + \tilde\Pi' = e_t$, and $\tilde\Pi = \tilde\Pi_+(\tilde\Xi)$, $\tilde\Pi' = \tilde\Pi_-(\tilde\Xi)$: a nontrivial idempotent is a root in disguise, and the idempotent, the root $\tilde\Xi = 2\tilde\Pi-e_t$, the unordered pair $\{\tilde\Pi,\tilde\Pi'\}$ and the decomposition carry the same information. By §*Idempotents and Orthogonal Idempotents* both $\tilde\Pi$ and $\tilde\Pi'$ are primitive, they are orthogonal, and $\tilde\Pi + \tilde\Pi' = e_t$, so $\tilde\Pi$ alone determines the pair $(\tilde\Pi, \tilde\Pi')$ and the decomposition

$$
\mathbb{B} = \tilde\Pi\mathbb{B}\tilde\Pi \oplus \tilde\Pi\mathbb{B}\tilde\Pi' \oplus \tilde\Pi'\mathbb{B}\tilde\Pi \oplus \tilde\Pi'\mathbb{B}\tilde\Pi' .
$$

Every nontrivial idempotent is conjugate to $\tilde\Pi_+$ (§*Systems of Matrix Units*), so this is the decomposition of §*The Biquaternion Case* transported by a unit: each corner is the conjugate of the corresponding standard corner and is therefore a line over $\mathbb{C}$,

$$
\tilde\Pi\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi, \qquad \tilde\Pi'\mathbb{B}\tilde\Pi' = \mathbb{C}\tilde\Pi', \qquad \tilde\Pi\mathbb{B}\tilde\Pi' = \mathbb{C}u, \qquad \tilde\Pi'\mathbb{B}\tilde\Pi = \mathbb{C}w,
$$

where $u$ and $w$ are any nonzero elements of the two mixed corners. The shape does not move with $\tilde\Pi$; only the four lines do. The two mixed corners are square-zero, so their nonzero elements are nilpotent (§*A Complete Orthogonal Family*), and a normalised pair multiplies back onto the diagonal, $\tilde\Pi = uw$ with $u^2 = w^2 = 0$: every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents (§*Systems of Matrix Units*).

Read in the matrix model, the idempotent $\tilde\Pi$ corresponds to a rank-one projector. The standard pair maps to the two diagonal projectors

$$
\mathsf{M}_2(\tilde\Pi_+)=\begin{pmatrix}1&0\\0&0\end{pmatrix}, \qquad \mathsf{M}_2(\tilde\Pi_-)=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

and a general primitive idempotent is determined by two lines of $\mathbb{C}^2$: its **image** line $L$, on which it is the identity, and its **kernel** line $K$, which it annihilates, with $L \oplus K = \mathbb{C}^2$. The map $(L, K) \mapsto \mathsf{M}_2(\tilde\Pi)$ is a bijection from the ordered pairs of distinct lines of $\mathbb{P}^1(\mathbb{C})$ onto the primitive idempotent matrices, so these form the set $\mathbb{P}^1(\mathbb{C}) \times \mathbb{P}^1(\mathbb{C}) \setminus \Delta$, where $\Delta$ is the diagonal of equal pairs, of real dimension $4$; this is the four-dimensional idempotent manifold of *Idempotents*, §*The Correspondence with the Roots of One*, read in the coordinates of the matrix model.

### The Peirce Table

**The four Peirce spaces multiply by the matrix-unit rule, and the mixed products are the nilpotent products $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$.**

The four products of the basis elements are collected in the table whose entry in row $S$ and column $T$ is the space containing the products of an element of $S$ with an element of $T$:

| $\cdot$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{+-}$ | $\mathbb{B}_{-+}$ | $\mathbb{B}_{--}$ |
|---|---|---|---|---|
| $\mathbb{B}_{++}$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{+-}$ | $0$ | $0$ |
| $\mathbb{B}_{+-}$ | $0$ | $0$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{+-}$ |
| $\mathbb{B}_{-+}$ | $\mathbb{B}_{-+}$ | $\mathbb{B}_{--}$ | $0$ | $0$ |
| $\mathbb{B}_{--}$ | $0$ | $0$ | $\mathbb{B}_{-+}$ | $\mathbb{B}_{--}$ |

The table is the rule $\delta_{jk}$ of §*A Complete Orthogonal Family* read on the corners, and it is sparser than the rule suggests: the products $\vec\Upsilon_x^2$ and $\vec\Upsilon_y^2$ vanish, so the diagonal entries of the two mixed rows and columns are zero, and the surviving entries are the four corners themselves. Reading the table by rows gives the two right-handed groupings and by columns the two left-handed groupings, as in §*A Complete Orthogonal Family*.

### The Peirce Coordinates

**In the Peirce coordinates an element is a $2\times2$ complex matrix, and the multiplication is the matrix product.**

The decomposition is read in coordinates. Write $\tilde Q = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$, and let $a_{ij}$ be the coefficient of the one-dimensional corner $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ in the expansion of $\tilde Q$, the matrix position $1$ carrying the $+$ member of the pair and the position $2$ the $-$ member, so that $a_{11}$ is the coordinate on $\mathbb{B}_{++}$, $a_{12}$ on $\mathbb{B}_{+-}$, $a_{21}$ on $\mathbb{B}_{-+}$ and $a_{22}$ on $\mathbb{B}_{--}$; then

$$
a_{11} = Q_t - iQ_z, \qquad a_{12} = -iQ_x - Q_y, \qquad a_{21} = -iQ_x + Q_y, \qquad a_{22} = Q_t + iQ_z,
$$

so that

$$
\tilde Q = a_{11}\tilde\Pi_+ + a_{12}\vec\Upsilon_x + a_{21}\vec\Upsilon_y + a_{22}\tilde\Pi_- ,
$$

and conversely

$$
Q_t = \tfrac12(a_{11}+a_{22}), \qquad Q_x = \tfrac{i}{2}(a_{12}+a_{21}), \qquad Q_y = \tfrac12(a_{21}-a_{12}), \qquad Q_z = \tfrac{i}{2}(a_{11}-a_{22}).
$$

The four numbers $a_{ij}$ are the **Peirce coordinates** of $\tilde Q$. They are linear functions of $\tilde Q$; the mean of the two diagonal coordinates is the scalar part, and the determinant of their $2\times2$ array is the central square,

$$
\boxed{\;
a_{11}a_{22} - a_{12}a_{21} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = \tilde Q\tilde Q^{\natural}
\;}
$$

The coordinates are nothing but the four entries of the corpus's fixed matrix element representation: the isomorphism $\mathsf{M}_2 : \mathbb{B}\to M_2(\mathbb{C})$ of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*, is

$$
\mathsf{M}_2(\tilde Q) = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} Q_t - iQ_z & -iQ_x - Q_y \\ -iQ_x + Q_y & Q_t + iQ_z \end{pmatrix}.
$$

The Peirce decomposition therefore supplies the matrix element representation directly: the four spaces are the four matrix units, and the coordinate functions are the entries. §*The Peirce Coordinates and the Matrix Model* below develops that reading.

### The Decomposition as a Grading

**The Peirce decomposition is a $\mathbb{Z}_2$-grading whose even part is the diagonal subalgebra and whose odd part is the sum of the mixed spaces.**

The Peirce decomposition of a complete orthogonal family carries a second structure, the parity of the indices. Let $A_0$ be the sum of the diagonal corners and $A_1$ the sum of the mixed ones; the rule $(e_iAe_j)(e_kAe_l)\subseteq\delta_{jk}e_iAe_l$ says that a product of two Peirce spaces vanishes unless the two inner indices agree, and that when they agree the outer indices combine. Reading the label $i+j$ modulo two, so that $A_0$ carries the even class and $A_1$ the odd one, the rule becomes

$$
A_0A_0 \subseteq A_0, \qquad A_0A_1 \subseteq A_1, \qquad A_1A_0 \subseteq A_1, \qquad A_1A_1 \subseteq A_0 ,
$$

which is the multiplication law of the group $\mathbb{Z}_{2}$: the decomposition $A = A_0\oplus A_1$ is a **grading** of the algebra, $A_0$ is a subalgebra and $A_1$ is carried into itself by multiplication by $A_0$ on both sides. In the biquaternion case $A_0 = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\tilde\Pi_-$ and $A_1 = \mathbb{C}\vec\Upsilon_x \oplus \mathbb{C}\vec\Upsilon_y$, and the four inclusions are the laws $\vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-$ together with $\vec\Upsilon_x^2 = \vec\Upsilon_y^2 = 0$. The grading is the checkerboard of a $2\times2$ matrix: two cells of like colour multiply into the diagonal part and two of unlike colour into the mixed part. In the biquaternion case the parity is the product $st$ of the two signs of the corner, and the checkerboard is the table of the sign products (§*The Biquaternion Case*).

### The Involutions on the Peirce Spaces

**The natural conjugation and the bar exchange the two idempotents and the two diagonal corners; the natural conjugation preserves each mixed corner with the sign $-1$, the bar exchanges them with the sign $-1$, and the star fixes the diagonal corners and exchanges the mixed ones with the sign $+1$.**

| Involution | $\tilde\Pi_+$ | $\tilde\Pi_-$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{--}$ | $\mathbb{B}_{+-}$ | $\mathbb{B}_{-+}$ |
|---|---|---|---|---|---|---|
| natural ${}^{\natural}$ | $\tilde\Pi_-$ | $\tilde\Pi_+$ | $\mathbb{B}_{--}$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{+-}$ | $\mathbb{B}_{-+}$ |
| bar $\bar{\cdot}$ | $\tilde\Pi_-$ | $\tilde\Pi_+$ | $\mathbb{B}_{--}$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{-+}$ | $\mathbb{B}_{+-}$ |
| star ${}^{*}$ | $\tilde\Pi_+$ | $\tilde\Pi_-$ | $\mathbb{B}_{++}$ | $\mathbb{B}_{--}$ | $\mathbb{B}_{-+}$ | $\mathbb{B}_{+-}$ |

The bar is the coefficient conjugation, which is the map $\sigma$ of §*The Real Structure*, and the star is the composite ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (*Conventions in Mathematics*). All three preserve the set of the four Peirce spaces, and they act on it differently. The natural conjugation exchanges the two diagonal corners and preserves each mixed space, on which it acts as $-\mathrm{id}$. The bar exchanges the two diagonal corners and also exchanges the two mixed spaces, with the sign $-\mathrm{id}$ on each. The star fixes each of the two diagonal corners and exchanges the two mixed spaces, with the sign $+\mathrm{id}$ on each. The last statement is the general exchange theorem of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*, read on $\mathbb{B}$: the standard idempotents are Hermitian, $\tilde\Pi_+^{*} = \tilde\Pi_+$ and $\tilde\Pi_-^{*} = \tilde\Pi_-$, so the involution carries each corner to itself and the mixed space $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ onto $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$, exchanging $\vec\Upsilon_x$ and $\vec\Upsilon_y$ and giving the pairing of the two nilpotents recorded in *Conventions in Mathematics*, §*The Nilpotent Convention*. The bar and the natural conjugation are the two factors of the composite, and each of them fails to fix the standard idempotents; the star is the one that respects them.

The diagonal part $\tilde\Pi_+\mathbb{B}\tilde\Pi_+ \oplus \tilde\Pi_-\mathbb{B}\tilde\Pi_- = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\tilde\Pi_-$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C} \times \mathbb{C}$. Each diagonal corner is the field $\mathbb{C}$.

A **null (null-cone) variant** of the same split is used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. The idempotents there are the uniform nullquaternions $N = \tfrac12(1, \vec u)$ and $\bar N = \tfrac12(1, -\vec u)$, and the two Peirce components of a biquaternion are its **signed parts**, whose sign the source reads as the chirality of the Weyl spinor. The pair is orthogonal and complete in the article's own product — the **outer** product, for which $N \odot N = N$, $\bar N \odot \bar N = \bar N$, $N \odot \bar N = 0$ and $N + \bar N = e_t$ — and the article's matrix isomorphism carries the outer product to the ordinary matrix product and $N, \bar N$ to the two standard diagonal idempotents. It is the same orthogonal pair as above, transported to the null-cone coordinates with the product changed; these same elements are **not** idempotent under the Hamilton product of this article, so the chiral split is naturally stated in that paper's algebra rather than in this one.

## The Peirce Coordinates and the Matrix Model

**In the idempotent basis the Peirce decomposition is the matrix decomposition of the algebra; the corners are the matrix units, and the Peirce coordinates are the matrix entries.**

The Peirce coordinates of §*The Peirce Coordinates* do more than parametrise the elements: read as a matrix, they carry the whole multiplication.

**Proposition.** The map that sends $\tilde Q$ to the matrix $\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$ of its Peirce coordinates is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$, and it carries the four Peirce spaces onto the four matrix units,

$$
\tilde\Pi_+ \mapsto \begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11}, \qquad
\vec\Upsilon_x \mapsto \begin{pmatrix}0&1\\0&0\end{pmatrix}=E_{12},
$$
$$
\vec\Upsilon_y \mapsto \begin{pmatrix}0&0\\1&0\end{pmatrix}=E_{21}, \qquad
\tilde\Pi_- \mapsto \begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22}.
$$

**Proof.** The map is $\mathbb{C}$-linear and bijective, since the four basis elements of $\mathbb{B}$ go to the four basis matrices of $M_2(\mathbb{C})$; it is multiplicative because the four Peirce basis elements multiply as the four matrix units do — the Peirce table of §*The Peirce Table* is the table $E_{ij}E_{kl} = \delta_{jk}E_{il}$ of *Matrix Algebras*, §*Matrix Units* — and both multiplications are bilinear.

The isomorphism is the corpus's $\mathsf{M}_2$ of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*, written there as an assignment on the basis; what the Peirce decomposition adds is the reading of its four entries as the coordinates of the four corners. Its trace and its determinant are the two invariants of the Peirce decomposition, $\operatorname{tr} = a_{11}+a_{22} = 2Q_t$ and $\det = a_{11}a_{22}-a_{12}a_{21} = \tilde Q\tilde Q^{\natural}$, so that the scalar part and the central square are the two symmetric functions of the corner coordinates (§*The Peirce Coordinates*). In this model the four matrix units group into two columns and two rows; the column grouping and the row grouping are read in *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*, and they are the two groupings that *Matrix Algebras*, §*The Case $n = 2$* distinguishes.

### Systems of Matrix Units

**Definition.** A **system of $2\times2$ matrix units** in $\mathbb{B}$ is a family $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ of elements of $\mathbb{B}$ with

$$
E_{ij}E_{kl} = \delta_{jk}E_{il}, \qquad E_{11} + E_{22} = e_t, \qquad E_{11} \neq 0 .
$$

The definition is the abstract form of the multiplication of the coordinate matrices, and it is redundant on purpose: the relations already give $E_{11}^2 = E_{11}$, $E_{22}^2 = E_{22}$ and $E_{11}E_{22} = E_{22}E_{11} = 0$, so that $E_{11}$ and $E_{22}$ are orthogonal idempotents summing to the unit, and the two off-diagonal elements are nilpotent, $E_{12}^2 = E_{21}^2 = 0$.

**Proposition.** A system of matrix units is the same data as a Peirce decomposition with two primitive idempotents, together with a basis of each of the two mixed spaces normalised by $E_{12}E_{21} = E_{11}$. The standard system is the one of §*The Biquaternion Case*,

$$
E_{11} = \tilde\Pi_+, \qquad E_{12} = \vec\Upsilon_x, \qquad E_{21} = \vec\Upsilon_y, \qquad E_{22} = \tilde\Pi_- .
$$

**Construction from an arbitrary idempotent.** Fix a primitive $\tilde\Pi$ and put $\tilde\Pi' = e_t - \tilde\Pi$; choose nonzero $u \in \tilde\Pi\mathbb{B}\tilde\Pi'$ and $w \in \tilde\Pi'\mathbb{B}\tilde\Pi$. Under a conjugacy carrying the standard pair to $(\tilde\Pi, \tilde\Pi')$ (§*From One Idempotent to Its Complement*), the elements $u$ and $w$ are the images of $\alpha\vec\Upsilon_x$ and $\beta\vec\Upsilon_y$ for some $\alpha, \beta \in \mathbb{C}^\times$, and the standard products $\vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-$ give

$$
u w = \alpha\beta\,\tilde\Pi, \qquad w u = \alpha\beta\,\tilde\Pi' .
$$

With $\lambda = \alpha\beta \in \mathbb{C}^\times$ the same on both sides, the elements

$$
E_{11} = \tilde\Pi, \qquad E_{22} = \tilde\Pi', \qquad E_{12} = u, \qquad E_{21} = \lambda^{-1} w
$$

form a system of matrix units with $E_{11} = \tilde\Pi$. The pair $(u, w)$ is not determined by $\tilde\Pi$: replacing $u$ by $\mu u$ and $w$ by $\mu^{-1} w$ with $\mu \in \mathbb{C}^\times$ leaves $\lambda$ and every product of the system unchanged. A fixed primitive idempotent therefore determines its Peirce decomposition but carries a reciprocal $\mathbb{C}^\times$ of normalised mixed bases, the off-diagonal rescaling that appears as the diagonal torus in the proof of the theorem below. The three routes to the same frame are compared in §*Three Constructions of the Peirce Frame*.

**Proposition (a nontrivial idempotent is a product of two nilpotents).** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents, and the two mixed units of its Peirce decomposition supply the factorisation.

**Proof.** Let $\tilde\Pi$ be a nontrivial idempotent and $\tilde\Pi' = e_t - \tilde\Pi$ its complement, so that $\tilde\Pi$ and $\tilde\Pi'$ are primitive, orthogonal and sum to $e_t$. The two mixed corners $\tilde\Pi\mathbb{B}\tilde\Pi'$ and $\tilde\Pi'\mathbb{B}\tilde\Pi$ are square-zero (§*From One Idempotent to Its Complement*), so every nonzero $u \in \tilde\Pi\mathbb{B}\tilde\Pi'$ and every nonzero $w \in \tilde\Pi'\mathbb{B}\tilde\Pi$ is nilpotent, $u^2 = w^2 = 0$. By the construction above, $uw = \lambda \tilde\Pi$ for some $\lambda \in \mathbb{C}^\times$; replacing $w$ by $\lambda^{-1} w$ keeps it in $\tilde\Pi'\mathbb{B}\tilde\Pi$, nonzero and square-zero, and gives $uw = \tilde\Pi$. So $\tilde\Pi$ is the product of the two nilpotents $u$ and $\lambda^{-1} w$. The standard case is the multiplication table of §*The Biquaternion Case*, $\vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-$ with $\vec\Upsilon_x^2 = \vec\Upsilon_y^2 = 0$.

The trivial idempotent $e_t$ is the one idempotent that is not such a product: if $uv = e_t$ then $u$ has the right inverse $v$, so $u$ is a unit, whereas a nilpotent is not a unit. The other trivial idempotent, $0$, is a product of two nilpotents, $0 \cdot 0 = 0$. Among the idempotents of $\mathbb{B}$, therefore, all but $e_t$ are products of two nilpotents.

**Theorem (the Peirce decomposition is unique up to conjugation).** Every system of $2\times2$ matrix units of $\mathbb{B}$ is the image of the standard system under an inner automorphism: there is a unit element $\tilde U \in \mathbb{B}$ with $E_{ij} = \tilde U\,\tilde E_{ij}\,\tilde U^{-1}$ for the standard system $\{\tilde E_{ij}\}$. Consequently all Peirce decompositions of $\mathbb{B}$ with two primitive idempotents are conjugate, and a statement about one of them is a statement about all.

**Proof.** By the matrix model of §*The Peirce Coordinates and the Matrix Model* the question is the corresponding statement for $M_2(\mathbb{C})$, and there it is proved by change of basis. A primitive idempotent $P$ of $M_2(\mathbb{C})$ is the projector onto a line $\ell$ along another line $m$, $\ell$ being its image and $m$ its kernel; choosing a basis with first vector in $\ell$ and second in $m$, and letting $G$ be the matrix of that basis, gives $GPG^{-1} = E_{11}$. The stabiliser of $E_{11}$ is the diagonal torus, since a conjugation that fixes $E_{11}$ must preserve its image and its kernel; conjugating by the diagonal matrix $\operatorname{diag}(a,d)$ fixes $E_{11}$ and $E_{22}$ and multiplies $E_{12}$ by $a/d$ and $E_{21}$ by $d/a$. In a system of matrix units with $E_{11}$ and $E_{22}$ fixed, the two off-diagonal elements are determined by a single scalar, because they lie in the one-dimensional mixed spaces and satisfy $E_{12}E_{21} = E_{11}$; the diagonal conjugation is transitive on that scalar, so the system is carried to the standard one. The unit group of $\mathbb{B}$ acts by conjugation, and a conjugation carries a system of matrix units to a system of matrix units.

The theorem is the rigidity of the Peirce decompositions, and it should be read with two counts that it does not contradict. The **idempotents** that occur are not unique: every primitive idempotent of $\mathbb{B}$ appears, and these form the real four-dimensional idempotent manifold of *Idempotents*, §*The Correspondence with the Roots of One*, not the two points $\tilde\Pi_+, \tilde\Pi_-$. What is unique is the decomposition up to conjugation: the idempotent may be carried anywhere by a unit, and the unit conjugation carries the decomposition with it. Equivalently, $\mathbb{B}$ has one Peirce decomposition of this shape modulo the inner automorphisms — the statement that the algebra has a single block structure, namely the $2\times2$ block structure of a matrix algebra, and that all the decompositions of §*The Peirce Decompositions* are that structure seen in different bases.

The **stabiliser** of the standard pair in the unit group of $\mathbb{B}$ is the torus $\{\,a\tilde\Pi_+ + b\tilde\Pi_- : a, b \in \mathbb{C}^\times\,\}$. It fixes $\tilde\Pi_+$ and $\tilde\Pi_-$ and acts on the two mixed elements by

$$
\vec\Upsilon_x \mapsto \frac{a}{b}\,\vec\Upsilon_x, \qquad \vec\Upsilon_y \mapsto \frac{b}{a}\,\vec\Upsilon_y,
$$

which is exactly the reciprocal $\mathbb{C}^\times$ scaling of the construction of §*Systems of Matrix Units*. The Peirce decompositions are therefore the points of the idempotent manifold — uncountably many — each carrying its $\mathbb{C}^\times$ of normalised mixed bases, and the inner automorphisms act transitively on the whole family.

## Three Constructions of the Peirce Frame

**A Peirce frame can be built from a pair of anticommuting roots of $+1$, from a complete orthogonal pair of idempotents together with a normalised choice of the two mixed units, or from a pair of nilpotents with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$; the three are three encodings of one frame. The idempotent pair forgets the transverse root, and the forgotten coordinate is the reciprocal rescaling $\mu$ of §*Systems of Matrix Units*.**

The three subsections build the same four elements independently. The first two start from the diagonal data and must choose the mixed units; the third starts from the mixed units and reads the diagonal data off. The comparison at the end of the section states what each route fixes and where $\mu$ enters.

### From Roots of One

**One root of $+1$ is not enough: it fixes the diagonal pair only. A second root of $+1$, anticommuting with the first, fixes the two mixed units, and the two roots together are the frame.**

Let $\tilde\Xi$ be a root of $+1$, $\tilde\Xi^2=e_t$. Its pair is

$$
\tilde\Pi_+=\frac{e_t+\tilde\Xi}{2},\qquad
\tilde\Pi_-=\frac{e_t-\tilde\Xi}{2},
$$

and the root is their difference, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$. The root alone stops at the pair. It fixes the two diagonal corners and the two mixed corners as lines, and it singles out no element in either mixed line: any nonzero multiple of a mixed element spans the same corner.

Take a second root $\tilde\Xi'$ of $+1$ that anticommutes with the first,

$$
\tilde\Xi\tilde\Xi'=-\tilde\Xi'\tilde\Xi.
$$

Then $\tilde\Xi\tilde\Xi'$ is a root of $-1$,

$$
(\tilde\Xi\tilde\Xi')^2=\tilde\Xi\tilde\Xi'\tilde\Xi\tilde\Xi'=-\tilde\Xi^2(\tilde\Xi')^2=-e_t,
$$

and the two elements

$$
\vec\Upsilon_x=\frac{\tilde\Xi'+\tilde\Xi\tilde\Xi'}{2},\qquad
\vec\Upsilon_y=\frac{\tilde\Xi'-\tilde\Xi\tilde\Xi'}{2}
$$

are nilpotent. The two summands have squares $e_t$ and $-e_t$ and anticommute, so the cross terms of the square cancel and

$$
\vec\Upsilon_x^2=\vec\Upsilon_y^2=0.
$$

Direct multiplication, using the same two facts, gives

$$
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
$$

and the Peirce action

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x=\vec\Upsilon_x\tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_+,
$$

with the four remaining products zero. The four elements are a system of matrix units.

For the standard roots $\tilde\Xi=i\vec e_z$ and $\tilde\Xi'=i\vec e_x$, one has $\tilde\Xi\tilde\Xi'=-\vec e_y$, and the formulas return

$$
\tilde\Pi_\pm=\frac{e_t\pm i\vec e_z}{2},\qquad
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}.
$$

This is the frame of §*The Biquaternion Case*.

No information is lost in passing to the two roots: the transverse root is recovered from the frame as

$$
\tilde\Xi'=\vec\Upsilon_x+\vec\Upsilon_y,
$$

so the frame and the ordered pair $(\tilde\Xi,\tilde\Xi')$ of anticommuting roots of $+1$ are the same data. Another transverse root gives another frame over the same pair, and the two mixed units are rescaled reciprocally. That rescaling is the freedom $\mu$; when both roots are Hermitian, the frame is star-compatible and $\lvert\mu\rvert=1$.

**The count.** The first root is four real parameters: it is the idempotent $e=(e_t+\tilde\Xi)/2$, a projection onto a line along another line, and each line is a point of $\mathbb{P}^1(\mathbb{C})$, of two real parameters. The second root contributes two. Conjugation carries any pair to the standard one, and it preserves dimensions, so it is enough to count in the matrix model of the standard pair. There, with $\tilde\Xi=\operatorname{diag}(1,-1)$, a root anticommuting with it is off-diagonal,

$$
\tilde\Xi'=\begin{pmatrix}0&a\\ b&0\end{pmatrix},
\qquad
(\tilde\Xi')^2=ab\,I,
$$

so the root condition is $ab=1$, that is $b=a^{-1}$, and one complex number, two real parameters, remains. The total is

$$
4+2=6.
$$

The second root is the choice of $\mu=a$; the first root alone stops at four.

### From Two Idempotents

**A complete orthogonal pair fixes the four corner lines; a nonzero element in each mixed corner, normalised by their product, gives the two nilpotents and the frame.**

Let $\tilde\Pi_+,\tilde\Pi_-$ be a complete orthogonal pair. The mixed corners are lines. Choose nonzero

$$
v\in\mathbb{B}_{+-},\qquad u\in\mathbb{B}_{-+}.
$$

The two products lie on the diagonal,

$$
uv=c\tilde\Pi_-,\qquad vu=c'\tilde\Pi_+,
$$

and the scalars agree: $uvu=c u=c'u$ with $u\neq0$, so $c=c'$. Choose $\alpha$ with $\alpha^2=c$ and set

$$
\vec\Upsilon_x=\frac{v}{\alpha},\qquad
\vec\Upsilon_y=\frac{u}{\alpha}.
$$

Then

$$
\vec\Upsilon_x^2=\vec\Upsilon_y^2=0,\qquad
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
$$

and the four elements are a system of matrix units.

The pair fixes the corner lines, not the elements. The input is the pair together with a nonzero element in each mixed corner; the normalisation fixes their product and leaves the reciprocal rescaling

$$
\vec\Upsilon_x\mapsto\mu\vec\Upsilon_x,\qquad
\vec\Upsilon_y\mapsto\mu^{-1}\vec\Upsilon_y,\qquad
\mu\in\mathbb{C}^{\times},
$$

which changes neither the idempotents nor any product. The standard pair of §*The Biquaternion Case* is the representative $\mu=1$. The pair is the root $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$ in disguise, so this construction is the previous one with the transverse root left free.

**The count.** The pair is four real parameters, two distinct lines of $\mathbb{P}^1(\mathbb{C})$. The choice of mixed units adds two. A nonzero $v$ and a nonzero $u$ carry two real parameters each, four in all, and the simultaneous rescaling

$$
(v,u)\mapsto(\lambda v,\lambda u),\qquad \lambda\in\mathbb{C}^{\times},
$$

changes neither the idempotents nor the normalised frame, since $\alpha$ may be taken to rescale by the same $\lambda$. That removes two real parameters from the four, and what remains over the fixed pair is the class of $(v,u)$, a torsor under the reciprocal rescaling with coordinate $\mu$; it is one complex number. The total is

$$
4+2=6.
$$

### From Two Nilpotents

**Two nilpotents with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ give the two idempotents as their products, hence the frame, with no further choice.**

Let $\vec\Upsilon_x,\vec\Upsilon_y$ satisfy

$$
\vec\Upsilon_x^2=\vec\Upsilon_y^2=0,\qquad
\vec\Upsilon_x\vec\Upsilon_y+\vec\Upsilon_y\vec\Upsilon_x=e_t.
$$

Put

$$
\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y,\qquad
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x.
$$

Then

$$
\tilde\Pi_+^2=\vec\Upsilon_x(\vec\Upsilon_y\vec\Upsilon_x)\vec\Upsilon_y
=\vec\Upsilon_x(e_t-\vec\Upsilon_x\vec\Upsilon_y)\vec\Upsilon_y
=\tilde\Pi_+,
$$

and likewise $\tilde\Pi_-^2=\tilde\Pi_-$. The two are orthogonal and complete,

$$
\tilde\Pi_+\tilde\Pi_-=\vec\Upsilon_x\vec\Upsilon_y\vec\Upsilon_y\vec\Upsilon_x=0,
\qquad
\tilde\Pi_-\tilde\Pi_+=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$

and the Peirce action is the defining multiplication,

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x=\vec\Upsilon_x\tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_+,
$$

with the four remaining products zero. So $\{\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-\}$ is a system of matrix units.

Nothing is chosen here: the two nilpotents are the input, the idempotents are read off, and the frame is fixed. If the input satisfies the nilpotency but not the normalisation, with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=c e_t$ for some $c\neq0$, the products satisfy $(\vec\Upsilon_x\vec\Upsilon_y)^2=c\,\vec\Upsilon_x\vec\Upsilon_y$ and $(\vec\Upsilon_y\vec\Upsilon_x)^2=c\,\vec\Upsilon_y\vec\Upsilon_x$, so $\vec\Upsilon_x\vec\Upsilon_y/c$ and $\vec\Upsilon_y\vec\Upsilon_x/c$ are the idempotents, and the normalised pair is $\vec\Upsilon_x/\sqrt c,\vec\Upsilon_y/\sqrt c$. The canonical anticommutator is exactly the normalisation $c=1$.

**The count.** The first nilpotent is four real parameters. In the matrix model it is

$$
N=\begin{pmatrix}a&b\\ c&-a\end{pmatrix},
\qquad
N^2=(a^2+bc)\,I,
$$

three complex coordinates cut by the one complex equation $a^2+bc=0$, hence two complex, four real, parameters. The second nilpotent contributes two. Every nonzero nilpotent is conjugate to $E_{12}$, so fixing $\vec\Upsilon_x=E_{12}$ is general; the anticommutator is then linear and gives

$$
\vec\Upsilon_y=\begin{pmatrix}p&q\\ 1&-p\end{pmatrix},
\qquad
\vec\Upsilon_y^2=(q+p^2)\,I,
$$

so nilpotency forces $q=-p^2$, and one complex number remains. The total is

$$
4+2=6.
$$

The second nilpotent is the choice of the corner element, and the idempotents are its two products; they are the diagonal ones exactly at $p=0$.

### The Six Real Parameters of a Frame

**A frame has six real parameters. The algebra has eight, but a frame is not a general element: the idempotent pair contributes four and the normalised mixed unit contributes two.**

The count is a count of configurations, not of coordinates. The four elements of a frame have $4\times 8=32$ real coordinates between them, and the matrix-unit table is what cuts the set down. The reduction is not read equation by equation, because the relations are not independent. Two stratifications give the number directly, and the three routes of this section agree with both.

**Over the idempotents.** The map that forgets the two mixed units,

$$
\{\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-\}\longmapsto(\tilde\Pi_+,\tilde\Pi_-),
$$

is surjective, and its fibre is the set of normalised mixed units over a fixed pair, a torsor under $\mathbb{C}^\times$ with coordinate $\mu$. A primitive idempotent is an ordered pair of distinct lines, its image and its kernel, and the lines of $\mathbb{C}^2$ form the projective line $\mathbb{P}^1(\mathbb{C})$, of real dimension two. So the idempotent manifold has real dimension $2+2=4$, the fibre has real dimension two, and

$$
6=4+2.
$$

**Through the group.** Every frame is the conjugate of the standard one by a unit, and the unit group is $GL_2(\mathbb{C})$, of real dimension eight. The centre acts trivially on every frame, and the centre is $\mathbb{C}^\times$, of real dimension two. The frames are therefore the orbit of the standard frame under

$$
PGL_2(\mathbb{C})=GL_2(\mathbb{C})/\mathbb{C}^\times,
$$

of real dimension $8-2=6$.

**The three routes, counted.** The three constructions above reach the same six by the same pattern, four for the first datum and two for the second, and each subsection makes its own count.

| route | first datum | real dimension | second datum | real dimension |
|---|---|---|---|---|
| two roots | $\tilde\Xi$ | $4$ | transverse root $\tilde\Xi'=\mu E_{12}+\mu^{-1}E_{21}$ | $2$ |
| idempotents | $(\tilde\Pi_+,\tilde\Pi_-)$ | $4$ | normalised mixed unit, $\mu\in\mathbb{C}^\times$ | $2$ |
| two nilpotents | $\vec\Upsilon_x$ | $4$ | $\vec\Upsilon_y$ | $2$ |

**The split of the six.** In the idempotent and root routes the six split as four for the flag and two for the choice of matrix units inside it. The nilpotent route splits them differently, four for the first nilpotent and two for the second; the family of §*From Two Nilpotents* shows why, since with $\vec\Upsilon_x$ fixed the idempotents move with $p$. The totals agree because both count the same six-dimensional manifold of frames. The star reduces the frame part to a phase: a Hermitian idempotent has two real parameters, the Bloch sphere, and the star-compatible frame adds the phase of $\mu$, so the star-compatible frames have real dimension three.

The number six is the dimension of the frame, not of the algebra. The eight of $\mathbb{B}$ is the ambient space in which each of the four elements lives; the Peirce table is what makes the four-tuple a frame rather than four unrelated elements.

**The comparison.** The three routes meet at the standard frame

$$
\left\{
\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-
\right\}
=
\left\{
\frac{e_t+i\vec e_z}{2},
\frac{i\vec e_x-\vec e_y}{2},
\frac{i\vec e_x+\vec e_y}{2},
\frac{e_t-i\vec e_z}{2}
\right\}.
$$

The root and the idempotent pair carry the same diagonal data, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$ and $\tilde\Pi_\pm=(e_t\pm\tilde\Xi)/2$, and the root is recovered up to sign, which is the interchange of the two members. The root pair and the nilpotent pair carry the whole frame, and the idempotent pair is their common quotient. On the one hand, after choosing the mixed units as in §*From Two Idempotents*,

$$
(\tilde\Pi_+,\tilde\Pi_-)
\longmapsto
(\vec\Upsilon_x,\vec\Upsilon_y)
\longmapsto
(\vec\Upsilon_x\vec\Upsilon_y,\vec\Upsilon_y\vec\Upsilon_x)
=
(\tilde\Pi_+,\tilde\Pi_-),
$$

which is the identity. On the other,

$$
(\vec\Upsilon_x,\vec\Upsilon_y)
\longmapsto
(\tilde\Pi_+,\tilde\Pi_-)
\longmapsto
(\mu\vec\Upsilon_x,\mu^{-1}\vec\Upsilon_y),
$$

which is the identity exactly when the chosen mixed units are the ones with $\mu=1$. So the idempotents do not determine the frame; they determine it up to the reciprocal rescaling. The number $\mu$ is the coordinate on the stabiliser torus modulo the centre, the freedom of the matrix model that fixes the Peirce pair, and a gauge: it changes no idempotent, no product, no Peirce corner and no spectrum. The standard frame is the section $\mu=1$. The star-compatible frames, $\vec\Upsilon_x^{*}=\vec\Upsilon_y$, are the circle $\lvert\mu\rvert=1$, on which the standard frame is the point $\mu=1$.

## The Real Structure

**The real structure makes the algebra not central over $\mathbb{R}$ and permutes the four Peirce spaces in pairs.**

Everything so far was stated over $\mathbb{C}$. We now regard the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$ and record what changes.

**(a) The algebra is not central over $\mathbb{R}$.** The centre of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_t$ and $i e_t$ — the **complex subspace** $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree $2$. In the Wedderburn–Artin description $\mathbb{B} \cong M_n(D)$ over $\mathbb{R}$, one has $n = 2$ and $D = \mathbb{C}$.

**(b) The enrichment appears after extension of scalars.** The complexification of the real algebra $\mathbb{B}$ is

$$
\mathbb{B} \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong (\mathbb{C} \oplus \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong \mathbb{B} \oplus \mathbb{B},
$$

using $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$ and the associativity and commutativity of $\otimes_{\mathbb{R}}$. The algebra on the right is a product of two copies of $\mathbb{B}$; the splitting is invisible over $\mathbb{R}$, where $\mathbb{B}$ carries no such factor. In contrast, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{B}$ does not split: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(c) The real structure on the Peirce spaces.** Each of the four Peirce spaces of §*The Peirce Decompositions* is a complex line, hence a real plane of dimension $2$; the decomposition into four real planes is what the real view adds to the complex statement. The coefficient conjugation $\sigma$ acts on the four spaces as in §*The Involutions on the Peirce Spaces*: it exchanges the two diagonal corners, $\sigma(\mathbb{C}\tilde\Pi_+) = \mathbb{C}\tilde\Pi_-$, and it exchanges the two mixed corners, $\sigma(\mathbb{C}\vec\Upsilon_x) = \mathbb{C}\vec\Upsilon_y$. It therefore preserves the Peirce grading of §*The Decomposition as a Grading* as a pair of subspaces — it fixes $A_0$ and $A_1$ — while permuting the two summands inside each, and it fixes none of the four spaces individually. The star, the composite of $\sigma$ with the natural conjugation, is the conjugation that respects the standard idempotents: it fixes each diagonal corner and exchanges the two mixed ones, the exchange of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*. So the real structure does not single out a Peirce space; what it singles out is the pair of Hermitian idempotents $\tilde\Pi_+, \tilde\Pi_-$ whose corners it fixes, and it is by that pair that the real and the complex Peirce decompositions are matched.

## The Standard Nilpotents and the Peirce Units

The nilpotents are the nonzero rank-one trace-free complex matrices, that is the matrices conjugate to the strictly triangular matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. The two standard nilpotents are the off-diagonal Peirce units

$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad \vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2},
$$

with $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, which are exchanged by the star and which, together with the two primitive idempotents $\tilde\Pi_+,\tilde\Pi_-$, form a $\mathbb{C}$-basis of $\mathbb{B}$ with the multiplication table $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$ (*The Peirce Decomposition*). Every nilpotent is a complex multiple of a conjugate of one of these two, and the cone is the orbit of $\vec\Upsilon_x$ under the group of invertible elements.


## Summary

- A complete orthogonal pair $\{\tilde\Pi,\tilde\Pi'\}$ cuts $\mathbb{B}$ into four corners $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$, each a complex line, with the corner rule $\mathbb{B}_{\sigma\tau}\mathbb{B}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}$.
- The two diagonal corners are spanned by the idempotents; the two mixed corners are square-zero and are exchanged by the reversal.
- The Peirce coordinates of an element are its four corner components; in the standard frame they are the entries of the $2\times2$ matrix model.
- The coefficient conjugation exchanges the two diagonal corners and the two mixed corners; the star fixes the idempotents and exchanges the two mixed corners.
- The Peirce decomposition needs the product and the idempotents alone; the frame needs in addition a normalised choice of the two mixed units. No form is used.
- The frame has three constructions: a pair of anticommuting roots of $+1$, a complete orthogonal pair with a normalised choice of the two mixed units, and a pair of nilpotents with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$. The idempotent pair forgets the transverse root, and the forgotten datum is the reciprocal rescaling $\mu$; $\mu=1$ is the standard frame.
- A frame has six real parameters, against the eight of one element: four for the idempotent pair and two for the normalised mixed unit.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi,\tilde\Pi'=e_t-\tilde\Pi$ | a complete orthogonal pair |
| $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$ | the four Peirce corners |
| $\mathsf M_{\tilde\Pi}(\tilde Q)$ | the Peirce matrix of $\tilde Q$ |
| $\mu$ | the reciprocal rescaling $\vec\Upsilon_x\mapsto\mu\vec\Upsilon_x$, $\vec\Upsilon_y\mapsto\mu^{-1}\vec\Upsilon_y$ of the two mixed units |

## Further Reading

- [Idempotents](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification of the pair.
- [The Regular Module](the-regular-module.html), for the modules over the algebra and the submodules of the regular object.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the spinor spaces.
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-representation-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix form.
