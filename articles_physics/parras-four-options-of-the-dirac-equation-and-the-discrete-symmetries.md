# __Parra's Four Options of the Dirac Equation and the Discrete Symmetries__

## Introduction

The Dirac equation, written out in real components, is a system of eight coupled real differential equations. Parra's observation, taken up and used by Fauser, is that this system admits a **vectorial** reading — each equation is a statement about a scalar and a pair of three-vectors — and that the reading can be set up in **four inequivalent ways**. The four readings give four different equations, which differ only in the relative signs of the gradient term and the coupling term. One of the four is the Dirac–Hestenes equation; the other three are not, and one of the other three is Daviau's space Clifford equation.

The four options are not four theories. They are four **inequivalent rewritings** of one theory, related among themselves by the discrete symmetries of the Dirac equation: parity, charge conjugation and time reversal. This is what makes them interesting to the corpus. The corpus treats each discrete symmetry in its own article (charge conjugation in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, the full set in *The CPT Theorem in Biquaternionic Form*), and it treats the spinor as a minimal left ideal in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. What it does not yet contain is the statement that the discrete symmetries act as a **permutation group** on a set of inequivalent Dirac equations, and that the set of particles of the theory — electron and positron, spin up and spin down — is precisely the set of orbits of this permutation. This article records that statement.

The article is an **equivalent rewriting**, as everywhere in this series: the four options are four forms of the standard equation, and nothing new is predicted. What is new to the corpus is the object: the discrete symmetries organising the four spinor types, and the algebraic datum that keeps them apart. The construction is taken from Parra as reported by Fauser; the corpus reproduces the report and does not claim to have consulted Parra's papers, which are unpublished or difficult to obtain.

## The Four Options

Parra starts from the four-component complex Dirac spinor $\Psi = (\Psi_1,\Psi_2,\Psi_3,\Psi_4)^{\mathsf T}$ and inspects the eight real equations. His assumption is that the **real part** $\Re(\Psi_1)$ of the first component transforms as a scalar; under that assumption the eight equations acquire a vector character once the **spin vector** $\mathbf n = -\mathbf n^{*}$ (the axial vector built from the spin degrees of freedom) is introduced. Two scalars and two vectors remain. Writing the two scalars as $\alpha$ and $\lambda$ and the two vectors as $\mathbf E = (E_1,E_2,E_3)$ and $\mathbf B = (B_1,B_2,B_3)$, the option-$\{0\}$ spinor is

$$
\Psi_{\{0\}} =
\begin{pmatrix} \alpha + iB_3 \\ -B_2 + iB_1 \\ E_3 + i\lambda \\ E_1 + iE_2 \end{pmatrix}.
$$

The assumption "$\Re(\Psi_1)$ is a scalar" can equivalently be made **for any of the four vector components** — scalar, first, second or third — and this is the origin of the four options. A suitable renaming of the scalars and vectors gives the four spinors

$$
\Psi_{\{0\}} =
\begin{pmatrix} \alpha + iB_3 \\ -B_2 + iB_1 \\ E_3 + i\lambda \\ E_1 + iE_2 \end{pmatrix},\qquad
\Psi_{\{2\}} =
\begin{pmatrix} B_2 + iB_1 \\ \alpha - iB_3 \\ E_1 - iE_2 \\ -E_3 + i\lambda \end{pmatrix},
$$

$$
\Psi_{\{1\}} =
\begin{pmatrix} E_1 - iE_2 \\ -E_3 + i\lambda \\ B_2 + iB_1 \\ \alpha - iB_3 \end{pmatrix},\qquad
\Psi_{\{3\}} =
\begin{pmatrix} E_3 + i\lambda \\ E_1 + iE_2 \\ \alpha + iB_3 \\ -B_2 + iB_1 \end{pmatrix}.
$$

The four spinors carry the same eight real fields in four different arrangements. With a Clifford basis $\{e_i\}$, $e_ie_j+e_je_i=2\eta_{ij}$, and with $\nabla$ the gradient, $A$ the potential, $m$ the mass and $q$ the charge, the four options satisfy the four equations

$$
\begin{aligned}
\{2\} &\quad \nabla\Psi_{\{2\}}e_{21} + qA\Psi_{\{2\}} + m\Psi_{\{2\}}e_0 = 0, && e^+_\uparrow,\\
\{0\} &\quad -\nabla\Psi_{\{0\}}e_{21} + qA\Psi_{\{0\}} + m\Psi_{\{0\}}e_0 = 0, && e^+_\downarrow,\\
\{3\} &\quad \nabla\Psi_{\{3\}}e_{21} - qA\Psi_{\{3\}} + m\Psi_{\{3\}}e_0 = 0, && e^-_\uparrow,\\
\{1\} &\quad -\nabla\Psi_{\{1\}}e_{21} - qA\Psi_{\{1\}} + m\Psi_{\{1\}}e_0 = 0, && e^-_\downarrow.
\end{aligned}
$$

The second column is Parra's identification of each equation with a "particle": the sign $\pm$ distinguishes electron from positron and the arrow $\uparrow\downarrow$ distinguishes spin up from spin down. The identification is a choice — one may exchange the two labels within each pair — and the corpus records it as Parra's reading rather than as a derivation.

**Proposition (the options are one theory in four sign conventions).** The four equations differ only in the **sign of the gradient term** ($\nabla$ or $-\nabla$) and the **sign of the coupling term** ($+qA$ or $-qA$), while the mass term is the same in all four. Consequently each option is a solution of the Dirac equation in its own conventions: reading the sign of $\nabla$ as defining the orientation of the Clifford basis and the sign of $qA$ as the charge convention, the four options become the same equation.

*Proof.* Compare the four equations term by term; they have the same structure and differ in the two signs displayed. The mass term $m\Psi e_0$ is common to all four.

**Corollary (which options the corpus already knows).** Option $\{2\}$ **is** the Dirac–Hestenes equation $\nabla\Psi i\sigma_3 - qA\Psi = m\Psi\gamma_0$ of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, upon identifying the bases $e_i$ and $\gamma_\mu$ and the spin bivector $e_{21}$ with $i\sigma_3$; Fauser states this identification. Option $\{1\}$ **is** the Daviau equation $\nabla\varphi\,i\sigma_1 = m\varphi^{*}+qA\varphi$ of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*, upon the passage between the two formulations described there. That two of the corpus's three formulations appear as two of Parra's four options, and the other two options are new, is the article's first structural point.

**Remark (the right action is common to all four).** In every option the spin bivector $e_{21}$ and the velocity vector $e_0$ multiply the spinor **on the right**, while the gradient and the coupling act on the left. This is the bi-module structure of *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*, and it is the same feature the corpus records for the Dirac–Hestenes equation. The four options do not differ in the left/right pattern; they differ only in the two signs.

## The Discrete Group and the Discrete Symmetries

**Statement (the permutations of the options).** The transformations that connect the four Parra options form the quotient

$$
D = \Gamma_{1,3}/\Gamma^{+}_{1,3},
$$

the Clifford–Lipschitz group modulo its even part. Its non-identity elements are, up to the identification, **space inversion**, **charge conjugation** and **time reversal**. The four options are the orbit of any one of them under $D$, and the four particle labels $e^\pm_{\uparrow\downarrow}$ are the labels of that orbit.

The quotient $D$ is a discrete group of order four. The even part $\Gamma^+_{1,3}$ consists of the products of an even number of vectors — the rotors, which generate the proper orthochronous Lorentz group and the double cover $SL(2,\mathbb C)$ — and the quotient by it leaves exactly the four cosets representing the four discrete reflections. Acting on the spinor module, an odd (reflection) transformation changes the relative signs of the gradient and coupling terms in the way displayed above, and the four options are the four sign patterns so obtained.

**What the corpus already has.** The corpus contains each of the three symmetries separately:

- *Charge conjugation* is built in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* from the algebra's real structure $\flat$ and the $\mathrm{Spin}^c$ structure, and in the spacetime-algebra language it is a right multiplication by a fixed bivector, as recorded in *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* (open question 4).
- *Parity and time reversal* are the reflections of *The Reflection and the Rotation in Biquaternionic Form*, where the grading by reflection count is set up and where the frame $\gamma_0$ and conjugation by it are treated.
- The combined statement is the corpus's *The CPT Theorem in Biquaternionic Form*.

**What the corpus does not have.** Nowhere does the corpus assemble these three symmetries into a **group acting on a set of inequivalent equations**, and nowhere does it identify the four particle types — electron and positron, spin up and spin down — with the orbit of that action. That is the new object this article contributes. In the corpus's usual reading the symmetries act on **one field** and the particle types are labels on the solution space; here the symmetries act on the **set of equations**, and the particle types are labels on the orbit. The two readings are compatible, and the second makes explicit what the first leaves implicit: the four types are not four solutions of one equation but four sign conventions of one equation, permuted by the discrete group.

**Remark (the discrete group is the quotient, not the full pin group).** The quotient $D=\Gamma_{1,3}/\Gamma^+_{1,3}$ has order four, so the options form a four-element orbit and no smaller orbit. The double cover is invisible at this level: $\pm$ elements of the pin group give the same transformation of the equation, which is why the corpus's articles on the spinor module record the double cover separately (*The Spinor Module in Biquaternionic Form and Its Lorentz Action*). The article does not claim that $D$ is the pin group; it is the quotient, and the quotient is what acts on the options.

## The Klein Four of the Conjugations

The discrete group $D$ of the previous section is the quotient of the Clifford–Lipschitz group by its even part. The same four-element group is met again, purely inside the algebra, as the group generated by the algebra's conjugations, and the block structure of *Relations Between Subspaces* binds the two. This section writes the table and reads the three symmetries on it.

**The table.** With the blocks in the fixed order $(T_{\mathrm{m}},T_{\mathrm{i}},X_{\mathrm{m}},X_{\mathrm{i}})$ of *Relations Between Subspaces*, the columns of the four conjugations are

| map | column | fixed space | type |
|---|---|---|---|
| $1$ | $(+,+,+,+)$ | $\mathbb{B}$ | identity |
| $\bar{\cdot}$ | $(-,+,+,-)$ | $\mathbb{H}_{\mathbb{B}}$, the real quaternions | anti-linear automorphism |
| ${}^{\natural}$ | $(+,+,-,-)$ | $\mathbb{C}_{\mathbb{B}}$, the centre | linear anti-automorphism |
| ${}^{*}={}^{\natural}\bar{\cdot}$ | $(-,+,-,+)$ | $\mathbb{M}_+$, the informational sector | anti-linear anti-automorphism |
| $\flat=-{}^{*}$ | $(+,-,+,-)$ | $\mathbb{M}_-$, the material sector | anti-linear anti-automorphism |

The first three rows together with the identity are the elements of the Klein four $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$, and the four blocks are its four characters, which is why the block decomposition is canonical. The last row is **not** a fourth group element — $\flat$ differs from ${}^{*}$ by the central sign — but the **fourth character**. The columns and the fixed spaces are *Relations Between Subspaces*'; the table is restated here because the discrete symmetries are read on it.

**Reading (the three symmetries on the characters).** The block action identifies the non-trivial characters with the discrete symmetries, the assignment being fixed by the standard transformation properties.

- **Parity $P$ is ${}^{\natural}$.** It fixes the two temporal blocks and negates the two spatial ones, sending the material four-vector $ict\,e_0+\mathbf{x}$ to $ict\,e_0-\mathbf{x}$: space inverted, time kept. It is $\mathbb{C}$-linear, the algebraic form of the unitarity of parity.
- **Time reversal $T$ is $\bar{\cdot}$.** On the material sector it negates the material time $T_{\mathrm{m}}=\mathbb{R}(ie_0)$ — the $ict$ direction — and fixes the material space, and it is **anti-linear**, which is the anti-unitarity of time reversal. The corpus reaches the same object as the anti-linear part of $T$ (*The CPT Theorem in Biquaternionic Form*).
- **The full reflection $PT$ is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$**, negating both material blocks and so sending $x^\mu\mapsto-x^\mu$.
- **Charge conjugation is $\flat=-{}^{*}$, the real structure.** It fixes the material sector and negates the informational one, is anti-linear, and is the object the corpus builds $C$ on (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*; *Charge Conjugation and the Division Ring*). That it is a character and not a group element is the algebraic statement that $C$ does not join $\{1,P,T,PT\}$ as an independent factor but is the sign that turns $PT$ into its negative.

**Caution (the second dictionary).** The Clifford-algebra literature attaches the names differently: with the generators $ie_k$ of $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, the grade involution is read as $P$, the reversion as $T$ and the Clifford conjugation as $PT$ (*The CPT Theorem in Biquaternionic Form*, quoting the literature). Since the grade involution is $\bar{\cdot}$, the reversion ${}^{*}$ and the Clifford conjugation ${}^{\natural}$, that dictionary reads $P=\bar{\cdot}$, $T={}^{*}$, $PT={}^{\natural}$ — the transpose of the reading above. Both dictionaries are labelled and neither is proved in the corpus; the difference is the choice of which structure is called space inversion, and the reading above is the one whose parity fixes time and negates space. The table is the fact, the naming is the reading, and the article keeps the two apart.

The two dictionaries are visible even inside this article. The previous section's quotient $D=\Gamma_{1,3}/\Gamma^{+}_{1,3}$ has for its three non-identity elements space inversion, charge conjugation and time reversal, and its orbit of four options therefore reads $C$ as the product $PT$ — the Clifford convention. The reading above instead places the three characters on $\{P,T,PT\}$ and the corpus's charge conjugation on the fourth character $\flat$, which is the corpus's own link (*Relations Between Subspaces*; *Charge Conjugation and the Division Ring*). The section records the difference rather than hiding it: the symmetries are a group of order four either way, and the question is only which of the four characters each one occupies.

## Why the Matrix Formulation Mixes the Options

The reason the four options are worth isolating is the failure of the matrix formulation to keep them apart. In the matrix Dirac theory a **complex linear combination** of the four components of the spinor is a standard operation — it is how one rotates the spinor, changes basis, or forms a plane wave. Such a combination **mixes the four options**: a complex linear combination of two Parra spinors is generally a spinor of a third type, and the relative signs cannot be undone. Fauser's formulation of the point: a complex linear combination intermingles the different Parra options "without any chance to re-obtain them as different equations".

This is the algebraic content of a familiar physical fact. In passing from the Dirac equation to quantum electrodynamics one must introduce **separate creation and annihilation operators for each spin polarisation** — a distinct field operator, in effect, for each of the four types. The formalism of the second quantised theory already "takes care of the different types of spinors", in Fauser's phrase, precisely because the first-quantised matrix formalism does not: the complex linear combinations available there are exactly the operations that destroy the distinction. Parra's four options make the distinction manifest by refusing the complexification — the spinors are real, the equations are real, and the four types are four inequivalent real equations rather than four components of one complex spinor.

**What this does and does not say.** It does **not** say that the second quantisation of the Dirac field is derivable from the four options, and it does not say that the four options replace the spin polarisation sum of quantum electrodynamics. It says that the algebraic necessity of separate field operators per spin polarisation has a first-quantised shadow: the four options are inequivalent under the operations that the matrix formalism actually performs on spinors, so the matrix formalism cannot represent the four types by one complex spinor without losing the distinction. The corpus records this as the source's physical reading and does not go further.

## The Quaternion and Matrix Forms of the Parra Spinors

Parra's spinors have a compact quaternion form. With the quaternion basis $1, ik:=ie_k$ ($k=1,2,3$) and quaternion conjugation $\phantom{q}^{\natural}$, the spinor of option $\{r\}$ is

$$
\Psi_r = q_{r1} + i\,\bar q_{r2},
$$

the sum of a quaternion and $i$ times a conjugate quaternion. Since the Hestenes spinor is an element of the even subalgebra $\mathrm{Cl}_{1,3}^+\subset\mathrm{Cl}_{1,3}\cong M_2(\mathbb H)$, this extends to the matrix spinor

$$
\Psi_{\{r\}} = \frac12\begin{pmatrix} q_{r1} & -\bar q_{r2} \\ \bar q_{r2} & q_{r1}\end{pmatrix},
$$

the $2\times2$ matrix structure being a matrix representation of the complex structure $(1,i)$.

**Proposition (the quaternion form is the corpus's field).** The map $q_{r1}+i\bar q_{r2}\mapsto\Psi_{\{r\}}$ sends the Parra spinor of each option into the biquaternion algebra $\mathbb B\cong\mathbb C\otimes_\mathbb R\mathbb H\cong\mathrm{Cl}^+_{1,3}$, and under the corpus's matrix representation $\Phi$ the result is a general element of $M_2(\mathbb C)$ — that is, a general biquaternion on the eight real parameters, exactly the corpus's Dirac field.

*Proof.* A quaternion $q=q_0+q_1e_1+q_2e_2+q_3e_3$ has four real parameters and $i\bar q$ has four more, so $q_{r1}+i\bar q_{r2}$ ranges over the eight-dimensional real algebra; the matrix display is the action of the complex structure on the pair, and $\Phi$ realises it as an element of $M_2(\mathbb C)$. The identification of the general element with the corpus's field is the eight-component match of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*.

This places the Parra spinors in the same family as the Daviau spinor and the Dirac–Hestenes spinor: all three are general elements of the biquaternion algebra on eight real parameters, and the differences between the formulations are the sign conventions and the basis choices, not the size of the spinor. The quaternion form shows this directly.

## The Spin-Particle Clifford Bundle

Fauser draws a structural conclusion from the four options. In the geometric-algebra literature the spinor bundle is often built from the **spin Clifford bundle** of Rodrigues and collaborators, whose typical fibre at a point is a space of idempotents. Fauser submits that this bundle is **too large**: it does not distinguish the four particle types, because idempotents that differ by an even (rotor) transformation give the same class and the rotor group does not see the discrete quotient $D$. What the four options suggest is a smaller bundle, the **spin-particle Clifford bundle**, whose fibre consists of **equivalence classes of idempotents under an even equivalence relation** — the relation by the even part $\Gamma^+_{1,3}$, so that two idempotents are in the same class exactly when the corresponding spinors are of the same Parra type. The commutator relation, and hence the Clifford structure, is invariant under the odd (discrete) transformations of the Clifford–Lipschitz group, so the refinement is well defined.

**Relation to the corpus.** The corpus's own spinor picture is the minimal left ideal $\mathbb B\tilde\Pi_1$ generated by a primitive idempotent, developed in *Spinors as Minimal Left Ideals with Inner Conjugation*, *Biquaternion Ideals and Peirce Decomposition* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The spin-particle bundle is that picture with the idempotent replaced by its equivalence class **modulo the even group**, and the four Parra types are the four classes that the even relation does not identify. In the corpus's language the refinement is: the minimal left ideals of $\mathbb B$ carry the spinor of the theory, and the discrete quotient $D$ acts on the set of idempotents by the odd reflections, with the four Parra types as the four orbits of an even-equivalence class.

*Proof sketch.* Two spinors of the same Parra type are related by an even transformation, so their idempotents are equivalent under the even group and lie in the same class; two spinors of different types are related only by an odd transformation, so their idempotents are inequivalent. The four classes are the four options. The identification of the classes with the options is Fauser's proposal; the corpus records it as a proposal and not as a theorem, since the even equivalence relation is not written out explicitly in the source.

## Open Questions

1. **The even equivalence relation.** What exactly is the even equivalence relation on idempotents whose classes are the four Parra types? In the corpus's terms, the classes are orbits of a primitive idempotent under the even group; the relation should be exhibited on the corpus's own idempotents $\tilde\Pi_1$, $\tilde\Pi_2$ and their Peirce companions.

2. **Which option is the framework's?** The corpus's Dirac equation as written in *The Dirac Equation in Biquaternionic Form* has its own sign conventions. Which of the four Parra options does it correspond to under the corpus's dictionary, and is the correspondence stable across the article's solutions and its non-relativistic limit?

3. **The discrete symmetries as a permutation group.** The corpus has each of $P$, $C$, $T$ acting on one field. Does the extension to a group acting on the set of four equations reproduce the corpus's $C$ (the $\flat$ real structure and the right multiplication by a bivector) and its $P$, $T$ (the reflections of the grading article) with the correct permutation?

4. **Spin polarisation and second quantisation.** The four options are four first-quantised equations. Is there a sense in which the separate creation and annihilation operators per spin polarisation of the second quantised theory are the four Fourier components of the option orbit, and does the corpus's path-integral formalism see them?

5. **The spin-particle bundle in the corpus's topology.** The corpus has a topology of the biquaternion unit group and of the null cone (*The Biquaternion Unit Group as a Topological Group*). Does the spin-particle bundle, with its finer fibres, have a characteristic class that the spin Clifford bundle does not, and is that class visible in the corpus's topological articles?

6. **Empirical contact.** None is claimed. The options are equivalent rewritings; the question, as everywhere, is whether isolating them makes a structural fact of the framework easier to see.

## Summary

Parra's four options are four inequivalent ways of reading the eight real Dirac equations as vector equations, arising from the four choices of which component's real part is declared scalar. They yield four equations differing only in the signs of the gradient and coupling terms, with the same mass term. Option $\{2\}$ is the Dirac–Hestenes equation and option $\{1\}$ is the Daviau space Clifford equation; the other two are new, and all four multiply the spinor on the right by the spin bivector and the velocity vector, so they share the bi-module structure. The options are permuted by the discrete quotient $D=\Gamma_{1,3}/\Gamma^+_{1,3}$, whose non-identity elements are space inversion, charge conjugation and time reversal, and Parra labels the orbit by electron and positron, spin up and spin down. The matrix formalism cannot keep the options apart: a complex linear combination mixes them, which is the first-quantised shadow of the separate creation and annihilation operators per spin polarisation of quantum electrodynamics. The Parra spinors have a quaternion form, and they are general elements of the biquaternion algebra, exactly the corpus's Dirac field on eight real parameters. Fauser's structural conclusion is a refinement of the spin Clifford bundle to the **spin-particle Clifford bundle**, whose fibre is a set of even-equivalence classes of idempotents; in the corpus's terms this is the minimal-left-ideal picture of the spinor with the idempotent taken modulo the even group, and the four Parra types are the four classes. The article records the construction as Parra's and Fauser's, reproduces it in the corpus's conventions, and claims no new physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Psi_{\{r\}}$, $r=0,1,2,3$ | The Parra spinor of option $\{r\}$, a four-component complex spinor |
| $\alpha,\lambda$ | The two scalars of the vector reading |
| $\mathbf E=(E_1,E_2,E_3)$, $\mathbf B=(B_1,B_2,B_3)$ | The two vectors of the vector reading |
| $\mathbf n=-\mathbf n^{*}$ | The spin vector, $=-iS$ in Parra's notation |
| $\{e_i\}$, $e_ie_j+e_je_i=2\eta_{ij}$ | The Clifford basis; $e_{21}=e_2e_1$ the spin bivector |
| $\nabla$, $A$, $m$, $q$ | Gradient, potential, mass, charge |
| $\Gamma_{1,3}$, $\Gamma^+_{1,3}$ | Clifford–Lipschitz group and its even part |
| $D=\Gamma_{1,3}/\Gamma^+_{1,3}$ | The discrete quotient; order four |
| $e^\pm_{\uparrow\downarrow}$ | Parra's particle labels: electron/positron, spin up/down |
| $\Psi_r=q_{r1}+i\bar q_{r2}$ | The quaternion form of the Parra spinor |
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra; the corpus's Dirac field on eight real parameters |

## Further Reading

- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §2.3, for the four options, their permutation group and the spin-particle bundle; the source of this article.
- J. M. Parra-Serra, "On Dirac and Darwin–Hestenes equation," in *Proceedings of the Conference on Clifford Algebras* (1989), and "Dirac's theory in real geometric formalism: multivectors versus spinors" (unpublished), for the original analysis. The corpus has not consulted these; they are cited through Fauser.
- W. A. Rodrigues Jr., E. C. de Oliveira and others, on the spin Clifford bundle, referred to by Fauser for the comparison with the spin-particle bundle.
- A. Crumeyrolle, *Orthogonal and Symplectic Clifford Algebras* (Kluwer, 1990), for the invariance of the Clifford structure under the odd transformations of the Clifford–Lipschitz group.
- The companion articles of this series: *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*, *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, *The CPT Theorem in Biquaternionic Form*, *The Reflection and the Rotation in Biquaternionic Form*, and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*.
