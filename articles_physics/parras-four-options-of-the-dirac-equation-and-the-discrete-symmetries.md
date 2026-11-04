# __Parra's Four Options of the Dirac Equation and the Discrete Symmetries__

## Introduction

The Dirac equation, written out in real components, is a system of eight coupled real differential equations. Parra's observation, taken up and used by Fauser, is that this system admits a **vectorial** interpretation — each equation is a statement about a scalar and a pair of three-vectors — and that the interpretation can be set up in **four inequivalent ways**. The four interpretations give four equations, which differ only in the relative signs of the gradient term and the coupling term. One of the four is the Dirac–Hestenes equation; the other three are not, and one of the other three is Daviau's space Clifford equation.

The four options are not four theories. They are four **inequivalent rewritings** of one theory, related among themselves by the discrete symmetries of the Dirac equation: parity, charge conjugation and time reversal. This is what makes them interesting to the corpus. The corpus treats each discrete symmetry in its own article (charge conjugation in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, the full set in *The CPT Theorem in Biquaternionic Form*), and it treats the spinor as an element of a Peirce carrier, a minimal left ideal here in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. What it does not yet contain is the statement that the discrete symmetries act as a **permutation group** on a set of inequivalent Dirac equations, and that the four particle labels of the theory — electron and positron, spin up and spin down — are precisely the four points of the orbit of this permutation. This article records that statement.

Two conventions frame everything below.

- **The article is written in cells.** A two-sided multiplication is a cell, and every operator of the body is a cell or a sum of cells. The Clifford names of the same five cells are collected once, in the closing section *The Legacy Pauli Gamma Formulation*, and none of those names is used before it.
- **The corpus carries two Dirac equations, not one:** the one-sided chiral pair on the spinor module, and the two-sided single equation on the algebra. Parra's options belong to the second family. The section *The Two Dirac Equations* states both and places the options, and the placement is what joins Parra's spin bivector to the corpus's chirality cell.

The article is an **equivalent rewriting**, as everywhere in this series: the four options are four forms of the standard equation, and nothing new is predicted. What is new to the corpus is the object: the discrete symmetries organising the four spinor types, and the algebraic datum that keeps them apart. The construction is taken from Parra as reported by Fauser; the corpus reproduces the report and does not claim to have consulted Parra's papers, which are unpublished or difficult to obtain.

**Notation, once.** The imaginary unit is $i$, with $i^2=-1$; every product of two of them is reduced before a formula is read, and no other object in the article is identified with it. The quaternion units are $e_t=1,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclic. A cell multiplies on the left by one element and on the right by another, $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_b\psi=a\psi b$, and two cells multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order; the side of an action is carried by position and never by a mark. The four frame cells are $\Gamma_\mu:=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}$, with $\tau(t)=x$ and $\tau(k)=y$ for $k=x,y,z$, and their sum with the derivative is the gradient cell $\mathcal{D}:=\Gamma_\mu\partial/\partial x_\mu$. The chirality cell is $\chi:=R_{-i\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$, the last step because $L_{e_t}^{\mathrm{axf}}=I_4$; it acts as $\chi\psi=-i\psi\vec e_z$, so it multiplies **on the right** and the factor $i$ is a scalar of the cell. This is the corpus's name for the cell, and it is a cell and not an element: $\chi$ below always acts on what stands to its right. The squares are then a count of minus signs, each frame cell carrying exactly one factor $i$,

$$
\Gamma_t^{\,2}=i^2L_{e_t}^{\mathrm{axf}}R_{\vec e_x^2}^{\mathrm{axf}}=(-1)(+1)(-1)I_4=I_4,\qquad
\Gamma_k^{\,2}=i^2L_{\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=(-1)(-1)(-1)I_4=-I_4,\qquad
\chi^2=(-i)^2R_{\vec e_z^2}^{\mathrm{axf}}=(-1)(-1)I_4=I_4 ,
$$

so the sign of each square is the parity of the number of negative factors, and the $i$ is exactly what puts the Lorentzian signature the right way round: without it the timelike cell would square to $-I_4$ and the three spatial ones to $+I_4$. The letter $\Gamma$ is used twice, for the frame cells $\Gamma_\mu$ and for the Clifford–Lipschitz group $\Gamma_{1,3}$; the index settles which is meant.

## The Four Options

**Parra's assumption.** Parra starts from the four-component complex Dirac spinor $\Psi=(\Psi_1,\Psi_2,\Psi_3,\Psi_4)^{\mathsf T}$ and inspects the eight real equations. His assumption is that the **real part** $\Re(\Psi_1)$ of the first component transforms as a scalar; under that assumption the eight equations acquire a vector character once the **spin vector** is introduced. Write it

$$
\vec s=-i\vec S,\qquad \vec S\in\mathbb R^3 ,
$$

so that $\vec s=\vec s^{*}$ under the star conjugation $^{*}=\bar\cdot\circ{}^{\natural}$, since the two flips it performs cancel on an imaginary vector; a vector with that property lies in the informational space $X_{\mathrm i}$ of the block table below. Two scalars and two vectors remain. Writing the scalars as $\alpha$ and $\lambda$ and the vectors as $\vec E=(E_1,E_2,E_3)$ and $\vec B=(B_1,B_2,B_3)$, the option-$\{0\}$ spinor is the first of the four displays below.

**The four spinors.** The assumption "$\Re(\Psi_1)$ is a scalar" can be made, after a suitable renaming, for **any of the four components** — the scalar itself or one of the three vector components — and this is the origin of the four options. The renaming of the scalars and the vectors gives the four spinors

$$
\Psi_{\{0\}}=
\begin{pmatrix}\alpha+iB_3\\ -B_2+iB_1\\ E_3+i\lambda\\ E_1+iE_2\end{pmatrix},\qquad
\Psi_{\{2\}}=
\begin{pmatrix}B_2+iB_1\\ \alpha-iB_3\\ E_1-iE_2\\ -E_3+i\lambda\end{pmatrix},
$$

$$
\Psi_{\{1\}}=
\begin{pmatrix}E_1-iE_2\\ -E_3+i\lambda\\ B_2+iB_1\\ \alpha-iB_3\end{pmatrix},\qquad
\Psi_{\{3\}}=
\begin{pmatrix}E_3+i\lambda\\ E_1+iE_2\\ \alpha+iB_3\\ -B_2+iB_1\end{pmatrix}.
$$

The four spinors carry the same eight real fields in four different arrangements, and the arrangements are related by fixed matrices. With $\Pi$ the fixed permutation that swaps the two halves — $1\leftrightarrow3$, $2\leftrightarrow4$ — and $J_2$, $J_1$ the signed permutations read off the displays,

$$
\Psi_{\{3\}}=\Pi\,\Psi_{\{0\}},\qquad
\Psi_{\{2\}}=J_2\,\bar\Psi_{\{0\}},\qquad
\Psi_{\{1\}}=J_1\,\bar\Psi_{\{0\}},
$$

so that two of the three are **antilinear**, and the third, $\Pi$, is a real permutation, hence complex-linear. The options therefore form two classes under complex-linear equivalence, $\{0\}\sim\{3\}$ and $\{2\}\sim\{1\}$, and all four transitions between the classes are conjugations; the section *Why the Matrix Formulation Mixes the Options* reads that as the failure of the matrix formalism. The three relations were recomputed on generic real fields.

**The four equations, in cells.** With the frame cells and the chirality cell of the notation paragraph, and with $\bar\Psi$ the coefficient conjugate, the four options satisfy the four equations

$$
\boxed{\;\begin{aligned}
\{2\}&\quad \mathcal{D}R_{e_{21}}\Psi+ϙA\Psi+m\,\chi\bar\Psi=0, && e^+_\uparrow,\\[2pt]
\{0\}&\quad -\mathcal{D}R_{e_{21}}\Psi+ϙA\Psi+m\,\chi\bar\Psi=0, && e^+_\downarrow,\\[2pt]
\{3\}&\quad \mathcal{D}R_{e_{21}}\Psi-ϙA\Psi+m\,\chi\bar\Psi=0, && e^-_\uparrow,\\[2pt]
\{1\}&\quad -\mathcal{D}R_{e_{21}}\Psi-ϙA\Psi+m\,\chi\bar\Psi=0, && e^-_\downarrow.
\end{aligned}\;}
$$

Here $\mathcal{D}=\Gamma_\mu\partial/\partial x_\mu$ is the gradient cell, the derivative acting on everything to its right; $ϙ$ is the charge and $A$ the potential; and $R_{e_{21}}$ is the right cell of the spin bivector. Under the corpus's dictionary the bivector $e_{21}$ of the source's Clifford basis is the element $-\vec e_z$ of the even algebra, so that

$$
R_{e_{21}}=R_{-\vec e_z}^{\mathrm{axf}}=-i\,\chi .
$$

The mass term is written as the chirality cell acting on the conjugated field, $m\chi\bar\Psi$, which is the corpus's representative of Parra's $m\Psi e_0$; the section *The Two Dirac Equations* gives the reason for the replacement and its price. The sign pattern of the four options is unaffected by it, because the mass term is common to all four.

The final column is Parra's identification of each equation with a "particle": the sign $\pm$ distinguishes electron from positron and the arrow $\uparrow\downarrow$ distinguishes spin up from spin down. The identification is a choice — one may exchange the two labels within each pair — and the corpus records it as Parra's interpretation rather than as a derivation.

**Proposition (the options are one theory in four sign conventions).** The four equations differ only in the **sign of the gradient term** ($\mathcal{D}$ or $-\mathcal{D}$) and the **sign of the coupling term** ($+ϙA$ or $-ϙA$), while the spin cell and the mass term are the same in all four. Consequently each option is a solution of the Dirac equation in its own conventions: reading the sign of the gradient as defining the orientation of the frame and the sign of $ϙA$ as the charge convention, the four options become the same equation.

*Proof.* Compare the four equations term by term; they have the same structure and differ in the two signs displayed. The mass term $m\chi\bar\Psi$ and the spin cell $R_{e_{21}}$ are common to all four, and the kinetic operator is the same up to its overall sign.

**Corollary (which options the corpus already knows).** Option $\{2\}$ **is** the Dirac–Hestenes equation. In Parra's writing, with the mass left on his side, option $\{2\}$ is $\nabla\Psi e_{21}+ϙA\Psi+m\Psi e_0=0$, and the corpus's display $L_\nabla R_{\omega\sigma_3}\psi-eL_A\psi=mR_{v_0}\psi$ of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* carries the same two right multipliers, the spin plane $\omega\sigma_3$ and the velocity $v_0$; the two differ only in the two sign conventions of the charge and the mass: with $ϙ=-e$ both coupling terms read $-eA\Psi$, and with $m\to-m$ both mass terms read $-m$ times the field, so the two coincide term by term, the spin bivector $e_{21}$ being identified with $\omega\sigma_3$ as Fauser states. Option $\{1\}$ **is** the Daviau equation $\nabla\varphi\,i\sigma_1=m\varphi^{*}+qA\varphi$ of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation* — the charge is written $q$ there — upon the passage between the two formulations described in that article. That two of the corpus's three formulations appear as two of Parra's four options, and the other two options are new, is the article's first structural result.

**Remark (the right action is common to all four).** In every option the spin cell $R_{e_{21}}=-i\chi$ multiplies $\Psi$ and the chirality cell $\chi$ multiplies $\bar\Psi$, both **on the right**, while the gradient and the coupling act on the left. This is the bi-module structure of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, and it is the same feature the corpus records for the Dirac–Hestenes equation. The four options do not differ in the left/right pattern; they differ only in the two signs.

## The Two Dirac Equations

The corpus writes the massive Dirac equation twice, and the two writings are not one equation. Parra's options belong to the second family, and the chirality cell is what they share with it.

**The one-sided chiral pair.** The biquaternion Dirac field is a section of the Dirac module $\Delta=S\oplus S^{\mathrm c}$, and its equation is the chirality-off-diagonal pair

$$
\boxed{\;L_{\tilde\nabla}\tilde\Psi_R=m\tilde\Psi_L,\qquad L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\tilde\Psi_R\;}
$$

with $\tilde\nabla=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ and $\tilde\nabla^{\natural}$ its quaternion conjugate. **Two equations, one per chirality.** Both gradients act on the left, so the pair is one-sided; at $m=0$ the two lines decouple into the two Weyl equations, and at $m\ne0$ the mass couples them off the diagonal.

**The two-sided single equation.** Read on the algebra rather than on the module, the same physics is one equation whose two sides are the two multiplications,

$$
\boxed{\;L_{\tilde\nabla^{\natural}}F=m\chi\bar F\;}
$$

with $\bar F$ the coefficient conjugate — the corpus's display $\tilde\nabla^{\natural}F=-mi\,\bar F\vec e_z$, the same equation, since by the definition of the cell $m\chi\bar F=-im\bar F\vec e_z$. The derivative acts on the left and the mass on the right, through the chirality cell; the mass term carries the conjugation, and it is that conjugation which supplies the second field of the pair.

**Where Parra's options sit.** In this parlance an option of Parra is a **two-sided** equation: the derivative on the left, the spin bivector and the mass on the right. The right multiplier of the spin bivector is the chirality cell up to the central factor,

$$
R_{e_{21}}=-i\,\chi,\qquad (R_{e_{21}})^2=(-i)^2\chi^2=-I_4,\qquad \chi^2=I_4 .
$$

The first identity is the dictionary of *The Legacy Pauli Gamma Formulation*: the spin bivector is the frame product $e_2e_1=-\vec e_z$, and the cell of a product is the composition of the cells, $R_{e_{21}}=R_{-\vec e_z}^{\mathrm{axf}}=-R_{\vec e_z}^{\mathrm{axf}}$. The two squares are the second point. Right multiplication by the spin bivector is a **complex structure** on the module, and right multiplication by the chirality cell is an **involution**; the two differ by a factor $i$, and $i^2=-1$ is the whole of the difference. The corpus's Hestenes article separates the same two objects by the same test, giving the phase to the spin plane, $(\omega\sigma_3)^2=-1$, and not to the chirality; in the cell language the test is the square, $-I_4$ against $I_4$. That is the precise sense in which the options join the two-sided operator theory to chirality: the object Parra multiplies on the right and the object the two-sided equation multiplies on the right are the same cell up to the central sign.

**The odd velocity.** Parra's mass term multiplies by the velocity $e_0$, an odd element, and an even field multiplied on the right by an odd element leaves the even carrier, so the term sits in the odd sector of the algebra. The corpus writes the same structure inside the even carrier as the chirality cell acting on the conjugated field, $m\chi\bar\Psi$: the conjugation absorbs the oddness, and the fixed direction plays the part of the velocity — a conjugation and a fixed direction, and nothing else. Daviau's $m\varphi^{*}$ is the same replacement in the space Clifford algebra. The two mass terms are one structure in two carriers, and the article writes the corpus's representative throughout. What the passage costs is linearity: Parra's mass term is linear in the field and the corpus's is antilinear, which is the difference the companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* records between the two kinds of mass.

## The Discrete Group and the Discrete Symmetries

**Statement (the permutations of the options).** The transformations that connect the four Parra options form the quotient

$$
\boxed{\;D=\Gamma_{1,3}/\Gamma^{0}_{1,3},\;}
$$

the Clifford–Lipschitz group modulo the component of its identity. Its three non-identity cosets are **space inversion** (determinant $-1$, time orientation kept), **time reversal** (determinant $-1$, time orientation reversed) and their product $PT$ (determinant $+1$, time orientation reversed), which the Clifford convention calls **charge conjugation**. The determinant and the time orientation are the two signs that name a component of $O(1,3)$, so the three cosets are the three non-identity pairs of signs; the element $PT$ acts as $x_\mu\mapsto-x_\mu$. The four options are the orbit of any one of them under $D$, and the four particle labels $e^\pm_{\uparrow\downarrow}$ are the labels of that orbit.

The quotient $D$ is a discrete group of order four. The Lipschitz group has four components, distinguished by the signs of the determinant and of the time orientation, and $\Gamma^{0}_{1,3}$ is the component of the identity, the proper orthochronous elements, which cover $SO^{+}(1,3)$ two-to-one; modulo the positive scalars they are $SL(2,\mathbb C)$, the unit-norm biquaternions. The quotient by it leaves exactly four cosets, one per component, and the three non-identity ones are the three discrete reflections. The quotient by the **even part** is not this group. A product of $k$ reflections has an image of determinant $(-1)^k$, so on the Lipschitz group the determinant of the image is the Clifford grading, and the even part is its kernel; the quotient by the even part has order two, carries that single bit, and cannot separate four options, because space inversion and time reversal are both odd. The four options therefore require the quotient by the identity component and not by the even part, and the article uses that one. Acting on the spinor module, a discrete reflection — any transformation outside $\Gamma^{0}_{1,3}$, odd or even in the Clifford grading — changes the relative signs of the gradient and coupling terms in the way displayed above, and the four options are the four sign patterns so obtained. Which of the three non-identity cosets flips which sign is the content of open question 3; the counting does not fix it, and nothing below depends on the choice.

**What the corpus already has.** The corpus contains each of the three symmetries separately:

- *Charge conjugation* is built in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* from the algebra's real structure $\flat$ and the $\mathrm{Spin}^c$ structure, and in the spacetime-algebra language it is a right multiplication by a fixed bivector, as recorded in *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* (open question 4).
- *Parity and time reversal* are the reflections of *The Reflection and the Rotation in Biquaternionic Form*, where the grading by reflection count is set up and where the timelike generator and conjugation by it are treated.
- The combined statement is the corpus's *The CPT Theorem in Biquaternionic Form*.

**What the corpus does not have.** Nowhere does the corpus assemble these three symmetries into a **group acting on a set of inequivalent equations**, and nowhere does it identify the four particle types — electron and positron, spin up and spin down — with the orbit of that action. That is the new object this article contributes. In the corpus's usual interpretation the symmetries act on **one field** and the particle types are labels on the solution space; here the symmetries act on the **set of equations**, and the particle types are labels on the orbit. The two interpretations are compatible, and the second makes explicit what the first leaves implicit: the four types are not four solutions of one equation but four sign conventions of one equation, permuted by the discrete group.

**Remark (the discrete group is the quotient, not the full Lipschitz group).** The quotient $D=\Gamma_{1,3}/\Gamma^{0}_{1,3}$ has order four, and its action on the options is free and transitive, so the four options form a single orbit of four elements — the permutation being the one the source records, not one the article derives. The double cover is invisible at this level: a Lipschitz element and its negative give the same transformation of the equation, which is why the corpus's articles on the spinor module record the double cover separately (*The Spinor Module in Biquaternionic Form and Its Lorentz Action*). The article does not claim that $D$ is the Lipschitz group; it is the quotient, and the quotient is what acts on the options.

## The Klein Four of the Conjugations

The discrete group $D$ of the previous section is the quotient of the Clifford–Lipschitz group by the component of its identity. The same abstract group is met again, purely inside the algebra, as the group generated by the algebra's conjugations, and the block structure of *The Biquaternion Space, the Group of Involutions and the Six Subspaces* binds the two. This section writes the table and reads the three symmetries on it.

**The blocks.** The eight real coordinates group into four blocks, written here $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$: the material time $T_{\mathrm m}=\mathbb R(ie_t)$, the informational time $T_{\mathrm i}=\mathbb R(e_t)$, the material space $X_{\mathrm m}=\mathbb R(\vec e_x,\vec e_y,\vec e_z)$ and the informational space $X_{\mathrm i}=iX_{\mathrm m}$. These are the blocks $A_2,A_1,B_1,B_2$ of *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, which writes them in the order $A_1,A_2,B_1,B_2$. With the blocks in the order $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$, the sign of each map on each of the four blocks is

| map | sign on $(T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i})$ | fixed space | type |
|---|---|---|---|
| $1$ | $(+,+,+,+)$ | $\mathbb{B}$ | identity |
| $\bar{\cdot}$ | $(-,+,+,-)$ | $\mathbb{H}_{\mathbb{B}}$, the real quaternions | anti-linear automorphism |
| ${}^{\natural}$ | $(+,+,-,-)$ | $\mathbb{C}_{\mathbb{B}}$, the centre | linear anti-automorphism |
| ${}^{*}={}^{\natural}\bar{\cdot}$ | $(-,+,-,+)$ | $\mathbb{M}_+$, the informational sector | anti-linear anti-automorphism |
| $\flat=-{}^{*}$ | $(+,-,+,-)$ | $\mathbb{M}_-$, the material sector | anti-linear, reverses products with a twist: $(\tilde Q_1\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde Q_1^{\flat}$ |

The first four rows are the Klein four $\{1,\bar{\cdot},{}^{\natural},{}^{*}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$, and the four blocks are indexed by its four characters: each block is a joint eigenspace, and the sign pattern on it is the value of the character that indexes it. That is why the block decomposition is canonical. The last row is **not** a fifth group element: $\flat$ differs from ${}^{*}$ by the central sign, and its sign pattern is the negative of the row of ${}^{*}$. It is the fifth pattern and not a fifth character, and the charge-conjugation pairing is read on it below. The columns and the fixed spaces are *The Biquaternion Space, the Group of Involutions and the Six Subspaces*'; the table is restated here because the discrete symmetries are read on it.

**Interpretation (the three symmetries on the characters).** The block action identifies the non-trivial characters with the discrete symmetries, the assignment being fixed by the standard transformation properties.

- **Parity $P$ is ${}^{\natural}$.** It fixes the two temporal blocks and negates the two spatial ones, sending the material four-vector $ict'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ to $ict'\,e_t-(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$: space inverted, time kept. It is $\mathbb{C}$-linear, the algebraic form of the unitarity of parity.
- **Time reversal $T$ is $\bar{\cdot}$.** It negates the material time $T_{\mathrm m}=\mathbb{R}(ie_t)$ — the $ict'$ direction — and the informational space $X_{\mathrm i}$, and fixes the material space, so on the material sector it is the flip of the time direction alone. It is **anti-linear**, which is the anti-unitarity of time reversal. The corpus reaches the same object as the anti-linear part of $T$ (*The CPT Theorem in Biquaternionic Form*).
- **The full reflection $PT$ is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$**, negating both material blocks, that is $x_\mu\mapsto-x_\mu$ on the material sector.
- **Charge conjugation is read on $\flat=-{}^{*}$, the real structure.** It fixes the material sector and negates the informational one, and it is anti-linear. It is level 1 of the four levels at which the corpus uses the name (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*): at the algebra level $\flat$ carries the **shape** of the pairing, whereas the operation itself is level 3 and lives on the module,

    $$
    \mathcal{C}[\psi]=\eta_C\,\psi^{*},\qquad \eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \eta_C^2=I_4 ,
    $$

  with $\psi^{*}$ the module conjugation and $\eta_C$ an **odd** cell (*Charge Conjugation and the Division Ring*). The bilinear is its second realization, $\psi^{\mathsf T}\eta\psi$ with the **even** cell $\eta=L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=R_{\vec e_x}^{\mathrm{axf}}$, whose square is $-I_4$, the square spending $\vec e_x^2=-e_t$; the sign that separates the two cells' squares is the division-ring sign the companion article records. That the shape is a pattern and not a group element is the algebraic statement that $C$ does not join $\{1,P,T,PT\}$ as an independent factor but is the sign that turns $PT$ into its negative.

**Caution (the second dictionary).** The Clifford-algebra literature attaches the names differently: with the generators $i\vec e_k$ of $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, the grade involution is read as $P$, the reversion as $T$ and the Clifford conjugation as $PT$ (*The CPT Theorem in Biquaternionic Form*, quoting the literature). Since the grade involution is $\bar{\cdot}$, the reversion ${}^{*}$ and the Clifford conjugation ${}^{\natural}$, that dictionary reads $P=\bar{\cdot}$, $T={}^{*}$, $PT={}^{\natural}$ — the transpose of the interpretation above. Both dictionaries are labelled and neither is proved in the corpus; the difference is the choice of which structure is called space inversion, and the interpretation above is the one whose parity fixes time and negates space. The table is the fact, the naming is the interpretation, and the article keeps the two apart.

The two dictionaries are visible even inside this article. The previous section's quotient $D=\Gamma_{1,3}/\Gamma^{0}_{1,3}$ has for its three non-identity cosets space inversion, time reversal and their product, and its orbit of four options therefore reads $C$ as that product $PT$ — the Clifford convention. The interpretation above instead places the three characters on $\{P,T,PT\}$ and the **shape** of the charge-conjugation pairing on the fourth pattern $\flat$ (*The Biquaternion Space, the Group of Involutions and the Six Subspaces*); the operation itself is defined at the module level, and the four levels of the name are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. The section records the difference rather than hiding it: the symmetries are a group of order four either way, and the question is only which of the four characters each one occupies.

## Why the Matrix Formulation Mixes the Options

The reason the four options are worth isolating is the failure of the matrix formulation to keep them apart. In the matrix Dirac theory a **complex linear combination** of the four components of the spinor is a standard operation — it is how one rotates the spinor, changes basis, or forms a plane wave. Such a combination **mixes the four options**: a complex linear combination of two solutions of different options is, in general, a solution of none of the four, and the relative signs cannot be undone. Fauser's formulation of the point: a complex linear combination intermingles the different Parra options "without any chance to re-obtain them as different equations".

The exact reason is the one displayed with the spinors, and it is narrower than the remark suggests. Of the three maps between the options one is the real permutation $\Pi$ and two are conjugations; since a real matrix is complex-linear, the four options fall into the two complex-linear classes $\{0\}\sim\{3\}$ and $\{2\}\sim\{1\}$, and the four transitions between the classes are antilinear. The invariant of the class is the product of the two signs of the equation: options $\{2\}$ and $\{1\}$ have agreeing signs, options $\{0\}$ and $\{3\}$ disagreeing ones, and a conjugation is exactly what turns agreement into disagreement. A formalism whose operations on spinors are complex-linear therefore separates the options into two types and no further; the datum that separates the two members of a class is the choice of the real form, which is precisely what the complex formalism does not carry.

This is the algebraic content of a familiar physical fact. In passing from the Dirac equation to quantum electrodynamics one must introduce **separate creation and annihilation operators for each of the four types** — a distinct pair for the particle and for the antiparticle, and for each spin polarisation. The formalism of the second quantised theory already "takes care of the different types of spinors", in Fauser's phrase, precisely because the first-quantised matrix formalism does not: the distinction is carried by a conjugation, and the operations of that formalism are complex-linear. Parra's four options make the distinction manifest by refusing the complexification — the spinors are real, the equations are real, and the four types are four inequivalent real equations rather than four components of one complex spinor.

**What this does and does not say.** It does **not** say that the second quantisation of the Dirac field is derivable from the four options, and it does not say that the four options replace the spin polarisation sum of quantum electrodynamics. It says that the algebraic necessity of separate field operators for the four types has a first-quantised shadow: the four options are not equivalent under the complex-linear operations that the matrix formalism performs on spinors, so the matrix formalism cannot represent the four types by one complex spinor without losing the distinction. The corpus records this as the source's **physical interpretation** and does not go further.

## The Quaternion and Matrix Forms of the Parra Spinors

Parra's spinors have a compact quaternion form. With the real quaternion basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and quaternion conjugation $^{\natural}$ — written $\bar q$ in the displays below, and distinct from the coefficient conjugation $\bar{\cdot}$ of the table above — the spinor of option $\{r\}$ is

$$
\boxed{\;\Psi_r=q_{r1}+i\,\bar q_{r2},\;}
$$

the sum of a quaternion and $i$ times a conjugate quaternion. An element of $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ is a pair of quaternions, and the pair is displayed in the standard block form, the matrix spinor

$$
\Psi_{\{r\}}=
\begin{pmatrix}q_{r1}&-\bar q_{r2}\\ \bar q_{r2}&q_{r1}\end{pmatrix}.
$$

The matrix is not a decorative rewriting: the map $\Theta$ that sends $q_1+i\bar q_2$ to that matrix is **multiplicative**. The product of two spinors is $(q_1+i\bar q_2)(p_1+i\bar p_2)=(q_1p_1-\bar q_2\bar p_2)+i\,(q_1\bar p_2+\bar q_2p_1)$, and the block product of the two matrices reproduces the two entries exactly, so $\Theta(\Psi\Psi')=\Theta(\Psi)\Theta(\Psi')$; the map is an algebra isomorphism onto the matrices of that block form, and the $2\times2$ structure is a matrix representation of the complex structure $(1,i)$. The product was recomputed on generic quaternion pairs.

**Proposition (the quaternion form is the corpus's field).** The map $q_{r1}+i\bar q_{r2}\mapsto\Psi_{\{r\}}$ sends the Parra spinor of each option into the biquaternion algebra $\mathbb B\cong\mathbb C\otimes_\mathbb R\mathbb H\cong\mathrm{Cl}^{+}_{1,3}$, and under the corpus's matrix representation $\Phi$ the result is a general element of $M_2(\mathbb C)$ — that is, a general biquaternion on the eight real parameters, exactly the corpus's Dirac field.

*Proof.* A quaternion $q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ has four real parameters and $i\bar q$ has four more, so $q_{r1}+i\bar q_{r2}$ ranges over the eight-dimensional real algebra; the matrix display is the action of the complex structure on the pair, and $\Phi$ realises it as an element of $M_2(\mathbb C)$. The identification of the general element with the corpus's field is the eight-component match of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*.

This places the Parra spinors in the same family as the Daviau spinor and the Dirac–Hestenes spinor: all three are general elements of the biquaternion algebra on eight real parameters, and the differences between the formulations are the sign conventions and the basis choices, not the size of the spinor. The quaternion form shows this directly.

## The Spin-Particle Clifford Bundle

Fauser draws a structural conclusion from the four options. In the geometric-algebra literature the spinor bundle is often built from the **spin Clifford bundle** of Rodrigues and collaborators, whose typical fibre at a point is a space of idempotents. Fauser submits that this fibre is **too large**: idempotents related by a rotor describe the same spinor, and nothing in the construction separates the four Parra types. What the four options suggest is a smaller bundle, the **spin-particle Clifford bundle**, whose fibre is the set of **equivalence classes of idempotents under the rotor group** — the identity component $\Gamma^{0}_{1,3}$ — so that two idempotents lie in the same class exactly when the corresponding spinors are of the same Parra type. The commutator relation, and hence the Clifford structure, is invariant under the discrete transformations of the Clifford–Lipschitz group, so the refinement is well defined.

**Relation to the corpus.** The corpus's own spinor picture is the Peirce carrier $\mathbb B\tilde\Pi_1$ generated by a primitive idempotent, a minimal left ideal here, developed in *Peirce Carriers and Inner Conjugation*, *Peirce Decompositions of the Biquaternion Algebra* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*. The spin-particle bundle is that picture with the idempotent replaced by its equivalence class **modulo the rotor group**, and the four Parra types are the four classes that this relation does not identify. In the corpus's language the refinement is: the Peirce carriers of $\mathbb B$ carry the spinor of the theory, and the discrete quotient $D$ acts on the set of idempotents by the discrete reflections.

*Proof sketch.* In Fauser's reading two spinors of the same Parra type are related by a rotor, so their idempotents are equivalent under the rotor group and lie in the same class; two spinors of different types require a transformation outside $\Gamma^{0}_{1,3}$, so their idempotents are inequivalent. The four classes are the four options. The identification of the classes with the options is Fauser's proposal; the corpus records it as a proposal and not as a theorem, since the even equivalence relation is not written out explicitly in the source.

## Open Questions

1. **The equivalence relation on idempotents.** What exactly is the relation modulo the rotor group whose classes are the four Parra types? In the corpus's terms, the classes are orbits of a primitive idempotent under the rotor group; the relation should be exhibited on the corpus's own idempotents $\tilde\Pi_1$, $\tilde\Pi_2$ and their Peirce companions.

2. **Which option is the framework's?** The corpus's Dirac equation as written in *The Dirac Equation in Biquaternionic Form* has its own sign conventions. Which of the four Parra options does it correspond to under the corpus's dictionary, and is the correspondence stable across the article's solutions and its non-relativistic limit?

3. **The discrete symmetries as a permutation group.** The corpus has each of $P$, $C$, $T$ acting on one field. Does the extension to a group acting on the set of four equations reproduce the corpus's $C$ (the $\flat$ real structure and the right multiplication by a bivector) and its $P$, $T$ (the reflections of the grading article) with the correct permutation, and which of the three real-linear maps between the options is the charge conjugation? Two of the three are antilinear, so the question is a sharp one.

4. **The odd velocity inside the even carrier.** The mass term $m\chi\bar\Psi$ replaces $m\Psi e_0$ by a conjugation together with the chirality cell. Is that replacement unique, or is it one of several even-carrier representatives of the same odd structure, and does the choice leave the four options' orbit intact?

5. **Spin polarisation and second quantisation.** The four options are four first-quantised equations. Is there a sense in which the four creation and annihilation operator pairs of the second quantised theory — one per type — are the four Fourier components of the option orbit, and does the corpus's path-integral formalism see them?

6. **The spin-particle bundle in the corpus's topology.** The corpus has a topology of the biquaternion unit group and of the null cone (*The Biquaternion Unit Group as a Topological Group*). Does the spin-particle bundle, with its finer fibres, have a characteristic class that the spin Clifford bundle does not, and is that class visible in the corpus's topological articles?

7. **Empirical contact.** None is claimed. The options are equivalent rewritings; the question, as everywhere, is whether isolating them makes a structural fact of the framework easier to see.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The left and right multiplications act by $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and the four frame cells and the chirality cell of the body become

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}
$$

In the axis-free display:

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}
$$

The four frame cells satisfy the cell relation of $\varepsilon=(1,-1,-1,-1)$, and their squares are $\pm I_4$:

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad (\gamma_0)^2=I_4,\qquad (\gamma_k)^2=-I_4\ \ (k=1,2,3) ,
\qquad \varepsilon=(1,-1,-1,-1),$$

The chirality cell is the fifth: it is the cell $\chi$ of the body, and it anticommutes with all four,

$$
\gamma_5=\chi=-iR_{\vec e_z}^{\mathrm{pau}},\qquad \gamma_5^2=I_4,\qquad \{\gamma_\mu,\gamma_5\}=0 .
$$

The same identities in the axis-free display:

$$
\gamma_5=\chi=-iR_{\vec e_z}^{\mathrm{axf}},\qquad \gamma_5^2=I_4,\qquad \{\gamma_\mu,\gamma_5\}=0 .
$$

All of these were recomputed on the module's explicit $4\times4$ representation. The cells of the body are sums of such products: a single product $L_aR_b$ is a pure tensor, the pure tensors form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element of $M_4(\mathbb C)$ is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

**The spin bivector.** The identity behind the body's spin cell is read off the frame,

$$
\gamma_2\gamma_1=-L_{\vec e_z}^{\mathrm{pau}},\qquad\text{hence}\qquad e_{21}=-\vec e_z,\qquad R_{e_{21}}=R_{-\vec e_z}^{\mathrm{pau}}=-i\,\chi ,
$$

Read in the axis-free display:

$$
\gamma_2\gamma_1=-L_{\vec e_z}^{\mathrm{axf}},\qquad\text{hence}\qquad e_{21}=-\vec e_z,\qquad R_{e_{21}}=R_{-\vec e_z}^{\mathrm{axf}}=-i\,\chi ,
$$

using $\chi=-iR_{\vec e_z}^{\mathrm{pau}}$ and $R_{-\vec e_z}^{\mathrm{pau}}=-R_{\vec e_z}^{\mathrm{pau}}$ in the last step. As an operator the bivector is the left multiplication by the frame product; as an element of the even algebra it is $-\vec e_z$. The spin *cell* that Parra's equation applies to the field is the right multiplication by that element, and it coincides with the chirality cell up to the central factor. That is the whole of the correspondence, and it needs no second imaginary unit: $(-i\chi)^2=(-i)^2\chi^2=-I_4$ while $\chi^2=I_4$, the factor $i^2=-1$ being the only place a sign is spent.

**The chirality operator and its representative.** $\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. The corpus writes the two with the same letter and separates them by the subscript (*The Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form*); this article keeps that spelling. The abstract sign is central and squares to the identity of the algebra; its representative is a cell and squares to the identity of the module.

The dictionary is complex-linear: over $\mathbb{R}$ the sixteen products of the frame cells span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and over $\mathbb{C}$ they span $M_4(\mathbb{C})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Parra's four options are four inequivalent ways of reading the eight real Dirac equations as vector equations, arising from the four choices of which component's real part is declared scalar. They yield four equations differing only in the signs of the gradient and coupling terms, with the same spin cell and the same mass term. Option $\{2\}$ is the Dirac–Hestenes equation and option $\{1\}$ is the Daviau space Clifford equation; the other two are new. All four multiply the field on the right by the spin bivector and by the mass, so they share the bi-module structure of the corpus's two-sided algebra, and the spin cell is the chirality cell up to the central factor, $R_{e_{21}}=-i\chi$. The four spinors are related by signed permutations, one complex-linear and two antilinear; that split is the two complex-linear classes of options, and it is the first-quantised shadow of the separate creation and annihilation operators of quantum electrodynamics, one pair per type.

The options are permuted by the discrete quotient $D=\Gamma_{1,3}/\Gamma^{0}_{1,3}$, whose three non-identity cosets are space inversion, time reversal and their product, and Parra labels the orbit by electron and positron, spin up and spin down. The quotient is taken by the component of the identity and not by the even part: the even part has index two and cannot separate four options. The Parra spinors have a quaternion form, and they are general elements of the biquaternion algebra, exactly the corpus's Dirac field on eight real parameters. Fauser's structural conclusion is a refinement of the spin Clifford bundle to the **spin-particle Clifford bundle**, whose fibre is a set of classes of idempotents modulo the rotor group; in the corpus's terms this is the minimal-left-ideal picture of the spinor with the idempotent taken modulo the rotor group, and the four Parra types are the four classes. The article records the construction as Parra's and Fauser's, reproduces it in the corpus's cells, and claims no new physics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Psi_{\{r\}}$, $r=0,1,2,3$ | The Parra spinor of option $\{r\}$, a four-component complex spinor |
| $\alpha,\lambda$ | The two scalars of the vector interpretation |
| $\vec E=(E_1,E_2,E_3)$, $\vec B=(B_1,B_2,B_3)$ | The two vectors of the vector interpretation |
| $\vec s=-i\vec S$ | The spin vector; $\vec S$ real, so $\vec s=\vec s^{*}$ under $^{*}=\bar\cdot\circ{}^{\natural}$ and $\vec s$ lies in $X_{\mathrm i}$ |
| $L_a$, $R_b$, $L_aR_b$ | Left, right and two-sided multiplication; $L_aR_b\psi=a\psi b$ and $L_aR_b\,L_cR_d=L_{ac}R_{db}$ |
| $\Gamma_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}$ | The four frame cells, $\tau(t)=x$ and $\tau(k)=y$; $\{\Gamma_\mu,\Gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ |
| $\chi=R_{-i\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ | The chirality cell, a right-multiplication cell, $\chi\psi=-i\psi\vec e_z$; $\chi^2=I_4$ and $\{\Gamma_\mu,\chi\}=0$ |
| $R_{e_{21}}=R_{-\vec e_z}^{\mathrm{axf}}=-i\chi$ | The right cell of the spin bivector; $(R_{e_{21}})^2=(-i)^2\chi^2=-I_4$ |
| $\mathcal{D}=\Gamma_\mu\partial/\partial x_\mu$ | The gradient cell of the body |
| $\nabla$, $A$, $m$, $ϙ$ | The multivector gradient, the potential, the mass and the charge of the source's displays; $ϙ$ is the corpus glyph and is not the quaternion components $q_{rj}$ |
| $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ | The central grading of the complexified algebra, $\chi_{\mathrm{ad}}^2=e_t$; a different object from the chirality cell $\chi$, and named only in the closing section |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | Biquaternionic gradient and its quaternion conjugate; $L_{\tilde\nabla}$ is the one-sided Dirac operator |
| $\Gamma_{1,3}$, $\Gamma^{+}_{1,3}$, $\Gamma^{0}_{1,3}$ | Clifford–Lipschitz group, its even part, and the component of its identity |
| $D=\Gamma_{1,3}/\Gamma^{0}_{1,3}$ | The discrete quotient; order four, permuting the four options |
| $e^{\pm}_{\uparrow\downarrow}$ | Parra's particle labels: electron/positron, spin up/down |
| $\Pi$, $J_2$, $J_1$ | The real permutation and the two signed permutations relating the four spinors: $\Psi_{\{3\}}=\Pi\Psi_{\{0\}}$ complex-linearly, $\Psi_{\{2\}}=J_2\bar\Psi_{\{0\}}$ and $\Psi_{\{1\}}=J_1\bar\Psi_{\{0\}}$ antilinearly |
| $\Psi_r=q_{r1}+i\bar q_{r2}$ | The quaternion form of the Parra spinor; $\bar q$ is quaternion conjugation in that display only |
| $T_{\mathrm m},T_{\mathrm i},X_{\mathrm m},X_{\mathrm i}$ | The four blocks: material time $\mathbb R(ie_t)$, informational time $\mathbb R(e_t)$, material space, informational space $iX_{\mathrm m}$ |
| $\eta=L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=R_{\vec e_x}^{\mathrm{axf}}$ | The **even** cell of the charge-conjugation bilinear, $\psi^{\mathsf T}\eta\psi$; $\eta^2=-I_4$ |
| $\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The **odd** cell of the operation $\mathcal{C}[\psi]=\eta_C\psi^{*}$; $\eta_C^2=I_4$ |
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra; the corpus's Dirac field on eight real parameters |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §2.3, for the four options, their permutation group and the spin-particle bundle; the source of this article.
- J. M. Parra-Serra, "On Dirac and Darwin–Hestenes equation," in *Proceedings of the Conference on Clifford Algebras* (1989), and "Dirac's theory in real geometric formalism: multivectors versus spinors" (unpublished), for the original analysis. The corpus has not consulted these; they are cited through Fauser.
- W. A. Rodrigues Jr., E. C. de Oliveira and others, on the spin Clifford bundle, referred to by Fauser for the comparison with the spin-particle bundle.
- A. Crumeyrolle, *Orthogonal and Symplectic Clifford Algebras* (Kluwer, 1990), for the invariance of the Clifford structure under the odd transformations of the Clifford–Lipschitz group.
- The companion articles of this series: [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html), [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html), [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html), [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html), [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html), [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), and [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html).
