# __The Unpolarized Module of the Biquaternion Algebra__

## Introduction

**The subject.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ acts on itself on the left, and the carrier of that action has four complex dimensions. The corpus meets this carrier in three shapes: as the pair of tensor factors of the Pauli display, as the pair of Peirce ideals of a root of the unit, and as the pair formed by a spinor and its conjugate in the Dirac module. The first two are one splitting and not two: the Pauli display is built from the root $\vec\Xi=i\vec e_z$, so its tensor index is the Peirce plane index, and the factorization it shows is the choice it made. The third is not a splitting of this module at all, and that difference fixes the name: only a split whose halves are held apart by a real structure is a chirality, and the Peirce pair, being two copies of $S$, is a copy index that is never one.

**This article is one of three.** A splitting of the carrier is a choice, so the carrier has to be described before the choice is made; an article that begins from the Peirce pair inherits the choice and can no longer say what it cost, which is why this one is placed after the concrete theory it qualifies. This article reads the carrier with nothing chosen, *The Polarized Module of the Biquaternion Algebra* reads the same carrier after one pair of points has been named, and *The Pauli Module of the Biquaternion Algebra* reads the one pair that the Pauli frame names for free, without showing that it named anything.

**The result in one line.** A splitting of the carrier into two planes is a point of a projective line, the algebra sees the family and not the point, so the module is **unpolarized**, and its canonical structure is not a splitting but the trace form, of which the swap is the reflection.

**The word.** A **polarization** is a decomposition of the carrier into two subspaces of equal dimension on which the algebra acts. The carrier with no such decomposition singled out is **unpolarized**. The word is taken from the geometry of Hermitian forms, where a polarization is the same kind of choice, and it is used here in that sense only: it names a splitting, not a complex structure and not a sign convention.

**The one fact that decides the question.** Over $\mathbb{C}$ the two halves of any splitting are isomorphic modules, because $M_2(\mathbb{C})$ has a single simple module up to isomorphism. Over $\mathbb{R}$ they are not: the conjugate of the quaternion module is not the quaternion module. A splitting whose halves are isomorphic is a choice of basis; a splitting whose halves are not is a fact of the algebra. The first is a polarization; the second is the split produced by the chirality cell $\gamma_5=-iR_{\vec e_z}$, which is the chirality itself, and no frame can convert the second into the first. That second split is §*The Conjugate Pair*.

**What the article does.** The module and its two actions are fixed first, with the faithfulness and the double centralizer (§*The Module and the Two Actions*), and the names of the elements are fixed with them, because a carrier that is its own algebra can be named in four ways and only one of them is free (§*The Names of the Elements*). A splitting into two planes is then defined and shown to be a choice of a point of a projective line, not a structure of the module (§*A Splitting Is a Pair of Points, Not a Structure*), and the splittings of the corpus are placed against that criterion (§*The Polarizations of the Corpus*). The axis-free frame is then read for what it does with the splitting: it displays none (§*The Axis-Free Frame Displays None*). The swap of the two sides is defined, because it is the one piece of structure that survives without a splitting (§*The Swap*); the article states what the module carries instead (§*What the Module Carries Instead*), what the conjugate pair is and why it is not a polarization (§*The Conjugate Pair*), and what the absence costs (§*What the Absence Costs*).

**Boundaries.** The regular module, its left and right actions and its two-sided ideals are *The Regular Module in the Biquaternion Algebra*; the chosen splitting, its minimal left ideals and the spinors they carry are *The Polarized Module of the Biquaternion Algebra*; the tensor display of one root is *The Pauli Module of the Biquaternion Algebra*. The classification of all modules is *The Category of Modules in the Biquaternion Algebra*; the algebra in the coefficient basis is *The Biquaternion Algebra*; the two families of matrices are *Families of Matrix Representations*, and their two worked instances are *$M_4(\mathbb{C})$ Axis-Free Representation* and *$M_4(\mathbb{C})$ Pauli Representation*. The Peirce decomposition and its idempotents are *The Peirce Decomposition of $M_4(\mathbb{C})$*; the $2+2$ spectral split of the carrier by the square of a root is *The Two Chiralities of $M_4(\mathbb{C})$*, whose involution $\Gamma=H^2$ grades the carrier without cutting it into submodules. The swap, treated as an operator on the endomorphism algebra, is *Operator Chirality on the Biquaternion Algebra*; this article defines it only far enough to state what it does to a splitting.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, $\vec e_k^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ and cyclic, and $i$ the central scalar imaginary. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_\mu\in\mathbb{C}$, its coefficient column is $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$, and $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The labels $\mathrm{axf}$ and $\mathrm{pau}$ are those of *Matrix Representations Conventions*, and the cells are $L_aR_b$, acting by $L_aR_b\tilde X=a\tilde Xb$.

## The Module and the Two Actions

**The carrier.** Let $V=\mathbb{B}$ as a complex vector space, of dimension four, and of real dimension eight. The **left action** is
$$
L(\tilde Q)\colon V\longrightarrow V,\qquad L(\tilde Q)\tilde X=\tilde Q\tilde X,
$$
and the **right action** is $R(\tilde Q)\tilde X=\tilde X\tilde Q$. Both are $\mathbb{C}$-linear, because $i$ is central.

**The left action is a representation.** Associativity gives $L(\tilde P)L(\tilde Q)=L(\tilde P\tilde Q)$, so $L$ is an algebra homomorphism $\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(V)$, and it is injective: $L(\tilde Q)=0$ forces $\tilde Q=L(\tilde Q)e_t=0$. The right action is anti-multiplicative, $R(\tilde P)R(\tilde Q)=R(\tilde Q\tilde P)$, and the two commute.

**The commutant.** Every right multiplication commutes with every left multiplication, so $R(\mathbb{B})$ lies in the commutant of $L(\mathbb{B})$. The two algebras have the same dimension, four, and the commutant is exactly $R(\mathbb{B})$: this is the double centralizer theorem for a simple algebra, and it is what makes the module a bimodule rather than a module. The consequence used below is that an operator on $V$ which commutes with the whole left action is a right multiplication, and conversely.

**What the module is not.** $V$ is not irreducible. Since $\mathbb{B}\cong M_2(\mathbb{C})$ has a simple module $S$ of dimension two, $V\cong S\oplus S$, and $V$ is semisimple of length two. The statement of this article is not that no splitting exists — splittings exist in abundance — but that none of them is canonical. The algebra acting is the regular model, the four-dimensional image of $\mathbb{B}\cong M_2(\mathbb{C})$ in $M_4(\mathbb{C})$, and not the full matrix algebra: the same $\mathbb{C}^4$ is the unique simple module of $M_4(\mathbb{C})$ and is irreducible there, while under $\mathbb{B}$ it has length two. The word *module* in the title names this carrier, and the length-two statement is a statement about $\mathbb{B}$.

**The two frames, on one carrier.** The same $V$ is written as a column of four coefficients in the axis-free frame, with $L^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=[\tilde Qe_\nu]_\mu$, and as the tensor product $\mathbb{C}^2\otimes\mathbb{C}^2$ in the Pauli frame, with $L^{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$. These are two displays of one module; the first is the frame of §*The Axis-Free Frame Displays None* below, the second is the frame of *The Pauli Module of the Biquaternion Algebra*, §*The Display Polarizes for Free*.

## The Names of the Elements

**The ambiguity, and why it is not a defect.** The carrier is the algebra, so one symbol does double duty: $\tilde X$ is an element of $V$ and also an element of $\mathbb{B}$ that may be multiplied. A reader may take this for sloppiness. It is the structure: $V$ is the regular module, the same set carries the vector structure and the algebra structure, and no notation can remove the overlap without inventing a distinction the algebra does not make. What notation can do is keep the four possible readings apart, and that is what this section fixes.

**Four names, four costs.**

| Name | What it is | What it depends on |
|---|---|---|
| $\tilde X$ | the element | nothing |
| $[X]_{\mathcal{F}}$ | its coefficient column in a named frame | the frame |
| $[X]^{\mathrm{pau}}$ | the $2\times2$ array of the Pauli display | the root $\vec e_z$ |
| $X_\Pi=\tilde X\Pi$ | a component, in the direction of an idempotent | the idempotent |

**The first name is the only free one.** $\tilde X$ refers to nothing chosen: not a frame, not a root, not an idempotent. Multiplication is available to it, and the module never uses it — $V$ is a vector space, and $\tilde X\tilde Y$ is not an operation of the module but of the algebra that happens to sit on the same set. A statement written in the first name is a statement about the module; a statement written in the third or the fourth is a statement about a chart until it is shown to be invariant.

**The third name is the one that misleads.** In the Pauli display an element of the carrier is a $2\times2$ array, because the carrier is $\mathbb{C}^2\otimes\mathbb{C}^2$ and an element is a tensor, that is a matrix. The "two components" of the folklore are its two **columns**: two vectors, not two halves of one spinor. Reading them as two halves of one object is the step that turns the display into a claim about the algebra, and it is the same step, in notation, as the one *The Pauli Module of the Biquaternion Algebra*, §*The Display Polarizes for Free* describes in geometry.

**The rule.** An element is named by the element. A component is named by the element together with the idempotent that cuts it, in the subscript and never by a bare subscript letter. Names such as $\psi_L$, $\psi_R$, "left part", "two-component spinor" or $u\otimes v$ are names of a component or of a chart, and each of them silently carries a point of $\mathbb{P}^1$ that the module does not contain. The rule is not pedantry: it is what keeps a statement's invariance visible, since a statement in the third or the fourth row of the table changes its truth value with the frame and a statement in the first does not.

**The exception, and why it is not one.** The Dirac module of the corpus is a different module, and its elements are pairs $(\psi,\psi^{\mathrm{c}})$. There the split is carried by a real structure rather than by a root, so the pair is a name of the carrier and not of a chart — which is exactly the distinction drawn in §*The Polarizations of the Corpus* and stated as a theorem in §*The Conjugate Pair*.

## A Splitting Is a Pair of Points, Not a Structure

**The submodules.** A submodule of $V$ is a left ideal of the algebra. The two-dimensional ones are the left ideals $V_\Pi=\mathbb{B}\Pi$ generated by a rank-one idempotent, and they are exactly the sets
$$
V_\Pi=\{\tilde X\in\mathbb{B}\;:\;\tilde X\Pi=\tilde X\}.
$$
The condition is an identity: for $\tilde X=\tilde Z\Pi$ one has $\tilde X\Pi=\tilde Z\Pi\Pi=\tilde Z\Pi=\tilde X$, and conversely $\tilde X\Pi=\tilde X$ exhibits $\tilde X$ as an element of $\mathbb{B}\Pi$. Each such $V_\Pi$ has complex dimension two and is stable under the left action, because $L(\tilde Q)(\tilde Z\Pi)=(\tilde Q\tilde Z)\Pi$.

**The idempotents.** A rank-one idempotent of $\mathbb{B}$ is
$$
\Pi_u=\tfrac12\bigl(e_t+i\,u\cdot\vec e\,\bigr),\qquad u=(u_x,u_y,u_z)\in\mathbb{C}^3,\quad u\cdot u=1,
$$
where $u\cdot\vec e=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$. The normalization is what makes it idempotent: $(u\cdot\vec e)^2=-(u\cdot u)e_t=-e_t$, hence $(iu\cdot\vec e)^2=e_t$, hence $\Pi_u^2=\Pi_u$. The element $\Pi_u$ has trace one in the $2\times2$ model and rank one; its image and its kernel are each a line of $\mathbb{C}^2$, and the two lines are distinct.

**Two points give a splitting.** The complement of $\Pi_u$ is $\Pi_{-u}=e_t-\Pi_u$, and the two ideals $V_{\Pi_u}$ and $V_{\Pi_{-u}}$ are complementary: they meet in $0$ and their sum is $V$. More generally, two idempotents with distinct kernels give complementary ideals, $V=V_{\Pi}\oplus V_{\Pi'}$, and distinct kernels are the only condition: two distinct points of the line give a splitting, and a splitting is nothing else.

**Where the choice lives.** The condition $u\cdot u=1$ is one complex equation in three unknowns, so the idempotents form a complex surface. The ideal does not depend on all of $\Pi$: since $\tilde X\Pi=\tilde X$ says that $\tilde X$ vanishes on $\ker\Pi$, the ideal is determined by the line $\ker\Pi$, equivalently by the row space of $\Pi$, and every element of $V_\Pi$ has that same row space. In the $2\times2$ model, with $\Pi=w\lambda$ and $\lambda w=e_t$, the row space is the line of $\lambda$ and the image is the line of $w$; only the first is fixed by the ideal, and the image line runs over $V_\Pi$ as the element varies. The fibres are therefore one-dimensional and the ideals form a projective line. A splitting of $V$ is an unordered pair of distinct points of that line, and any two distinct points give one, because the two ideals meet in $0$.

**The Peirce case is one pair of points.** The choice $u=\vec e_z$ gives the pair $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ of *The Peirce Decomposition of $M_4(\mathbb{C})$*, and the splitting $V=S_+\oplus S_-$ with $S_\pm=\mathbb{B}\Pi_\pm$. It is one pair of points of the line, the pair the symbol $\vec e_z$ names. Nothing in the algebra prefers it: the choice is the root.

## The Polarizations of the Corpus

**The criterion.** A splitting is canonical when the algebra itself distinguishes its two halves, that is when no automorphism of the module carries one splitting into another. The module endomorphisms are the right multiplications, $\operatorname{End}_{\mathbb{B}}(V)=R(\mathbb{B})$, and the automorphisms are the $R(\tilde P)$ with $\tilde P$ invertible, a group isomorphic to $\mathrm{GL}_2(\mathbb{C})$. Such a change of frame carries $V_\Pi$ to $V_{\tilde P^{-1}\Pi\tilde P}$ and moves the point $\ker\Pi$ to $\tilde P^{-1}\ker\Pi$: the group acts on the projective line by its natural action. That action is transitive on points and on pairs of distinct points, so the automorphism group is transitive on the splittings. A splitting can therefore be canonical only if the two halves are modules over different structures, and that requires more than the complex algebra.

| Splitting | The two halves | Where it comes from | Exchanged by an automorphism? |
|---|---|---|---|
| Peirce, and the tensor split of the Pauli display | $S_+=\mathbb{B}\Pi_+$, $S_-=\mathbb{B}\Pi_-$ | the root $\vec e_z$, written as a tensor index | yes, by any automorphism moving the root |
| Any other pair of points | $V_\Pi$, $V_{\Pi'}$ | an unordered pair of distinct points of $\mathbb{P}^1$ | yes |
| Dirac | $S$, $S^{\mathrm{c}}$ | the conjugate module, a real structure | no |

**The first two rows are one family.** Both split $V$ into two submodules, both come from a choice, and both are moved by the automorphisms of the module, because the $\mathrm{SU}(2)$ of the algebra rotates the roots into one another and carries the pair of planes with it. What the Pauli display adds to this family is not a second splitting: its factorization is the Peirce split of one root, written in another notation. *The Pauli Module of the Biquaternion Algebra*, §*The Display Polarizes for Free* reads that notation.

**Why the equivalence matters.** A reader who takes the tensor factor and the Peirce pair for two independent structures counts two polarizations where there is one, and expects a frame that displays the first without the second. No such frame exists: a factorization of the carrier into two planes of equal dimension is a rank-two idempotent up to the exchange of the two factors, that is a point of $\mathbb{P}^1$, and a point of $\mathbb{P}^1$ is a root.

**The third is not a splitting of this module.** The conjugate $S^{\mathrm{c}}$ is a module for the conjugate algebra, and over $\mathbb{C}$ it is isomorphic to $S$, so the pair $S\oplus S^{\mathrm{c}}$ is again a sum of two copies. What distinguishes it is the real structure: over $\mathbb{R}$ the quaternion module and its conjugate are not isomorphic, and the exchange that exists over $\mathbb{C}$ does not exist over $\mathbb{R}$. This is the precise sense in which chirality is not a polarization: it is carried by a splitting whose halves are held apart by a real structure, not by a basis.

**The consequence for the frames.** A frame can display a polarization, and both of the first two are displayed somewhere in the corpus. A frame cannot manufacture chirality, because a frame is a change of basis over $\mathbb{C}$ and chirality is not a basis phenomenon. This is the dividing line the rest of the article follows.

## The Axis-Free Frame Displays None

**The display.** In the axis-free frame the left matrix is
$$
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix},
$$
with entries the coefficients and the signs of the multiplication table, and no tensor factor anywhere.

**What is lost and what is not.** Nothing of the module is lost: it is the same $V$, the same left action, the same projective line of splittings. What is lost is the free display of one point of that line. The axis-free frame displays the module unpolarized, which is what the module is, and a reader who wants a splitting must name one — an idempotent, a root, a line.

**The three directions enter alike.** The three vector columns are built by one rule, so no direction is singled out, and the choice that the Pauli frame made silently is not made at all. The price is stated in the axis-free article and is the same price here: the idempotents are not adapted to the basis, and there is no tensor display. The gain is that no accidental structure is mistaken for the algebra's.

## The Swap

**The definition.** On the cells, the **swap** is
$$
\sigma(L_aR_b)=L_bR_a .
$$
The sixteen cells are a basis of $\operatorname{End}_{\mathbb{C}}(V)$, so this defines a $\mathbb{C}$-linear map $\sigma$ of the endomorphism algebra into itself.

**The three properties.** The swap is an involution, $\sigma^2=\mathrm{id}$; it is an anti-automorphism, $\sigma(XY)=\sigma(Y)\sigma(X)$; and it is frame-independent, because the cells are coordinate-free operators and exchanging the two factors of $aXb$ refers to no basis. Each is proved in *Operator Chirality on the Biquaternion Algebra*, where the swap is the subject; here only its role for the module is needed.

**What the swap is for.** A polarization is a choice, and a choice is what an unpolarized module does not contain. What the module does contain is the pair of sides: every operator is built from left and right multiplications, and the swap is the only canonical operation that refers to the pair without choosing between them. It is therefore the structure that survives when the splitting is withdrawn, and it is what replaces it in the statements of the next section.

## What the Module Carries Instead

**The trace form.** On $V$ there is the symmetric bilinear form
$$
\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y),
$$
which is $\mathbb{C}$-bilinear and symmetric because the scalar part of a product is invariant under cyclic permutation. Its Gram matrix on the four units is $D=\operatorname{diag}(1,-1,-1,-1)$, which is invertible, so the form is nondegenerate. It is not positive and it is not even anisotropic: $\beta(\tilde X,\tilde X^{\natural})=\langle\tilde X\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ vanishes on the cone of the zero divisors, and that cone is one of the objects of the algebra rather than a defect of the form.

**A form is not a switch.** Two different matrices carry the two-sided structure of a frame, and they must not be confused. The Gram matrix of $\beta$ on the four units is $D=\operatorname{diag}(1,-1,-1,-1)$. The **switch** is the matrix $\mathsf W$ with $R(\tilde Q)=\mathsf W L(\tilde Q)^{\mathsf T}\mathsf W$: it is $D$ in the axis-free frame, where the switch and the Gram matrix coincide, and the pure swap $\mathsf P$ in the Pauli frame, because a change of display moves the switch by a congruence. It is the switch, not the Gram matrix, that the transpose identity of the companion article needs.

**What the form gives.** A nondegenerate symmetric form identifies $V$ with its dual and $\operatorname{End}_{\mathbb{C}}(V)$ with $V\otimes V$, and the symmetric square with the exterior square:
$$
\operatorname{End}_{\mathbb{C}}(V)=\operatorname{Sym}^2V\oplus\Lambda^2V,\qquad 16=10+6 .
$$
The first summand is the operators self-adjoint for the form, the second those skew-adjoint for it, and the swap is the reflection across the decomposition: it fixes the first summand and negates the second. In the axis-free frame the matrix of the reflection and the Gram matrix of the trace form coincide, so the decomposition can be read off either. The dimensions are $10$ and $6$, and they add to the dimension of the endomorphism algebra.

**Why this is the right replacement.** The form is not a splitting: it names no subspace of $V$, and it is available in every frame without a choice. It reproduces, without a polarization, the two things a splitting is usually asked to supply: an identification of $V$ with its dual, through which adjoints are taken, and a distinction of self-adjoint from skew-adjoint operators. The distinction is not a chiral one, and §*What the Absence Costs* says why it cannot be made to serve as one.

**The six-dimensional summand.** $\Lambda^2V$, of dimension six, is the space spanned by the commutators $[L_a,R_b]=L_aR_b-L_bR_a$, and it is closed under the commutator: it is the orthogonal Lie algebra of the trace form, of the dimension of $\mathfrak{so}(4,\mathbb{C})$, and it is a canonical object of the unpolarized module.

**It is not the span of the bivectors.** The span of the six Lorentz bivectors $\gamma_\mu\gamma_\nu$ of the gamma frame is also six-dimensional and also closed under the commutator, and the two spaces must not be identified. No bivector is skew for the trace form: the two spaces meet only in $0$ and together span twelve dimensions. The Lorentz generators of the frame are cells, not skew-adjoint operators, and the passage from one space to the other is not a change of basis.

**Why that comparison is invariant.** The two spaces being compared are not of the same kind, and the comparison is nevertheless stable. A unit $\tilde S$ conjugates every cell, hence carries the bivector span of the frame to the bivector span of the conjugated frame, and the same conjugation preserves the trace form, so it leaves $\Lambda^2V$ fixed. The intersection therefore stays $0$ under the whole unit group: the statement is invariant under the changes of frame the algebra itself performs, and it is not a statement about one display. A general change of basis is a different matter, and an empty one, because it destroys the notion of bivector: only the frames attached to the algebra have bivectors to compare.

**The lesson the corpus should draw.** The comparison has a grade content, and it is the sharpest form of the observation that the two sides carry different kinds of object. Read in the gamma frame, the left multipliers are
$$
L_{\vec e_t}=1,\qquad L_{\vec e_x}=\gamma_2\gamma_3,\qquad L_{\vec e_y}=-\gamma_1\gamma_3,\qquad L_{\vec e_z}=\gamma_1\gamma_2,
$$
all of them even, and the right ones are
$$
R_{\vec e_t}=1,\qquad R_{\vec e_x}=-i\gamma_0,\qquad R_{\vec e_y}=i\gamma_1\gamma_2\gamma_3,\qquad R_{\vec e_z}=-\gamma_0\gamma_1\gamma_2\gamma_3,
$$
which mix grades. The left family lies in the even part of the Clifford algebra, spanned by the scalar and the bivectors; the right family does not, because it holds a vector, a trivector and the volume element. No reading of the pair as two copies of the same object survives the comparison, and the swap is what carries one family to the other.

## The Conjugate Pair

**What a polarization cannot produce.** The family of polarizations is one object of the carrier and the conjugate pair is another. This section states the second, because it is the one structure of the carrier that no choice of a splitting can supply, and because it is where the word chirality belongs.

**The conjugate module.** The conjugate algebra acts on the same set by $\tilde Q\cdot\tilde X=\bar{\tilde Q}\tilde X$, with the coefficients conjugated, and the resulting module $S^{\mathrm{c}}$ is the conjugate of $S$. Over $\mathbb{C}$ the two are isomorphic, since $M_2(\mathbb{C})$ has one simple module; the isomorphism is antilinear and refers to a real structure. Over $\mathbb{R}$ they are not isomorphic: the conjugate of the quaternion module is not the quaternion module. That difference is the whole difference between a polarization and a chirality, and it is invisible to the complex algebra.

**The complexification.** Complexified, the algebra splits,

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\;\cong\;M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$

and the conjugation swaps the two summands. The nontrivial central idempotents of the complexification are therefore $\tfrac12(e_t\mp\chi)$, where $\chi$ is the **central sign**: $\chi^2=e_t$, $\chi$ is central, and $\chi\notin\mathbb{B}$. Concretely $\chi=i\tilde\Xi_{\mathrm{ad}}$ for an adjoined root $\tilde\Xi_{\mathrm{ad}}$ with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and $\tilde\Xi_{\mathrm{ad}}\notin\mathbb{B}$.

**The no-go theorem.** No element of $\mathbb{B}$ acts as $\chi$ on the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$. In the matrix model an element acts as $\operatorname{diag}(A,\epsilon\bar A\epsilon^{-1})$, and $\operatorname{diag}(-I,I)$ would require $A=-I$ together with $\bar A=I$, which is a contradiction. The central sign therefore cannot be read as multiplication by an element of the algebra: it exists on the complexification only, and there only as a grading of the pair.

**The consequence for the name.** The grading is not an element, and it is not a splitting of this carrier $V$: it acts on $\Delta$. It is an **operator** on that module, the cell

$$
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},
$$

with $\gamma_5^2=I_4$. The central sign $\chi$ is the *central form* of that cell and not its definition: the cell is what acts, and $\chi$ is what the cell becomes when the algebra is complexified and split. This is why chirality is a Lorentz-invariant label that survives the mass term, while the Peirce index is a copy index that names no chirality at all.

**The two eigenspaces and the mass.** On $\Delta$ the cell has the two eigenspaces $S$ and $S^{\mathrm{c}}$, of opposite eigenvalue. On the regular module the same cell is the right multiplication $R_{\vec e_z}$: it commutes with every $L_{\tilde Q}$ and is therefore an endomorphism of the left module, but it is not $L_{\tilde Q}$ for any element of the algebra. That inequality is the no-go theorem above in another form, and it is why the label is carried by an operator on the module and not by an element of the algebra. There its eigenspaces are instead the two Peirce planes, $-1$ on $S_+$ and $+1$ on $S_-$, so the two readings agree on the signs and not on the objects: $S_+$ and $S_-$ are isomorphic copies of $S$, while $S$ and $S^{\mathrm{c}}$ are not isomorphic over $\mathbb{R}$. The mass is the off-diagonal invariant pairing between the two halves, $\bar\Psi\Psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L$ in the Dirac reading: it couples the halves, and it is neither an element of the algebra nor a Peirce nilpotent. Because $\gamma_5$ anticommutes with each $C_\mu$, the massless equation separates on the two halves and the mass is exactly the term that joins them.

## What the Absence Costs

**No Weyl projectors.** Without a splitting there are no projectors onto the two halves, so the decomposition of a state into a left part and a right part is not available until an operator is supplied. The operator that supplies it is not a cell of the frame but a choice. On the Dirac module it is the cell $\gamma_5=-iR_{\vec e_z}$, which is the chirality itself and whose central form is the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra; on the carrier $\mathbb{C}^4$ of the matrix model it is instead the involution $\Gamma=H^2$ of *The Two Chiralities of $M_4(\mathbb{C})$*, a $\mathbb{Z}/2$ quotient of the root's $\mathbb{Z}/4$ grading that grades the carrier without splitting it into submodules. Each has to be named.

**Chirality becomes an operator, and that is the honest bookkeeping.** The swap supplies exactly one of them without a choice: it sends the rotation generator $L_{\vec e_z}$ to $R_{\vec e_z}$, and $R_{\vec e_z}=i\gamma_5$. So the chirality operator of the frame is, up to the factor $i$, the swap of a rotation generator. The statement is proved in the companion article; its content here is that the module does not carry chirality in its splitting, it carries it in the exchange of its two sides.

**No factorized tensor product.** In a frame with no tensor factor there is no bipartition into two slots, so there is no partial trace and no system-environment split of the kind a tensor product supplies. The information-theoretic articles of the corpus do not use one: their losses are stated sector by sector, on a subalgebra, and the conditional expectation is the instrument. That is a choice the absence forces, and it is worth stating, because a reader trained on a tensor product will look for the factorization and not find it.

**No sign in a Lagrangian.** The swap is an anti-automorphism, so it has no multiplicative $\pm1$ character, and it cannot appear as the sign of a mass term. That is not a defect of the swap but a division of labour: the swap says which slot an operator occupies, and the sign that a Lagrangian needs is supplied by an operator on the module, namely $\gamma_5$.

## Summary

The carrier of the left action is four complex dimensional and semisimple of length two, so it splits into two planes in many ways and canonically in none. A splitting is the choice of an unordered pair of points of a projective line: the rank-one idempotents are $\Pi_u=\tfrac12(e_t+iu\cdot\vec e)$ with $u\cdot u=1$, their ideals are the two-dimensional submodules $V_\Pi=\{\tilde X:\tilde X\Pi=\tilde X\}$, and the ideal depends only on the **kernel** line, so the idempotents collapse onto the line by one complex dimension. The Peirce pair $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ is one point of that line, and the tensor factorization of the Pauli display is the same point written as an index, which is why that frame appears to supply a splitting for free: the index is the root, no left multiplication moves it, and the splitting then looks like a property of the algebra when it is a property of the display. The axis-free frame displays the same module with no factor and therefore no free splitting, which is not a loss of structure but the absence of an illusion.

The polarizations of the corpus are of two kinds and not three. The Peirce pair and the tensor split of the Pauli display are one splitting, since the display is built from the root $\vec\Xi=i\vec e_z$: one writes the pair as ideals, the other as a tensor index, and both are moved by the $\mathrm{SU}(2)$ that rotates the roots into one another. Every other pair of points of $\mathbb{P}^1$ gives a polarization of the same kind, with nothing to distinguish it. The Dirac pair is not one of them. It joins $S$ to its conjugate $S^{\mathrm{c}}$; over $\mathbb{C}$ the two halves are isomorphic and over $\mathbb{R}$ they are not, the pairing is turned into a grading by the cell $\gamma_5=-iR_{\vec e_z}$, whose central form is the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$, and no element of $\mathbb{B}$ acts as that sign. That is the dividing line: a splitting whose halves are isomorphic is a polarization and a choice of basis, and a splitting whose halves are not is the one the chirality cell produces, which no frame can supply.

What the unpolarized module carries instead is the trace form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$, nondegenerate and symmetric, with Gram matrix $D$; the switch of a frame is the matrix that carries the transpose, and it is $D$ itself in the axis-free frame and the pure swap $\mathsf P$ in the Pauli one, so the two matrices coincide in the first frame and not in the second. The form splits the endomorphism algebra into the self-adjoint and the skew-adjoint parts, of dimensions ten and six, and the swap $\sigma(L_aR_b)=L_bR_a$ is the reflection across that decomposition. The six-dimensional part is the orthogonal Lie algebra of the form, spanned by the commutators $[L_a,R_b]$ and of the dimension of $\mathfrak{so}(4,\mathbb{C})$; the six Lorentz bivectors of the gamma frame are cells, none of them is skew for the form, and their span meets the skew part only in zero.

The absence of a splitting costs the Weyl projectors, the $2+2$ partial trace and the mass sign, and each of them must be supplied by a named operator rather than read from a basis. The swap supplies one of them without a choice, and it supplies it in the only place the module can hold it: $R_{\vec e_z}=i\gamma_5$, so the chirality operator is the swap of a rotation generator. The module holds the exchange of its two sides, not a splitting of its carrier, and every statement about chirality in this category is a statement about that exchange.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{B}$ | the carrier, four complex and eight real dimensions |
| $L(\tilde Q)$, $R(\tilde Q)$ | left and right multiplication, $L(\tilde Q)\tilde X=\tilde Q\tilde X$, $R(\tilde Q)\tilde X=\tilde X\tilde Q$ |
| $S$ | the simple module, $\dim_{\mathbb{C}}S=2$, with $V\cong S\oplus S$ |
| $S^{\mathrm{c}}$ | the conjugate module, isomorphic to $S$ over $\mathbb{C}$ and not over $\mathbb{R}$ |
| $\Pi_u$ | the rank-one idempotent $\tfrac12(e_t+iu\cdot\vec e)$ with $u\cdot u=1$ |
| $\Pi_\pm$ | the Peirce idempotents $\tfrac12(e_t\pm i\vec e_z)$ |
| $S_\pm=\mathbb{B}\Pi_\pm$ | the two Peirce planes, each a copy of $S$ |
| $\vec\Xi=i\vec e_z$ | the root whose halves are $\Pi_\pm$ |
| $\mathcal{P}$ | the Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ of the Pauli display |
| $V_\Pi$ | the two-dimensional submodule $\mathbb{B}\Pi=\{\tilde X:\tilde X\Pi=\tilde X\}$, determined by the line $\ker\Pi$ |
| $[X]_{\mathcal{F}}$, $[X]^{\mathrm{pau}}$ | the coefficient column in a frame, the $2\times2$ array in the Pauli display |
| $X_\Pi=\tilde X\Pi$ | the component of $\tilde X$ in the direction of $\Pi$; the idempotent always appears |
| $u\cdot\vec e$ | $u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$ |
| $\mathbb{P}^1$ | the projective line of polarizations, a point for each **kernel** line $\ker\Pi$; the image line indexes the right ideals instead |
| $\beta(\tilde X,\tilde Y)$ | the trace form $\operatorname{Sc}(\tilde X\tilde Y)$ |
| $D$, $\mathsf P$ | the switch of the axis-free and the Pauli frames; $D$ is also the Gram matrix of $\beta$ |
| $\sigma$ | the swap $\sigma(L_aR_b)=L_bR_a$ |
| $\operatorname{Sym}^2V$, $\Lambda^2V$ | the self-adjoint and skew-adjoint parts, of dimensions $10$ and $6$ |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$ | the central sign of the complexification, $\chi^2=e_t$, $\chi\notin\mathbb{B}$; the central form of $\gamma_5$ |
| $\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}$ | the chirality cell, $\gamma_5^2=I_4$; eigenspaces $S$ and $S^{\mathrm{c}}$ on $\Delta$, $S_+$ and $S_-$ on the regular module |
| $\mathrm{axf}$, $\mathrm{pau}$ | the labels of the two frames |

## Further Reading

- [The Regular Module in the Biquaternion Algebra](the-regular-module.html), for the left, right and two-sided actions of the algebra on itself and the two-sided ideals.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the carrier after a pair of points is chosen: the minimal left ideals, the spinors and their Peirce coordinates.
- [The Pauli Module of the Biquaternion Algebra](the-pauli-module-of-the-biquaternion-algebra.html), for the one root that the Pauli display chooses silently.
- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the classification of all modules, the Morita equivalence and the lattice of left ideals.
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the swap as an operator, its eigenspaces and its action on the frame.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chirality involution $\Gamma=H^2$, the $2+2$ spectral split of the carrier, and the proof that those two chiralities are not minimal left ideals.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the idempotents of a root and the Peirce frame.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the frame with no tensor factor.
- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for the frame with the tensor factor and the pure swap.
- [Families of Matrix Representations](families-of-matrix-representations.html), for the two sides, the change of frame and the switch.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the labels $\mathrm{axf}$ and $\mathrm{pau}$ and the conventions of the category.
