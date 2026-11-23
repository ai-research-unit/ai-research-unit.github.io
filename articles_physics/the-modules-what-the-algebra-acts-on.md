# __The Modules: What the Algebra Acts On__

## Introduction

This entry reads the fourth section of the mathematical category: the module structure of the algebra, that is, the algebra acting on a space rather than on itself. Five mathematics articles establish it.

The section changes the question. The first three sections ask what an element is, what its matrix image is, and how one element cuts the algebra. This one asks what the algebra *does*: it fixes a space, lets every element act on it by left multiplication, and classifies the spaces on which that action can live.



$$
\text{one simple module }S\text{ of complex dimension }2,\qquad \text{every module }M\cong S^{\oplus k}.
$$

The carrier of the action is the algebra itself. It is four complex dimensions, eight real, and it is not irreducible: it is the direct sum of two copies of $S$. So the algebra acts on a space that splits in many ways and canonically in none, and the entire section is the bookkeeping of that fact.

The single idea is that a splitting of the carrier is a choice and not a structure. The algebra prefers no splitting; a frame may display one, and a display that shows a splitting for free is showing a property of that frame. Everything the section proves is a separation of what the module carries from what a description of the module adds.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| ideals, the two-sided ideals, Artinian and semisimple, length two, the radical, the three regular modules, the submodules are the ideals, the endomorphisms of the regular object | [The Regular Module](../articles_maths/the-regular-module-in-the-biquaternion-algebra.html) |
| the two minimal left ideals, all minimal left ideals, the simple module, the two spinor spaces, the canonical splitting, the ladder, the gauge, the invariants of a single spinor, the Peirce index, right multiplication, what the spinor is not | [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html) |
| the root and the frame, the display polarizes for free, what the display is not | [The Pauli Module of the Biquaternion Algebra](../articles_maths/the-pauli-module-of-the-biquaternion-algebra.html) |
| representations and modules, the category of left modules, projectivity and the parity of freeness, the standard bimodule, Morita equivalence, torsion, real structures, the lattice of left ideals, the projective line and the Möbius action | [The Category of Modules](../articles_maths/the-category-of-modules-in-the-biquaternion-algebra.html) |
| the module and the two actions, the names of the elements, a splitting is a pair of points, the polarizations of the corpus, the axis-free frame, the swap, what the module carries instead, the conjugate pair, what the absence costs | [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html) |

The regular module first, because it names the carrier; then the polarized module, which fixes one splitting and develops it; then the Pauli module, which is the frame that displays a splitting silently; then the unpolarized module, which proves that no splitting is canonical; then the category of modules, which classifies the carriers.

## The Results in Brief

### The Regular Module

The algebra is a module over itself, and the submodules are the ideals.

$$
{}_{\mathbb{B}}\mathbb{B}\ :\ \mathbb{B}\times\mathbb{B}\to\mathbb{B},\qquad (\tilde Q_1,\tilde Q_2)\mapsto\tilde Q_1\tilde Q_2 .
$$

The module axioms are the ring axioms. Distributivity, associativity and the unit law are needed by the module and are already supplied by the algebra, so the regular module costs nothing new.



| property | value |
| --- | --- |
| Artinian | yes, the complex dimension is finite |
| semisimple | yes, the radical is $0$ |
| simple | yes, the two-sided ideals are $0$ and $\mathbb{B}$ |
| length as a left module over itself | $2$ |

Every left ideal is $0$, a minimal left ideal, or the algebra; every nonzero proper left ideal is minimal, of real dimension four; every minimal left ideal is also maximal.

The endomorphisms of the regular module are the algebra. Left multiplications give $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B}$, and the bimodule endomorphisms are the centre, $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong\mathbb{C}e_t$.

### The Submodules Are the Ideals

Left submodules are left ideals, right submodules are right ideals, and sub-bimodules are two-sided ideals. The identity map on subsets is an isomorphism of lattices, preserving inclusion, intersection and sum.

Simplicity therefore says two things at once. As an algebra, $\mathbb{B}$ has no proper nonzero two-sided ideal; as a bimodule, it has no proper nonzero sub-bimodule. The two statements are one statement.

The base field does not matter. An additive subgroup closed under left multiplication is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $ie_t$. So the ideal lattice is the same over $\mathbb{R}$ and over $\mathbb{C}$.

The annihilator of a zero divisor is a computed object. For a nonzero nilpotent $\vec P$ the ideal generated and the annihilator coincide, $\mathbb{B}\vec P=I_{\vec P}$; for every other zero divisor the two are distinct and complementary,

$$
\mathbb{B}=\mathbb{B}\tilde Q\oplus I_{\tilde Q}=\tilde Q\mathbb{B}\oplus J_{\tilde Q}.
$$

### The Simple Module and Its Copies

**There is exactly one simple module up to isomorphism, and it is two complex dimensions.**

$$
S=\mathbb{B}\tilde\Pi_{\mathrm{id},+}\cong\mathbb{C}^2,\qquad \operatorname{End}_{\mathbb{B}}(S)=\mathbb{C},\qquad \dim_{\mathbb{C}}S=2 .
$$



$$
M\cong S^{\oplus k},\qquad \dim_{\mathbb{C}}M=2k,\qquad {}_{\mathbb{B}}\mathbb{B}\cong S\oplus S .
$$

Every module is projective, and freeness has a parity. The module $S^{\oplus k}$ is free exactly when $k$ is even, that is, when $2k$ is divisible by four.

$$
S^{\oplus k}\ \text{free}\iff 2\mid k\iff 4\mid\dim_{\mathbb{C}}S^{\oplus k} .
$$

So $S$ itself is projective and not free: a two-dimensional complex module with no basis over the algebra.

The same parity is the obstruction to a real structure. A module descends to a quaternionic module exactly when it is free,

$$
W\ \text{admits a real structure}\iff W\ \text{is a free }\mathbb{B}\text{-module},
$$

and the minimal counterexample is again $S$.



$$
\operatorname{Hom}_{\mathbb{B}}(S,-):\operatorname{Mod}(\mathbb{B})\longrightarrow\operatorname{Mod}(\mathbb{C}),\qquad \dim_{\mathbb{C}}\bigl(S\otimes_{\mathbb{C}}W\bigr)=2\dim_{\mathbb{C}}W .
$$

The module theory of the algebra is the linear algebra of the complex field, with every dimension doubled, and the algebra is recovered as $\operatorname{End}_{\mathbb{C}}(S)$.

### The Polarized Module

With $\tilde\Pi_{\mathrm{id},\pm}$ a complete orthogonal pair of primitive idempotents, the two spinor spaces are

$$
S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+},\qquad S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-},\qquad \mathbb{B}=S_+\oplus S_-,\qquad \dim_{\mathbb{C}}S_\pm=2 .
$$

Each spinor space splits canonically into a diagonal line and a mixed line.

$$
S_+=\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{B}_{-+},\qquad S_-=\mathbb{B}_{+-}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-},
$$

so every positive spinor has a unique intrinsic form

$$
\psi_+=a\tilde\Pi_{\mathrm{id},++}\nu_+,\qquad a\in\mathbb{C},\quad \nu_+\in\mathbb{B}_{-+},
$$

and every negative spinor the mirror form $\psi_-=\nu_-+d\tilde\Pi_{\mathrm{id},-}$. The coefficient $a$ is the diagonal part and $\nu_+$ is the nilpotent part; both are intrinsic, and the coordinate $c$ of $\nu_+$ in a chosen basis is not.

The ladder has two rungs.

$$
\vec\Pi_{\mathrm{nil},+-}\psi_+=c\,\tilde\Pi_{\mathrm{id},+},\qquad \vec\Pi_{\mathrm{nil},-+}\psi_+=a\,\vec\Pi_{\mathrm{nil},-+},
$$

so left multiplication by one nilpotent keeps the mixed part and kills the diagonal part, and the other does the reverse. Both maps are square-zero, and the two composites are the projections onto the two lines.

The gauge acts on the coordinates and not on the element.

$$
a'=a,\qquad c'=t^{-1}c,\qquad b'=tb,\qquad d'=d,\qquad t\in\mathbb{C}^{\times}.
$$

The diagonal coefficients are invariant and the mixed ones carry reciprocal factors. The Hermitian norm, when the family is Hermitian and $|t|=1$, is

$$
\operatorname{Sc}(\psi_+\psi_+^{*})=\tfrac12\bigl(|a|^{2}+|c|^{2}\bigr).
$$

Right multiplication is the other action, and it does not respect the split. Right multiplication by $\tilde Q$ preserves $S_+$ exactly when $\tilde\Pi_{\mathrm{id},+}\tilde Q\tilde\Pi_{\mathrm{id},-}=0$; the two mixed units exchange $S_+$ and $S_-$, each being square-zero and the two being inverse to one another.

**The star does not exchange the two spinor spaces.** If the family is Hermitian then $S_+^{*}=\tilde\Pi_{\mathrm{id},+}\mathbb{B}$, the right Peirce row, which is not $S_-$. Chirality belongs to the left grouping; the star groups by the right index.

### The Pauli Module



$$
\vec Z=i\vec e_z,\qquad L_{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q).
$$

The carrier arrives already split. The matrix acts on the second tensor factor only, so $V=(\mathbb{C}e_1\otimes\mathbb{C}^2)\oplus(\mathbb{C}e_2\otimes\mathbb{C}^2)$ is a splitting that no left multiplication can see.

**That invisibility is the source of the illusion.** A splitting invisible to the action looks like a property of the algebra. It is a property of the display: the first tensor factor is the Peirce index of the root $\vec Z=i\vec e_z$.

The two slots are copies and not chiralities. The two summands are $S_+$ and $S_-$, both copies of $S$. Chirality is the pair graded by the basis operator

$$
\mathsf V_{\mathrm{vol}}=-iR_{\vec e_z},\qquad (\mathsf V_{\mathrm{vol}})^{2}=I_4,
$$

whose eigenspaces are $S$ and $S^{\mathrm{c}}$, and those two are not isomorphic over $\mathbb{R}$.

Replace $\vec e_z$ by a general real unit $\vec n$ and read the statement again. A statement about the Peirce index survives with $\vec n$ in place of $\vec e_z$; a statement about chirality does not change at all, because the grading is built from a right multiplier and anticommutes with the frame.

### The Unpolarized Module



$$
V=\mathbb{B},\qquad L(\tilde Q)\tilde X=\tilde Q\tilde X,\qquad R(\tilde Q)\tilde X=\tilde X\tilde Q .
$$

The right action is the commutant of the left one, and it is all of it. The double centraliser makes the regular module a faithful bimodule, with $\operatorname{End}_{\mathbb{B}}(V)=R(\mathbb{B})$.

The rank-one idempotents are

$$
\Pi_u=\tfrac12\bigl(e_t+i\,u\cdot\vec e\,\bigr),\qquad u\in\mathbb{C}^{3},\quad u\cdot u=1,
$$

a complex surface, and the ideal $\mathbb{B}\Pi_u$ depends only on the kernel line of $\Pi_u$. Two idempotents with distinct kernels give complementary ideals, so a splitting is an unordered pair of distinct points of $\mathbb{P}^{1}$.

**No splitting is canonical.** The automorphisms of the module are the right multiplications by invertibles, and they move the pairs of points transitively. The Peirce pair and the tensor split of the Pauli display are the same splitting, written twice.

The module carries a form and a swap instead.

$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y),\qquad \operatorname{Gram}=\operatorname{diag}(1,-1,-1,-1),\qquad \sigma(L_aR_b)=L_bR_a .
$$

The form is symmetric, non-degenerate and indefinite, and it splits the endomorphism algebra as $\operatorname{Sym}^{2}V\oplus\Lambda^{2}V$, of dimensions $10+6$. The swap is an involution, an anti-automorphism, and it is the only canonical operation that refers to the two sides without choosing one.

The conjugate pair is not a splitting of this module. The conjugate module $S^{\mathrm{c}}$ is a module for the conjugate algebra, and over $\mathbb{C}$ it is isomorphic to $S$. The grading that separates $S$ from $S^{\mathrm{c}}$ is not an element of the algebra: the central sign $\chi$ satisfies $\chi^2=e_t$, is central, and lies outside $\mathbb{B}$.

### The Category of Modules



$$
0\ \subset\ \{\text{minimal left ideals}\}\ \subset\ \mathbb{B},
$$

the middle layer being a projective line of pairwise incomparable ideals, each minimal and maximal.

**The parameter is the kernel line, not the image line.** The left ideals are indexed by $\ker\tilde\Pi_{\mathrm{id}}$ and the right ideals by $\operatorname{im}\tilde\Pi_{\mathrm{id}}$, and applying the image criterion to the left family is the standard error.

The invertibles act on the line by Möbius transformations.

$$
\tilde Q\cdot[\zeta]=[P\zeta],\qquad z'=\frac{az+b}{cz+d},\qquad \mathbb{B}^{\times}/\mathbb{C}^{\times}e_t\cong PGL_2(\mathbb{C})\cong\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}).
$$

The action is transitive, and simply transitive on ordered triples of distinct points. In the chart of the standard family, $\tilde\Pi_{\mathrm{id},+}$ sits at $z=0$ and $\tilde\Pi_{\mathrm{id},-}$ at $z=\infty$, and the stabiliser of a point is a Borel subgroup of complex dimension two.

Coefficient conjugation has no fixed point on the family. It acts by $t\mapsto-1/\bar t$, which has no fixed point, so no minimal left ideal is stable under the real structure; on the real subfamily $\mathbb{P}^{1}(\mathbb{R})$ it acts as the antipodal map.

## The Interpretations

### I.4.a — There Is No Hilbert Space Outside the Algebra

Read: the carrier of the action is the algebra. A field is an element, an operator is an element, and the space they live in is the set of elements.

This is not a stylistic choice and it has a price. In the standard formulation a state is a vector in a Hilbert space and an observable is an operator on that space; the two objects belong to different types, and the space is external to the algebra of observables. Here the algebra acts on itself by left multiplication, so the carrier and the algebra are one set with two structures on it: the algebra structure, which supplies the product, and the module structure, which supplies the action.

The archive states the consequence and this entry gives the reason. A spinor is not a vector in an external space; its coordinates are the Peirce coordinates in an adapted basis, and when a Hermitian form is used, that form is a form on the algebra. The reason is module-theoretic: the regular module is faithful, so every element of the algebra is a distinct operator on the carrier, and every element of the carrier is a vector on which the algebra acts. There is nowhere else for either to live.

Fock space, the multi-particle space and the infinite-dimensional Hilbert space of a quantum field are not this carrier. The regular module is finite and eight-real-dimensional. An entry that needs infinitely many modes needs an infinite direct sum of copies of the carrier, and that construction is not in this section.

### I.4.b — Two Copies of One Module Is Not One Object in Two Halves

Read: the regular module is $S\oplus S$, and the two summands are copies of one simple module. There is one isomorphism type, with multiplicity two.

This is the exact content of the "two components" of the spinor folklore. An element of the four-dimensional carrier is two vectors of a two-dimensional space, and the doubled structure is a multiplicity and not an internal decomposition. The module $S$ is simple, so a single copy has no invariant subspace and no internal parts at all; the only structure a two-component object can have is the structure of a basis of $S$.

Why the count two appears everywhere. Trace doubles, determinant squares, the spectrum repeats, and the semisimple length is two — those are the phenomena of I.2, and this is their module-theoretic source. A multiplicity-two module has twice the dimension and one isomorphism type.

The physical reading is a degeneracy and not a symmetry. Two copies of the same module can be exchanged by an isomorphism, so nothing in the module forbids the exchange; but the exchange is not an automorphism of the algebra and it changes no physics. The multiplicity is bookkeeping, and the multiplicity of the regular module is exactly the number of Peirce columns, which is two because the matrix algebra is $2\times2$.

The Dirac module $\Delta_\Phi=S\oplus S^{\mathrm{c}}$ is not this sum. There the two summands are related by a real structure and are not isomorphic over $\mathbb{R}$, so the sum is a genuine pair and not a multiplicity. The two-looking notations must not be identified, and the section is explicit about which is which.

### I.4.c — A Splitting That the Action Cannot See Is a Splitting of the Frame

Read: the Pauli display shows the carrier as $\mathbb{C}^2\otimes\mathbb{C}^2$ with one factor untouched by the algebra. The untouched factor is a copy index of the root, and it looks like a property of the algebra only because no left multiplication can move it.

The illusion has a precise shape. A left action of the form $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ is blind to the first factor, so the two blocks of the display are invariant under every element. Invariance under the whole algebra is the definition of a canonical splitting, and the display appears to satisfy it. It does not: the invariance is invariance under $\mathrm I_2\otimes\mathsf M_2(\mathbb{B})$, which is the algebra as *written in that frame*, and the frame itself was built from the root $i\vec e_z$.

The mechanical test. Replace $\vec e_z$ by a general real unit $\vec n$. A statement about the Peirce index survives and becomes a statement about $\vec n$; a statement about chirality does not change at all. A statement that silently changes its meaning is a statement about the frame.

The physical reading is that a spin direction named in the algebra is a choice of frame. The algebra has a sphere of roots and $\mathrm{SU}(2)$ acts transitively on it, so the frame that writes $\vec e_z$ is one of a sphere of equally good frames. A computation done in that frame is correct; a law derived in that frame and not tested for invariance is a convention.

The display is exact and it is used throughout the corpus; the mistake it invites is in the reading and not in the display. The statement is not that the Pauli frame is wrong but that one particular promotion of it is: reading the copy index as a chirality.

### I.4.d — Chirality Is a Real Structure and Not a Slot

Read: the two slots of the display are $S_+$ and $S_-$, both copies of $S$, while chirality is the pair $(S,S^{\mathrm{c}})$ graded by a basis operator. The slots are a polarization; the pair is a real structure.

The distinguishing property is the isomorphism over $\mathbb{R}$. $S_+$ and $S_-$ are isomorphic as left modules, so over $\mathbb{C}$ they are the same object. $S$ and $S^{\mathrm{c}}$ are isomorphic over $\mathbb{C}$ as well, but not over $\mathbb{R}$: the quaternionic module and its conjugate are genuinely different real objects. A label that survives a change of frame must be carried by a structure that no frame can move, and only the real structure qualifies.

The algebra says this twice, independently. It says it in the no-go theorem: no element of $\mathbb{B}$ acts as the central sign $\chi$, so the grading cannot be an element and must be an operator. And it says it in the parity of §*The Category of Modules in the Biquaternion Algebra*: a module descends to a quaternionic module exactly when it is free, that is when $k$ is even, so a single copy of $S$ has no real structure at all.

The physical reading is that chirality is Lorentz-invariant and a polarization is not. A Lorentz transformation is an automorphism of the algebra, and it moves the pairs of points of the projective line; it does not move the real structure. That is why a chirality is a physical label and a spin-frame component is not.

The grading operator on the Dirac module is $\mathsf V_{\mathrm{vol}}=-iR_{\vec e_z}$, and it is built from a right multiplier and a named frame. The label is invariant; the operator that realises it is written in a frame. A computation may use either, provided it does not claim that the operator is canonical.

### I.4.e — A Single Chirality Has No Real Structure, and That Is the Parity

Read: the module $S$ is projective and not free, and the same parity that obstructs freeness obstructs the descent to the quaternion algebra.

$$
S^{\oplus k}\ \text{free}\iff 2\mid k\iff W\ \text{descends to } \mathbb{H}.
$$

The smallest object with a real structure is two copies. One copy is defined over $\mathbb{C}$ and over $\mathbb{R}$, but not over the quaternions. Two copies are. So the algebra's own statement is that a real object of this kind is a pair, and that a lone copy of the simple module is a complex object with no quaternionic descent.

The physical reading is the pairing that a mass needs. The Dirac carrier of the corpus is one element multiplying another on the left, and its two values live in the two ideals; the massive field is the pair, and the field confined to one ideal is a two-component Weyl field. The parity says the same thing from the module side: the minimal object that can be read over the real quaternion algebra is the pair, not the single chirality.

The no-fixed-point statement is the same fact a third time. Coefficient conjugation acts on the projective line by $t\mapsto-1/\bar t$, with no fixed point, so no minimal left ideal is stable under the real structure. There is therefore no chirality that conjugation leaves alone, and a "real chirality" is not an object of this algebra.

This is a statement about the module category and not about masses. It says that the minimal real object is a pair; it does not say that the pair has a mass, and it does not give the value. The mass is a norm condition, and the norm is the subject of a later entry.

### I.4.f — Two Structures on One Carrier: Composition and Probability

Read: the carrier has the module structure and, separately, a Hermitian form. The two are independent, and the algebra's own bilinear form supplies neither positivity nor a norm on the carrier.

**The algebra's form is degenerate on the carrier.**

$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y),\qquad \beta\big|_{S}=\begin{pmatrix}\tfrac12&0\\0&0\end{pmatrix},
$$

of rank one, with the nilpotent direction as its radical. So the form cannot separate the two basis spinors and cannot produce a norm on the carrier.

The two forms therefore close the carrier in two different ways. The module complement is $\mathbb{B}(e_t-\tilde\Pi_{\mathrm{id}})$ and the Hilbert complement is $\mathbb{B}(e_t-\tilde\Pi_{\mathrm{id}}^{*})$, and they coincide exactly when the vacuum idempotent is Hermitian.

The Hermitian form does the job, and it is a second structure. With $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})$ the Gram matrix on the adapted basis is $\tfrac12 I_2$: the two basis spinors are orthogonal and of equal norm, and the carrier is a two-dimensional Hilbert space with the standard metric.

The physical reading is that composition and probability are two data and not one. The module structure gives what the algebra does — the action, the closure, the representation. The Hermitian structure gives what can be compared and counted — orthogonality, norm, probability. An indefinite form can do the first and cannot do the second; positivity is not a property of the plain product at all.

This is the honest reason the corpus has two sectors. The informational sector carries the star and therefore the probabilities; the material sector carries the indefinite norm and therefore the causal signs. A single carrier read with one form would have to choose, and the algebra does not choose.

The Hermitian form is positive definite on the algebra, which is a strong and special property. It is not the Lorentzian form of spacetime, and the entry does not identify them: the inertia of $\beta$ on the four real units is $(1,3)$, and that is a different object on the same set.

### I.4.g — The Operator Acts on One Side, and the Other Side Is the Frame

Read: every element of the algebra has a left action and a right action, they commute, and they are not symmetric: the swap $\sigma(L_aR_b)=L_bR_a$ is an anti-automorphism and has no multiplicative sign.

The left action is the representation and the right action is the commutant. $L$ is an algebra homomorphism and $R$ is anti-multiplicative; the double centraliser says the two are each other's commutant, of equal dimension four. So the two sides are equally large and structurally different.

The differential operator of the corpus is a left multiplication. A gradient times a field, with no right multiplication anywhere in the equation, so the carrier condition is one line: the subspace must be a left ideal, because the equation must hold for every coefficient. This is why the minimal left ideal is the carrier of a spin-half field and the right ideal is not.

The physical reading is a division of labour. The left action carries the dynamics; the right action carries the frame. Every right multiplication is an endomorphism of the left module, so it commutes with the dynamics and cannot appear in the equation of motion; what it can do is change the presentation, which is exactly what a frame change does. A term in a Lagrangian that needs a right multiplication is a term written in a frame.

The swap is what remains when no frame is chosen. It refers to the two sides without preferring one, it is canonical, and it negates the six-dimensional anti-Hermitian summand of the endomorphism algebra. It is the only canonical operation of the carrier that uses both sides, and it is the reason the two-sided structures of the corpus can be stated without a polarization.

The swap has no $\pm1$ multiplicative character, so it cannot be the sign of a mass term. It says which slot an operator occupies; the sign is supplied by an operator on the module.

### I.4.h — The Ladder Has Two Rungs

Read: the two companion nilpotents act on a spinor as two steps, each square-zero, and the composite of the two is a projection.

$$
\vec\Pi_{\mathrm{nil},+-}\psi_+=c\,\tilde\Pi_{\mathrm{id},+},\qquad \vec\Pi_{\mathrm{nil},-+}\psi_+=a\,\vec\Pi_{\mathrm{nil},-+},\qquad \vec\Pi_{\mathrm{nil},-+}\vec\Pi_{\mathrm{nil},+-}=\tilde\Pi_{\mathrm{id},-} .
$$

The two steps are not inverses, and that is the point. The first keeps the mixed part and kills the diagonal part; the second keeps the diagonal part and kills the mixed part. Applying either twice gives zero, and applying them in the two orders gives two different projections.

The physical reading is a two-state mode. A rung exists or it does not, the step up is not a step down, and there is no third rung. The occupation parity of the archive is the same statement: two steps exhaust the ladder, and the algebra has no nilpotent of index three, so a third rung cannot be built. The cap at two is not a truncation imposed from outside; it is the length of the module.

The reason the cap is two is module-theoretic. A spinor space is two complex dimensions and splits into two complex lines. A ladder step is a map between two lines, so there are two steps and no more; any further map would have to leave the carrier.

This is the kinematics of the ladder and not the dynamics. It does not say when a step is taken, and it does not supply the operator that takes it. The differential and the supercharge are structures on top of this one.

### I.4.i — The Amplitude Is One Complex Number and a Direction

Read: a spinor has an intrinsic form $a\tilde\Pi_{\mathrm{id},++}\nu_+$ and the coordinate description $(a,c)$ is not intrinsic. Only the diagonal coefficient and the nilpotent element are.

The gauge makes the difference exact.

$$
a'=a,\qquad c'=t^{-1}c ,
$$

so $a$ is invariant and $c$ is not; the vanishing of $c$ is invariant, since $c=0$ exactly when $\nu_+=0$, but the value of a nonzero $c$ is not. Reading the pair $(a,c)$ as two amplitudes is therefore reading a coordinate.

The physical reading is that a state has one invariant magnitude and one dirigible part. The diagonal coefficient is a complex number attached to the idempotent; the mixed part is an element of a line, which is a direction with a magnitude that the gauge can absorb. What is invariant is the magnitude of $a$ and the ray of $\nu_+$, not the two numbers of a column.

The probabilities are invariant only after the gauge is cut. The Hermitian norm $\tfrac12(|a|^{2}+|c|^{2})$ is invariant under the circle $|t|=1$ and not under the full $\mathbb{C}^{\times}$. So the two entries of a column carry the two probabilities in the Hermitian gauge, and in that gauge only. The modulus of the gauge is not a symmetry of the norm, and a computation that uses the full gauge and the norm together is inconsistent.

The Hermitian gauge is available when the family and the basis are Hermitian, and that is one case of the section and not the general one. In the general case there is no invariant norm and no probability, and the entry says so.

### I.4.j — The Line of Polarizations Is the Celestial Sphere

Read: the minimal left ideals are indexed by the kernel lines, the index set is a projective line, and the invertibles act on it by Möbius transformations through $PGL_2(\mathbb{C})$.

$$
\mathbb{B}^{\times}/\mathbb{C}^{\times}e_t\cong PGL_2(\mathbb{C})\cong\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong SO^{+}(1,3).
$$

The group that acts is the Lorentz group. The quotient of the invertibles by the scalars is the automorphism group of the algebra, and the automorphism group is the proper orthochronous Lorentz group acting by inner automorphisms. A projective line with a transitive Möbius action of that group is the sphere of null directions.

The physical reading is that a polarization is a null direction. A minimal left ideal names a line in the defining module, and a Lorentz transformation moves that line by a Möbius map. So choosing a spin frame is choosing a point of the celestial sphere, and the family of spin frames is the sphere itself, not a discrete set.

Transitivity has a sharp consequence. The action is transitive, so no point of the line is privileged and no polarization is algebraic. It is simply transitive on ordered triples of distinct points, so a polarization is pinned down by three points and no fewer — which is the precise sense in which "a frame" is a set of data and not a single vector.

The stabiliser is a Borel, and that is the little group of the choice. The matrices fixing one line are the upper triangular ones of complex dimension two. Choosing a polarization therefore breaks $PGL_2(\mathbb{C})$ to that Borel, exactly as choosing a rest frame breaks the Lorentz group to the rotation subgroup.

The identification of $PGL_2(\mathbb{C})$ with $SO^{+}(1,3)$ is an isomorphism of real Lie groups, not of complex ones: the complex group is $SO(3,\mathbb{C})$. And the celestial sphere here is the projective line of the *defining module* of the algebra; the entry does not claim that it is the sphere of the directions of physical null momenta, which is a different identification on a different space.

### I.4.k — What the Module Category Does Not Contain

Read: the module category of the algebra is the linear algebra of $\mathbb{C}$ with every dimension doubled, and nothing else.

$$
\operatorname{Mod}(\mathbb{B})\simeq\operatorname{Mod}(\mathbb{C}),\qquad \dim_{\mathbb{C}}\bigl(S\otimes_{\mathbb{C}}W\bigr)=2\dim_{\mathbb{C}}W .
$$

The equivalence is exact, and it is a subtraction. Every statement that can be made about a module is a statement about a complex vector space read through $S$, and the algebra is recovered as the endomorphism algebra of $S$. So the module structure alone carries no biquaternion information beyond the doubling: the multiplicity, the dimension, the projectivity, the parity.

The physical reading is a location statement. The physics of this algebra cannot live in its module category, because that category is the complex one. It must live in what the module does not see: the forms, the norms, the star, the real structure, the products. This is the most useful boundary in the section, and it is the reason the corpus's physical content is carried by the norms and not by the representations.

What this buys a reader. A claim that a phenomenon follows from "the representation theory of the biquaternion algebra" is a claim that can be checked by asking whether it survives the Morita equivalence. If it does, it is a statement about complex vector spaces and belongs to the complex field; if it does not, it names one of the structures that the equivalence drops.

The equivalence is about modules and not about algebras with extra structure. The star, the quaternion conjugation and the four products are not functorial for it, and that is exactly why they carry the content.

## The Limits

**The entry states the module structure and not the norms.** Which modules carry a mass, which carry a causal sign, and which are positive are norm questions, and they belong to the entries on the four forms and the four norms.

Two assignments are labelled and not proved. That the left action carries the dynamics and the right action carries the frame is a reading consistent with the archive and with the one-sidedness of the Dirac operator; the algebra states only that the two actions commute and are unequally multiplicative. And the identification of the line of polarizations with the sphere of null directions uses an identification of $PGL_2(\mathbb{C})$ with $SO^{+}(1,3)$ that is an isomorphism of real groups, stated elsewhere in the corpus.

The infinite-dimensional case is not treated. A quantum field needs infinitely many modes, hence an infinite direct sum of copies of $S$, and the finiteness arguments of this section do not extend to it. The archive's Fock constructions are read on a one-mode truncation, which is what makes them finite and what makes them belong to this section.

The carrier of the module is not yet a field. A field is an element of the carrier depending on a point of spacetime, and the dependence is a further structure. The entry gives the fibre and not the field.

## Summary

- The algebra is a module over itself by left multiplication, by right multiplication and by the two together, and the submodules are the ideals.
- The algebra is simple, semisimple, Artinian and of length two as a left module; every nonzero proper left ideal is minimal and maximal.
- There is one simple module $S$, of complex dimension two; every module is $S^{\oplus k}$, and the regular module is $S\oplus S$.
- Every module is projective; $S^{\oplus k}$ is free exactly when $k$ is even, and the same parity is the obstruction to a real structure.
- The module category of the algebra is the category of complex vector spaces, with every dimension doubled.
- A splitting of the regular module is an unordered pair of distinct points of a projective line, and no pair is canonical.
- The Peirce pair and the tensor split of the Pauli display are one splitting, written as ideals and as a tensor index.
- The two slots of the display are copies of $S$; chirality is the pair $(S,S^{\mathrm{c}})$, graded by $\mathsf V_{\mathrm{vol}}=-iR_{\vec e_z}$, and it is a real structure.
- The star does not exchange the two spinor spaces: it maps $S_+$ to the right row $\tilde\Pi_{\mathrm{id},+}\mathbb{B}$.
- A spinor has an intrinsic diagonal coefficient and an intrinsic nilpotent part; the mixed coordinate is gauge-dependent.
- The two nilpotents are two square-zero steps, and the ladder has two rungs because the carrier has two lines.
- The module carries an indefinite bilinear form and a canonical swap, and no positivity: the Hermitian form is a second structure.
- The invertibles act on the line of polarizations by Möbius transformations through $PGL_2(\mathbb{C})$, transitively, with a Borel stabiliser.
- The module category contains no biquaternion physics beyond the doubling; the content lies in the forms, the norms and the real structure.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| ${}_{\mathbb{B}}\mathbb{B}$, $\mathbb{B}_{\mathbb{B}}$, ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ | the left, right and two-sided regular modules |
| $S=\mathbb{B}\tilde\Pi_{\mathrm{id}}$ | the simple module, $\dim_{\mathbb{C}}S=2$ |
| $S_{\pm}=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | the two spinor spaces of a polarized module |
| $S^{\mathrm{c}}$ | the conjugate module |
| $V=\mathbb{B}$ | the carrier of the regular module |
| $L(\tilde Q)$, $R(\tilde Q)$ | left and right multiplication by $\tilde Q$ |
| $\Pi_u=\tfrac12(e_t+iu\cdot\vec e)$ | the rank-one idempotent at $u\in\mathbb{C}^{3}$, $u\cdot u=1$ |
| $\psi_+=a\tilde\Pi_{\mathrm{id},++}\nu_+$ | the intrinsic form of a positive spinor |
| $a,c,b,d$ | Peirce coordinates of the two spinors |
| $t\in\mathbb{C}^{\times}$ | the gauge parameter of a Peirce basis |
| $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ | the trace form on the carrier |
| $\sigma(L_aR_b)=L_bR_a$ | the swap |
| $\mathsf V_{\mathrm{vol}}=-iR_{\vec e_z}$ | the chirality basis operator |
| $\chi$ | the central sign, $\chi^2=e_t$, outside $\mathbb{B}$ |
| $S^{\oplus k}$ | the general module, of complex dimension $2k$ |

## Further Reading

In the mathematics corpus. The five articles of the source table, and inside the last of them *Morita Equivalence with the Complex Field* and *Real Structures*, which carry the two results this entry uses most.

In this category. *The Idempotents, the Ideals and the Observables* constructs the minimal left ideal that this entry names as a carrier. *The Spectrum and the Two Modes* asks what an element does to a carrier it does not preserve. *The Four Forms and the Four Norms* supplies the positivity that this entry shows the plain product cannot supply.

The sources of this entry. [Introduction to the Spin-Half Bispinor Spaces](the-spin-half-bispinor-spaces.html) is the case where the carrier is a minimal left ideal, with the one-sidedness of the operator and the two dimensions as the whole content. [Rotor, Spin, Pair and Carrier: A Survey of the Closure Block](rotor-spin-pair-and-carrier-a-survey-of-the-closure-block.html) sets the module structure beside the probability structure on one carrier and shows that the algebra's own form is degenerate there. [Spin Zero and the Centre: Why the Scalar Field Lies Outside the State Module](spin-zero-and-the-centre-why-the-scalar-field-lies-outside-the-state-module.html) is the boundary case, where the missing one-dimensional module is proved missing. [Biquaternion Physical Interpretation of Operator Chirality](biquaternion-physical-interpretation-of-operator-chirality.html) treats the swap and the chirality operator at length.
