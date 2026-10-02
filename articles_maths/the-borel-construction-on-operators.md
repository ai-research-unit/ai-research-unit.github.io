# __The Borel Construction on Operators__

## Introduction

The Borel construction replaces a space with an action of $G$ by the homotopy quotient $X_G = EG\times_G X$, on which the group acts freely and whose cohomology is the equivariant cohomology. It is a functor, so it acts on maps, and therefore on operators: a $G$-equivariant operator on $X$ — an endomorphism of the chains commuting with the action — is carried to an operator on the homotopy quotient, and the assignment is a ring homomorphism from the fixed part of the operator algebra of $X$ to the operator algebra of $X_G$. Two features make the construction an operator theory of its own. First, the action operators themselves are in the domain, and the image of the generator of the group is the **induced involution** $\tau$ on the homotopy quotient: for the group of order two it is the involution of $X_{\mathbb{Z}/2}$ that the involution of $X$ induces, it acts fibrewise over $B\mathbb{Z}/2$, and it is trivial in the coarse homotopy type exactly when the action is free. Second, the construction adds the operators of the base: the multiplication by the generator $x$ of $H^*(BG)$ acts on the equivariant cohomology and does not come from any operator on $X$, so the operator algebra of the homotopy quotient is the image of the fixed part of the operator algebra of $X$ together with the operators coming from the classifying space.

The article develops the Borel construction at the level of operators. It defines the homotopy quotient as a functor and records the functoriality and the homotopy invariance together with the free case, defines the Borel construction of an operator and shows that it is a ring homomorphism from the fixed part of the operator algebra to the operator algebra of the homotopy quotient and that it sends the action operators to the induced involution, identifies the structure of the induced involution and proves that its homotopy quotient is the Borel construction for the square of the group, and closes with the examples of the free action, the trivial action and the action of the group of order two. The homotopy quotient and the equivariant cohomology are those of *Equivariant Cohomology*; the transfer and its adjointness are those of *The Transfer and the Involution* and *Equivariant Operators and the Transfer*; the orbit space and its cohomology are those of *The Cohomology of an Orbit Space*; the fixed-point functors are those of *Equivariant Homotopy Theory*; and the operator algebra is that of *The Operators on an Algebra*. Nothing analytic and nothing geometric was used.

Throughout, $G$ is a finite group acting on a space $X$, $EG$ is a free contractible $G$-space, $BG = EG/G$ is the classifying space, and $X_G = EG\times_G X$ is the **homotopy quotient**, written $X_{\mathbb{Z}/2}$ when $G=\mathbb{Z}/2$. The **Borel fibration** is $X\to X_G\to BG$; its cohomology is the equivariant cohomology $H_G^*(X) = H^*(X_G)$. The action of an element $g$ on $X$ is the operator $\rho(g)$, the fixed part of the operator algebra is $\mathrm{End}_G(C_*(X)) = \{T : T\rho(g)=\rho(g)T\}$, and for $G=\mathbb{Z}/2$ the generator is $\sigma$ so that $\rho(\sigma)=\sigma$ and the induced involution on $X_{\mathbb{Z}/2}$ is written $\tau$. The coefficient ring is written $k$.

## The Borel Construction as a Functor

### The Homotopy Quotient

**Definition.** For a $G$-space $X$ the **homotopy quotient** is the balanced product

$$
X_G = EG\times_G X = \frac{EG\times X}{(e,x)\sim(eg,g^{-1}x)},
$$

and the **Borel construction** is the assignment $X\mapsto X_G$; the projection to the classifying space is $X_G\to BG$, a fibre bundle with fibre $X$.

**Proposition.** The homotopy quotient is well defined, it is a space over $BG$, and the Borel fibration $X\to X_G\to BG$ is a fibre bundle with fibre $X$ and structure group $G$; the construction preserves disjoint unions and quotients, and it is the total space of the homotopy-theoretic replacement of the action.

*Proof.* The balanced product is the quotient of $EG\times X$ by the diagonal free action of $G$, which is free because $EG$ is free; the projection to $BG$ is the induced map of the quotient and the fibres are the copies of $X$. $\square$

### Functoriality and Homotopy Invariance

**Theorem.** The Borel construction is a functor from the $G$-spaces to the spaces over $BG$: a $G$-map $f : X\to Y$ induces a map $f_G : X_G\to Y_G$ over $BG$, and the identities and the composites are preserved; a $G$-homotopy $H : X\times I\to Y$ induces a homotopy $H_G : X_G\times I\to Y_G$ because the interval has the trivial action, so $G$-homotopic maps induce homotopic maps. The construction carries a $G$-homotopy equivalence to a homotopy equivalence, and it is natural for the maps of groups.

*Proof.* The induced map is the descent of $f\times\mathrm{id} : EG\times X\to EG\times Y$, which is well defined because $f$ is equivariant; the composite of two equivariant maps descends to the composite of the induced maps, and the homotopy descends because $I$ has the trivial action and the homotopy is equivariant. $\square$

### The Free Case

**Theorem.** If the action of $G$ on $X$ is free, then the projection $EG\times X\to X$ is a $G$-homotopy equivalence, so the Borel construction is homotopy equivalent to the orbit space,

$$
X_G \simeq X/G ,
$$

and the equivariant cohomology is the cohomology of the quotient; in general the comparison map $X_G\to X/G$ exists and is induced by the projection $EG\to\mathrm{pt}$, and it is an equivalence exactly in the free case.

*Proof.* The projection $EG\times X\to X$ is a map of free $G$-spaces which is an ordinary homotopy equivalence, hence a $G$-homotopy equivalence because both actions are free and the underlying spaces are $G$-CW complexes; descending to the quotient gives the equivalence $X_G\simeq X/G$, and the comparison map is the descent of the projection. $\square$

## The Borel Construction on Operators

### The Functor on the Operator Level

**Definition.** The **Borel construction of an operator** $T \in \mathrm{End}_G(C_*(X))$, equivariant endomorphism of the chains, is the operator

$$
T_G = \mathrm{id}_{EG}\times_G T \ \in \mathrm{End}(C_*(X_G)) ,
$$

the endomorphism of the chains of the homotopy quotient induced by $T$ on the $X$-factor; equivalently, $T_G = (T\times\mathrm{id})_{G}$ on the balanced product.

**Theorem.** The assignment $T\mapsto T_G$ is a functor: it is additive, it preserves the identities and the compositions, and it is natural for the equivariant maps of spaces;

$$
(T\circ S)_G = T_G\circ S_G, \qquad (\mathrm{id})_G = \mathrm{id}, \qquad (f\,T\,f^{-1})_G = f_G\,T_G\,f_G^{-1} ,
$$

so it is a ring homomorphism $\mathrm{End}_G(C_*(X))\to\mathrm{End}(C_*(X_G))$; on cohomology it induces a ring homomorphism $\mathrm{End}_G(H^*(X;k))\to\mathrm{End}(H_G^*(X;k))$ from the fixed part of the operator algebra of $X$ to the operator algebra of the homotopy quotient.

*Proof.* The operator $T\times\mathrm{id}$ on $EG\times X$ is $G$-equivariant because $T$ is, so it descends to the balanced product; composition is preserved because the balanced product of the composites is the composite of the balanced products, and the naturality is the naturality of the balanced product. $\square$

### The Operators of the Group

**Theorem.** The image under the Borel construction contains the operators coming from the group: the norm $N=\sum_{g}\rho(g)$ maps to $N_G = \sum_g (\rho(g))_G$, the transfer of a subgroup maps to its transfer in the homotopy quotient, and the multiplications by the invariant classes map to the multiplications by their pullbacks. The image of the action operator $\rho(g)$ is the operator $(\rho(g))_G$ on $X_G$ induced by $g$ acting on the $X$-factor; for a free action the coarse homotopy quotient is $X/G$, on which $\rho(g)$ acts trivially because $g$ is in the deck group, so the image of the group action in the operator algebra of the quotient is trivial exactly on the free part.

*Proof.* Each statement is the functoriality of the previous theorem; the triviality of the action of a deck transformation on the orbit space is the definition of the quotient action, and the transfer is the sum of the action operators over the cosets, whose image is the sum of the images. $\square$

### The Operators of the Base

**Theorem.** The operator algebra of the homotopy quotient contains operators that do not come from the Borel construction of any operator on $X$: the multiplications by the classes of the base, in particular the multiplication by the generator $x \in H^1(BG;k)$, act on $H_G^*(X;k)$ and enlarge the algebra. Hence the image of the fixed part of the operator algebra of $X$ is a proper subalgebra of the operator algebra of the homotopy quotient in general, and the equivariant operators are the image of the fixed part together with the base multiplications:

$$
\mathrm{End}_G(H^*(X;k)) \ \text{maps into}\ \mathrm{End}(H_G^*(X;k)), \qquad x\smile(-) \ \text{acts on}\ H_G^*(X;k) ,
$$

with the base acting through the projection $X_G\to BG$ and the module structure of *Equivariant Cohomology*.

*Proof.* The multiplication by a base class is the pullback along the projection to $BG$, which is not the image under $T\mapsto T_G$ of an operator on $X$ because it raises the filtration by the base degree; the module structure is that of *Equivariant Cohomology*, and the inclusion of the image is proper because the base cohomology is infinite-dimensional for $G$ of order two. $\square$

## The Induced Involution

### The Involution on the Homotopy Quotient

**Theorem.** Let $G=\mathbb{Z}/2$ with generator $\sigma$. The Borel construction of the action operator $\rho(\sigma)=\sigma$ is the **induced involution**

$$
\tau = (\sigma)_G : X_{\mathbb{Z}/2}\longrightarrow X_{\mathbb{Z}/2} , \qquad \tau[e,x] = [e,\sigma x] = [\sigma e,x] ,
$$

a well-defined involution of $X_{\mathbb{Z}/2}$ covering the identity of $B\mathbb{Z}/2$, so that it acts fibrewise on the fibres of the Borel fibration; it is natural in the space with involution, and it is the image of the generator of the group under the ring homomorphism of the previous section. On a fibre the involution acts by $\sigma$, and the whole structure $(X_{\mathbb{Z}/2},\tau)$ is the Borel construction of the pair $(X,\sigma)$.

*Proof.* The map $\sigma\times\mathrm{id}$ on $EG\times X$ is $\mathbb{Z}/2$-equivariant because the group is abelian, so it descends to the balanced product; the two expressions for $\tau[e,x]$ agree by the balanced relation with the group element $\sigma$, and $\tau^2=\mathrm{id}$ because $\sigma^2=\mathrm{id}$. $\square$

### The Free Action and the Triviality of the Involution

**Theorem.** For the free action the equivalence $X_{\mathbb{Z}/2}\simeq X/\sigma$ of the free case carries the induced involution $\tau$ to the map of $X/\sigma$ induced by $\sigma$, which is the identity because $\sigma$ acts trivially on the orbit space; so the induced involution is trivial, up to homotopy, exactly on the free part, and away from it $\tau$ acts with fixed points, whose locus is the homotopy fixed set of the action. On the coarse quotient the induced involution is therefore an obstruction to the freeness of the action: it is homotopic to the identity exactly when the action is free.

*Proof.* The equivalence descends the projection $EG\times X\to X$; on $X$ the automorphism $\sigma$ acts trivially modulo the equivalence relation $x\sim\sigma x$, which defines the orbit space, so the descent of $\tau$ is the identity; conversely, if $\tau$ were homotopic to the identity then the action of $\sigma$ on the fibres would be null in the homotopy of the quotient, which forces the fibres to be orbits, that is the free case. $\square$

### The Homotopy Quotient of the Induced Involution

**Theorem.** The homotopy quotient of the induced involution is the Borel construction for the group $\mathbb{Z}/2\times\mathbb{Z}/2$:

$$
(X_{\mathbb{Z}/2})_{\mathbb{Z}/2} \;=\; E\mathbb{Z}/2\times_{\mathbb{Z}/2}\bigl(E\mathbb{Z}/2\times_{\mathbb{Z}/2}X\bigr) \;\cong\; E(\mathbb{Z}/2\times\mathbb{Z}/2)\times_{(\mathbb{Z}/2)^2}X \;=\; X_{(\mathbb{Z}/2)^2},
$$

with the first factor of the square acting trivially on $X$ and the second acting by $\sigma$; the iterated construction therefore computes the equivariant cohomology of a group of order four from the involution, and the operators of the two factors are the two commuting involutions on the homotopy quotient. The fixed points of $\tau$ and its homotopy fixed set in the sense of the homotopy limit are the invariants of this square action, and their calculation belongs to the equivariant cohomology of *Equivariant Cohomology*.

*Proof.* The balanced products associate: $(E\times_{\mathbb{Z}/2}(E'\times_{\mathbb{Z}/2}X))\cong(E\times E')\times_{(\mathbb{Z}/2)^2}X$, and $E\times E'$ is a free contractible $(\mathbb{Z}/2)^2$-space; the action of the second factor on $X$ is the given involution and the first acts trivially, which is the stated group action. $\square$

## The Simplicial Model and the Module Structure

### The Simplicial Borel Construction

**Theorem.** If $X$ is a simplicial $G$-space whose geometric realisation is the space of the article, the homotopy quotient is the diagonal of the bisimplicial space $(p,q)\mapsto EG_p\times X_q$, and its chains are the balanced tensor product

$$
C_*(X_G) \simeq C_*(EG)\otimes_{k[G]}C_*(X)
$$

up to the natural quasi-isomorphism; the Borel construction of an operator $T$ is the induced map $\mathrm{id}\otimes_{k[G]}T$, so the operator theory is the algebra of the balanced tensor product and the computations are the computations of the bar construction.

*Proof.* The realisation of the diagonal of the bisimplicial space is the balanced product of the realisations, which is the homotopy quotient; the chains of the balanced product are the balanced tensor product of the chains by the Eilenberg–Zilber theorem, and the induced map of an equivariant operator is the balanced tensor with $T$. $\square$

### The $E^2$ Page

**Theorem.** The Serre spectral sequence of the Borel fibration has the $E^2$ page

$$
E_2^{p,q} = H^p\bigl(G;H^q(X;k)\bigr) ,
$$

the group cohomology with coefficients in the cohomology of the fibre, and it converges to $H_G^*(X;k)$; for the trivial action and the field of coefficients it reduces to the tensor product $H^p(BG;k)\otimes H^q(X;k)$ under the Künneth hypothesis, and the Borel construction of an operator acts on the pages as the induced map on the coefficient modules. The spectral sequence is that of *The Leray–Serre Spectral Sequence*, with the local system of the fibre cohomology along the base.

*Proof.* The Serre spectral sequence of the fibration $X\to X_G\to BG$ has $E_2^{p,q}=H^p(BG;\mathcal H^q(X;k))$ with the local system $\mathcal H^q(X;k)$; the local system is the module $H^q(X;k)$ with the action of the fundamental group $G$, and its cohomology is the group cohomology, which is the stated page. $\square$

### The Module Structure

**Theorem.** The equivariant cohomology $H_G^*(X;k)$ is a module over $H^*(BG;k)$ through the projection of the Borel fibration, and the Borel construction of an operator is linear over this ring:

$$
(T_G)^*(x\smile\alpha) = x\smile(T_G)^*\alpha , \qquad x\in H^*(BG;k),\ \alpha\in H_G^*(X;k);
$$

hence the image of the fixed part of the operator algebra of $X$ lies in the endomorphisms of $H_G^*(X;k)$ that are linear over $H^*(BG;k)$, an algebra that contains the base multiplications and acts on the equivariant cohomology.

*Proof.* The module structure is the pullback along $X_G\to BG$ and the cup product; the linearity of $T_G$ follows because $T_G$ commutes with the projection to $BG$ as a map over the base, so it pulls the base classes back to themselves. $\square$

**Corollary.** For the trivial action the homotopy quotient is $X\times BG$ up to homotopy and the induced involution acts on the base factor while the Borel construction of an operator of $X$ acts on the other factor; the two families of operators commute, and the equivariant cohomology is the tensor product of the two cohomologies under the Künneth hypothesis.

*Proof.* The trivial action splits the balanced product as $X\times BG$; the induced involution is the identity on the first factor and the free involution on the second, and an operator of $X$ is the identity on the second. $\square$

## The Comparison and the Localisation

**Theorem.** The comparison map $X_G\to X/G$ induces a map $H^*(X/G;k)\to H_G^*(X;k)$ which is an isomorphism for a free action when two is invertible in $k$, and whose kernel and cokernel are computed by the fixed set through the localisation of *Equivariant Cohomology*; the Borel construction is the free replacement of the action, and the failure of the comparison to be an equivalence is exactly the fixed-point contribution of the equivariant cohomology.

*Proof.* The comparison map is the descent of the projection $EG\to\mathrm{pt}$, and for a free action the projection is a $G$-homotopy equivalence by the free case of the article; in general the discrepancy is the fixed set by the localisation theorem of *Equivariant Cohomology*, whose operator form is the ring homomorphism of the previous section. $\square$

## Examples

**Example (the free action).** For the antipodal involution of $S^n$ the homotopy quotient is $\mathbb{RP}^n$ up to homotopy, the induced involution $\tau$ is homotopic to the identity on $\mathbb{RP}^n$, and the Borel construction on the operator algebra sends the action operator $\sigma$ to an operator homotopic to the identity; the operators of the base, the multiplications by the generator of $H^*(\mathbb{RP}^{\infty};\mathbb{F}_2)$, act on the equivariant cohomology and their action is the one computed in *The Mod 2 Cohomology of an Involution*.

**Example (the trivial action).** For the trivial action $X_{\mathbb{Z}/2}\cong X\times B\mathbb{Z}/2$, the induced involution is $\mathrm{id}\times(\text{the antipodal map of }B\mathbb{Z}/2)$, which acts on the base factor, and the iterated homotopy quotient is $X_{(\mathbb{Z}/2)^2}$; the example shows that the induced involution is not the identity in general, its action being the free involution of the classifying space, and that the Borel construction of an operator is additive over the tensor product with the base.

**Example (the fixed point).** For $X=\mathrm{pt}$ with the trivial action the homotopy quotient is $B\mathbb{Z}/2=\mathbb{RP}^{\infty}$, the action operator $\sigma$ is the identity on the point, and the induced involution is the antipodal self-map of $B\mathbb{Z}/2$, homotopic to the identity; the example is the universal case, in which the induced involution carries no information and the operator algebra of the homotopy quotient is the full cohomology algebra of the classifying space.

## Summary

The Borel construction $X\mapsto X_G = EG\times_G X$ is a functor from the $G$-spaces to the spaces over $BG$, natural for equivariant maps and sending $G$-homotopic maps to homotopic maps, and it reduces to the orbit space in the free case. On the operator level it sends an equivariant endomorphism $T$ of the chains of $X$ to the operator $T_G = \mathrm{id}_{EG}\times_G T$ on the homotopy quotient, and the assignment is a ring homomorphism from the fixed part of the operator algebra $\mathrm{End}_G(C_*(X))$ to $\mathrm{End}(C_*(X_G))$, hence from $\mathrm{End}_G(H^*(X;k))$ to the operator algebra of the equivariant cohomology. The image contains the norms, the transfers and the multiplications by the invariant classes, and the image of the generator of the group of order two is the induced involution $\tau$ on $X_{\mathbb{Z}/2}$, which acts fibrewise over $B\mathbb{Z}/2$, is homotopic to the identity exactly on the free part, and whose homotopy quotient is the Borel construction $X_{(\mathbb{Z}/2)^2}$ of the square of the group; the operator algebra of the homotopy quotient additionally contains the multiplications by the classes of the base, which do not come from operators on $X$, so the image of the fixed part of the operator algebra of $X$ is a proper subalgebra in general. The homotopy quotient and the equivariant cohomology are those of *Equivariant Cohomology*, the transfer is that of *Equivariant Operators and the Transfer*, the orbit space is that of *The Cohomology of an Orbit Space*, and the fixed-point functors are those of *Equivariant Homotopy Theory*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $EG$, $BG = EG/G$ | Finite group, free contractible $G$-space, classifying space |
| $X_G = EG\times_G X$ | Homotopy quotient (Borel construction) |
| $X\to X_G\to BG$ | Borel fibration with fibre $X$ |
| $H_G^*(X;k)=H^*(X_G;k)$ | Equivariant cohomology |
| $X_G\simeq X/G$ | The free case |
| $\rho(g)$, $\mathrm{End}_G(C_*(X))$ | Action operator, fixed part of the operator algebra |
| $T_G = \mathrm{id}_{EG}\times_G T$ | Borel construction of the operator $T$ |
| $(T S)_G = T_G S_G$ | The Borel construction is a ring homomorphism on the operators |
| $\tau=(\sigma)_G$ | Induced involution on $X_{\mathbb{Z}/2}$; $\tau[e,x]=[e,\sigma x]=[\sigma e,x]$ |
| $\tau\simeq\mathrm{id}$ on the free part | Triviality of the induced involution exactly for the free action |
| $(X_{\mathbb{Z}/2})_{\mathbb{Z}/2}\cong X_{(\mathbb{Z}/2)^2}$ | Iterated construction; the homotopy quotient of the induced involution |
| $x\smile(-)$ on $H_G^*(X;k)$ | Base multiplication; an operator that is not the image of an operator on $X$ |

## Further Reading

- Armand Borel, *Seminar on Transformation Groups* (Annals of Mathematics Studies 46, 1960), for the homotopy quotient, the classifying space and the equivariant cohomology.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Borel construction and the operators on the equivariant cohomology.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the homotopy quotient, the induced maps and the iterated constructions.
- J. Peter May, *A Concise Course in Algebraic Topology* (University of Chicago Press, 1999), for the balanced products, the universal bundles and the classifying spaces.
- Paul G. Goerss and John F. Jardine, *Simplicial Homotopy Theory* (Birkhäuser, 1999), for the homotopy-theoretic Borel construction and its functoriality.
- Alejandro Adem and R. James Milgram, *Cohomology of Finite Groups* (Springer, 2nd ed. 2004), for the Borel construction, the classifying spaces and the operators on the equivariant cohomology.
