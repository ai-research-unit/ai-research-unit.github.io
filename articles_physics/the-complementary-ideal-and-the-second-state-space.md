# __The Complementary Ideal and the Second State Space__

## Introduction

The spinor space is one minimal left ideal, $S=\mathbb{B}\tilde\Pi_+$, and the plain product splits the algebra into two of them:

$$
\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-,\qquad
\tilde\Pi_-=e_t-\tilde\Pi_+=\tfrac12(e_t-i\vec e_z).
$$

The second summand, $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ with $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, is the **complementary ideal**. It is a left module, it is isomorphic to $S$, and it is a different subspace of the algebra. The article reads it as the **second state space**: a second copy of the same carrier, metrically identical, which an operator acting on the right can mix with the first.

The reading has three parts, and the article keeps them apart. The first is the **doubling**: the algebra offers two copies and not one. The second is the **mass**: the pair of right multiplications by the nilpotents $\vec\Upsilon_x$ and $\vec\Upsilon_y$ carries $S$ onto its complement and back, and the chirality-off-diagonal mass is that operation. The third is the **separation of the complements**: the module complement, the Hilbert complement and the algebra's-own-form complement are three different notions, and they coincide only under a condition on the idempotent.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The idempotents, the Peirce decomposition and the minimal left ideals | [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The module theory: the simple module, the regular module and its two summands | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The column ideals of a matrix ring and their one-idempotent-one-nilpotent bases | [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html) |
| The canonical Hermitian form and the positivity of the sesquilinear pairing | [The Canonical Hermitian Form on the Regular Module of the Biquaternioid Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternioid-algebra.html) |
| The four forms, the algebra's own bilinear form and the sectors | [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html) |
| The coefficient conjugation and the real structure of the algebra | [The Realification and the Effect of the Change of Scalars](../articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.html) |
| The roots of $+1$ and the non-Hermitian idempotents | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |

## The Second Column

The complement is a left ideal for the same reason $S$ is. The Peirce decomposition with respect to the pair $(\tilde\Pi_+,\tilde\Pi_-)$ cuts the algebra into four one-dimensional complex corners, and the second column is the sum of its diagonal and off-diagonal corners:

$$
\mathbb{B}\tilde\Pi_-=
\tilde\Pi_-\mathbb{B}\tilde\Pi_-\oplus\tilde\Pi_+\mathbb{B}\tilde\Pi_-
=\mathbb{C}\tilde\Pi_-\oplus\mathbb{C}\vec\Upsilon_x .
$$

In the matrix model $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ the four elements are the matrix units

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

## The Occupation Reading

The two columns have a second reading, in which they are the two levels of one mode. Writing the matrix units as occupation idempotents,

$$
\tilde\Pi_+=|0\rangle\langle0|,\qquad
\tilde\Pi_-=|1\rangle\langle1|,\qquad
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
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y,\qquad
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,
\qquad
(\mathbb{B}\tilde\Pi_-)\vec\Upsilon_y=S .
$$

The naive basis swap is **not** the map. The relabelling $\tilde\Pi_+\leftrightarrow\tilde\Pi_-$, $\vec\Upsilon_y\leftrightarrow\vec\Upsilon_x$ does not commute with the left action: $\tilde\Pi_-\tilde\Pi_+=0$ while $\tilde\Pi_-\tilde\Pi_-=\tilde\Pi_-$. The isomorphism must mix the two idempotents, and right multiplication by the nilpotent is exactly such a mixing.

> **The complement is reached by multiplying on the right by a nilpotent, not by relabelling the basis.**

Two properties of the map are worth naming. It is **$\mathbb{C}$-linear and $\mathbb{B}$-linear on the left**, so it preserves the module structure and the Lorentz action. It is **not invertible as an element of the algebra**, because $\vec\Upsilon_x^2=0$ and a nilpotent is not a unit; its inverse between the modules is the right multiplication by $\vec\Upsilon_y$, and the two maps compose to the identity on each side, $S\vec\Upsilon_x\vec\Upsilon_y=S$ and $(\mathbb{B}\tilde\Pi_-)\vec\Upsilon_y\vec\Upsilon_x=\mathbb{B}\tilde\Pi_-$. So the *element* is not invertible while the *map* is an isomorphism: the inverse is another right multiplication, not an inverse element.

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
S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\},
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

**The independence is sharper than the dimension count.** Multiplication by the central imaginary exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, so a complex subspace contained in one sector is zero; the two ideals are complex two-dimensional and can never be split along $\mathbb{M}_\pm$. The sector content of an ideal sits entirely on its **diagonal** corner: $\mathbb{C}\tilde\Pi_+\cap\mathbb{M}_+=\mathbb{R}\{\tilde\Pi_+\}$ and $\mathbb{C}\tilde\Pi_+\cap\mathbb{M}_-=\mathbb{R}\{i\tilde\Pi_+\}$, while the nilpotent line $\mathbb{C}\vec\Upsilon_y$ meets both sectors in $\{0\}$. The sector label therefore attaches to the idempotent and not to the ladder: the doubling is an **informational** doubling, two idempotents of $\mathbb{M}_+$, and not a material–informational pair.

The map that does carry $S$ onto the complement at the level of the ring is the **coefficient conjugation** $\bar{\cdot}$, which fixes the four basis elements and negates $i$:

$$
\overline{\tilde\Pi_+}=\tilde\Pi_-,\qquad
\overline{\vec\Upsilon_y}=-\vec\Upsilon_x,\qquad
\bar S=\mathbb{B}\tilde\Pi_- .
$$

It is anti-linear, it is a real structure, and it is not an operation of the plain product. The complement is therefore reached by two different maps: the $\mathbb{B}$-linear right multiplication by the nilpotent, and the anti-linear coefficient conjugation. The first is the module isomorphism; the second is the ring-level conjugation. They agree on the subspace and differ in what they preserve.

## The Second Vacuum

The choice of idempotent selects the module: $\tilde\Pi_+$ generates $S$, $\tilde\Pi_-$ generates the complement. The simple module is unique up to isomorphism, but the **idempotent** is not, and the complement is what the other choice of vacuum produces.

That is the exact sense in which the doubling is a choice of vacuum and not a new particle. The algebra gives two vacua and two copies; no algebraic fact prefers one. The preference, if there is one, is a dynamical input. The reading is the algebraic form of the statement that a two-component state space has two one-mode vacua, and that the mass is what mixes them.

## Physical Readings

- **The state space is doubled.** The interpretation is that the algebra offers two copies of the same state space, module-isomorphic and Hilbert-orthogonal, and that this doubling is the framework's two-component structure. Boundary: a counting statement; it adds no second particle.
- **The mass takes a state to its complement.** The interpretation is that the chirality-off-diagonal mass is the right multiplication by the nilpotent $\vec\Upsilon_x$, which carries $S$ onto $\mathbb{B}\tilde\Pi_-$ and flips the column. Boundary: the mechanism is algebraic; the mass value and the spectrum are not in the article.
- **The mass generator is null and off-diagonal.** The interpretation is that the coupling cannot be a left multiplication, because the left action preserves the ideals; its natural generator is the nilpotent matrix unit, so the generator is not a unit, while the map it induces is an isometry of the Hilbert structures. Boundary: a statement about the shape of the coupling, not about its strength; the isometry is between the two copies and not a unitary evolution in time.
- **The two ideals are the two levels of one mode.** The interpretation is that the columns are the empty and the occupied ideal of a single fermionic mode, and the nilpotents that exchange them are the raising and lowering operators. Boundary: the same pair of ideals reads as two chiralities and as two levels; the article does not choose, and the mass reading uses the column.
- **The second vacuum is the other idempotent.** The interpretation is that the two one-mode ideals are the two vacuum choices, and no algebraic fact selects one. Boundary: the module is unique; only the vacuum is a choice.
- **The module and Hilbert complements coincide.** The interpretation is that the decomposition into the two ideals is at once a module decomposition and an orthogonal decomposition of Hilbert spaces, and that this is why the doubling can be read as two copies of one state space. Boundary: the coincidence uses the Hermiticity of the vacuum idempotent; it fails for a general idempotent.
- **The algebra's own form does not see the split.** The interpretation is that $S^{\perp_B}$ is a third subspace, sharing only the idempotent, so the orthogonal reading of the doubling needs the metric and not the composition form. Boundary: a statement about the two forms, not a new decomposition.

## Limits

- **No mass value and no spectrum.** The article states the coupling's algebraic shape; the number is dynamical.
- **No choice between the interpretations of the doubling.** The second chirality, the occupation ladder and the conjugate state space are three readings of one algebraic fact, and the article does not choose among them.
- **The coincidence is conditional.** The module and Hilbert complements coincide for the Hermitian vacuum pair. For a general idempotent they separate.
- **One pair of ideals only.** The general idempotent $\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$ generates a minimal left ideal for every unit vector, and its complement is a different subspace. The article treats the coordinate pair.
- **Not the dual and not a sector.** The dual is the right ideal reached by ${}^{*}$; the sectors cut across both ideals and contain no nonzero idempotent in $\mathbb{M}_-$.
- **No dynamics.** Nothing here says how a state moves between the copies in time, or why the mass has the value it has.

## Summary

The complementary ideal is the second minimal left ideal $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$, the second column of the matrix model, with a basis of one idempotent and one nilpotent. It is a left module isomorphic to $S$ through right multiplication by $\vec\Upsilon_x$, which sends $\tilde\Pi_+\mapsto\vec\Upsilon_x$ and $\vec\Upsilon_y\mapsto\tilde\Pi_-$; the naive basis swap is not a module map. The algebra is the direct sum of the two ideals, and the sum is at once a module decomposition and, for the Hermitian vacuum pair, an orthogonal decomposition for the positive definite form.

The complement is read as the second state space. The mass coupling is the pair of right multiplications by the two nilpotents, off-diagonal and column-flipping; the natural generators are null, the induced maps are isometries, and the nilpotence is a choice of generator and not an invariant of the coupling. It gives the algebraic shape of the chirality-off-diagonal mass and not its value. Three complements must be kept apart: the module and Hilbert complements coincide, the algebra's-own-form complement $S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$ is a third subspace, and the coincidence of the first two is conditional on the Hermiticity of the vacuum idempotent. The complement is not the dual, not a second representation and not a sector.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$, $\tilde\Pi_-=e_t-\tilde\Pi_+$ | the vacuum idempotent and its Peirce complement |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the nilpotent matrix units $E_{12}$ and $E_{21}$ |
| $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\vec\Upsilon_y\}$ | the spinor space, first column |
| $\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\vec\Upsilon_x\}$ | the complementary ideal, second column |
| $\mathbb{B}=S\oplus\mathbb{B}\tilde\Pi_-$ | the Peirce (module) decomposition |
| $S\vec\Upsilon_x=\mathbb{B}\tilde\Pi_-$ | the module isomorphism, right multiplication |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ | the algebra's symmetric bilinear form |
| $S^{\perp_B}=\mathbb{C}\{\vec\Upsilon_y,\tilde\Pi_-\}$ | its orthogonal complement of $S$ |
| $\langle\cdot,\cdot\rangle_{*}=\operatorname{Sc}(\cdot\,\cdot^{*})$ | the positive definite Hilbert form |
| $S^{*}=\tilde\Pi_+\mathbb{B}$ | the dual, a right ideal, not the complement |
| $\bar{\cdot}$ | the coefficient conjugation, $\bar S=\mathbb{B}\tilde\Pi_-$ |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian sectors |

## Further Reading

- [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for the corners, the matrix units and the ideals.
- [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html), for the simple module and the regular module.
- [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](../articles_maths/the-column-ideals-of-a-matrix-ring.html), for the structural basis count.
- *The Complementary Space of the Spinor Space in the Biquaternion Algebra*, for the same algebra read at length.
- *The Complementary Space of the Spinor Space and Its Physical Meaning*, for the doubling, the mass and the three interpretations.
- *The Spinor Space as a Module and as a Hilbert Space*, for the two structures of the first copy.
- *The Biquaternion Vacuum as a Minimal Idempotent*, for the vacuum choice and the family of idempotents.
- *The Spectral Triple of the Biquaternion Algebra* and *Bosonization in Biquaternionic Form*, for the chirality conventions of the doubling.
