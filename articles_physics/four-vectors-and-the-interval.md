# __Four-Vectors and the Interval__

## Introduction

This entry reads the second article of the fourth section of the category: the material sector as the home of the four-vector. The sector is the anti-Hermitian half of the algebra, four real dimensions, and it is the only part of the algebra in which the order of events is written. The entry states what the algebra supplies to a four-vector, what it refuses, and which of the standard relativistic statements are theorems rather than conventions.

$$
\mathbb{B}_{\Phi}=\{\tilde Q\in\mathbb{B}:\tilde Q^{*}=-\tilde Q\},
\qquad
\tilde R_{\Phi}=i\,r'_t\,e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z,
\qquad
r'_t,r_x,r_y,r_z\in\mathbb{R}.
$$

The first claim is that the interval is the norm, and that its signs are produced by one symbol. On the sector the quaternionic norm is real, with three positive directions and one negative, because the temporal coordinate is multiplied by the central imaginary and the spatial ones are not. Nothing is added to obtain the Lorentzian sign pattern. The minus sign on the time term is the square of $i$, and the placement of the imaginary unit on the two blocks is what distributes the signs: with $i$ on the temporal block the form is $(3,1)$ and with $i$ on the spatial block it is $(1,3)$, so the two Lorentzian placements are the two Hermitian halves.

The second claim is that the sector is a Lie algebra and not an algebra. The bracket of two material elements is twice the cross product of their space parts and has no temporal component, so the temporal direction is central and the bracket is $\mathfrak{su}(2)$ on a line. The product of two material elements, by contrast, leaves the sector: it is Hermitian exactly when the two commute, and the anticommutator is Hermitian always. A four-vector therefore generates rotations and is never itself a product of two four-vectors.

The third claim is that the Lorentz action comes from outside the sector. The map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ preserves the sector for every invertible $\tilde U$ and preserves the interval exactly when $N(\tilde U)=1$. The rotations of that action are carried by the real unit quaternions inside the sector, the boosts are carried by the Hermitian units outside it, and the sector is a representation space rather than a group. This is the precise sense in which a change of frame is not an element of the thing it acts on.

The fourth claim is that the spectrum of a four-vector is a Doppler pair, and that its eigenprojectors are not material. The two eigenvalues of a momentum are $i(E/c\pm\lvert\vec p\rvert)$, the two light-cone frequencies, and their product is the mass squared. The projectors that produce them are Hermitian idempotents, so they lie in $\mathbb{B}_{\Psi}$ and not in $\mathbb{B}_{\Phi}$: the modes of a four-vector are states, and the sector that carries the vector does not carry its own decomposition.

The fifth claim is that the branch is data. The pair of frequencies is fixed once the momentum is given, but the statement that both are non-negative needs $E/c\ge\lvert\vec p\rvert$, which is the choice of the future sheet. The two sheets are not exchanged by the proper orthochronous group, so the branch is a Lorentz-invariant declaration and not a representative. Every statement below that mentions a sign of energy names the branch it uses.

The sixth claim is a correction to a plausible reading. It is tempting to say that the four-vector is an element of the algebra and therefore that the algebra contains spacetime. It does not: the sector contains the points of a flat kinematic space and the invariants of its linear motions, and it contains neither a metric field, nor a connection, nor an equation of motion. What it contains is exactly the data that a four-vector formalism contains, and the entry says so in the same place where it says what the formalism is used for.

The seventh claim is the reading, and it is stated here so that it can be judged against the mathematics. The material sector is the kinematic layer of the framework: it is where an event, a worldline, a momentum and a wave covector are the same kind of object, and where the difference between them is the invariant that each one's norm carries. The interval is not a distance and not a metric; it is the invariant of the sector, and the three classes of four-vector are the three regions of its zero set.

The strongest objection is that this is the standard four-vector formalism with new letters. The algebra does supply a dictionary, and a dictionary is not a derivation. The answer is that three statements here are theorems and not translations. The coincidence of the light cone with the zero-divisor cone is one. The split of the Lorentz algebra into one part inside the sector and one part outside it is the second. The presence of the eigenprojectors in the other sector is the third. Each of the three is a fact about this algebra that a general four-vector formalism does not state.

A second objection is that the interval has been placed in the algebra by hand, through the factor $i$ on the time coordinate. The factor is not free: the sector is defined as the fixed space of the reversal, and on that fixed space the coefficient of $e_t$ is imaginary by definition. The alternative convention, the Hermitian sector, gives the negative of the same form and the same geometry. What is not available is a real four-plane on which the norm is real and positive definite *and* indefinite somewhere else; the signs are distributed by the involution, not chosen per element.

The interpretation labels continue the category's sequence. *The H Norm: Amplitude and Frame* carries I.8.a to I.8.k, *The N Norm: Mass, Angle and the Cone* carries I.9.a to I.9.l, the five entries from *The Partition: Two Invariants and Four Regimes* to *The Vacuum and the Nilpotent Ladder* carry I.10.a to I.10.bd, and *The K Norm and the Indefinite Structure* carries I.11.a to I.11.l. The first entry of this section, *The Two Sectors: The Hermitian Split and the Four Bridges*, is a catalogue and carries no labels. This entry carries I.12.a to I.12.l.

The readings are readings. Every physical name below is attached to an algebraic object defined without it, and §*The Limits* states what the readings do not carry. No field equation, no dynamics, no statistics and no curved metric are supplied here.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the sector, its basis, its coordinate blocks and its position among the six subspaces | [Subspaces and Decompositions of the Biquaternion Algebra](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |
| the norm, its signs, the inverse formula, the invertibles and the zero-divisor cone | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the four forms, their Gram matrices and their inertia on the sector | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the products, the symmetric and antisymmetric decomposition and the cross-product formula | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| the bracket, the anticommutator and the Lie algebra of the sector | [Lie Algebras of Sesqualgebras](../articles_maths/lie-algebras-of-sesqualgebras.html) |
| the rotor conjugation, the double covers, $SO^{+}(1,3)$ and $\mathrm{Spin}(1,3)$ | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| the exponential, the boost and rotation families and their closed forms | [Biquaternion Lie Group and Exponential Structure](../articles_maths/biquaternion-lie-group-and-exponential-structure.html) |
| the eigenvalue decomposition, the eigenprojectors and the degenerate case | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| the spectrum, the centraliser and the semisimple–nilpotent split | [The Spectrum](../articles_maths/the-spectrum-of-a-biquaternion.html) |
| the K norm and the coincidence of the two null sets on this sector | [Kr-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/kr-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| the rank of the one-sided multiplications and the polar decomposition | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |

Two physics companions are quoted and not rebuilt. The reading of the eigenpair is *The Spectral Reading of a Four-Vector*. The indefinite form and the two null sets are *The K Norm and the Indefinite Structure*, the previous section of this series. The dictionary of the seven four-vectors, the interval and the Lorentz action is this entry's own. What this entry adds to those two is the position of the sector in the category: which of its properties are inherited from the algebra, which are inherited from the involution that defines it, and which are the sector's alone.

## The Results in Brief

The temporal block $\mathbb{R}(ie_t)$ is one-dimensional and central; the spatial block $k=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ is three-dimensional. The two blocks behave differently under every operation of the algebra, and the difference is the whole content of the sector.

| operation | temporal block $\mathbb{R}(ie_t)$ | spatial block $k$ | whole sector |
| --- | --- | --- | --- |
| quaternionic norm $N$ | $-r_t'{}^{2}$ | $+\lvert\vec r\rvert^{2}$ | $-r_t'{}^{2}+\lvert\vec r\rvert^{2}$, three positives and one negative |
| Hermitian norm $H$ | $+r_t'{}^{2}$ | $+\lvert\vec r\rvert^{2}$ | positive definite, $(4,0)$ |
| plain norm $P$ | $-r_t'{}^{2}$ | $-\lvert\vec r\rvert^{2}$ | negative definite, $(0,4)$ |
| K norm $\mathrm{Kr}$ | $+r_t'{}^{2}$ | $-\lvert\vec r\rvert^{2}$ | $r_t'{}^{2}-\lvert\vec r\rvert^{2}$, one positive and three negatives |
| bracket $[\cdot,\cdot]$ | $0$ | $2\vec r_1\times\vec r_2$ | stays in the sector |
| anticommutator $\{\cdot,\cdot\}$ | — | — | leaves the sector |
| product | — | — | leaves the sector unless the factors commute |
| action $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ | preserved | preserved | preserved |
| central imaginary $i\cdot$ | leaves the sector | leaves the sector | $\mathbb{B}_{\Phi}\to\mathbb{B}_{\Psi}$ |

On the sector the four forms are all real, because the star is minus the identity there. They are therefore four real quadratic forms on one real four-space, and their counts of positive and negative directions are $(3,1)$, $(4,0)$, $(0,4)$ and $(1,3)$. Only two of them are indefinite, and the two indefinite ones are negatives of each other:

$$
N=-\mathrm{Kr},
\qquad
H=-P .
$$

For $\tilde R_{\Phi,1}=ir'_{1t}e_t+\vec r_1$ and $\tilde R_{\Phi,2}=ir'_{2t}e_t+\vec r_2$,

$$
[\tilde R_{\Phi,1},\tilde R_{\Phi,2}]=2\,\vec r_1\times\vec r_2,
$$

with no temporal part and no dependence on $r'_{1t}$ or $r'_{2t}$. The temporal coordinate is therefore central in the sector, and the sector's Lie algebra is $\mathfrak{u}(2)=\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$.

**The Lorentz action is a congruence by an invertible element, and the invertible need not be in the sector.** For any invertible $\tilde U$ the map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ carries $\mathbb{B}_{\Phi}$ into itself, since $(\tilde U\tilde Q\tilde U^{*})^{*}=\tilde U\tilde Q^{*}\tilde U^{*}=-\tilde U\tilde Q\tilde U^{*}$. The norm scales by $\lvert N(\tilde U)\rvert^{2}$, so the action is by isometries exactly on the elements with $\lvert N(\tilde U)\rvert=1$, a set of real dimension $7$ strictly larger than the norm-one group.

For a momentum $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$ the eigenvalues are $\eta_{\pm}=i(E/c\pm\lvert\vec p\rvert)$, the two frequencies are $f_{\mathrm{dop},\pm}=mc\,e^{\pm\theta_{\mathrm{rpd}}}$ for a massive momentum, and the product is the mass squared.

The eigenprojectors lie in the other sector. They are $\tilde\Pi_{\mathrm{id},\pm}=\frac12(e_t\mp i\vec u_p)$, Hermitian idempotents, so $\tilde\Pi_{\mathrm{id},\pm}\in\mathbb{B}_{\Psi}$ although $\tilde P_{\Phi}\in\mathbb{B}_{\Phi}$. The decomposition of a material element is written with informational idempotents.

Two null sets coincide here and nowhere else. On the sector the K norm is minus the algebraic norm, so lightlike and massless are one equation. That coincidence is *The K Norm and the Indefinite Structure*, §*The Six Restrictions*, and it is used here as a boundary rather than reproved.

## The Sector and Its Coordinates

The material sector is the fixed space of the reversal. The algebra carries one involution and two reversals, and the syntax of the corpus is fixed by the conventions article: ${}^{*}$ is the Hermitian involution, ${}^{\natural}$ the quaternionic conjugation, and the material reversal is the composite

$$
\tilde Q^{\flat}=-{}^{*}\tilde Q .
$$

The sector is the set of elements fixed by the reversal, and the fixed space of a linear involution is a linear subspace. The definition therefore costs nothing and adds nothing: the sector is a subspace of the algebra before any physical word is used.

In coordinates the definition is a statement about real and imaginary parts. With the coefficient vector $(Q_t,Q_x,Q_y,Q_z)\in\mathbb{C}^{4}$ the involution acts as

$$
\tilde Q^{*}=(\bar Q_t,-\bar Q_x,-\bar Q_y,-\bar Q_z),
$$

so the fixed space of $-{}^{*}$ is the set of vectors with $Q_t$ purely imaginary and $Q_x,Q_y,Q_z$ real. That is the four real parameters $r'_t,r_x,r_y,r_z$ of the display in the introduction. The prime on the temporal coordinate marks the convention that the temporal component carries the imaginary unit explicitly, and it is the same prime that this entry uses throughout.

The temporal block and the spatial block are different objects. The first is $\mathbb{R}(ie_t)$, a line, and the second is $k=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, a three-space. Every table in this entry separates them, because every claim about the sector either holds for both blocks or distinguishes them, and the distinction is never the one that a reader expects. The norm is negative on the first block and positive on the second. The bracket vanishes on the first block and is the cross product on the second. The K norm has the opposite signs. The central imaginary exchanges the signs of the two blocks.

**The sector is not an algebra and the failure is structural.** The star is an anti-automorphism, so for two anti-Hermitian elements

$$
(\tilde R_{\Phi,1}\tilde R_{\Phi,2})^{*}=\tilde R_{\Phi,2}^{*}\tilde R_{\Phi,1}^{*}=\tilde R_{\Phi,2}\tilde R_{\Phi,1},
$$

and the product is Hermitian exactly when the two factors commute. A product of two distinct material elements is therefore not material. The square of a material element is always informational, since the element commutes with itself. A four-vector multiplied by a four-vector is a state or a density, and not another four-vector.

The bracket does not fail. The antisymmetric part of the product is the commutator, and the commutator of two anti-Hermitian elements is anti-Hermitian:

$$
[\tilde R_{\Phi,1},\tilde R_{\Phi,2}]^{*}
=(\tilde R_{\Phi,1}\tilde R_{\Phi,2})^{*}-(\tilde R_{\Phi,2}\tilde R_{\Phi,1})^{*}
=\tilde R_{\Phi,1}\tilde R_{\Phi,2}-\tilde R_{\Phi,2}\tilde R_{\Phi,1}.
$$

Writing the two elements in components, the product is

$$
\tilde R_{\Phi,1}\tilde R_{\Phi,2}
=-\bigl(r'_{1t}r'_{2t}+\vec r_1\cdot\vec r_2\bigr)e_t
+i\bigl(r'_{1t}\vec r_2+r'_{2t}\vec r_1\bigr)
+\vec r_1\times\vec r_2,
$$

and the antisymmetric part of that expression is twice the cross product of the space parts, with the temporal coordinates cancelling. The entry verifies the identity numerically as well as symbolically, and the cancellation is exact.

The symmetric part of the same product is Hermitian and carries the temporal mixing. Its scalar part is minus the Euclidean pairing of the four coefficients, and its vector part is the symmetric temporal mixture $i(r'_{1t}\vec r_2+r'_{2t}\vec r_1)$. The anticommutator is the sum of twice each, and it is informational.

The two halves of the product are the two halves of the algebra. The commutator, which stays, is the compact part and generates rotations. The anticommutator, which leaves, is the non-compact part and carries the boosts. This is the Cartan decomposition of the Lorentz algebra, obtained here without naming the group: the compact generators are the real vectors, and the non-compact ones are the imaginary vectors, which lie in the informational sector.

That the boost generators are informational is a coordinate fact. The element $i\vec e_x$ has coefficient vector $(0,i,0,0)$, and its star is $(0,i,0,0)$ again, so it is Hermitian. The rotation generator $\vec e_x$ has star $-\vec e_x$ and is material. Hence

$$
\mathfrak{so}(1,3)=\mathfrak{su}(2)_{J}\oplus i\,\mathfrak{su}(2)_{K},
\qquad
J\in\mathbb{B}_{\Phi},
\qquad
K\in\mathbb{B}_{\Psi},
$$

and the Lie algebra of the Lorentz group uses both sectors. Nothing in the sector alone generates a boost.

The centre of the sector is the time axis, and the bracket cannot see it. Since the bracket is the cross product of the spatial parts, the coordinate $r'_t$ does not enter. Two four-vectors with the same space part and different energies have the same bracket with everything. The bracket of the sector is therefore $\mathfrak{su}(2)$ and not $\mathfrak{so}(1,3)$, and the temporal line is an abelian summand: $\mathfrak{u}(2)$ rather than $\mathfrak{su}(2)$.

A four-vector is a generator of spatial rotations, and the temporal component is a label that rotations do not touch. The Lorentz boosts, which are what mix the temporal component into the spatial ones, are not in the sector's bracket at all; they are the action of the sector's Hermitian complement. The entry returns to this in §*The Lorentz Action*.

The sector sits in the six-subspace decomposition as one of the two Hermitian halves. The other half is $\mathbb{B}_{\Psi}$, the fixed space of ${}^{*}$ itself, with basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$. The two halves intersect in $\{0\}$ and span the algebra, and the central imaginary exchanges them. The remaining four subspaces of the six-subspace list are the centre, the quaternion layer, the vector subspace and the scalar-free part; the entry uses only the two halves and the two blocks inside $\mathbb{B}_{\Phi}$.

## The Interval

The interval is the quaternionic norm restricted to the sector, and on the sector it is real. The norm of a general biquaternion is complex; the general formula is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$, and it is real exactly when the element lies in one of the two Hermitian halves. On the sector,

$$
N(\tilde R_{\Phi})=\tilde R_{\Phi}\tilde R_{\Phi}^{\natural}=-r_t'{}^{2}+r_x^{2}+r_y^{2}+r_z^{2},
$$

and the right-hand side is a real quadratic form with one negative direction, the temporal one, and three positive ones, the spatial ones.

The signs are produced by the square of the central imaginary. The temporal coordinate enters the display as $ir'_t$, and $(ir'_t)^{2}=-r_t'{}^{2}$. With a real temporal coefficient the form would be $r_t'{}^{2}+\lvert\vec r\rvert^{2}$, positive definite, with no null set and no cone. The Lorentzian sign pattern is therefore a consequence of the placement of $i$ in the definition of the sector, and the placement is a consequence of the involution that defines the sector. Nothing is added.

The inverse formula fails exactly on the cone. For a unit-norm element the inverse is $\tilde R_{\Phi}^{-1}=\tilde R_{\Phi}^{\natural}/N(\tilde R_{\Phi})$, and for zero norm there is no inverse. The zero set of the norm is therefore the boundary of the set of invertibles, and on it the element is a zero divisor:

$$
N(\tilde R_{\Phi})=0,\quad \tilde R_{\Phi}\neq0
\quad\Longleftrightarrow\quad
\tilde R_{\Phi}\ \text{annihilates a non-zero element on the left and on the right}.
$$

The origin is the one null point that is not a zero divisor. It is null and it annihilates nothing that is not already zero. The distinction matters because the light cone is usually drawn with its apex included, and the apex is the single point where the algebraic and the geometric descriptions differ: the cone without its apex is a smooth three-manifold, the apex is the singularity that closes it.

The four forms on the sector are all real, and their signs are the four combinations. The plain form is the bilinear partner of the quaternionic one, the Hermitian form is the sesquilinear one, and the K form is the fourth. On the sector the star is minus the identity, so the sesquilinear forms differ from the bilinear ones only by a sign, and the four read

| form | expression on $\tilde R_{\Phi}$ | signs | on the sector |
| --- | --- | --- | --- |
| $\langle\tilde R,\tilde R\rangle$ | $-r_t'{}^{2}-\lvert\vec r\rvert^{2}$ | $(0,4)$ | negative definite |
| $\langle\tilde R,\tilde R\rangle_{\natural}$ | $-r_t'{}^{2}+\lvert\vec r\rvert^{2}$ | $(3,1)$ | the interval |
| $\langle\tilde R,\tilde R\rangle_{*}$ | $+r_t'{}^{2}+\lvert\vec r\rvert^{2}$ | $(4,0)$ | positive definite |
| $\langle\tilde R,\tilde R\rangle_{\natural*}$ | $+r_t'{}^{2}-\lvert\vec r\rvert^{2}$ | $(1,3)$ | minus the interval |

The identities that relate them are two. The first is $N=-\mathrm{Kr}$, which is the statement that the two indefinite forms on the sector are negatives of each other. The second is $H=-P$, which is the same statement for the two definite ones. Both hold because the star acts as minus the identity on the sector, and both fail on the informational sector, where the star acts as plus the identity and the two indefinite forms coincide with opposite orientation.

The consequences of $N=-\mathrm{Kr}$ are the whole of the coincidence of the two null sets. A material element is null for one if and only if it is null for the other, so a lightlike four-vector is a zero divisor and a zero-divisor four-vector is lightlike. That is *The K Norm and the Indefinite Structure*, §*The Six Restrictions*, and the entry records it here because it is the reason a four-vector's null set has one name rather than two.

The interval is multiplicative, and that is not true of the other three forms. For any two elements of the algebra, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, because the norm is the determinant of the $2\times2$ image. The K form is not multiplicative, the Hermitian form is not multiplicative, and the plain form is multiplicative only on the quaternionic layer. On the sector the multiplicativity of $N$ has a consequence that the other forms do not have: the sign of the interval of a product is the product of the signs of the factors.

That consequence is the algebra's version of a composition law for causal character. The product of two timelike elements is spacelike in this convention, since two negative factors give a positive product; the product of a timelike and a spacelike element is timelike; a null factor makes the product null. The statement is algebraic and its physical reading is the composition of causal characters along a chain of transformations, which is what a worldline is.

The temporal sign convention is a convention and the entry names it once. In this corpus a timelike element has negative interval and a spacelike element positive. The opposite convention is obtained by reading the informational sector instead, or by exchanging $\tilde Q$ with $i\tilde Q$, and the geometry is the same. Every statement about "future" and "past" below is a statement about the sign of $r'_t$, and it is stated in the branch where the temporal coordinate is positive for a future-pointing vector.

**The proper time is the square root of minus the interval, and it exists exactly off the null set.** For a timelike displacement one writes

$$
d\tau=\frac{1}{c}\sqrt{-N(d\tilde R_{\Phi})}
=\sqrt{dr_t'{}^{2}-\frac{dr_x^{2}+dr_y^{2}+dr_z^{2}}{c^{2}}},
$$

and the parameter is defined where the interval is negative. On the null set the proper time vanishes and the worldline is a light ray. The formula is a consequence of the norm and not an independent axiom, and it is the only place where the speed of light enters the sector: as the constant that converts the spatial coordinates into the invertibles of the temporal one.

The speed of light is local because the conversion is a choice of coordinates. The number $c$ does not appear in the algebra; it appears in the identification of the temporal coordinate with a length. In a medium, $c=1/\sqrt{\epsilon\mu}$ varies, so the cone varies from point to point and the identification varies with it. The vacuum value is the case in which the conversion is the same everywhere. The sector carries the kinematic structure; the variation of the conversion is a statement about a medium and not about the algebra.

## The Bracket

With $\tilde R_{\Phi,1}=ir'_{1t}e_t+\vec r_1$ and $\tilde R_{\Phi,2}=ir'_{2t}e_t+\vec r_2$ the product is

$$
\tilde R_{\Phi,1}\tilde R_{\Phi,2}
=-\bigl(r'_{1t}r'_{2t}+\vec r_1\cdot\vec r_2\bigr)e_t
+i\bigl(r'_{1t}\vec r_2+r'_{2t}\vec r_1\bigr)
+\vec r_1\times\vec r_2,
$$

and the antisymmetric part of the product is twice the cross product of the space parts:

$$
[\tilde R_{\Phi,1},\tilde R_{\Phi,2}]=2\,\vec r_1\times\vec r_2 .
$$

The temporal coordinates $r'_{1t}$ and $r'_{2t}$ do not appear in the bracket, so the temporal line is central. And the bracket is a real vector, so it lies in the spatial block $k$ and not merely in the sector.

The bracket is therefore $\mathfrak{su}(2)$ on a central line, and the sector is $\mathfrak{u}(2)$ as a Lie algebra. The cross product is the Lie bracket of $\mathbb{R}^{3}$ with the standard orientation, the identification of $k$ with $\mathfrak{su}(2)$ is the standard one, and the central line adds the abelian summand. The sector is a Lie algebra of real dimension four, and its derived algebra is the three-dimensional $\mathfrak{su}(2)$.

**The bracket closes and the product does not, and the difference is the involution.** This is the sharpest structural statement about the sector, and it deserves the display:

$$
[\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}]\subseteq\mathbb{B}_{\Phi},
\qquad
\{\mathbb{B}_{\Phi},\mathbb{B}_{\Phi}\}\subseteq\mathbb{B}_{\Psi},
\qquad
\mathbb{B}_{\Phi}\cdot\mathbb{B}_{\Phi}\not\subseteq\mathbb{B}_{\Phi}.
$$

The first inclusion says that a four-vector generates a rotation of four-vectors. The second says that the symmetrised product of two four-vectors is a state. The third says that a four-vector times a four-vector is neither. The sector is closed under the operation that generates transformations and open under the operation that composes objects, and that asymmetry is what makes it a kinematic space rather than a material one.

The central element $ie_t$ is the one direction the bracket cannot move. It commutes with every element of the algebra, since it is a scalar multiple of the identity in the matrix image. Its bracket with anything is zero, so the temporal direction of a four-vector is invisible to rotations. A rotation of a four-vector changes its space part and leaves its temporal component alone, and the algebra says so before any frame is chosen.

The boosts are the elements that do move the temporal direction, and they are not in the sector. An element of the sector acts on another element of the sector by the bracket, and the bracket is a cross product, which is orthogonal to both factors and has no temporal component. A boost, by contrast, mixes the temporal component into the spatial ones, and it is carried by an element of the informational sector acting by the two-sided map. The sector's own algebra therefore generates the compact part of the Lorentz group and only the compact part.

That split is the Cartan decomposition, reached from the sector rather than assumed. The compact generators are the material vectors and the non-compact generators are the informational imaginary vectors, and the two commute into the whole $\mathfrak{so}(1,3)$. The display

$$
\mathfrak{so}(1,3)=\mathfrak{su}(2)\oplus i\,\mathfrak{su}(2)
$$

is the statement that the Lie algebra of the Lorentz group needs both Hermitian halves of the algebra, and it is the reason a boost cannot be a rotation of the same kind as a rotation. The two summands are exchanged by the central imaginary, so a complex rotation is a boost: that is the statement $i\mathfrak{su}(2)=\mathfrak{su}(2)_{\mathbb{C}}$ restricted to the imaginary axis, and it is what makes the complexification of the rotation group a Lorentz group.

The anticommutator is what carries the temporal mixing, and it is Hermitian. The symmetric part of the product in the display above is

$$
\{\tilde R_{\Phi,1},\tilde R_{\Phi,2}\}
=-2\bigl(r'_{1t}r'_{2t}+\vec r_1\cdot\vec r_2\bigr)e_t
+2i\bigl(r'_{1t}\vec r_2+r'_{2t}\vec r_1\bigr),
$$

an element of $\mathbb{B}_{\Psi}$ whose scalar part is minus twice the Euclidean pairing of the four coefficients and whose vector part is twice the symmetric temporal mixture. The scalar part of half the anticommutator is therefore minus that pairing, and the vector part of half of it is the generator of the boost that would carry one four-vector into the other. Both are informational.

The Minkowski pairing is one conjugation away, and the conjugation is the natural one. The plain product pairs the four coefficients with a plus in every slot, so its scalar part is the definite form $P$ and not the interval. The indefinite pairing is read through the natural conjugation,

$$
\operatorname{Sc}\bigl(\tilde R_{\Phi,1}\tilde R_{\Phi,2}^{\natural}\bigr)
=-r'_{1t}r'_{2t}+\vec r_1\cdot\vec r_2,
$$

and this is the corpus's definition of the Minkowski pairing of two four-vectors. The scalar is real, and the element it is read from is neither material nor informational; what the second reading buys is the minus on the temporal slot, which is the whole of the difference between the interval and a Euclidean distance.

The two pairings are the two forms, read on pairs. $P$ is negative definite on the sector and $N$ is indefinite, and the two polar forms differ by the conjugation and not by a sign. A sentence that says *the pairing* without naming which one is therefore ambiguous in this sector, and the entry names it each time.

The Jordan structure and the Lie structure are therefore two different sectors. The symmetric product closes on $\mathbb{B}_{\Psi}$ and the antisymmetric one on $\mathbb{B}_{\Phi}$; the first is a Jordan algebra, the second a Lie algebra. This is the algebra's own version of the statement that the observables and the generators of a theory are different kinds of object, and the entry records it here because it is a property of the involution and not of any physical choice.

The mixed products do not close anywhere, and they are the interesting ones. A material element times an informational one is neither material nor informational in general, because the product of an anti-Hermitian and a Hermitian element has no definite symmetry. Those products are the ones a change of frame uses: a boost times a four-vector, a rotation times a four-vector, and the rotor products of the next section.

## The Lorentz Action

The action is a congruence by an invertible element, and the sector is its carrier. For $\tilde U\in\mathbb{B}$ with $N(\tilde U)=1$ the map

$$
\Lambda_{\tilde U}:\ \mathbb{B}_{\Phi}\longrightarrow\mathbb{B}_{\Phi},
\qquad
\Lambda_{\tilde U}(\tilde Q)=\tilde U\tilde Q\tilde U^{*},
$$

is real-linear, preserves the interval, and composes as an action. The three properties are one computation each. The sector is preserved because the star is an anti-automorphism; the interval is preserved because the norm is multiplicative and $N(\tilde U)=N(\tilde U^{*})=1$; and the action law is the associativity of the product.

The sector is preserved by a much larger set than the invertibles. The computation of the previous paragraph used only the anti-automorphism property, so $\Lambda_{\tilde U}$ carries the sector into itself for *every* invertible $\tilde U$, unit or not. What the unit condition buys is the preservation of the interval: for a general unit the norm scales as

$$
N\bigl(\Lambda_{\tilde U}(\tilde Q)\bigr)=N(\tilde U)N(\tilde Q)N(\tilde U^{*})=\lvert N(\tilde U)\rvert^{2}N(\tilde Q).
$$

So the congruences by invertible elements form a group larger than the Lorentz group. A central rescaling $\tilde U=Q_te_t$ acts on the sector as multiplication by $Q_t^{2}$ and moves the interval by the positive factor $\lvert Q_t\rvert^{4}$, while the invertibles act by isometries. Only the second is the Lorentz group, and the first is the reason a four-vector can be rescaled without leaving the sector.

The group of invertibles is the double cover of the proper orthochronous Lorentz group. The kernel of the action is the set of invertibles that act trivially, and it is the centre $\{\pm e_t\}$. Hence

$$
\mathbb{B}^{\times}_{1}/\{\pm e_t\}\cong SO^{+}(1,3),
\qquad
\mathbb{B}^{\times}_{1}\cong\mathrm{Spin}(1,3),
$$

and the map is two-to-one. The sign ambiguity is not a defect of the representation: it is the statement that a rotor and its negative are the same frame, and it is the same ambiguity that the double cover of the rotation group carries.

Every unit factors into a boost and a rotation. A unit-norm biquaternion is a Hermitian positive factor and a real quaternion,

$$
\tilde U=\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta_{\mathrm{axr}}}{2}+\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r},
$$

with the boost factor on the left. The boost factor is Hermitian and lies in $\mathbb{B}_{\Psi}$; the rotation factor is real and lies in $\mathbb{B}_{H}$, the quaternion layer. Only a general rotor uses the whole algebra.

The two factors act on the sector in two recognisable ways. The rotation factor $\tilde u_{\mathrm r}$ is invertible in the real quaternion algebra, so its congruence is a rotation of the spatial block and fixes the temporal coordinate. The boost factor $\tilde U_{\Psi,\mathrm b}$ is Hermitian, so its congruence mixes the temporal coordinate into the spatial ones and is the hyperbolic rotation of a change of velocity. The two commute only when the boost axis and the rotation axis coincide, and the product is written with the boost on the left because the two do not commute in general.

Rotations are inside the sector: $\tilde u_{\mathrm r}$ is a material element of unit norm, and its action is the congruence by an element of the sector. Boosts are not: $\tilde U_{\Psi,\mathrm b}$ is informational. A sector closed under the action of its own invertibles would generate only rotations, and the reason it does not is that the boost factor is not one of its own.

The action is transitive on each class of four-vector and preserves the class. A timelike four-vector is carried to any other timelike four-vector of the same interval, a null one to any null one of the same temporal sign, and a spacelike one to any spacelike one of the same interval. The invariant that separates the orbits is the norm, and it is the only one, because the group is large enough to move any direction into any other direction of the same length. The statement is the orbit classification of *Biquaternion Rotations and Lorentz Transformations*, §*Orbits and the Invariants*, restricted to the sector.

The two sheets of the timelike region are not exchanged. The action preserves the sign of the temporal component of a timelike or null element, so the future and past hyperboloids are separate orbits and not one orbit in two pieces. The statement is the proper orthochronous condition, and it is a property of the group of invertibles as defined by a continuous path from the identity: a single reflection would exchange the sheets, and a reflection is not in the connected component.

The action is what the word frame means in this entry. A frame is an orbit point; a change of frame is a rotor; the invariants of a four-vector are the quantities constant on the orbit. Nothing in that sentence is a new assumption, and nothing in it is specific to the material sector: the same three sentences describe an observable in the informational sector, with the same group acting.

The infinitesimal form separates the two factors. Writing $\tilde U=e_t+\epsilon\tilde A$ with $N(\tilde U)=1$ to first order gives $Q_t(\tilde A)=0$, and the congruence expands as

$$
\Lambda_{\tilde U}(\tilde Q)=\tilde Q+\epsilon\bigl(\tilde A\tilde Q+\tilde Q\tilde A^{*}\bigr)+O(\epsilon^{2}).
$$

The correction is a bracket for an anti-Hermitian generator and an anticommutator for a Hermitian one. If $\tilde A$ is anti-Hermitian the correction is $\tilde A\tilde Q-\tilde Q\tilde A=[\tilde A,\tilde Q]$, the infinitesimal rotation. If $\tilde A$ is Hermitian it is $\tilde A\tilde Q+\tilde Q\tilde A=\{\tilde A,\tilde Q\}$, the infinitesimal boost. Both corrections are anti-Hermitian when $\tilde Q$ is, so both preserve the sector, and the two cases are the two summands of the Cartan decomposition: $\tilde A=\vec a$ generates a rotation and $\tilde A=i\vec a$ a boost.

**The two kinds of generator sit in different sectors, and only one of them is in the sector's own bracket.** The rotation generator is a material vector and its action is the sector's bracket. The boost generator is an informational imaginary vector and its action is the anticommutator, which leaves the sector as a product while preserving it as an operator. A boost is therefore realisable as an action on the sector and not as an element of the sector's Lie algebra.

A Lorentz transformation is the congruence by an invertible element; the unit is the exponential of an element of the Lie algebra $\mathfrak{so}(1,3)=\mathfrak{su}(2)\oplus i\mathfrak{su}(2)$; and only the first summand is material. So the exponential of a material element is a rotation, the exponential of an informational element is a boost, and the general unit is the product of the two. The sector's own exponential is the rotation subgroup, and it is compact.

## The Spectrum

For $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$ with $B=\lvert\vec p\rvert$ the characteristic equation is $\eta^{2}-2Q_t\eta+N=0$ with $Q_t=iE/c$ and $N=-E^{2}/c^{2}+B^{2}$, so

$$
\eta_{\pm}=i\left(\frac{E}{c}\pm B\right),
\qquad
\eta_{+}+\eta_{-}=2i\frac{E}{c},
\qquad
\eta_{+}\eta_{-}=-m^{2}c^{2}.
$$

The eigenvalues are imaginary and the frequencies are real. Writing $f_{\mathrm{dop},\pm}=\eta_{\pm}/i$ gives the two non-negative numbers

$$
f_{\mathrm{dop},\pm}=\frac{E}{c}\pm\lvert\vec p\rvert,
\qquad
f_{\mathrm{dop},+}+f_{\mathrm{dop},-}=\frac{2E}{c},
\qquad
f_{\mathrm{dop},+}-f_{\mathrm{dop},-}=2\lvert\vec p\rvert,
\qquad
f_{\mathrm{dop},+}f_{\mathrm{dop},-}=m^{2}c^{2}.
$$

The pair is the Doppler pair of the momentum's own rapidity. For $m>0$ the rapidity is fixed by $\cosh\theta_{\mathrm{rpd}}=E/(mc^{2})$ and $\sinh\theta_{\mathrm{rpd}}=\lvert\vec p\rvert/(mc)$, so

$$
f_{\mathrm{dop},\pm}=mc\,e^{\pm\theta_{\mathrm{rpd}}},
\qquad
\frac{f_{\mathrm{dop},+}}{f_{\mathrm{dop},-}}=e^{2\theta_{\mathrm{rpd}}},
$$

and the two frequencies are the rest frequency $mc$ scaled by the two reciprocal Doppler factors. The product is the mass squared and does not depend on the frame; the ratio is the squared Doppler factor and depends on nothing else.

Only the product is invariant, and the entry insists on the difference. The sum is twice the energy, the difference is twice the momentum, the ratio is the squared Doppler factor, and each of the three changes under a boost. The product is the mass shell. A reading that takes one of the two factors as *the* frequency of the particle has confused the pair with one of its members.

The degenerate cases are two and they are different. At $\vec p=0$ the two eigenvalues coincide at $iE/c$ and the element is a scalar multiple of the identity on the sector; the two-projector writing is not unique, and any pair of orthogonal Hermitian idempotents summing to $e_t$ will do. At $E/c=\lvert\vec p\rvert$ the element is null, one frequency vanishes, and the element stays semisimple: it is a zero divisor, but its spectrum is a pair with a zero member and not a repeated root. The first case is a spectral degeneracy without a null element; the second is a null element without a spectral degeneracy.

The two cases are the exceptional point and the massless point, and they are not the same point. The first is the rest frame, where the two modes coincide; the second is the light ray, where one mode is absent. The corpus treats them in *The Rest Frame and the Exceptional Point* and *The Massless Regime* respectively, and the distinction is exactly the one between a repeated eigenvalue and a vanishing one.

**The eigenprojectors are Hermitian idempotents and they are not material.** With $\vec u_p=\vec p/\lvert\vec p\rvert$,

$$
\tilde\Pi_{\mathrm{id},\pm}=\frac12\bigl(e_t\mp i\vec u_p\bigr),
\qquad
\tilde\Pi_{\mathrm{id},\pm}^{2}=\tilde\Pi_{\mathrm{id},\pm},
\qquad
\tilde\Pi_{\mathrm{id},\pm}^{*}=\tilde\Pi_{\mathrm{id},\pm},
\qquad
\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t,
\qquad
\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0,
$$

and the element reconstructs as $\tilde P_{\Phi}=\eta_{+}\tilde\Pi_{\mathrm{id},++}\eta_{-}\tilde\Pi_{\mathrm{id},-}$. The projectors satisfy $\tilde P_{\Phi}\tilde\Pi_{\mathrm{id},\pm}=\eta_{\pm}\tilde\Pi_{\mathrm{id},\pm}$, so they are right eigenprojectors, and the reconstruction is exact.

Each projector is a null element, and that is the whole point of the display. A pure state is a null element of the algebra, so the two pieces into which a massive momentum splits are lightlike. The momentum is not null; its two spectral components are. The mass is the product of the two eigenvalues, which are scalars, and the null set is not closed under addition: the sum of two null elements need not be null, and that is why a massive momentum can be written as a sum of two lightlike pieces.

The projectors lie in the informational sector while the momentum lies in the material one. Two statements are involved and only the second is specific to this element. First, there is no non-zero anti-Hermitian idempotent: if $\tilde\Pi_{\mathrm{id}}^{2}=\tilde\Pi_{\mathrm{id}}$ and $\tilde\Pi_{\mathrm{id}}^{*}=-\tilde\Pi_{\mathrm{id}}$, then $\tilde\Pi_{\mathrm{id}}^{*}=(\tilde\Pi_{\mathrm{id}}^{2})^{*}=\tilde\Pi_{\mathrm{id}}^{*}\tilde\Pi_{\mathrm{id}}^{*}=\tilde\Pi_{\mathrm{id}}$, so $\tilde\Pi_{\mathrm{id}}=0$. The projectors therefore cannot be material. Second, they are exactly the Hermitian ones, because the spectral projectors of a semisimple element are polynomials in it,

$$
\tilde\Pi_{\mathrm{id},\pm}=\frac{\tilde P_{\Phi}-\eta_\mp e_t}{\eta_{\pm}-\eta_\mp},
$$

and the interpolation of the two imaginary eigenvalues returns $\frac12(e_t\mp i\vec u_p)$. Non-Hermitian idempotents do exist in the algebra: for a real unit $\vec u$ and a null complex unit vector $\hat w$ orthogonal to it, $\tfrac12(e_t+i\vec u-\hat w)$ is idempotent and not Hermitian. They are simply not the spectral projectors of this element. The modes of a four-vector are therefore states, and the sector that carries the vector does not carry its own decomposition.

The spectral decomposition is the one operation of this entry that leaves the sector and re-enters it. The element is material, the projectors are informational, the eigenvalues are imaginary scalars, and the reconstruction is a sum of informational elements with imaginary coefficients whose result is material. That is the algebra's version of the statement that a mode decomposition is a change of description and not a change of object.

The eigenprojectors are also the idempotents of the Peirce decomposition of the momentum. The pair $\{\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-}\}$ is a complete set of orthogonal idempotents, so it defines a Peirce decomposition of the algebra relative to the momentum, with $\tilde P_{\Phi}$ acting as $\eta_{+}$ on the first Peirce space and $\eta_{-}$ on the second. The statement and its proofs are *The Biquaternion Eigenvalue Decomposition*; the entry uses only the pair and the two eigenvalues.

## The Seven Four-Vectors

The sector carries the standard four-vectors, and each one is a different invariant. The table is the dictionary. Every row has the same shape: an imaginary temporal component, a real spatial part, and a norm that names the physical quantity.

| four-vector | element | components | norm $N$ | reading of the norm |
| --- | --- | --- | --- | --- |
| four-position | $\tilde R=i r'_t e_t+\vec r$ | $(r'_t,r_x,r_y,r_z)$ | $-r_t'{}^{2}+\lvert\vec r\rvert^{2}$ | the squared interval |
| four-velocity | $\tilde V_{\Phi}=i\gamma c\,e_t+\gamma\vec v$ | $(\gamma c,\gamma\vec v)$ | $-c^{2}$ | the normalisation |
| four-momentum | $\tilde P_{\Phi}=i\frac{E}{c}e_t+\vec p$ | $(E/c,\vec p)$ | $-m^{2}c^{2}$ | the mass shell |
| four-wavevector | $\tilde\Upsilon_{\Phi}=i\frac{\omega}{c}e_t+2\pi\vec\nu_\Phi$ | $(\omega/c,\vec\nu_\Phi)$ | $0$ for light | the dispersion relation |
| four-potential | $\tilde A_{\Phi}=i a'_t e_t+\vec A$ | $(a'_t,\vec A)$ | representative-dependent | not an invariant |
| four-current | $\tilde J_{\Phi}=i c\rho\,e_t+\vec j$ | $(c\rho,\vec j)$ | not fixed | not an invariant |
| four-force | $\tilde{\mathcal F}_{\Phi}=i\frac{\gamma\vec f\cdot\vec v}{c}e_t+\gamma\vec f$ | $(\gamma\vec f\cdot\vec v/c,\gamma\vec f)$ | not fixed | orthogonality to $\tilde V_{\Phi}$ |

**Three of the seven have a fixed norm and four do not, and the difference is the physical content.** The position has its interval, the velocity has its normalisation, and the momentum has its mass shell; those three are level sets that the motion cannot leave. The wavevector's norm vanishes exactly for light, which is a constraint and not a level set. The potential, the current and the force have norms that depend on the configuration, and for those three the sector supplies the carrier and not the invariant.

The four-velocity's norm is a constant, and that is what makes it a normalised direction. $N(\tilde V_{\Phi})=-c^{2}$ for every velocity with $\lvert\vec v\rvert<c$, so the four-velocity is a point of the timelike hyperboloid of radius $c$ and the three-velocity is a coordinate on it.

The four-force is orthogonal to the four-velocity in the Minkowski pairing of §*The Bracket*. The identity of that section applies with $\tilde R_{\Phi,1}=\tilde{\mathcal F}_{\Phi}$ and $\tilde R_{\Phi,2}=\tilde V_{\Phi}$, and $\operatorname{Sc}(\tilde{\mathcal F}_{\Phi}\tilde V_{\Phi}^{\natural})$ is their Minkowski pairing. That scalar vanishes when the temporal component of the force is the power divided by $c$, which is the statement that such a force preserves the rest mass. A force whose temporal component is anything else has a non-zero pairing and changes $N(\tilde V_{\Phi})$: it changes the rest mass, and the algebra says so through the scalar part of an element of the algebra.

The four-potential's redundancy is a motion inside the sector. The transformation $\tilde A_{\Phi}\mapsto\tilde A_{\Phi}+\partial\xi$ adds to the potential an element of the sector that is the gradient of a scalar, and the norm of the sum is not the sum of the norms. The field strength, built from the antisymmetrised derivative, is the object whose components are the entries of a matrix in $\mathbb{B}_{\Phi}$ and whose norm is invariant. The entry does not derive the field equations; it records that the object whose norm is invariant exists in the sector and the potential does not have that property.

The four-current's norm is not fixed because a current is a density and not a state. The continuity equation $\operatorname{Sc}\bigl((\tilde\nabla_{\Phi})^{\natural}\tilde J_{\Phi}\bigr)=0$ is the statement that a divergence vanishes, and the divergence is the scalar part of a product of an informational operator with a material element. The current is a material four-vector whose scalar part is a charge density and whose vector part is a flux; the equation constrains the pair and not the norm.

The seven entries are one object in seven costumes, and the costume is the invariant. The entry states this because it is the summary of the section: the sector is not a list of physical quantities, it is the space in which each of them is a direction, and the invariant attached to the direction is what tells one from another.

## The Interpretations

### I.12.a — The Sector Is Spacetime, and the Interval Is Its Norm

Read: the sector definition, the basis $\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ and the norm of §*The Interval*.

The element $ir'_t e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ is an event. Its four coordinates are the coordinates of a point of flat spacetime, and its norm is the squared interval, negative for timelike, zero for null, positive for spacelike. The three cases are the three regions of the null set, and the null set is the boundary between them.

The interval is the norm itself and not the square of a separate norm. There is no additional quadratic form to introduce and no metric matrix to write down: the form is $N$, and the fact that $N$ has one negative direction is the fact that the sector has one imaginary coordinate. The Lorentzian sign pattern is the arithmetic of $i^{2}=-1$ placed on the temporal coefficient.

The proper time is the square root of minus the norm along a timelike path. A worldline is a path in the sector on which the norm is negative, its proper time is the integral of $\sqrt{-N(d\tilde R)}$, and the path is a light ray where the integrand vanishes. The definitions are the standard ones, and their content here is that they are read off the norm rather than assumed.

Boundary. The sector is a kinematic space. It carries events, intervals, directions and the transformations among them; it does not carry a metric field, a connection, curvature or a field equation. The identification with the spacetime of a physical theory is the corpus's reading, and the anti-Hermitian convention is a convention: the Hermitian sector gives the same geometry with the opposite sign.

### I.12.b — The Signs Are the Placement of the Imaginary Unit

Read: the coordinate form of the involution and the four sign readings of §*The Interval*.

The temporal coordinate is $ir'_t$ because the sector is the fixed space of the reversal. On that fixed space the coefficient of $e_t$ is imaginary and the other three are real. The minus sign of the Minkowski form is $(ir'_t)^{2}$, and it is the only place in the entry where a sign is produced rather than counted.

The two Hermitian halves are the two placements that give a Lorentzian form. On the quaternion layer the norm is positive definite. On the material half the temporal block is imaginary and the spatial block real, which gives $(3,1)$; on the informational half the roles are reversed, and there $N=a_0^{2}-\lvert\vec a\rvert^{2}$, which gives $(1,3)$. The two halves are exchanged by the central imaginary, and that exchange is also the exchange of the interval with minus itself. A mixed placement, imaginary on the temporal block and on one spatial coordinate, gives $(2,2)$ and is not a Lorentzian plane: the Lorentzian possibility is located rather than chosen, and there are exactly two placements that realise it.

The four sign readings over one sector are four readings of one placement. Reverse the sign of the temporal block and the interval becomes the negative interval; take absolute values and the Hermitian norm appears; take the difference in the other order and the K norm appears. Every one of them is a real form on the same four coordinates.

Boundary. The assignment is a property of the involution and not of the element. Which elements are timelike is a property of the element and the sector together, so a statement about the sign of the interval is always a statement about a pair.

### I.12.c — The Commutator Is Twice the Cross Product

Read: the coefficient computation and the closure display of §*The Bracket*.

Two four-vectors generate the rotation that carries one into the other, and the generator is the cross product of their space parts. The temporal coordinates do not enter. A four-vector is therefore a generator of spatial rotations with an energy label, and the label is invisible to the bracket.

The Lie algebra of the sector is $\mathfrak{su}(2)$ on a central line. The cross product is the bracket of the rotation algebra, the central line is the time direction, and the sum is $\mathfrak{u}(2)$. The derived algebra is the rotation algebra, so every bracket of brackets is a rotation and the time direction never appears again.

A boost is not in the sector's bracket, and that is a statement about the algebra and not about a choice of coordinates. The boost generators are the imaginary vectors, which are Hermitian and therefore informational. The Lie algebra of the Lorentz group is the direct sum of a material part and an informational part.

Boundary. The bracket is a Lie bracket and not a product. It generates transformations and does not compose objects; a reader who takes the cross product as a multiplication of four-vectors has left the sector.

### I.12.d — A Four-Vector Squared Is a State

Read: the anti-automorphism computation and the closure display of §*The Bracket*.

The product of two material elements is Hermitian exactly when the two commute. The square of one is therefore always informational, and a product of two distinct ones is informational never. A four-vector multiplied by a four-vector has left the sector by the first factor's own involution.

The anticommutator is always informational and its scalar part is the definite pairing. Its scalar part is minus twice the Euclidean pairing of the four coefficients, so the scalar part of half of it is minus that pairing, and its vector part is twice the symmetric temporal mixture. The Minkowski pairing is read from the same two elements one conjugation away, $\operatorname{Sc}(\tilde R_{\Phi,1}\tilde R_{\Phi,2}^{\natural})$, and it is a scalar part too, so both pairings are computed inside the algebra.

The Jordan and Lie structures are the two sectors. Symmetric products close on the informational half and antisymmetric products on the material half. The observables and the generators of a theory are the two halves here, and the split is the involution's and not a modelling decision.

Boundary. The reading names roles. It does not claim that every observable is a product of two four-vectors, and it does not claim that every state is one.

### I.12.e — The Modes of a Four-Vector Are in the Other Sector

Read: the eigenprojector display and the idempotent argument of §*The Spectrum of a Biquaternion*.

The two spectral projectors of a momentum are Hermitian idempotents, so they lie in the informational half. The momentum lies in the material half. The decomposition $\eta_{+}\tilde\Pi_{\mathrm{id},++}\eta_{-}\tilde\Pi_{\mathrm{id},-}$ therefore writes a material element as a combination of informational ones with imaginary coefficients.

An idempotent cannot be anti-Hermitian. If $\tilde\Pi_{\mathrm{id}}^{2}=\tilde\Pi_{\mathrm{id}}$ and $\tilde\Pi_{\mathrm{id}}^{*}=-\tilde\Pi_{\mathrm{id}}$, then $\tilde\Pi_{\mathrm{id}}^{*}=(\tilde\Pi_{\mathrm{id}}^{2})^{*}=\tilde\Pi_{\mathrm{id}}^{*}\tilde\Pi_{\mathrm{id}}^{*}=\tilde\Pi_{\mathrm{id}}$, hence $\tilde\Pi_{\mathrm{id}}=0$. There is therefore no material idempotent and no decomposition of a four-vector inside its own sector. The projectors that do occur are the Hermitian ones, obtained as the interpolation of the element at its two eigenvalues; the algebra also contains non-Hermitian idempotents, which are not the spectral projectors of anything in this entry.

The modes are null elements. A pure state is a null element, and the projectors of a massive momentum are pure states. The two pieces of a massive momentum are lightlike even though the momentum is not, which is why the mass can be a product of two lightlike eigenvalues while the momentum is timelike.

Boundary. The projectors are a basis of a two-dimensional complex space and not two particles. The reading does not double the particle content of a momentum.

### I.12.f — The Spectrum Is a Doppler Pair

Read: the eigenvalues, the rapidity and the ratio of §*The Spectrum of a Biquaternion*, and *The Spectral Reading of a Four-Vector*.

The two eigenvalues are imaginary and their quotients by $i$ are the two light-cone frequencies. For a massive momentum they are $mc\,e^{\pm\theta_{\mathrm{rpd}}}$, the rest frequency scaled by the two reciprocal Doppler factors of the momentum's own rapidity. The sum is twice the energy, the difference twice the momentum, the ratio the squared Doppler factor, and the product the mass squared.

Only the product is invariant. A boost rescales the two factors reciprocally and leaves the product alone. The two factors are therefore not two properties of the particle: they are one property read in two frames at once, and the invariant is the mass.

The frame dependence has a closed form, and that is why it is a reading and not a slogan. The rapidity is the parameter of the boost that would carry the momentum to its rest frame, and the pair is the orbit of $(mc,mc)$ under the rescaling that the boost induces.

Boundary. The pair needs a non-zero space part for its members to differ, and it needs a chosen branch for both to be non-negative. Neither condition is a property of the algebra.

### I.12.g — The Branch Is Declared and Not Derived

Read: the fifth claim of the introduction and the two degenerate cases of §*The Spectrum of a Biquaternion*.

**The statement that both frequencies are non-negative is the statement $E/c\ge\lvert\vec p\rvert$, and that is the choice of the future sheet.** The proper orthochronous group preserves the sign of the temporal component, so the choice is stable under every transformation the entry uses. It is nonetheless a choice: the past sheet gives the same pair with both signs reversed, and the two sheets are exchanged by a reflection and not by a boost.

Off the shell one of the two frequencies changes sign. A momentum with $E/c<\lvert\vec p\rvert$ is spacelike, its norm is positive, and the pair $E/c\pm\lvert\vec p\rvert$ has one negative member. The sign of a frequency is therefore a statement about the position of the momentum relative to the cone, and the declaration of a branch is the declaration that the momentum is inside the future cone.

The declaration is where a physical reading enters and where it can be checked. Every sentence of the entry that says *energy* rather than *temporal component* uses the branch. A reader who wants the branch-free statement has it: it is the pair of eigenvalues with their signs, and it holds on the whole sector.

Boundary. Branch selection is not derivable from the algebra and is not claimed to be. What the algebra supplies is that the two sheets are separate orbits, which is what makes the declaration consistent.

### I.12.h — The Interval Is Multiplicative, and Causal Character Composes

Read: the multiplicativity of $N$ and its consequence in §*The Interval*.

The norm is a determinant, so it is multiplicative on the whole algebra, and on the sector that fact has a reading. The product of two timelike elements is spacelike, the product of a timelike and a spacelike is timelike, and a null factor makes the product null. The composition of causal characters along a chain of elements is therefore a rule about signs.

The same rule does not hold for the K norm. The K form is not multiplicative, and the entry records the contrast because the two indefinite forms of the sector are negatives of each other and one of them composes while the other does not. The interval is the one to use when a product is taken; the K norm is the one to use when a weight is assigned.

The composition rule is why the interval is a law and the K value is a label. A quantity that is multiplicative survives a chain of transformations with a predictable sign; a quantity that is not multiplicative does not. Both are invariants of the isometry group on a single element; only one of them is an invariant of a product.

Boundary. The rule is about the algebra's product and not about the composition of velocities. A product of two four-vectors is not a four-vector, so the rule concerns the signs carried by a chain of elements.

### I.12.i — The Light Cone Is the Zero-Divisor Cone

Read: the inverse formula and the null-set display of §*The Interval*, and *The K Norm and the Indefinite Structure*, §*The Six Restrictions*.

A null four-vector has no inverse and annihilates a non-zero element. The first statement is the failure of $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$; the second is the definition of a zero divisor. The light cone of the sector is therefore the zero-divisor cone of the algebra, a structural identity rather than an additional assumption.

The apex is the one null point that is not a zero divisor. It annihilates nothing non-zero, and it is the only point where the geometric and the algebraic descriptions differ. The cone without the apex is a smooth three-manifold with two components; with the apex it is a single singular set.

A null momentum therefore has no rest frame, and the reason is algebraic. A rest frame would be a congruence carrying the momentum to a multiple of $ie_t$, and the orbit of a null element under the proper orthochronous group is the set of null elements of the same temporal sign and never contains a timelike one. The absence of a rest frame is the statement that the orbit does not meet the temporal axis.

Boundary. The identity is between two sets and not between two theories. It says that the set on which the interval vanishes is the set on which invertibility fails; it does not say that every zero divisor is a light ray in a physical spacetime.

### I.12.j — A Frame Is an Orbit and the Rotor Is Outside the Sector

Read: the action display, the kernel and the factorisation of §*The Lorentz Action*.

The group of invertibles acts on the sector by congruence, the kernel is $\{\pm e_t\}$, and the quotient is $SO^{+}(1,3)$. A frame is an orbit point of a four-vector, a change of frame is invertible acting by congruence, and the invariants are the orbit labels. The double cover is the statement that two units give the same frame.

Neither factor of a general unit need be in the sector. A rotation factor is material and a boost factor is informational, and a general unit is their product. The acting group is therefore larger than the acted-on space, and the sector is a representation space in the strict sense: a module for a group it does not contain.

This is the precise content of the phrase that the Lorentz group acts on spacetime. The group is not a subset of the space and not a product of its points; it is the group of congruences of the algebra that preserve the norm of the space. The algebra makes the statement literal, and it also explains why the complexification is needed: the six parameters of the group do not fit in the four dimensions of the sector.

Boundary. The action is linear and acts on a flat space. No local action, no bundle and no connection is constructed here, and the entry does not claim that a change of frame is a physical operation performed on an object.

### I.12.k — Seven Four-Vectors Are One Object in Seven Costumes

Read: the dictionary table of §*The Seven Four-Vectors*.

Every row of the table has an imaginary temporal component, a real space part, and a norm that names a physical quantity. The position, the velocity, the momentum, the wavevector, the potential, the current and the force are therefore one algebraic object read with seven invariants. The reading is what the sector is for.

Three rows have a fixed norm and four do not. The interval, the normalisation of the velocity and the mass shell are level sets; the dispersion of the wavevector is a constraint; the potential, the current and the force have norms that depend on the configuration. The difference is the difference between a kinematic constraint and a dynamical variable, and it is visible in the table as the difference between a constant entry and a blank one.

The orthogonality of the four-force to the four-velocity is read in the other sector. The pairing is a scalar part of a product, $\operatorname{Sc}(\tilde{\mathcal F}_{\Phi}\tilde V_{\Phi}^{\natural})$, so the statement that a force preserves the rest mass is the statement that a scalar part vanishes. The algebra puts the pairing where the physics needs it.

Boundary. The table is a dictionary and not a derivation. The field equations, the Lorentz force law and the wave equations are not results of the algebra; the algebra supplies the carrier space and the invariant for each entry.

### I.12.l — What the Sector Cannot Do

Read: the closures of §*The Bracket* together with the limits stated in each interpretation.

The sector cannot multiply, cannot decompose and cannot curve. Its product leaves it, its idempotents are in the other half, and its norm is a constant form rather than a field. Each of the three limitations is a theorem, and each of them marks a place where a physical theory must add something the algebra does not contain.

The sector also cannot distinguish a four-vector from its reading. The interval tells a timelike element from a null one, and nothing in the algebra says which of them is a particle, which is a potential and which is a force. The dictionary is an interpretation, and it is the interpretation's job to attach the names.

The three limitations are the useful part of the entry. A framework that claimed to derive dynamics from the sector would be claiming more than the algebra supports; a framework that claimed nothing would be a notation. What the algebra supports is the carrier, the invariant, the action and the spectral pair, and the entry has stated exactly those four.

Boundary. Everything in this entry that is not a computation is a reading. The computations are the anti-automorphism identity, the cross-product formula, the norm scaling, the eigenvalue pair and the projector identities, and each of them can be checked by hand or by machine.

## The Limits

The object is a real four-plane and the readings are readings of its quadratic form. The mathematical content is one real vector space of dimension four, two involutions that fix it and negate it, one real quadratic form with one negative direction, one bracket, and one group action. Everything the entry names — event, worldline, momentum, mass, frame — is a name for what those objects mean when a chart supplies a physical vocabulary.

No dynamics is supplied. The interval is a constant on the sector and says nothing about how a four-vector changes. A law that keeps a worldline inside the cone, one that crosses it, and one that does neither are all compatible with the interval. Conservation of the norm along a path is a constraint that a theory may impose; it is not implied here.

No field equation is supplied. The sector carries the four-potential and the four-current as elements, and it carries no operator that would annihilate them into an equation. The wave operator, the field strength and the connection belong to later entries of the category, and the entry refers to them and does not restate them.

No statistics is supplied. The spectral pair is a pair of complex numbers and not a pair of occupation numbers. Nothing here says whether the two modes are distinguishable, and no Fock space, no commutation relation and no spin-statistics connection is constructed.

No curved metric is supplied. The form is constant on the sector: the same four coordinates, the same signs at every point. A metric field would be a map from a base into the sector, and the entry has no base. The statement that the speed of light is local is a statement about a medium, and the entry says so where it makes it.

No particle content is supplied. The seven four-vectors are seven invariants of one algebra, and the entry does not say which of them are realised in nature. The dictionary is a dictionary: it says what an element would be if it were a four-momentum, not that some element is one.

No absolute scale is supplied. The norm is homogeneous of degree two, so every non-zero element has a one-parameter family of rescalings that stay on its level set. The choice of a level set on which to normalise is a separate act, and the mass shell is a choice of level rather than a consequence of the algebra.

The sector is a chart and the informational sector is the other chart. The identities $N=-\mathrm{Kr}$ and $H=-P$ are exact on this chart, and every reading here is a reading through them. A statement that holds on one chart and fails on the other is a statement about the chart, and the entry names the chart at each place.

**The formalism is standard and the placement is not.** Four-vectors, the Minkowski interval, the Lorentz action by a two-by-two matrix and the Doppler pair are classical. What this entry contributes is the placement: the sector as the material placement of the imaginary unit, the split of the Lorentz algebra into a material and an informational summand, the location of the eigenprojectors in the other half, and the identification of the light cone with the zero-divisor cone.

## Summary

| result | content |
| --- | --- |
| the sector | $\mathbb{B}_{\Phi}=\{\tilde Q^{*}=-\tilde Q\}$, basis $\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$, real dimension four |
| the blocks | $\mathbb{R}(ie_t)$ of dimension one, central; $k=\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ of dimension three |
| the interval | $N=-r_t'{}^{2}+\lvert\vec r\rvert^{2}$, real, three positives and one negative |
| the companions | $H=r_t'{}^{2}+\lvert\vec r\rvert^{2}$ positive definite; $P=-H$; $\mathrm{Kr}=-N$ |
| the inverse | $\tilde R^{-1}=\tilde R^{\natural}/N(\tilde R)$, defined off the cone |
| the closure | bracket in the sector, anticommutator in $\mathbb{B}_{\Psi}$, product in the sector only when the factors commute |
| the bracket | $[\tilde R_1,\tilde R_2]=2\vec r_1\times\vec r_2$; the sector is $\mathfrak{u}(2)$ |
| the Lorentz algebra | $\mathfrak{so}(1,3)=\mathfrak{su}(2)_{J}\oplus i\,\mathfrak{su}(2)_{K}$, $J$ material, $K$ informational |
| the action | $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$, sector preserved for every invertible $\tilde U$, norm scaled by $\lvert N(\tilde U)\rvert^{2}$ |
| the group | $\mathbb{B}^{\times}_{1}/\{\pm e_t\}\cong SO^{+}(1,3)$, $\mathbb{B}^{\times}_{1}\cong\mathrm{Spin}(1,3)$ |
| the factorisation | $\tilde U=\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, boost informational, rotation material |
| the spectrum | $\eta_{\pm}=i(E/c\pm\lvert\vec p\rvert)$; $f_{\mathrm{dop},\pm}=mc\,e^{\pm\theta_{\mathrm{rpd}}}$; $f_{\mathrm{dop},+}f_{\mathrm{dop},-}=m^{2}c^{2}$ |
| the projectors | $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\mp i\vec u_p)$, Hermitian idempotents, null elements, in $\mathbb{B}_{\Psi}$ |
| the degeneracies | $\vec p=0$: repeated eigenvalue; $E/c=\lvert\vec p\rvert$: null element, one zero eigenvalue |
| the null set | the zero-divisor cone, real dimension three, apex excluded from the divisors |
| the multiplicativity | $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, so causal character composes |

## Summary of Notation

| object | notation | content |
| --- | --- | --- |
| the element | $\tilde R_{\Phi}=i r'_t e_t+\vec r$ | imaginary temporal part, real spatial part |
| the reversal | $\tilde Q^{\flat}=-{}^{*}\tilde Q$ | the involution whose fixed space is the sector |
| the interval | $N(\tilde R_{\Phi})$ | $-r_t'{}^{2}+\lvert\vec r\rvert^{2}$, real |
| the Hermitian norm | $H(\tilde R_{\Phi})$ | $r_t'{}^{2}+\lvert\vec r\rvert^{2}$, positive |
| the K norm | $\mathrm{Kr}(\tilde R_{\Phi})$ | $r_t'{}^{2}-\lvert\vec r\rvert^{2}$, equal to $-N$ |
| the bracket | $[\tilde R_1,\tilde R_2]$ | $2\vec r_1\times\vec r_2$ |
| the definite pairing | $\operatorname{Sc}(\tilde R_{\Phi,1}\tilde R_{\Phi,2})$ | minus the Euclidean pairing of the coefficients |
| the Minkowski pairing | $\operatorname{Sc}(\tilde R_{\Phi,1}\tilde R_{\Phi,2}^{\natural})$ | $-r'_{1t}r'_{2t}+\vec r_1\cdot\vec r_2$ |
| the Lorentz rotor | $\tilde U$ | an invertible element, $N(\tilde U)=1$ |
| the boost factor | $\tilde U_{\Psi,\mathrm b}$ | $\cosh\tfrac{\theta}{2}+i\sinh\tfrac{\theta}{2}\vec u_{\mathrm b}$, Hermitian |
| the rotation factor | $\tilde u_{\mathrm r}$ | $\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\vec u_{\mathrm r}$, real |
| the rapidity | $\theta_{\mathrm{rpd}}$ | $\tanh\theta_{\mathrm{rpd}}=\lvert\vec p\rvert c/E$ |
| the eigenvalues | $\eta_{\pm}$ | $i(E/c\pm\lvert\vec p\rvert)$ |
| the frequencies | $f_{\mathrm{dop},\pm}$ | $\eta_{\pm}/i=mc\,e^{\pm\theta_{\mathrm{rpd}}}$ |
| the projectors | $\tilde\Pi_{\mathrm{id},\pm}$ | $\tfrac12(e_t\mp i\vec u_p)$, Hermitian idempotents |
| the four-velocity | $\tilde V_{\Phi}$ | $i\gamma c\,e_t+\gamma\vec v$, norm $-c^{2}$ |
| the four-momentum | $\tilde P_{\Phi}$ | $i\frac{E}{c}e_t+\vec p$, norm $-m^{2}c^{2}$ |
| the four-wavevector | $\tilde\Upsilon_{\Phi}$ | $i\frac{\omega}{c}e_t+\vec\nu_\Phi$, norm zero for light |
| the four-potential | $\tilde A_{\Phi}$ | $i a'_t e_t+\vec A$, representative-dependent norm |
| the four-current | $\tilde J_{\Phi}$ | $i c\rho\,e_t+\vec j$ |
| the four-force | $\tilde{\mathcal F}_{\Phi}$ | $i\frac{\gamma\vec f\cdot\vec v}{c}e_t+\gamma\vec f$ |

## Further Reading

The indefinite form. [The K Norm and the Indefinite Structure](the-k-norm-and-the-indefinite-structure.html) is the previous entry of the series, and its §*The Six Restrictions* is where the coincidence of the two null sets is proved.

The partition. [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html) places the momentum among the four sectors of the norm and the spectrum.

The group of invertibles. [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) reads the complement of the cone as the set of reversible processes.

The mathematics. [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) owns the double covers and the orbit classification, and [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) owns the norm, the invertibles and the cone.
