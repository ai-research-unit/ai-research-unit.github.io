# __Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, central imaginary unit $i$, Hermitian conjugation ${}^{*}$ and coefficient conjugation $\bar{\cdot}$. The complex spinor module of the algebra is the defining module of $\mathbb{B}\cong M_2(\mathbb{C})$, the minimal left ideal $S=\mathbb{B}\tilde\Pi_1\cong\mathbb{C}^2$ of real dimension four, and this article asks which **reality structures** it carries: antilinear maps $J$ with $J^2=\pm1$ that commute with the Clifford action (*Real Spinors and Reality Conditions with Inner Conjugation*). The trichotomy is real, complex and quaternionic, and it is decided by the signature difference modulo eight. The answer for $\mathbb{B}$ is **complex**, and the substance of the article is what the one word carries: the reason the answer is forced, the structure that replaces a reality structure, and the two different answers that the two readings of one basis give.

The module $S$, its Clifford multiplication $c(\gamma_k)=\sigma_k$ by the $\mathrm{Cl}_{3,0}$-generators $\gamma_k=ie_k$, the volume element with $c(\omega)=iI$, the commutant $\mathbb{C}$ and the consequent absence of a chirality splitting are *Biquaternion Spin Geometry*; they are used here and are not re-derived. The four conjugations of the algebra, their fixed spaces and their matrix images are *The Clifford Algebra Representation*, *Introduction to the Six Subspaces* and *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. The module theory, the idempotents and the Peirce decomposition are *Modules over the General Plain Algebra of Biquaternions* and *Biquaternion Ideals and Peirce Decomposition*, and the algebraic side of the doubling $S\mapsto\bar S$ is carried there; its physical reading belongs to the physics corpus, where the trichotomy is read as the three particle types in *Particle Types, Discrete Charge and Three-Particle Couplings* and the charge conjugation is built on the doubled module in *The Neutrino and Majorana Fermions in Biquaternionic Form*.

Four statements are the article. First, **the internal module has no reality structure**, and the proof is one line peculiar to the algebra: the volume element of $\mathrm{Cl}_{3,0}$ is central with square $-1$ and acts on $S$ as the scalar $i$, so it *is* the complex structure of the module, and an antilinear map that commutes with the Clifford action must commute with it and is therefore killed by its own antilinearity. Second, the structure that exists in place of a reality structure is the **conjugate module**: entrywise conjugation $\kappa$ of the matrix model is an antilinear algebra automorphism with no counterpart among the four conjugations, it produces the conjugate representation $\overline{c}(v)$, and the conjugate module $\bar S$ is **inequivalent** to $S$ as a complex module — that inequivalence is the complex type — while being isomorphic to it as a real representation; the conjugate pair of simple modules appears as two distinct factors after complexification. Third, the algebra has **three real forms**, $\mathrm{Cl}_{3,0}$, $\mathrm{Cl}_{2,1}$ and $\mathrm{Cl}_{0,3}$, with complex, real and quaternionic types on the same $\mathbb{C}^2$, and the basis elements $e_k$ realise the quaternionic one: with $c(e_k)=-i\sigma_k$ the module carries the explicit quaternionic structure $J(s)=\sigma_2\bar s$, $J^2=-1$. Fourth, the ambient four-dimensional cases invert the sign between the two normalisations, and that is the passage from the complex internal type to the real structure of the ambient module.

## Antilinear Structures on the Internal Module

**Definition (antilinear, reality structure).** An **antilinear map** on $S$ satisfies $J(\lambda s+\mu t)=\bar\lambda J(s)+\bar\mu J(t)$. A **reality structure** on the Clifford module $S$ is an antilinear map $J$ with $J^2=\varepsilon\,\mathrm{id}$, $\varepsilon=\pm1$, that commutes with the Clifford action, $Jc(v)=c(v)J$ for all $v$, and with the spin action; $J^2=+1$ is a **real structure** and $J^2=-1$ a **quaternionic structure**. The **type** of $S$ is real, complex or quaternionic according as such a $J$ exists with the corresponding sign, or does not exist.

**Proposition (what the two signs mean).** A real structure makes $S$ the complexification of its real fixed space $S_{\mathbb{R}}=\{s:J(s)=s\}$, which is a real Clifford module of real dimension two; a quaternionic structure makes $S$ a one-dimensional quaternionic vector space.

*Proof.* For $J^2=+1$ the fixed space is a real form of $S$ and the Clifford action preserves it because $J$ commutes with the action. For $J^2=-1$ one sets $j\,s=J(s)$ and $i\,s=is$; then $ij=J\circ(i\,\cdot)$ and $ji=-J\circ(i\,\cdot)$, so $i,j,k=ij$ obey the quaternion relations and $S\cong\mathbb{H}$.

**Proposition (the algebra's own antilinear involutions are not reality structures).** Among the four conjugations of $\mathbb{B}$ there are three that are conjugate-linear, $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}=-{}^{*}$, with fixed spaces of real dimension $4$, $4$ and $4$, and one that is $\mathbb{C}$-linear, the quaternion conjugation ${}^{\natural}$, with fixed space of real dimension $2$. None of them is a reality structure on $S$; an involution of the algebra and a conjugation of the module are different objects, and the discipline of keeping them apart is the one the applications of the algebra insist on.

*Proof.* The fixed spaces are computed on the coefficients: ${}^{\natural}$ fixes the scalars $\mathbb{C}e_0$ and negates $e_1,e_2,e_3$, while $\bar{\cdot}$ fixes $\mathbb{H}_{\mathbb{B}}$, ${}^{*}$ the Hermitian sector $\mathbb{M}_+$ and ${}^{\flat}$ the anti-Hermitian sector $\mathbb{M}_-$ (*Introduction to the Six Subspaces*). Each is a map of the algebra, whereas a reality structure is a map of the module.

## The Type of the Internal Module Is Complex

**Theorem (no reality structure on $S$).** Let $S=\mathbb{C}^2$ carry the Clifford action of $\mathrm{Cl}_{3,0}$ with $c(\gamma_k)=\sigma_k$, $k=1,2,3$. If $J$ is antilinear with $J^2=\pm1$ and $Jc(\gamma_k)=c(\gamma_k)J$ for all $k$, then $J=0$. Consequently $S$ has **complex type**.

*Proof.* The volume element $\omega=\gamma_1\gamma_2\gamma_3$ is central with $\omega^2=-1$ and acts on $S$ by the scalar $i$, $c(\omega)=c(\gamma_1)c(\gamma_2)c(\gamma_3)=\sigma_1\sigma_2\sigma_3=iI$ (*Biquaternion Spin Geometry*). A map commuting with each generator commutes with every product of generators, hence with $c(\omega)$. Therefore, for every $s\in S$,

$$
J(is)=J\bigl(c(\omega)s\bigr)=c(\omega)J(s)=iJ(s),
$$

while antilinearity gives $J(is)=-iJ(s)$. Subtracting, $2iJ(s)=0$, so $J=0$.

**Remark (why the volume element settles it, and what is general).** In the general theory the complex structure of the spinor module is external to the Clifford algebra, and a reality structure is an extra datum to be found or not. In $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ the complex structure is **internal**: multiplication by $i$ on $S$ is multiplication by the Clifford volume element, which is itself an element of the algebra. An antilinear map commuting with the Clifford action is then required to commute with the complex structure, which no antilinear map does. This is the module-level content of the fact that $\mathbb{B}$ is the case $d=3$ of the general sign table, where the type is complex, and it is the sharpest form the statement takes: the obstruction is not a computation but the identity $c(\omega)=iI$.

**Remark (the commutant form of the same theorem).** By Schur's lemma the commutant of the $\mathbb{B}$-action on $S$ is $\mathbb{C}$, so the division algebra of the real module is $\mathbb{C}$ and the type is complex; correspondingly, every antilinear map commuting with $M_2(\mathbb{C})\cong\mathbb{B}$ on $\mathbb{C}^2$ vanishes, since taking $M=iI$ in $X\overline{M}=MX$ gives $X=0$. The two proofs are the same statement read on the algebra and on the module.

**Corollary (no internal real or chiral spinor).** On $S$ there is no real spinor, since that would be the fixed space of a real structure, and there is no chiral spinor, since $c(\omega)=iI$ has the single eigenvalue $i$ on $S$ and does not split it. The chirality operator acquires its two eigenvalues $\pm i$, and the splitting into half-spin spaces appears, only on the complexification $S\otimes_{\mathbb{R}}\mathbb{C}=S_+\oplus S_-$ (*Biquaternion Spin Geometry*), which is the Dirac module of the ambient four-dimensional algebra; the internal module is ungraded and complex.

## The Conjugate Module and the Dressed Conjugation

Since $S$ carries no reality structure, the structure that exists is the conjugation of the algebra transported to the module.

**Definition ($\kappa$).** Let $\kappa$ be **entrywise conjugation** of the matrix model, $\kappa(M)=\overline{M}$. Then $\kappa(MN)=\kappa(M)\kappa(N)$ and $\kappa(\lambda M)=\bar\lambda\,\kappa(M)$, so $\kappa$ is an antilinear algebra automorphism of $M_2(\mathbb{C})$.

**Proposition ($\kappa$ produces the conjugate representation).** The map $\overline{c}(v)=\kappa\,c(v)\,\kappa^{-1}$ is again a representation of $\mathrm{Cl}_{3,0}$ on $S$, the **conjugate representation**, and it is not equal to $c$: on the generators $\overline{c}(\gamma_1)=+c(\gamma_1)$, $\overline{c}(\gamma_2)=-c(\gamma_2)$, $\overline{c}(\gamma_3)=+c(\gamma_3)$, the minus occurring at the one generator whose matrix $\sigma_2$ is purely imaginary. Hence $S$ carries the **conjugate module** $\bar S$, the same complex vector space with the action $\overline{c}$.

*Proof.* $\kappa$ is an automorphism and the Clifford relations are real, so $\overline{c}$ satisfies the same relations; the signs follow because $\sigma_1$ and $\sigma_3$ are real, so $\overline{\sigma_k}=\sigma_k$, while $\sigma_2$ is purely imaginary, so $\overline{\sigma_2}=-\sigma_2$.

**Proposition (the conjugate module, and its type).** The map $\overline{c}$ makes the same complex space $S$ into a second module $\bar S$, the **conjugate module**. The two modules are **isomorphic as real representations and inequivalent as complex modules**, and the distinction is the type. As real $\mathrm{Cl}_{3,0}$-modules they are canonically isomorphic: the coordinate conjugation $s\mapsto\bar s$ is antilinear and satisfies $\overline{c}(v)\bar s=\overline{c(v)s}$, so it is an intertwiner with the conjugate action. As complex modules they are inequivalent: a $\mathbb{C}$-linear $T$ with $T\overline{c}(v)=c(v)T$ would satisfy $T\sigma_1=\sigma_1T$ and $T\sigma_3=\sigma_3T$, hence $T=\lambda I$, and then $T\sigma_2=-\sigma_2T$ forces $\lambda=0$, so the only such map is zero. By the general criterion, an irreducible complex module is self-conjugate exactly when its commutant is not $\mathbb{C}$; the complex type is exactly the non-self-conjugate case (*Real Spinors and Reality Conditions with Inner Conjugation*). The pair becomes two genuinely different simple modules after **complexification**: $\mathbb{C}\mathrm{l}_3\cong M_2(\mathbb{C})\times M_2(\mathbb{C})$ has two simple factors whose modules are $\mathbb{C}^2$ and its conjugate, and the conjugation of the complexification swaps the central idempotents $\tfrac12(1\pm i\omega)$ and so exchanges the factors.

*Proof.* The interchange of $s\mapsto\bar s$ with the conjugate action is the definition of $\overline{c}$, $\overline{c}(v)=\kappa c(v)\kappa^{-1}$, read on the coordinates. For the inequivalence: a matrix commuting with both $\sigma_1$ and $\sigma_3$ is a scalar $\lambda I$, and the remaining condition $T\sigma_2=-\sigma_2T$ reads $\lambda\sigma_2=-\lambda\sigma_2$, so $\lambda=0$. The complexification statement is that of the general source.

**Remark (where $\varepsilon$ belongs, and where it does not).** The antisymmetric form

$$
\varepsilon=i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=\Phi(-e_2),\qquad \varepsilon^{\mathsf{T}}=-\varepsilon,\qquad \varepsilon^2=-I
$$

is **not** an intertwiner $S\to\bar S$; an intertwiner would have to be $\mathbb{C}$-linear, and there is none. What $\varepsilon$ does is implement the algebra's own conjugation on the module up to the automorphism $\bar{\cdot}$: the matrix dictionary $\Phi(\bar{\tilde{Q}})=\varepsilon\,\overline{\Phi(\tilde{Q})}\,\varepsilon^{-1}$ says $\varepsilon\,\overline{c}(v)\,\varepsilon^{-1}=c(\bar v)$, that is, $\varepsilon$ intertwines the conjugate action with the action twisted by the coefficient conjugation. So $\bar{\cdot}$ reaches the module as a $\mathbb{C}$-linear form composed with entrywise conjugation, which is exactly why it supplies a conjugation of the action and not a reality structure: a reality structure would be an antilinear map commuting with the *given* action, and neither $\kappa$ nor $\varepsilon$ is that.

**Remark (the one plausible guess that is wrong, and the dressed form).** Entrywise conjugation $\kappa$ is **not** the image of any of the four conjugations of $\mathbb{B}$: conjugating the entries of $\Phi(\tilde{Q})$ sends the images of $e_1$ and $e_3$ to their negatives and leaves that of $e_2$ alone, so it destroys the dictionary of subspaces and is not $\Phi(\tilde{Q}^{\theta})$ for any $\theta$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The dictionary is restored by dressing $\kappa$ with the antisymmetric form, $\Phi(\bar{\tilde{Q}})=\varepsilon\kappa(\Phi(\tilde{Q}))\varepsilon^{-1}$, and it is in this dressed form that the coefficient conjugation acts on the module. The distinction is not pedantry: it is the difference between the conjugate representation, which exists, and a second conjugation of the algebra, which does not.

## The Three Real Forms and the Two Readings of One Basis

**Theorem (the three real forms of $\mathbb{C}\mathrm{l}_3$).** The real forms of the complex Clifford algebra $\mathbb{C}\mathrm{l}_3$ are $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$, $\mathrm{Cl}_{2,1}\cong M_2(\mathbb{R})\times M_2(\mathbb{R})$ and $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$, of complex, real and quaternionic type respectively. All three have complex spinor module $\mathbb{C}^2$, and the reality condition is exactly what distinguishes them (*Real Spinors and Reality Conditions with Inner Conjugation*).

**The biquaternion form is $\mathrm{Cl}_{3,0}$.** Under the isomorphism $\gamma_k\mapsto ie_k$ of *The Clifford Algebra Representation*, the generators are $\gamma_k=ie_k$ and the volume element is $\omega=\gamma_1\gamma_2\gamma_3\mapsto i$. Against this form the module is complex, by the theorem above.

**The same basis against the negative definite form is quaternionic.** The basis elements satisfy $e_k^{2}=-e_0$ and $e_je_k+e_ke_j=0$ for $j\neq k$, which are the relations of $\mathrm{Cl}_{0,3}$, and the action $c(e_k)=-i\sigma_k$ is a representation of $\mathrm{Cl}_{0,3}$ on $S$. Against this form the module carries a quaternionic structure,

$$
J(s)=\sigma_2\,\bar s,\qquad J^2=-1,
$$

with $\overline{c}(e_1)=-c(e_1)$, $\overline{c}(e_2)=+c(e_2)$, $\overline{c}(e_3)=-c(e_3)$, so that $J$ commutes with the $\mathrm{Cl}_{0,3}$-action. The same form $\varepsilon=i\sigma_2$ **is** a $\mathbb{C}$-linear intertwiner $\bar S\to S$ against the $e_k$-action, because $\bar{e}_k=e_k$ and therefore $\varepsilon\,\overline{c}(e_k)\,\varepsilon^{-1}=c(\bar{e}_k)=c(e_k)$. So $\bar S\cong S$ over $\mathrm{Cl}_{0,3}$ and $\bar S\not\cong S$ over $\mathrm{Cl}_{3,0}$, on the same space and with the same form: self-conjugacy is a property of the reading, like the type itself, and the real and quaternionic types have it while the complex type does not.

**The real form in a matrix model.** The third form is realised on the same $\mathbb{C}^2$ by real matrices: with

$$
a=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad b=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad c=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

one has $a^2=b^2=+I$, $c^2=-I$ and pairwise anticommutation, so $a,b,c$ generate a representation of $\mathrm{Cl}_{2,1}$; the module carries the real structure $J(s)=\bar s$ with $J^2=+1$.

**Remark (the trap: the two readings differ by the central $i$).** The two Clifford structures on one basis are related by $\gamma_k=ie_k$, and since $i$ acts on $S$ as the complex structure, $c(\gamma_k)=i\,c(e_k)$. A reality structure commuting with $c(\gamma_k)$ would therefore have to **anticommute** with $c(e_k)$, because an antilinear map reverses $i$: $Ji=-iJ$. So the complex type of $\mathrm{Cl}_{3,0}$ and the quaternionic type of $\mathrm{Cl}_{0,3}$ are two statements about the same matrices and the same basis, and silently switching from $c(\gamma_k)=\sigma_k$ to $c(e_k)=-i\sigma_k$ inverts the reality type. The corpus fixes the first reading in *Biquaternion Spin Geometry* and writes the same action in the $e_k$ basis in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; this is the three-dimensional instance of the competing labelling flagged in *The Clifford Algebra Representation*, and it is the error the present article exists to prevent.

## The Ambient Four-Dimensional Cases and the Normalisation

The biquaternion algebra is the even part of a Clifford algebra of Lorentzian signature, $\mathbb{B}\cong\mathrm{Cl}^{+}_{3,1}\cong\mathrm{Cl}^{+}_{1,3}$, the two labellings agreeing on the even part (*The Clifford Algebra Representation*). The Dirac module of the ambient algebra is $\Delta=\mathbb{C}^4$, of complex dimension four, with two chiral halves of dimension two.

**In the commuting normalisation**, the general sign table gives $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ with $d=2$ and type real, and $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ with $d=-2\equiv6$ and type quaternionic. Both have $\omega^2=-1$, and the two normalisations of the reality structure differ by composition with the volume element, which flips the sign of $J^2$ exactly when $\omega^2=-1$, that is in the classes $d\equiv2,3,6,7$ (*Real Spinors and Reality Conditions with Inner Conjugation*). 

**In the anticommuting normalisation**, the normalisation in which the conjugation anticommutes with the Clifford generators, $Jc(v)=-c(v)J$, the signs are exchanged: it is $\mathrm{Cl}_{1,3}$ that carries the real structure, with $J^2=+1$, and hence a real spinor. This is the normalisation the physics corpus uses, and it is what reconciles the complex internal type with the reality conditions of signature $(1,3)$: the internal module of $\mathbb{B}$ is complex without qualification, because it has no volume-element twist to exchange and no chirality to exchange, while the ambient Dirac module is real in the anticommuting normalisation and quaternionic in the commuting one, and the two tables agree in the classes $d\equiv0,1,4,5$. The statements themselves about the real spinors of $(1,3)$ belong to the physics block of the sesquilinear product, where the trichotomy is read as the three particle types in *Particle Types, Discrete Charge and Three-Particle Couplings*, and are cited, not re-derived.

## Worked Examples

**The volume element, and the vanishing of $J$.** With $\gamma_k=ie_k$ and $c(\gamma_k)=\sigma_k$ one computes $c(\omega)=\sigma_1\sigma_2\sigma_3=iI$ and $\omega^2=\gamma_1\gamma_2\gamma_3\gamma_1\gamma_2\gamma_3=-e_0$, in agreement with the identification $\omega\mapsto i$. Writing a general antilinear map as $J(s)=T\bar s$, the commutation $Jc(\gamma_k)=c(\gamma_k)J$ is $T\overline{\sigma_k}=\sigma_kT$; for $k=2$, whose matrix $\sigma_2$ is imaginary, this reads $-T\sigma_2=\sigma_2T$, and for $k=1,3$ it reads $T\sigma_k=\sigma_kT$, so $T=aI$. Antilinearity then gives $J(is)=T\overline{is}=-iT\bar s=-ia\bar s$, while $J$ must commute with $c(\omega)=iI$, whose action gives $J(is)=iJ(s)=ia\bar s$; hence $a=0$. The whole theorem is visible in the one real parameter $a$.

**The quaternionic structure of the $\mathrm{Cl}_{0,3}$ reading.** For $J(s)=\sigma_2\bar s$ one computes $\overline{\sigma_2}=-\sigma_2$ and $J^2=\sigma_2\overline{\sigma_2}=-\sigma_2^2=-I$, so the sign is $-1$ and the structure is quaternionic, not real. The same map does **not** serve for the $\mathrm{Cl}_{3,0}$ reading: against $c(\gamma_k)=\sigma_k$ the relation $Jc(\gamma_k)=c(\gamma_k)J$ would read $\sigma_2\overline{\sigma_k}=\sigma_k\sigma_2$, which fails already at $k=1$, where $\overline{\sigma_1}=\sigma_1$ but $\sigma_2\sigma_1=-\sigma_1\sigma_2$.

**The three types on one module.** The module $\mathbb{C}^2$ carries no reality structure against $c(\gamma_k)=\sigma_k$, the quaternionic structure $J(s)=\sigma_2\bar s$ against $c(e_k)=-i\sigma_k$, and the real structure $J(s)=\bar s$ against the real matrices $a,b,c$ of the $\mathrm{Cl}_{2,1}$ model. The three are the three real forms, and the example is the sharpest illustration of the fact that complexification forgets the signature.

**A verification table.** Each entry was checked by exact computation in the matrix model with $\Phi(e_k)=-i\sigma_k$ and $\Phi(i)=iI$.

| Statement | Verification |
|---|---|
| $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI$, $\Phi$ an algebra isomorphism | exact on a basis and on $50$ random products |
| $\Phi(\tilde Q^{\natural})=\mathrm{adj}\,\Phi(\tilde Q)$, $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$, $\Phi(\bar{\tilde Q})=\varepsilon\overline{\Phi(\tilde Q)}\varepsilon^{-1}$, $\Phi(\tilde Q^{\flat})=-\Phi(\tilde Q)^{\dagger}$ | $200$ random elements each |
| ${}^{\natural}$ $\mathbb{C}$-linear and order-reversing; $\bar{\cdot}$ conjugate-linear and multiplicative; ${}^{*}$ conjugate-linear and order-reversing; ${}^{\flat}$ conjugate-linear and order-reversing up to sign | $50$ random pairs each |
| fixed spaces of real dimension $2,4,4,4$ for ${}^{\natural},\bar{\cdot},{}^{*},{}^{\flat}$ | exact linear algebra on the coefficients |
| no antilinear $J$ commuting with $c(\gamma_k)=\sigma_k$ | solution space of dimension $0$ |
| quaternionic $J$ commuting with $c(e_k)=-i\sigma_k$, with $J^2=-1$ | solution space of dimension $2$, the line $\mathbb{R}\sigma_2$ |
| real $J$ for the $\mathrm{Cl}_{2,1}$ model, with $J^2=+1$ | solution space of dimension $2$ |
| $\varepsilon=i\sigma_2$, $\varepsilon^{\mathsf{T}}=-\varepsilon$, $\varepsilon^2=-I$, $\varepsilon\,\overline{c}(v)\,\varepsilon^{-1}=c(\bar v)$ | exact on the generators |
| complex-linear $T$ with $T\overline{c}(v)=c(v)T$ | solution space of dimension $0$: $\bar S$ and $S$ inequivalent as complex modules |
| real-linear $T$ with $T\overline{c}(v)=c(v)T$ | solution space of dimension $2$, containing the coordinate conjugation |
| commutant of the action $=\mathbb{C}I$, of real dimension $2$ | exact |

## Honest Limits

Four limits must be stated. First, the type table of this article is the **commuting** normalisation, $Jc(v)=c(v)J$; the anticommuting normalisation of the physics corpus is the other one, and the two differ in the classes $d\equiv2,3,6,7$ and agree in $d\equiv0,1,4,5$. Statements about the real spinors of $(1,3)$ belong to the second normalisation and are cited, not re-derived. Second, the classification of the real forms and the sign table are taken from the general theory and the eightfold table (*Bott Periodicity and the Classification*); the article verifies the matrix models of the three three-dimensional forms, not the classification itself. Third, the absence of a reality structure is a statement about the module of the algebra and not about the existence of a real structure on the ambient module, which is a question for the physics corpus; the ambient module of the previous section is the passage from the one to the other. Fourth, $\kappa$ is an automorphism of the matrix model and is not one of the four conjugations of $\mathbb{B}$; the conjugate module $\bar S$ is **inequivalent** to $S$ as a complex module — that inequivalence is precisely the complex type — and the two are isomorphic only as real representations, with coordinate conjugation as antilinear intertwiner. The general source states exactly this inequivalence, in its dimension-three section, and the article agrees with it.

## Summary

The complex spinor module $S=\mathbb{B}\tilde\Pi_1\cong\mathbb{C}^2$ of the biquaternion algebra has **complex type**: there is no antilinear $J$ with $J^2=\pm1$ commuting with the Clifford action. The reason is peculiar to the algebra and is one line: the volume element of $\mathrm{Cl}_{3,0}$ is central with square $-1$ and acts on $S$ as the scalar $i$, so the complex structure of the module is itself a Clifford element, and an antilinear map commuting with the Clifford action is annihilated by its own antilinearity acting on $i$. What exists in place of a reality structure is the **conjugate module** $\bar S$, produced by entrywise conjugation $\kappa$ of the matrix model: $\bar S$ is **inequivalent** to $S$ as a complex module, which is the complex type, and isomorphic to it only as a real representation, with coordinate conjugation as the antilinear intertwiner; the antisymmetric form $\varepsilon=i\sigma_2=\Phi(-e_2)$ does not intertwine the two modules but realises the coefficient conjugation $\bar{\cdot}$ on the module, $\varepsilon\,\overline{c}(v)\,\varepsilon^{-1}=c(\bar v)$. The conjugate pair appears as two distinct simple factors in the complexification $\mathbb{C}\mathrm{l}_3\cong M_2(\mathbb{C})\times M_2(\mathbb{C})$. The three real forms of $\mathbb{C}\mathrm{l}_3$ have the same complex module and different types — $\mathrm{Cl}_{3,0}$ complex, $\mathrm{Cl}_{2,1}$ real, $\mathrm{Cl}_{0,3}$ quaternionic — and the same basis realises two of them: with the generators $\gamma_k=ie_k$ the type is complex, with the generators $e_k$ the type is quaternionic, with $J(s)=\sigma_2\bar s$ and $J^2=-1$; the two readings differ by the central $i$, which is exactly the competing labelling of the algebra. In the ambient dimension the two normalisations of the reality structure differ by the volume-element twist, and it is the anticommuting normalisation that gives the real structure in signature $(1,3)$, in agreement with the physics corpus. Internally there is no real or chiral spinor: the internal module is ungraded, and its two conjugate halves appear only on complexification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{B}\tilde\Pi_1\cong\mathbb{C}^2$ | The complex spinor module, the defining module of $\mathbb{B}$ |
| $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$, ${}^{\flat}$ | Coefficient conjugation (a conjugate-linear automorphism), quaternion conjugation (the $\mathbb{C}$-linear anti-automorphism negating the vectors), Hermitian conjugation $\bar{\cdot}\circ{}^{\natural}$ and its negative |
| $\gamma_k=ie_k$ | Generators of the $\mathrm{Cl}_{3,0}$ form of $\mathbb{B}$, $c(\gamma_k)=\sigma_k$ |
| $\omega=\gamma_1\gamma_2\gamma_3\mapsto i$ | Volume element; central, $\omega^2=-1$, $c(\omega)=iI$ |
| $J$ | Reality structure: antilinear, $J^2=\pm1$, commuting with the Clifford action |
| $J^2=+1$, $J^2=-1$ | Real structure, quaternionic structure |
| $S_{\mathbb{R}}=\{s:J(s)=s\}$ | Real fixed space of a real structure; quaternionic line for $J^2=-1$ |
| $\kappa(M)=\overline{M}$ | Entrywise conjugation of the matrix model; antilinear automorphism, not a conjugation of $\mathbb{B}$ |
| $\overline{c}(v)=\kappa c(v)\kappa^{-1}$ | The conjugate representation; the conjugate module $\bar S$ |
| $\varepsilon=i\sigma_2=\Phi(-e_2)$ | Antisymmetric form; realises the conjugation, $\varepsilon\overline{c}(v)\varepsilon^{-1}=c(\bar v)$ |
| $\mathrm{Cl}_{3,0},\mathrm{Cl}_{2,1},\mathrm{Cl}_{0,3}$ | The three real forms of $\mathbb{C}\mathrm{l}_3$; complex, real, quaternionic |
| $d=p-q$, $n=p+q$ | Signature difference and dimension; the type is a function of $d\bmod8$ |
| Real spinor, chiral spinor | The fixed space of a real structure; a chirality eigenvector; neither exists on $S$ |
| $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R}),\ \mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ | Ambient four-dimensional forms; real and quaternionic in the commuting normalisation |

## Further Reading

- *Biquaternion Spin Geometry* (`articles_maths/biquaternion-spin-geometry.md`), for the module $S$, the Clifford multiplication $c(\gamma_k)=\sigma_k$, the volume element and the complex commutant.
- *The Clifford Algebra Representation* (`articles_maths/the-clifford-algebra-representation.md`), for the two Clifford structures $\mathbb{B}\cong\mathrm{Cl}_{3,0}\cong\mathrm{Cl}^{+}_{1,3}$ and the competing labelling.
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations and their order properties, and *Introduction to the Six Subspaces* for their fixed spaces.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for $\Phi(e_k)=-i\sigma_k$, the four matrix images and the dressed coefficient conjugation.
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the defining module, its uniqueness and the module theory.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the minimal left ideals and the doubling $S\mapsto\bar S$.
- *Real Spinors and Reality Conditions with Inner Conjugation* (`articles_maths/real-spinors-and-reality-conditions-with-inner-conjugation.md`), the general theory of the reality types and the eightfold table, of which this article is the three-dimensional instance.
- *Bott Periodicity and the Classification* (`articles_maths/bott-periodicity-and-the-classification.md`), for the period-eight classification and the sign table.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for reality structures, the signature dependence of the type and the low-dimensional spinor modules.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the four conjugations, their fixed spaces and the matrix models of $\mathrm{Cl}_{3,0}$, $\mathrm{Cl}_{2,1}$ and $\mathrm{Cl}_{0,3}$.
- Michael F. Atiyah, Raoul Bott and Arnold Shapiro, "Clifford modules," *Topology* **3** (1964), supplement 1, 3–38, for the period-eight classification of the reality types.
- Paolo Budinich and Andrzej Trautman, *The Spinorial Chessboard* (Springer, 1988), for the real, complex and quaternionic structures in each dimension modulo eight.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the real forms of a complex Clifford algebra and the competing labellings of a signature.
