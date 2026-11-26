# __The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$__

## Introduction

**At order two the corner recursion has one step: an idempotent of rank one cuts the algebra into four corner lines, and each corner is a copy of $M_1(\mathbb{C})=\mathbb{C}$, so the recursion that runs $M_n\to M_{n-1}\to\cdots$ stops at the first move.**

The article states the spectral flag at order two, the Peirce lines of a root with simple spectrum, the coarse split by a single idempotent with the dimensions $p^{2}$, $p(2-p)$, $(2-p)p$ and $(2-p)^{2}$, the corner isomorphisms, and the recursion, and it states what the decomposition is not. It assumes *The Peirce Decomposition in Two Dimensions*, *The Peirce Basis and the Corners at $n=2$* and *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*.

It defers the full general-order recursion to *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*, and the general frame to *The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$*.

## The Spectral Flag at Order Two

**A root of unity with simple spectrum at order two is an involution of trace zero, and it produces the flag of two lines.** Let $H^{2}=I$ have the distinct eigenvalues $\omega_{+}=1$ and $\omega_{-}=-1$, with the projectors $P_{\pm}=\tfrac12(I\pm H)$. Put $V_{\pm}=\operatorname{im}P_{\pm}$, a line each. The two lines are independent and sum to $\mathbb{C}^{2}$, and the partial sums give the flag

$$
0\subset F_{1}=V_{+}\subset F_{2}=\mathbb{C}^{2},\qquad \dim F_{k}=k .
$$

**Proposition.** The root of simple spectrum at order two is exactly an involution with trace zero, and every such involution gives a complete flag.

**Proof.** An involution has the eigenvalues $\pm1$; the spectrum is simple exactly when both eigenvalues occur; and the trace is the sum of the eigenvalues, so it is zero. Conversely an involution with trace zero has the eigenvalues $1$ and $-1$, and its eigenspaces are two independent lines.

**Corollary.** The flag at order two is the single choice of a line, so the space of flags is the projective line.

**Proof.** The flag is $0\subset V_{+}\subset\mathbb{C}^{2}$, and it is determined by $V_{+}$, which is a line; the lines form the projective line.

**Corollary.** The standard flag is the case $H=\operatorname{diag}(1,-1)$, and every other involution of trace zero gives a flag in general position.

**Proof.** At the diagonal involution the two lines are the coordinate axes, and a non-diagonal involution rotates them off the axes.

## The Peirce Lines

**The Peirce corner $A_{kl}$ is the space of maps from the $l$-th line to the $k$-th line.** Put

$$
A_{kl}=P_{k}M_2(\mathbb{C})P_{l},\qquad k,l\in\{+,-\}.
$$

**Proposition.** Each $A_{kl}$ is a complex line, the four lines are independent and sum to the algebra, and the dimensions are $1,1,1,1$.

**Proof.** Each corner is the image of a nonzero linear map between two one-dimensional spaces, so it is a line; the four lines are independent because their sum has the dimension $1+1+1+1=4$, which is the dimension of the algebra; and the sum is the whole algebra by the Peirce decomposition.

**Corollary.** The Peirce line $A_{kl}$ multiplies by the index rule, $A_{kl}A_{lm}\subseteq A_{km}$ and $A_{kl}A_{lm}=0$ when $l\ne l'$.

**Proof.** $P_{k}XP_{l}\cdot P_{l}YP_{m}=P_{k}XP_{l}YP_{m}$ because $P_{l}^{2}=P_{l}$, and the product is zero when the intermediate projectors are orthogonal.

**Corollary.** The four lines are the four corners of *The Peirce Basis and the Corners at $n=2$*, with $\upsilon_{+}$ a generator of $A_{+-}$ and $\upsilon_{-}$ a generator of $A_{-+}$.

**Proof.** The two constructions use the same projectors, and the generators are the elements of the mixed lines normalised so that their product is the idempotent.

## The Coarse Split

**A single idempotent of rank $p$ cuts the algebra into four blocks of dimensions $p^{2}$, $p(2-p)$, $(2-p)p$ and $(2-p)^{2}$.** Let $e$ be an idempotent of rank $p$.

**Proposition.** At order two the four dimensions are $p^{2}$, $p(2-p)$, $(2-p)p$ and $(2-p)^{2}$, which gives $1,1,1,1$ for $p=1$ and $4,0,0,0$ for $p=2$.

**Proof.** The corner $eMe$ consists of the matrices that are the composition of a map into the image of $e$, a map of the algebra and a map out of the kernel of $1-e$; its dimension is $p\cdot p$. The other three are the same count with one or both factors replaced by the rank of the complementary idempotent, which is $2-p$.

**Corollary.** The sum of the four dimensions is four in both cases, and the two extreme idempotents give a single nonempty block.

**Proof.** $p^{2}+2p(2-p)+(2-p)^{2}=(p+(2-p))^{2}=4$, and for $p=2$ the three other entries vanish.

**Corollary.** A rank-one idempotent gives the finest split of the algebra, since all four blocks are one-dimensional.

**Proof.** At $p=1$ the four entries are one each, so no block can be split further.

## The Corner Isomorphisms

**Theorem.** Each corner at order two is isomorphic to $M_1(\mathbb{C})=\mathbb{C}$, and the isomorphism sends the unit of the corner to the idempotent.

**Proof.** The corner $eMe$ is one-dimensional, so every element is a scalar multiple of $e$; the product is $(\lambda e)(\mu e)=\lambda\mu e$, which is the multiplication of scalars, and $e$ is the unit of the corner.

**Corollary.** The two diagonal corners are copies of the scalars, and the two mixed corners are one-dimensional bimodules over them.

**Proof.** The diagonal corners are the ends of the algebra and their products are scalar products; the mixed corners are modules over the diagonal corners on the two sides, and each is one line.

**Corollary.** The algebra is generated by the four corner lines together with the products that pair them.

**Proof.** The four lines span the algebra, and every product of two elements is a sum of products of corner elements, each of which is again a corner element or zero.

## The Recursion Stops

**The general corner recursion replaces a frame of order $n$ by a diagonal corner isomorphic to $M_{n-1}(\mathbb{C})$ and a mixed corner, and the process continues until the order is one.** At order two the first step already reaches order one.

**Proposition.** The corner $eMe$ of an idempotent of rank $n-1$ is isomorphic to $M_{n-1}(\mathbb{C})$; at order two with $p=1$ this is $M_1(\mathbb{C})=\mathbb{C}$.

**Proof.** Choose a basis whose first $n-1$ vectors span the image of $e$; in that basis $e$ is the diagonal idempotent with the first $n-1$ entries equal to one, and $eMe$ is the block of the first $n-1$ rows and columns.

**Corollary.** The recursion at order two has exactly one step, and the terminal algebra is the field itself.

**Proof.** The first step gives $M_1(\mathbb{C})$, which is the field, and the corner of the identity of the field is the field again, so nothing further happens.

**Corollary.** The recursion embeds $M_1(\mathbb{C})$ in $M_2(\mathbb{C})$ twice, once in each diagonal corner, and the two embeddings are conjugate.

**Proof.** The two diagonal corners are the corners of $e$ and of $1-e$, which are idempotents of the same rank, and a conjugating matrix carries one to the other.

## The Biquaternion Case

**Proposition.** In the biquaternion language the coarse split is the splitting of the algebra into the four corners $\mathbb{B}_{st}$, and the recursion at order two is the statement that each corner is a copy of the scalars.

**Proof.** The corners $\mathbb{B}_{st}$ are the four products of the idempotent pair $\tilde\Pi_{\mathrm{id},\pm}$ with the algebra on the two sides, which is the same construction as the four corners here, and each corner is one complex line over the field.

**Corollary.** The companion nilpotents $\vec\Pi_{\mathrm{nil},+-}$ and $\vec\Pi_{\mathrm{nil},-+}$ generate the two mixed corners, and their product is the idempotent of the diagonal corner.

**Proof.** The companion pair of the corpus is the pair of generators of the mixed corners normalised so that the product is $\tilde\Pi_{\mathrm{id},+}$, which is the normalisation used here.

## What the Decomposition Is Not

**Proposition.** The Peirce decomposition is not a direct-sum decomposition of the algebra into subalgebras, and the corners other than the diagonal ones are not closed under multiplication.

**Proof.** A mixed corner is square-zero, so it is not a subalgebra; and the product of two elements of different mixed corners lands in a diagonal corner, so the sum of the mixed corners is not closed either.

**Corollary.** The decomposition is a decomposition of the vector space with a multiplication rule across the pieces, not an isomorphism with a product of four algebras.

**Proof.** The four pieces span the space directly, and the multiplication rule is the index rule, which mixes the pieces.

**Corollary.** The only subalgebras among the four pieces are the two diagonal corners, and they are unital subalgebras with their own units.

**Proof.** The diagonal corners are closed under multiplication and contain $e$ and $1-e$, which are idempotents acting as units there.

## Summary

At order two a root of unity with simple spectrum is an involution of trace zero, and it gives the flag $0\subset V_{+}\subset\mathbb{C}^{2}$, a single line. The Peirce corners are the four lines $A_{kl}=P_{k}MP_{l}$, each of dimension one, and a single idempotent of rank $p$ gives the dimensions $p^{2}$, $p(2-p)$, $(2-p)p$ and $(2-p)^{2}$, which are $1,1,1,1$ at $p=1$.

Each corner is isomorphic to $M_1(\mathbb{C})=\mathbb{C}$, so the corner recursion has one step and stops at the field. The decomposition is a splitting of the vector space with a multiplication rule across the pieces, not a product of subalgebras, and in the biquaternion language it is the splitting into the four corners $\mathbb{B}_{st}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | the involution of simple spectrum |
| $P_{\pm}$ | its projectors, $\tfrac12(I\pm H)$ |
| $A_{kl}$ | the Peirce corner $P_{k}MP_{l}$ |
| $p$ | the rank of the idempotent of the coarse split |
| $\mathbb{B}_{st}$ | the corners of the biquaternion algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the corner decomposition of a finite-dimensional algebra and the corner isomorphisms.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the recursive use of the Peirce decomposition.
- [The Peirce Decomposition in Two Dimensions](the-peirce-decomposition-in-two-dimensions.html), for the four spaces and the index rule.
- [The Peirce Basis and the Corners at $n=2$](the-peirce-basis-and-the-corners-at-n-2.html), for the corners and the frame group.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the recursion at general order.
