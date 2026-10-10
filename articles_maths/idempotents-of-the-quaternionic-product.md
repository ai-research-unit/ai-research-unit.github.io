
# __Idempotents of the Quaternionic Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*). This group of articles is the reading of the second of them as a multiplication,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\mu P_\mu Q_\nu\, e_\mu e_\nu , \qquad \varepsilon = (1,-1,-1,-1) ,
$$

the **general quaternionic bilinear product**, in which ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$. The coordinate rule and the scalar–vector form are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Bilinear Product*; the algebra the product defines, its failure of associativity and its left unit are *Introduction to the General Quaternionic Algebra of Biquaternions*; its place among the four general products is the property table of *Comparison Between the Four General Products*.

An **idempotent** of a multiplication is an element with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$. The two **trivial** idempotents are $0$ and $e_0$, and an idempotent different from both is **nontrivial**. The idempotents are the first of the element-theoretic data of a multiplication: for an associative unital algebra they are the projectors, and they carry the Peirce decompositions and the minimal ideals of the algebra, which for the multiplication $\tilde P\tilde Q$ of $\mathbb{B}$ are *Idempotents of the General Plain Algebra* and *Biquaternion Ideals and Peirce Decomposition*. This article asks the same question of the product $\star$.

The answer is as small as it could be. The square of every biquaternion lies in the centre,

$$
\tilde Q\star\tilde Q = \tilde Q^{\natural}\tilde Q = N(\tilde Q)\,e_0 , \qquad N(\tilde Q) = Q_0^2+Q_1^2+Q_2^2+Q_3^2 ,
$$

so an idempotent is central, and on the centre the idempotent equation collapses to $A^2 = A$.

**Theorem (idempotents).** The solutions of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ are $\tilde\Pi = 0$ and $\tilde\Pi = e_0$; the quaternionic product has no nontrivial idempotent.

The contrast with the associative multiplication is the content of the article. There the nontrivial idempotents are the **Hermitian projectors** $\tfrac12(e_0 + i\hat\mu)$, the family over the real unit vectors $\hat\mu$; here the idempotent set is the pair $\{0,e_0\}$ alone. The Hermitian projectors are not lost, however: reading the first slot of the product through ${}^{\natural}$ converts each of them into a **square-zero** element, so that the whole family is displaced from the idempotents into the nilpotents, which is where the next article (*The Nilpotents and the Zero Divisors of the Quaternionic Product*) reads it. The article closes by reading the idempotent equation on each of the remarkable subspaces of *Introduction to the Remarkable Subspaces*: the centre, the quaternion subspace and the Hermitian subspace carry the two trivial idempotents, and the other three carry $0$ alone.

## The Square and the Idempotent Equation

The whole article rests on one computation, which is the statement that $\star$ squares every element into the centre.

**Lemma (the square is central).** For every $\tilde Q \in \mathbb{B}$,

$$
\tilde Q\star\tilde Q = \tilde Q^{\natural}\tilde Q = N(\tilde Q)\,e_0 ,
$$

where $N(\tilde Q) = Q_0^2+Q_1^2+Q_2^2+Q_3^2$ is the norm of the algebra.

**Proof.** Write $\tilde Q = Q_0e_0 + \mathbf Q$ with $\mathbf Q = Q_1e_1+Q_2e_2+Q_3e_3$, so that $\tilde Q^{\natural} = Q_0e_0 - \mathbf Q$. The scalar–vector form of the product (*The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Bilinear Product*) gives the scalar part $P_0Q_0 + (\mathbf P,\mathbf Q)$ and the vector part $P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q$. At $\tilde P = \tilde Q$ the vector part is $Q_0\mathbf Q - Q_0\mathbf Q - \mathbf Q\times\mathbf Q$, and the cross product of a vector with itself vanishes; the scalar part is $Q_0^2 + (\mathbf Q,\mathbf Q) = N(\tilde Q)$. Hence $\tilde Q\star\tilde Q = N(\tilde Q)e_0$. $\square$

The lemma is the reason the idempotent equation is trivial here and nontrivial for the associative product. The latter has $\tilde Q\tilde Q = Q_0^2e_0 + 2Q_0\mathbf Q + \mathbf Q^2$, whose vector part is not obliged to vanish, and whose solutions are the projectors of *Idempotents of the General Plain Algebra*. For $\star$ the square carries no vector part at all, and the idempotents are decided by a single quadratic in one complex variable.

**Theorem (idempotents).** The solutions of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ are $\tilde\Pi = 0$ and $\tilde\Pi = e_0$.

**Proof.** By the lemma the left-hand side is $N(\tilde\Pi)e_0$, an element of the centre, so an idempotent is central, that is $\tilde\Pi = Ae_0$ for some $A \in \mathbb{C}$. For a central element the equation reads $A^2e_0 = Ae_0$, that is $A^2 = A$, or $A(A-1) = 0$. Since $\mathbb{C}$ is a field, $A = 0$ or $A = 1$. Conversely both $\tilde\Pi = 0$ and $\tilde\Pi = e_0$ satisfy the equation. $\square$

**Remark.** In coordinates the proof says that $\tilde\Pi$ is an idempotent exactly when its vector part vanishes and its scalar coordinate is a root of $X^2 - X$. The single equation $N(\tilde\Pi) = \Pi_0$ is weaker than idempotence and must be read with centrality attached: every nonzero nilpotent, an element with $N(\tilde Q) = 0$ and $\tilde Q \neq 0$, satisfies $N(\tilde Q) = Q_0$ and is not an idempotent, its square being $0$ whereas it is itself not $0$ and not central. The nilpotents are the subject of the next article; here they matter only as the warning that the equation in one coordinate is necessary and not sufficient.

**Corollary.** The square of every element lies in the centre, so the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ contains the image of the square map, and in particular every idempotent of the quaternionic product is central.

## The Isotope Reading

The product $\star$ is not an arbitrary second multiplication on $\mathbb{B}$; it is the **isotope** of the associative product $\tilde P\tilde Q$ by the $\mathbb{C}$-linear map ${}^{\natural}$, that is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ (*Introduction to the General Quaternionic Algebra of Biquaternions*). The idempotents of an isotope are governed by the twisting map, and the general statement explains in advance why the family of projectors of the algebra cannot survive.

**Proposition (idempotents of an isotope).** Let $A$ be an algebra with a linear map $\sigma$ and the product $x\star_\sigma y = \sigma(x)y$. Then $e$ satisfies $e\star_\sigma e = e$ if and only if $\sigma(e)e = e$. In particular an element fixed by $\sigma$, $\sigma(e) = e$, is idempotent for $\star_\sigma$ exactly when it is idempotent for the original product.

**Proof.** The first statement is the definition, $e\star_\sigma e = \sigma(e)e$. For the second, if $\sigma(e) = e$ then $\sigma(e)e = e^2$ and the two equations coincide. $\square$

The twisting map here is the natural conjugation, an **anti-automorphism** of order two, $\sigma(xy) = \sigma(y)\sigma(x)$ and $\natural\natural = \mathrm{id}$, and the elements it fixes are exactly the central ones, $Q_1 = Q_2 = Q_3 = 0$. The proposition therefore separates the two cases. A nontrivial Hermitian projector is an idempotent of the algebra but is not fixed by ${}^{\natural}$, its vector part $i\hat\mu$ being nonzero, so the proposition gives no reason for it to be idempotent for $\star$, and by the theorem above it is not. Conversely an idempotent of the algebra that is fixed by ${}^{\natural}$ must be central and hence one of $0,e_0$, in agreement with the full computation.

**Remark.** The isotope reading explains where the projectors went but does not by itself compute the idempotents of $\star$, because the proposition only describes the $\natural$-fixed ones. The certificate that the list is complete is the centrality of the square, and it is the direct computation of the lemma that supplies it. Isotopes of an algebra differ from it in exactly these element-theoretic data — the units, the idempotents, the zero divisors — while sharing its underlying vector space.

## What the Hermitian Projectors Become

The Hermitian projectors are the nontrivial idempotents of the associative multiplication, and they are the family that the $\natural$-reading is about to move.

**Definition.** For a **real unit vector** $\hat\mu = \mu_1e_1+\mu_2e_2+\mu_3e_3$, $\mu_1^2+\mu_2^2+\mu_3^2 = 1$, the **Hermitian projector** is

$$
\tilde\Pi_1(\hat\mu) = \tfrac12\bigl(e_0 + i\hat\mu\bigr) .
$$

**Lemma.** Every Hermitian projector is a nontrivial idempotent of the general plain bilinear product, and it lies in the Hermitian subspace: $\tilde\Pi_1(\hat\mu)\tilde\Pi_1(\hat\mu) = \tilde\Pi_1(\hat\mu)$ and $\tilde\Pi_1(\hat\mu) \in \mathbb{M}_+$ (*Introduction to the Remarkable Subspaces* §*The Hermitian Subspace*).

**Proof.** The element $i\hat\mu$ has square $(i\hat\mu)^2 = i^2\hat\mu^2 = (-1)(-e_0) = e_0$ because $\hat\mu$ is a real unit vector, and it is fixed by Hermitian conjugation, which conjugates the coefficients and negates the vector part while both operations leave $i\hat\mu$ unchanged. Hence $\tilde\Pi_1^2 = \tfrac14(e_0 + 2i\hat\mu + e_0) = \tfrac12(e_0+i\hat\mu) = \tilde\Pi_1$; the element has real scalar part and purely imaginary vector part, which is the coordinate condition of $\mathbb{M}_+$. It is not $0$ and not $e_0$. $\square$

This is the statement of *Idempotents of the General Plain Algebra* that the nontrivial idempotents of the algebra are exactly these, one for each real unit vector, so that the idempotent set of the associative product is the family $\tilde\Pi_1(\hat\mu)$ over the real unit vectors, together with $0$ and $e_0$. The quaternionic product answers differently.

**Proposition (the projectors become nilpotents).** For every real unit vector $\hat\mu$,

$$
\tilde\Pi_1(\hat\mu)\star\tilde\Pi_1(\hat\mu) = 0 .
$$

**Proof.** The natural conjugation negates the vector part, so $\tilde\Pi_1(\hat\mu)^{\natural} = \tfrac12(e_0 - i\hat\mu)$, the **complementary projector** $\tilde\Pi_2(\hat\mu) = e_0 - \tilde\Pi_1(\hat\mu)$. Therefore

$$
\tilde\Pi_1(\hat\mu)\star\tilde\Pi_1(\hat\mu) = \tilde\Pi_1(\hat\mu)^{\natural}\tilde\Pi_1(\hat\mu) = \tilde\Pi_2(\hat\mu)\tilde\Pi_1(\hat\mu) = \tfrac14\bigl(e_0 - (i\hat\mu)^2\bigr) = \tfrac14(e_0 - e_0) = 0 ,
$$

using $(i\hat\mu)^2 = e_0$ from the lemma. $\square$

**Remark (what replaces them).** The family of Hermitian projectors is not lost; it is displaced from one element-theoretic set to another. As idempotents of $\star$ it is empty, the two trivial elements being the whole idempotent set by the theorem above; as **square-zero** elements it is exactly the family $\{\tilde\Pi_1(\hat\mu) : \hat\mu \text{ a real unit vector}\}$, and in the next article this family is read as sitting inside the nilpotent cone $N(\tilde Q) = 0$. The displacement is caused by the change of one operation: the derived multiplication $\tilde P\tilde Q^{*}$ has the Hermitian projectors as its nontrivial idempotents, because its first slot carries no conjugation and its second carries the Hermitian conjugation, which fixes them; the quaternionic product $\tilde P^{\natural}\tilde Q$ moves the conjugation to the first slot, where ${}^{\natural}$ sends $\tilde\Pi_1$ to its complement, and the product of a projector with its complement vanishes. The same computation is the reason the projectors of the algebra are zero divisors of the algebra, whereas here they are square-zero and every nonzero square-zero element is a zero divisor of the algebra — a reading that belongs to the next article.

## The Idempotent Equation on the Remarkable Subspaces

The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ (*Introduction to the Remarkable Subspaces*). Since the idempotent equation is $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ and the square is always central, the equation can hold inside a subspace only if the subspace contains the two trivial idempotents, and this is what distinguishes the remarkable subspaces.

| subspace | element | $\tilde\Pi\star\tilde\Pi$ | idempotents |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$ | $A^2e_0$ | $0$, $e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf P$ | $(\mathbf P,\mathbf P)e_0$ | $0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $h$ | $(h_0^2+h_1^2+h_2^2+h_3^2)e_0$ | $0$, $e_0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$ | $-(h_0^2+h_1^2+h_2^2+h_3^2)e_0$ | $0$ |
| $\mathbb{M}_+$ | $a_0e_0 + i\mathbf p$ | $(a_0^2-(\mathbf p,\mathbf p))e_0$ | $0$, $e_0$ |
| $\mathbb{M}_-$ | $ib_0e_0 + \mathbf q$ | $(-b_0^2+(\mathbf q,\mathbf q))e_0$ | $0$ |

**The centre.** Here the equation is $A^2 = A$, so the centre carries exactly the two trivial idempotents, and no other subspace can carry more.

**The quaternion subspace.** For $h$ a biquaternion with all four coordinates in $\mathbb{R}$, the square is $\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$, a **real** scalar times $e_0$. An idempotent inside $\mathbb{H}_{\mathbb{B}}$ must therefore be a real multiple of $e_0$, and the equation $h_0^2 = h_0$ leaves $h_0 = 0$ and $h_0 = 1$: the quaternion subspace carries the two trivial idempotents and no others.

**The Hermitian subspace.** For $\tilde\Pi = a_0e_0 + i\mathbf p$ with $a_0 \in \mathbb{R}$ and $\mathbf p \in \mathbb{R}^3$, the square is $\bigl(a_0^2 - (\mathbf p,\mathbf p)\bigr)e_0$, whose vector part is zero. An idempotent in $\mathbb{M}_+$ must therefore have $i\mathbf p = 0$, hence $\mathbf p = 0$, and then $a_0^2 = a_0$; the Hermitian subspace carries the two trivial idempotents. The Hermitian projectors $\tilde\Pi_1(\hat\mu)$ lie in $\mathbb{M}_+$ and are the elements of $\mathbb{M}_+$ for which the alternative, associative square is the identity of the projector equation; the quaternionic square of every one of them is $0$.

**The vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace.** In $\mathrm{Vect}(\mathbb{B})$ the square is $(\mathbf P,\mathbf P)e_0$, a central element, and a central element equals the vector $\mathbf P$ only when $\mathbf P = 0$; a nonzero isotropic vector, $(\mathbf P,\mathbf P) = 0$, has square $0$ and is not an idempotent. In $i\mathbb{H}_{\mathbb{B}}$ the square of $ih$ is $-h^{\natural}h = -\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)e_0$, a real scalar multiple of $e_0$ with the **opposite sign** to the square in $\mathbb{H}_{\mathbb{B}}$, the norm being negative definite there; a real multiple of $e_0$ equals the purely imaginary element $ih$ only when $h = 0$. In $\mathbb{M}_-$ the square of $ib_0e_0+\mathbf q$ is a central element, so an idempotent has $\mathbf q = 0$ and then $-b_0^2 = ib_0$, which for real $b_0$ forces $b_0 = 0$. Each of the three carries only the trivial idempotent $0$.

**Remark.** Three of the remarkable subspaces carry the two trivial idempotents and three carry only $0$, and no subspace of the remarkable subspaces carries a nontrivial one. This is the exact opposite of the algebraic reading of the same remarkable subspaces, where the nontrivial idempotents are the Hermitian projectors and live in $\mathbb{M}_+$, with the centre and the quaternion subspace carrying the trivial pair and the anti-Hermitian subspace none (*Introduction to the Remarkable Subspaces*). The change of product moves the nontrivial idempotents out of the idempotent set altogether.

## The Peirce Decomposition It Does Not Carry

A nonzero idempotent of an associative unital algebra carries the **Peirce decomposition** of the algebra relative to it, $A = A_1 \oplus A_{1/2} \oplus A_0$ with $A_\lambda = \{x : \Pi x = \lambda x\}$; the summands are the images of the maps $x\mapsto \Pi x$ and $x\mapsto x\Pi$, and the decomposition is the source of the minimal ideals and the matrix units of the algebra (*Unital Algebras* §*Idempotents and the Peirce Decomposition*). The construction uses associativity twice, in reading the two maps as projections and in verifying that their images add up.

For the quaternionic product the construction has nothing to attach to. The only nonzero idempotent is the left unit $e_0$, and the left multiplication $L_{e_0}(\tilde X) = e_0\star\tilde X = \tilde X$ is the identity, so the only Peirce piece is the whole algebra and the decomposition is the trivial one. The nontrivial Peirce decompositions of the algebra — the frame of two orthogonal projectors, the four Peirce lines of real dimension two, the minimal left ideals — are properties of the associative multiplication alone, and none of them is available for $\star$. What the quaternionic product has in their place is the central value of the square; the elements it separates are the nilpotents rather than the Peirce pieces, which is the reading of the next article.

## The Idempotents Among the Elements

**The idempotents and the unit.** The nonzero idempotent $e_0$ is the left unit of the multiplication, $e_0\star\tilde Q = \tilde Q$, and it is a unit of the algebra, with inverse $e_0$; the other idempotent, $0$, is neither. In the associative multiplication a nonzero idempotent different from $e_0$ is never a unit and is always a zero divisor; here no such idempotent exists, so the statement is vacuous. What is not vacuous is the converse direction: the idempotents of the quaternionic product are exactly the central elements whose scalar coordinate is a root of $X^2 = X$; the central element $-e_0$ has norm $1$ and is not an idempotent, so the norm alone is not the criterion.

**The idempotents and the zero divisors.** An element of norm zero is a zero divisor of the algebra, and a nonzero idempotent of the quaternionic product is $e_0$, of norm $N(e_0) = 1$, while the zero idempotent has norm $0$. Hence **no nonzero idempotent of the quaternionic product is a zero divisor**, which is the exact opposite of the situation in the associative multiplication, where every nontrivial idempotent is a zero divisor. The zero divisors of the quaternionic product are instead the square-zero elements, among which the displaced Hermitian projectors sit; the precise statement is the equivalence $N(\tilde Q) = 0 \iff \tilde Q\star\tilde Q = 0 \iff \tilde Q$ is a zero divisor of the algebra, proved in the next article.

**The four general products.** The idempotent sets of the four general products are four different sets, and this is the sharpest single distinction among them (*Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*):

| product | idempotents |
|---|---|
| $\tilde P\tilde Q$ | $0$, $e_0$, and the Hermitian projectors $\tfrac12(e_0+i\hat\mu)$ |
| $\tilde P^{\natural}\tilde Q$ | $0$ and $e_0$ alone |
| $\tilde P\tilde Q^{*}$ | $0$, $e_0$, and the Hermitian projectors |
| $\tilde P^{\natural}\tilde Q^{*}$ | $0$, $e_0$, and $-\tfrac12e_0+\mu$ for a real vector $\mu$ with $(\mu,\mu) = \tfrac34$ |

The quaternionic column is this article; the comparison article owns the table, and the present article supplies only the proof of its second column and the displacement reading of the first and third.

**The matrix reading.** In the model $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_0) = I$ the two idempotents of the quaternionic product are $\mathsf{M}_2(0) = 0$ and $\mathsf{M}_2(e_0) = I$; the projections of the matrix algebra, the images $\mathsf{M}_2(\tilde\Pi_1(\hat\mu))$, are idempotents of the plain product and have quaternionic square $\mathsf{M}_2(0) = 0$. The invertible element of the model is $I$ alone among idempotents, in agreement with the norm computation above. The matrix model is *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

## Summary

The square of every biquaternion in the general quaternionic bilinear product lies in the centre, $\tilde Q\star\tilde Q = N(\tilde Q)e_0$, so the idempotent equation forces centrality and reduces to $A^2 = A$ on the centre. The idempotents of the product are the two trivial elements $0$ and $e_0$ and nothing else, in sharp contrast with the associative multiplication, whose nontrivial idempotents are the Hermitian projectors. The Hermitian projectors are not lost: reading the first slot through ${}^{\natural}$ converts each of them into a square-zero element, and the family of projectors is displaced from the idempotent set into the nilpotent cone, where the next article reads it. Read on the remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre, the quaternion subspace and the Hermitian subspace, and only $0$ in the vector, anti-quaternion and anti-Hermitian subspaces; no subspace carries a nontrivial idempotent, and no nonzero idempotent is a zero divisor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde P = \sum_\mu P_\mu e_\mu$ | an element and its four complex coordinates |
| $\mathbf P = \sum_{k=1}^{3}P_ke_k$ | the vector part |
| $(\mathbf P,\mathbf Q)$ | the complex bilinear dot product $\sum_k P_kQ_k$ |
| $\mathbf P\times\mathbf Q$ | the complex bilinear cross product |
| ${}^{\natural}$ | the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$ |
| $N(\tilde P) = \tilde P^{\natural}\tilde P = P_0^2+P_1^2+P_2^2+P_3^2$ | the norm of the algebra |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the multiplication of this group |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ |
| $\tilde\Pi_1(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ | the Hermitian projector over a real unit vector $\hat\mu$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector, quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces |
| $A \in \mathbb{C}$, $h \in \mathbb{H}_{\mathbb{B}}$, $a_0,b_0 \in \mathbb{R}$, $\mathbf p,\mathbf q \in \mathbb{R}^3$ | the running elements of the subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for idempotents and square-zero elements in a non-associative algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent, the Peirce decomposition and the projector equation in the absence of associativity.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for idempotents and their order in a ring with an involution, and for the comparison of two idempotents.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugations of an algebra and the elements they fix.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion conjugation and the coordinate form of the quaternion product.
