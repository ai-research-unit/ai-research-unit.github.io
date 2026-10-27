# __Spin and the Two State Spaces__

## Introduction

The spinor space of the biquaternion framework is the minimal left ideal

$$
S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\},
\qquad
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),
\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),
$$

of complex dimension two. The algebra acts on it by left multiplication, and the action carries the defining representation of the double cover of the Lorentz group. That is one structure. The same carrier also carries a positive definite Hermitian form and a Born pairing, and that is a second structure, belonging to a different product of the same algebra.

The algebra also offers a **second copy**. The plain product splits it into two minimal left ideals,

$$
\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-,
\qquad
\tilde\Pi_-=e_t-\tilde\Pi_+=\tfrac12(e_t-i\vec e_z),
$$

and the second summand, $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ with $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, is the complementary ideal. It is a left module isomorphic to $S$, metrically identical, and a different subspace. The mass coupling is the pair of right multiplications by the two nilpotents that carries $S$ onto its complement and back.

The article's thesis is that the structures are **not two views of one object**, and that the doubling is a copy and not a second particle. The module structure belongs to the plain bilinear product, the Hilbert structure to the plain sesquilinear product, and the complement to the right multiplication. The sharpest evidence for the separation is that the algebra's own bilinear form is degenerate on the carrier: its Gram matrix is $\operatorname{diag}(\tfrac12,0)$. The module has no norm of its own, and the metric is added by the second slot.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The plain product as the only associative unital law of the twelve, and left alternativity as its threshold | [The Biquaternion Algebra and Its Vector Spaces](../articles_maths/the-biquaternion-algebra-and-its-vector-spaces.html) |
| The idempotents, the Peirce decomposition, the minimal left ideals and the matrix units | [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](../articles_maths/ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html) |
| The module theory: the simple module, $\mathbb{B}\cong S\oplus S$ and $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$ | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The column ideal of a matrix ring: one idempotent and $n-1$ nilpotents | [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html) |
| The canonical Hermitian form on the regular module, its positivity and its Gram matrix | [The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.html) |
| The four forms of the twelve products, their Gram matrices and their signatures | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| The embedding of the algebra in $\operatorname{End}_{\mathbb{C}}(S)$ | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The roots of $+1$ and the non-Hermitian idempotents | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The spectral triple and the chirality conventions | [The Spectral Triple of the Biquaternion Algebra](the-spectral-triple-of-the-biquaternion-algebra.html) |

## The Carrier and Its Forced Basis

The two idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ are orthogonal and complete in the plain product, and the Peirce decomposition cuts the algebra into four one-dimensional complex corners:

$$
\tilde\Pi_+\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+,\quad
\tilde\Pi_+\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_x,\quad
\tilde\Pi_-\mathbb{B}\tilde\Pi_+=\mathbb{C}\vec\Upsilon_y,\quad
\tilde\Pi_-\mathbb{B}\tilde\Pi_-=\mathbb{C}\tilde\Pi_-.
$$

The spinor space is one column, the sum of a diagonal corner and an off-diagonal one:

$$
S=\tilde\Pi_+\mathbb{B}\tilde\Pi_+\oplus\tilde\Pi_-\mathbb{B}\tilde\Pi_+
=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y .
$$

The basis is therefore not a choice. A minimal left ideal is one column of the matrix model, and a column of a rank-two matrix algebra is one diagonal corner plus one off-diagonal corner. The diagonal corner contributes the idempotent $\tilde\Pi_+$; the off-diagonal corner contributes a nilpotent, $\vec\Upsilon_y$. Every element of an off-diagonal corner is square-zero, because $(fae)(fae)=fa(ef)ae=0$ for orthogonal idempotents $e,f$. In rank $n$ the same count gives one idempotent and $n-1$ nilpotents; the spinor space is the case $n=2$.

> **The basis of the spinor space is one idempotent and one nilpotent, and the nilpotency is structural.** It is not a property of the particular column, and it is not a choice of coordinates.

The physical reading of the basis is the first statement of the article. The idempotent is the **state** direction of the column, and the nilpotent is the **shift** direction, the off-diagonal element that raises or lowers the column index. The two directions are what a two-level carrier needs: one projection and one shift. The algebra supplies both, and it supplies them in that proportion.

## The Module Structure: Composition

The plain product makes $S$ a left $\mathbb{B}$-module. On the basis $(\tilde\Pi_+,\vec\Upsilon_y)$ the left multiplications by the four basis elements are

$$
L_{\tilde\Pi_+}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
L_{\tilde\Pi_-}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
L_{\vec\Upsilon_x}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L_{\vec\Upsilon_y}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

the matrices of $\mathsf M_2(\mathbb{C})$ in the model $\mathsf M_2(\vec e_k)=-i\sigma_k$. The module is literally the column space $\mathbb{C}^2$ on which the algebra acts by matrix multiplication.

Three module-theoretic facts carry the reading.

- **The module is simple and unique.** $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and finite-dimensional, so its modules are completely reducible and there is, up to isomorphism, exactly one simple module. By Schur's lemma $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$.
- **The algebra is the endomorphism algebra.** $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$, and the left regular module splits as $\mathbb{B}\cong S\oplus S$. The algebra is the algebra of all linear maps of the carrier, and the regular module is two copies of it.
- **The Lorentz action is the left action.** A unit-norm biquaternion $\tilde U$, $\tilde U\tilde U^{\natural}=e_t$, acts by $\psi\mapsto\tilde U\psi$, and the action is the defining representation of $SL(2,\mathbb{C})$.

The third fact is the physical content of the module structure. The action is faithful, and it does not descend to the Lorentz group: $-e_t$ acts as $-\mathrm{id}$ on $S$ while it acts trivially by conjugation on the four-vectors of $\mathbb{M}_-$. The double cover therefore appears on the module side and not on the four-vector side, and **spin-$\tfrac12$ is a module datum**. It is a property of how the algebra acts on the carrier, not of a form on the carrier.

One caution belongs here, because it is easy to state wrongly. **A single minimal left ideal is one chirality, not two.** The ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$ and carry the same defining representation. The two Weyl halves are $S$ and its conjugate module $\bar S$, which are non-isomorphic as complex representations. The doubling below treats the second ideal; this section treats one carrier and its two structures.

## The Probability Structure: the Second Slot

The second structure uses the plain sesquilinear product. Its scalar part is the Hermitian form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*}),
$$

which is positive definite on the algebra. Restricted to the carrier, its Gram matrix on the basis $(\tilde\Pi_+,\vec\Upsilon_y)$ is

$$
\boxed{\;G=\begin{pmatrix}\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{*} & \langle\tilde\Pi_+,\vec\Upsilon_y\rangle_{*}\\[2pt]\langle\vec\Upsilon_y,\tilde\Pi_+\rangle_{*} & \langle\vec\Upsilon_y,\vec\Upsilon_y\rangle_{*}\end{pmatrix}
=\tfrac12 I_2\;}.
$$

The carrier is therefore a two-dimensional Hilbert space with the standard metric, and the two basis spinors are orthogonal and of equal norm. The form is invariant under the unitary slice $\mathrm{U}(2)=\{\tilde U:\tilde U\tilde U^{*}=e_t\}$; inside $SL(2,\mathbb{C})$ the invariance is the compact subgroup $SU(2)$, and a generic phase $e^{i\theta}e_t$ is an isometry of the Hilbert structure that lies outside $SL(2,\mathbb{C})$. The Hilbert form is therefore invariant under a group that is not the Lorentz group, and the difference is exactly the phase. In module coordinates the same form is the spinor inner product $h(\psi,\phi)=\psi^{\dagger}\phi$. The **Born pairing** is the trace formula

$$
\operatorname{Tr}(\tilde\Pi\tilde H^{*})=2\operatorname{Sc}(\tilde\Pi\tilde H),
$$

which pairs a state idempotent with an observable. The normalisation $\langle\psi,\psi\rangle_{*}=1$ is a condition on the Hilbert structure alone.

The physical reading of the second structure is the one the informational sector has built. A **state** is a Hilbert vector, an **observable** is a Hermitian element, and the pairing is the probability. The ray, not the vector, is the state: $\psi$ and $e^{i\alpha}\psi$ define the same ray and the same probabilities, and the Hilbert form is blind to the phase.

The sharpest way to see that this is a second structure and not a second view is the behaviour of the **algebra's own form** on the same carrier. The symmetric bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)
$$

is non-degenerate on $\mathbb{B}$, of signature $(4,4)$ on the real space. On the carrier its Gram matrix is

$$
\boxed{\;B_S=\begin{pmatrix}\tfrac12&0\\0&0\end{pmatrix}\;},
$$

of rank one, with radical $\mathbb{C}\vec\Upsilon_y$. The nilpotent is orthogonal to both basis spinors and to every element of $S$: it has zero scalar part and squares to zero. **The algebra's own form cannot separate the two basis spinors and cannot produce a norm on the carrier.** Positivity is not a property of the plain product at all; it needs the second slot.

## The Second Column

The complement is a left ideal for the same reason $S$ is. The Peirce decomposition with respect to the pair $(\tilde\Pi_+,\tilde\Pi_-)$ cuts the algebra into four one-dimensional complex corners, and the second column is the sum of its diagonal and off-diagonal corners:

$$
\boxed{\;\mathbb{B}\tilde\Pi_-=
\tilde\Pi_-\mathbb{B}\tilde\Pi_-\oplus\tilde\Pi_+\mathbb{B}\tilde\Pi_-
=\mathbb{C}\tilde\Pi_-\oplus\mathbb{C}\vec\Upsilon_x\;}.
$$

In the matrix model $\mathsf M_2(\vec e_k)=-i\sigma_k$ the four elements are the matrix units

$$
\tilde\Pi_+\leftrightarrow E_{11},\quad
\vec\Upsilon_y\leftrightarrow E_{21},\quad
\vec\Upsilon_x\leftrightarrow E_{12},\quad
\tilde\Pi_-\leftrightarrow E_{22},
$$

so $S$ is the first column and $\mathbb{B}\tilde\Pi_-$ is the second. The basis of the complement is again one idempotent and one nilpotent, and the nilpotent is again structural: it is the off-diagonal corner.

The left action on the complement's own basis is the mirror of the action on $S$:

$$
L_{\tilde\Pi_+}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
L_{\tilde\Pi_-}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
L_{\vec\Upsilon_x}=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
L_{\vec\Upsilon_y}=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The pattern is the interchange $\tilde\Pi_+\leftrightarrow\tilde\Pi_-$ and $\vec\Upsilon_x\leftrightarrow\vec\Upsilon_y$, but that interchange is a statement about the two left actions and **not** a map between the modules. The next section supplies the actual map.

The two columns have a second reading, in which they are the two levels of one mode. Writing the matrix units as occupation idempotents,

$$
\tilde\Pi_+=|0\rangle\langle0|,\qquad
\tilde\Pi_-=|1\rangle_{*}\langle1|,\qquad
\vec\Upsilon_x=|0\rangle\langle1|,\qquad
\vec\Upsilon_y=|1\rangle\langle0|,
$$

the spinor space is the ideal of the level $|0\rangle$ and the complement is the ideal of the level $|1\rangle$. The nilpotents that exchange the two are the raising and lowering operators of the mode, and their nilpotency is the algebraic form of the statement that two raises erase the state. The **occupation reading** is that the doubling is the ground and the excited ideal, or the empty and the occupied ideal, of a single fermionic mode.

The reading is one of several and not a decision. The same map that reads as a chirality flip reads as a level shift, and the two vocabularies are different readings of one algebraic fact: the mass section uses the column, the occupation reading uses the level, and neither is derived from the other.

## The Isomorphism Is a Right Multiplication

The module isomorphism $S\to\mathbb{B}\tilde\Pi_-$ is right multiplication by the nilpotent:

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
\qquad
S\vec\Upsilon_x=\mathbb{C}\{\vec\Upsilon_x,\tilde\Pi_-\}=\mathbb{B}\tilde\Pi_- .
$$

It is a module map because it acts on the right and the algebra acts on the left: $\tilde Q(x\vec\Upsilon_x)=(\tilde Qx)\vec\Upsilon_x$. It is nonzero between simple modules of the same dimension, so it is an isomorphism. Symmetrically, right multiplication by $\vec\Upsilon_y$ returns:

$$
\boxed{\;\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y,\qquad
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
(\mathbb{B}\tilde\Pi_-)\vec\Upsilon_y=S\;}.
$$

The naive basis swap is **not** the map. The relabelling $\tilde\Pi_+\leftrightarrow\tilde\Pi_-$, $\vec\Upsilon_y\leftrightarrow\vec\Upsilon_x$ does not commute with the left action: $\tilde\Pi_-\tilde\Pi_+=0$ while $\tilde\Pi_-\tilde\Pi_-=\tilde\Pi_-$. The isomorphism must mix the two idempotents, and right multiplication by the nilpotent is exactly such a mixing.

> **The complement is reached by multiplying on the right by a nilpotent, not by relabelling the basis.**

Two properties of the map are worth naming. It is **$\mathbb{C}$-linear and $\mathbb{B}$-linear on the left**, so it preserves the module structure and the Lorentz action. It is **not invertible as an element of the algebra**, because $\vec\Upsilon_x^2=0$ and a nilpotent is not a unit; its inverse between the modules is the right multiplication by $\vec\Upsilon_y$, and the two maps compose to the identity on each side. So the *element* is not invertible while the *map* is an isomorphism: the inverse is another right multiplication, not an inverse element.

That asymmetry is the algebraic form of a physical statement. The complement is a copy, and the operation that reaches it is a nilpotent: a step whose generator squares to zero. The next section reads that step as the mass.

## The Mass Coupling

The corpus's chirality-off-diagonal mass is a right multiplication, and the pair of right multiplications by $\vec\Upsilon_x$ and $\vec\Upsilon_y$ moves a state from $S$ to its complement and back. The reading rests on three algebraic facts.

- **The mass is off-diagonal.** A coupling that is $\mathbb{B}$-linear on the left cannot be a left multiplication by an element of $\mathbb{B}$: the left action preserves each ideal, since the ideals are left ideals. Such a coupling is a right multiplication, and right multiplication is what the module theory supplies.
- **The generator is null, the map is an isometry.** The natural generator is the matrix unit $\vec\Upsilon_x$: it has vanishing norm and $\vec\Upsilon_x^2=0$, so it is not a unit of the algebra. The map it induces is nevertheless an isometry of the two Hilbert structures, because $\vec\Upsilon_x\vec\Upsilon_x^{*}=\tilde\Pi_+$ acts as the identity on $S$. The nilpotence is a property of the chosen generator and not of the map: the representatives that induce the same map differ by an element of $\operatorname{Ann}(S)=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$, and some of them are units. The inverse between the modules is the right multiplication by $\vec\Upsilon_y$.
- **The coupling flips the column.** It sends $\tilde\Pi_+\mapsto\vec\Upsilon_x$ and $\vec\Upsilon_y\mapsto\tilde\Pi_-$, so the column index changes. In the corpus's chirality-off-diagonal convention that column index is the chirality, and the mass term is a chirality flip. In the spectral-triple reading the same off-diagonal entry is the finite Dirac operator, odd under the chirality, and the two ideals are its two chiralities.

> **The mass is the right multiplication that takes a state to the other state space.**

The reading has a boundary that must be stated in the same breath. **The article gives the algebraic mechanism and no mass value and no mass spectrum.** The number belongs to the dynamical articles, where the mass is a parameter of the equation and not a property of the doubling. What the algebra supplies is the **shape** of the coupling: off-diagonal, column-flipping, generated by a nilpotent matrix unit. What it does not supply is its size.

A convention warning belongs here, because the corpus uses the word *chirality* in two ways. The two ideals are sometimes called the two chiralities, and the two Weyl halves are $S$ and its conjugate module $\bar S$. These are different objects. The ideals are isomorphic as modules; $S$ and $\bar S$ are not. The mass coupling of this section moves between the two **ideals**, and the chirality flip it performs is the column flip of the first convention. It is not the passage to the conjugate module.

## Three Complements

The word *complement* names three subspaces in this algebra, and only two of them coincide.

| complement | definition | subspace | dimension over $\mathbb{C}$ |
| --- | --- | --- | --- |
| module complement | the other Peirce summand | $\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ | $2$ |
| Hilbert complement | $S^{\perp}$ for the positive definite form $\langle\cdot,\cdot\rangle_{*}$ | $\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ | $2$ |
| $\langle\cdot,\cdot\rangle$-orthogonal complement | $S^{\perp_B}$ for the algebra's own form | $\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$ | $2$ |

The **module complement** is the second ideal. The **Hilbert complement** is the orthogonal complement for the sesquilinear form of the second slot, $S^{\perp}=\{v:\langle u,v\rangle_{*}=0\ \forall u\in S\}$, and it is computed on the matrix units: the four units are mutually orthogonal of norm $\tfrac12$, so the orthogonal complement of the first column is the second column. The coincidence is exact, and it is the algebraic core of the doubling:

$$
\mathbb{B}=S\oplus\mathbb{B}\tilde\Pi_-=S\perp\mathbb{B}\tilde\Pi_-,
$$

a direct sum of left modules and an orthogonal direct sum of Hilbert spaces at once.

The coincidence is not automatic. **It holds because $\tilde\Pi_+$ is Hermitian.** The Peirce complement of a Hermitian idempotent is Hermitian, so $\tilde\Pi_-$ is Hermitian, and the two columns are orthogonal for the positive definite form. For a general idempotent $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$, whose root $\tilde\Xi$ need not be Hermitian, the two summands are still complementary left modules, but the Hilbert complement need not coincide with the module complement: the cross pairing $\langle\tilde\Pi,e_t-\tilde\Pi\rangle_{*}$ can be nonzero. The identification of the two complements is therefore a property of the **vacuum pair**, not of the algebra's decomposition alone.

The **algebra's-own-form complement** is a third subspace. Because the symmetric form $\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ is degenerate on the carrier, with $B_S=\operatorname{diag}(\tfrac12,0)$ and radical $\mathbb{C}\vec\Upsilon_y$, the orthogonal complement of $S$ is

$$
\boxed{\;S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}\;},
$$

which shares the idempotent $\tilde\Pi_-$ with the module complement and differs in its nilpotent. Equivalently,

$$
\langle\vec\Upsilon_y,\vec\Upsilon_x\rangle=\tfrac12,
\qquad
S\cap S^{\perp_B}=\operatorname{rad}B_S=\mathbb{C}\vec\Upsilon_y,
\qquad
S+S^{\perp_B}=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y,\tilde\Pi_-\},
$$

a sum of dimension three. The nilpotent direction is exactly what the algebra's own form cannot see, and the module decomposition is not orthogonal for it.

> **The module and Hilbert complements coincide; the algebra's-own-form complement does not.**

The three-way table is the sharpest statement of the article about the word *complement*. The first two are the doubling the physics uses: two identical copies, module-isomorphic and metrically orthogonal. The third is a different subspace, and it is a warning that the algebra's bilinear form is not the metric.

## What the Complement Is Not

Three negative statements keep the reading exact.

- **It is not the dual.** The dual of $S$ is the right ideal $S^{*}=\tilde\Pi_+\mathbb{B}=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_x\}$, the first row of the matrix model, reached by the Hermitian conjugation ${}^{*}$. The complement is a left ideal reached by right multiplication. A bra is not an antiparticle.
- **It is not a second representation.** The complement is isomorphic to $S$, so it carries the same defining representation of the double cover. The two chiral halves, in the module sense, are $S$ and its conjugate module $\bar S$, which are non-isomorphic. The doubling is a **copy**, not a second representation.
- **It is not a second sector.** Each ideal meets each sector in exactly one real dimension: $S\cap\mathbb{M}_+=\mathbb{R}\{\tilde\Pi_+\}$, $S\cap\mathbb{M}_-=\mathbb{R}\{i\tilde\Pi_+\}$, and similarly for the complement. Neither ideal is material or informational, and the sector split cuts across both. There is, in particular, no nonzero idempotent in $\mathbb{M}_-$, so the complement cannot be the material sector.

The independence is sharper than the dimension count. Multiplication by the central imaginary exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, so a complex subspace contained in one sector is zero; the two ideals are complex two-dimensional and can never be split along $\mathbb{M}_\pm$. The sector content of an ideal sits entirely on its **diagonal** corner: $\mathbb{C}\tilde\Pi_+\cap\mathbb{M}_+=\mathbb{R}\{\tilde\Pi_+\}$ and $\mathbb{C}\tilde\Pi_+\cap\mathbb{M}_-=\mathbb{R}\{i\tilde\Pi_+\}$, while the nilpotent line $\mathbb{C}\vec\Upsilon_y$ meets both sectors in $\{0\}$. The sector label therefore attaches to the idempotent and not to the ladder: the doubling is an **informational** doubling, two idempotents of $\mathbb{M}_+$, and not a material–informational pair.

The map that does carry $S$ onto the complement at the level of the ring is the **coefficient conjugation** $\bar{\cdot}$, which fixes the four basis elements and negates $i$:

$$
\overline{\tilde\Pi_+}=\tilde\Pi_-,\qquad
\overline{\vec\Upsilon_y}=-\vec\Upsilon_x,\qquad
\bar S=\mathbb{B}\tilde\Pi_- .
$$

It is anti-linear, it is a real structure, and it is not an operation of the plain product. The complement is therefore reached by two different maps: the $\mathbb{B}$-linear right multiplication by the nilpotent, and the anti-linear coefficient conjugation. The first is the module isomorphism; the second is the ring-level conjugation. They agree on the subspace and differ in what they preserve.

## What the Structures Do Not Carry

Three separations keep the article honest.

- **No positivity.** The algebra's form is indefinite on the real space and degenerate on $S$. The module has no canonical normalised state.
- **No Born rule.** The probability pairing is the scalar part of the sesquilinear product, not of the plain product. It belongs to the second structure.
- **No pairing of the carrier by the product.** The sesquilinear products do not preserve $S$: they couple a state to a conjugate slot and land outside the ideal. A sesquilinear product pairs the space; it does not act on it.

A fourth separation is about the sectors. The carrier meets each of $\mathbb{M}_\pm$ in one real dimension, so **the spinor space is not a sector**, and its two structures are not the material–informational split. The sector split is a third structure, real and independent, and it cuts across the ideal.

The doubling adds its own separations:

- **No mass value and no spectrum.** The mass coupling is a shape; the number is dynamical.
- **No choice between the readings of the doubling.** The second chirality, the occupation ladder and the conjugate state space are readings of one algebraic fact.
- **The coincidence is conditional.** The module and Hilbert complements coincide for the Hermitian vacuum pair; for a general idempotent they separate.
- **One pair of ideals only.** The general idempotent $\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$ generates a minimal left ideal for every unit vector, and its complement is a different subspace. The article treats the coordinate pair.
- **No dynamics.** Nothing here says how a state moves between the copies in time, or why the mass has the value it has.

## The Two Structures Side by Side

| job | structure | the algebra's part | the physical carrier |
| --- | --- | --- | --- |
| composition | module | plain left multiplication | the Lorentz action and the double cover |
| probability | Hilbert space | the plain sesquilinear pairing | the norm, the normalisation and the Born rule |

The module structure makes the carrier an **arena**: the algebra is the algebra of operators and the carrier is what they act on. The Hilbert structure makes the arena a **probability space**: the form is what can be evaluated on a state and squared into a number. Neither structure alone gives the pair. A module without a form has no numbers; a form without an action has no observables.

The two structures separate the two physical data of a spinor.

- **The spin is a module datum.** The double cover acts faithfully on the module, $-e_t$ acts as $-\mathrm{id}$, and that is where spin-$\tfrac12$ lives.
- **The ray is a Hilbert datum.** The form is blind to the sign and to the phase, so the state is a ray and not a vector.
- **The vacuum is a module datum.** The choice of idempotent $\tilde\Pi_+$ selects the module, and the module is fixed only up to the equivalence of idempotents.
- **The normalisation is a Hilbert datum.** $\langle\psi,\psi\rangle_{*}=1$ is a condition on the form and makes the amplitudes into probabilities.

The state space is normalised by the metric and selected by the vacuum, and the two acts are of different kinds: one is a pairing, the other is a choice of generator. The two structures also meet the corpus's word **quantisation**. The insertion of the star into the second slot, the step from $\tilde Q_1\tilde Q_2$ to $\tilde Q_1\tilde Q_2^{*}$, is what turns the composition pairing into the probability pairing. Read on the carrier, the spinor space is **compositional before the step and probabilistic after it**. The step is not an added axiom; it is the choice of what to put in the second slot.

## Physical Readings

- **One carrier, two structures, two jobs.** The state space is not one structure but two: the composition structure that makes the algebra act, and the probability structure that makes the states pair. Boundary: a statement about the algebraic structures, and it adds no identity between composition and probability.
- **The module is composition.** The plain product composes two elements, and the module is that composition read with one factor held fixed. Boundary: an interpretation of the algebra's law, not a dynamics.
- **The spin is a module datum, the ray is a Hilbert datum.** The double cover acts faithfully on the module, while the Hilbert structure is blind to the phase and yields the ray. Boundary: a separation of two known facts by the two structures.
- **The observables are module endomorphisms.** $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$, so the observables are the endomorphisms of the carrier and the trace formula is the pairing of the two structures. Boundary: the identification of the spinor and the qubit is not made.
- **The carrier has no norm of its own.** The algebra's form is degenerate on $S$, so an unnormalised spinor is what the module gives, and normalisation is added by the metric. Boundary: a statement about the two forms.
- **The Born rule is a product, not a postulate.** The probability pairing is the scalar part of the plain sesquilinear product, so positivity is the definiteness of a form and the trace formula is the scalar pairing. Boundary: the derivation and its bounds are *The Born Rule from the Hermitian Form*.
- **The spinor and the qubit are one carrier read twice.** The Weyl spinor of the Lorentz action and the two-level state of the informational sector inhabit one complex plane, once as the defining module and once as the Hilbert space. Boundary: the carrier is one; the physics of the two readings is not thereby identified.
- **Quantisation is the second slot.** The step from the plain product to the plain sesquilinear product is exactly the step from the module structure to the Hilbert structure. Boundary: the algebra supplies the pairing and no equation of motion and no measure.
- **The state space is doubled.** The algebra offers two copies of the same state space, module-isomorphic and Hilbert-orthogonal. Boundary: a counting statement; it adds no second particle.
- **The mass takes a state to its complement.** The chirality-off-diagonal mass is the right multiplication by the nilpotent $\vec\Upsilon_x$, which carries $S$ onto $\mathbb{B}\tilde\Pi_-$ and flips the column. Boundary: the mechanism is algebraic; the mass value and the spectrum are not in the article.
- **The mass generator is null and off-diagonal.** The coupling cannot be a left multiplication, because the left action preserves the ideals; its natural generator is the nilpotent matrix unit, so the generator is not a unit, while the map it induces is an isometry. Boundary: a statement about the shape of the coupling, not its strength.
- **The two ideals are the two levels of one mode.** The columns are the empty and the occupied ideal of a single fermionic mode, and the nilpotents that exchange them are the raising and lowering operators. Boundary: the same pair reads as two chiralities and as two levels; the article does not choose.
- **The second vacuum is the other idempotent.** The two one-mode ideals are the two vacuum choices, and no algebraic fact selects one. Boundary: the module is unique; only the vacuum is a choice.
- **The module and Hilbert complements coincide.** The decomposition into the two ideals is at once a module decomposition and an orthogonal decomposition of Hilbert spaces. Boundary: the coincidence uses the Hermiticity of the vacuum idempotent; it fails for a general idempotent.
- **The algebra's own form does not see the split.** $S^{\perp_B}$ is a third subspace, sharing only the idempotent, so the orthogonal reading of the doubling needs the metric and not the composition form. Boundary: a statement about the two forms.

## Limits

- **No measurement postulate and no Born derivation.** The Born rule is cited from its owner; the article states where it sits among the structures.
- **No identification of the two physics.** The carrier is one, but the spinor index is not identified with the qubit's two levels.
- **No mass value and no spectrum.** The article states the coupling's algebraic shape; the number is dynamical.
- **No choice between the interpretations of the doubling.** The second chirality, the occupation ladder and the conjugate state space are three readings of one algebraic fact.
- **The coincidence is conditional.** The module and Hilbert complements coincide for the Hermitian vacuum pair. For a general idempotent they separate.
- **One pair of ideals only.** The general idempotent generates a minimal left ideal for every unit vector, and its complement is a different subspace.
- **Not the dual and not a sector.** The dual is the right ideal reached by ${}^{*}$; the sectors cut across both ideals.
- **The algebra's form is not the metric.** It is indefinite and degenerate on $S$; the positive definite form is $\langle\cdot,\cdot\rangle_{*}$.
- **One ideal is one chirality.** The two ideals are isomorphic; the two Weyl halves are $S$ and $\bar S$.
- **No dynamics.** Nothing here says how a state moves between the copies in time, or why the mass has the value it has.

## Summary

The spinor space $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ is a minimal left ideal of the plain algebra, with a forced basis of one idempotent and one nilpotent. As a module it is the unique simple module, with $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$, $\mathbb{B}\cong S\oplus S$ and $\mathbb{B}\cong\operatorname{End}_{\mathbb{C}}(S)$; the left action is the defining representation of the double cover, and $-e_t$ acts as $-\mathrm{id}$, which is where spin-$\tfrac12$ lives.

The same carrier carries a second structure from the plain sesquilinear product: a positive definite Hermitian form of Gram matrix $\tfrac12 I_2$, the Born pairing and the normalisation. The two structures do not coincide: the algebra's own bilinear form is degenerate on the carrier, $\operatorname{diag}(\tfrac12,0)$, with radical the nilpotent line. The module is composition and the Hilbert space is probability; the spin is a module datum and the ray a Hilbert datum; the vacuum is a module choice and the normalisation a metric condition.

The algebra also splits into two minimal left ideals, the second column $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$, module-isomorphic to $S$ through right multiplication by $\vec\Upsilon_x$ and Hilbert-orthogonal to it. The mass coupling is the pair of right multiplications by the two nilpotents, off-diagonal and column-flipping; the natural generators are null, the induced maps are isometries, and the nilpotence is a choice of generator and not an invariant. The complement is not the dual, not a second representation and not a sector. Three complements must be kept apart: the module and Hilbert complements coincide, the algebra's-own-form complement $S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$ is a third subspace, and the coincidence of the first two is conditional on the Hermiticity of the vacuum idempotent.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$, $\tilde\Pi_-=e_t-\tilde\Pi_+$ | the vacuum idempotent and its Peirce complement |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the nilpotent matrix units $E_{12}$ and $E_{21}$ |
| $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ | the spinor space, first column |
| $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ | the complementary ideal, second column |
| $\mathbb{B}=S\oplus\mathbb{B}\tilde\Pi_-$ | the Peirce (module) decomposition |
| $S\vec\Upsilon_x=\mathbb{B}\tilde\Pi_-$ | the module isomorphism, right multiplication |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hilbert form of the second slot |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ | the algebra's own bilinear form |
| $B_S=\operatorname{diag}(\tfrac12,0)$ | the restriction of the algebra's form to $S$ |
| $S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$ | its orthogonal complement of $S$ |
| $S^{*}=\tilde\Pi_+\mathbb{B}$ | the dual, a right ideal, not the complement |
| $\bar{\cdot}$ | the coefficient conjugation, $\bar S=\mathbb{B}\tilde\Pi_-$ |

## Further Reading

- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](../articles_maths/ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the corners, the matrix units and the minimal ideals.
- [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html), for simplicity, the endomorphism ring and the regular module.
- [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html), for the structural count of the basis.
- [The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.html), for the positive definite form and its Gram matrix.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the probability structure.
- [The Born Rule from the Hermitian Form — Derivation and Comparison](the-born-rule-as-a-trace-formula-derivation-and-comparison.html), for the derivation and its bounds.
- [The Biquaternion Vacuum as a Minimal Idempotent](the-biquaternion-vacuum-as-a-minimal-idempotent.html), for the vacuum choice and the family of idempotents.
- [The Spectral Triple of the Biquaternion Algebra](the-spectral-triple-of-the-biquaternion-algebra.html), for the chirality conventions of the doubling.
