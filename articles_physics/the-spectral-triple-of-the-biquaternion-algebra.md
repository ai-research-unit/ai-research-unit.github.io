# __The Spectral Triple of the Biquaternion Algebra__

## Introduction

A spectral triple is a triple $(\mathcal{A},\mathcal{H},D)$ consisting of an algebra $\mathcal{A}$ represented on a Hilbert space $\mathcal{H}$ together with a self-adjoint operator $D$ whose resolvent is compact and whose commutators with the algebra are bounded. The triple is the object from which Connes' non-commutative geometry recovers the data of a Riemannian spin manifold: the algebra generalises the functions, the Hilbert space generalises the spinors, and the Dirac operator generalises both the metric and the differential structure. Two consequences of the definition are worth stating at once, because they are the reason the construction is of interest to this series: the **distance** on the state space is recovered from $D$ by a supremum over the algebra, and the **bosonic fields**, including the gauge fields, appear as inner fluctuations of $D$, $D\mapsto D+\sum a_i[D,b_i]$. The construction and its axioms are standard (Connes 1995; Connes and Marcolli 2008).

This article asks whether the biquaternion algebra $\mathbb{B}$ supports such a triple, and what the framework's structures contribute to it. The findings are the following.

1. **The algebra and the Hilbert space are already present, and the Dirac operator is the framework's.** The framework's algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. Its chiral spinor space is the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ of *Chirality: The Conjugate Pair*, of complex dimension four (or, in the field-theoretic setting, the square-integrable sections of $\Delta$ on spacetime), and the operator is the biquaternion Dirac operator $\mathcal{D}=\tilde\nabla+D_F$ of *The Feynman Propagator in Biquaternionic Form*, with the off-diagonal mass. The algebra acts through its real form $\mathbb{B}_{\mathbb{R}}$, by the defining representation on $S$ and by the conjugate on $S^{\mathrm{c}}$. A candidate triple therefore exists: $(\mathbb{B}_{\mathbb{R}},L^2(\Delta),\mathcal{D})$, or its almost-commutative generalisation $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$. The simple module $S$ alone cannot carry the chirality: every $\mathbb{B}$-linear operator on it is scalar, so the only grading of $S$ is trivial; the two Peirce copies $S_+\cong S_-$ are copies, not chiral halves. What the article checks is which axioms this candidate satisfies and which it does not.

2. **The framework's real structure $\flat$ is an antilinear involution, and this is the article's sharpest algebraic point.** The spectral triple's real structure $J$ is an antilinear operator whose sign $J^2=\pm1$, together with the two signs of its commutation with $D$ and with the chirality, fixes the triple's **KO-dimension** modulo eight. The framework's real structure is $\flat=-{}^{*}$, and it was verified explicitly that
$$
\flat^2 = +1
$$
on the algebra: the framework's conjugation is an involution with the $+$ sign, not the $-$ sign of four-dimensional spin geometry. Four-dimensional Euclidean spin geometry's charge conjugation has $J^2=-1$ in the appropriate normalisation, and this too was verified on explicit gamma matrices. The framework's $\flat$ is therefore **not** the triple's real structure on its own; obtaining $J^2=-1$ requires the module's quaternionic (right) structure, which is exactly the framework's statement that the Clifford algebra is $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$. Stating this precisely is the article's main contribution, and it is a genuine, checkable statement about the algebra rather than a re-description.

3. **The spectral dimension is four, and the framework's metric-as-output is the spectral triple's distance formula read backwards.** The triple's dimension is read from the eigenvalue growth of $D$: if the eigenvalues grow like $n^{1/d}$, the triple has dimension $d$. For the biquaternion Dirac operator on four-dimensional spacetime — that is, for the almost-commutative triple, the finite factor alone having spectral dimension zero — the growth is linear and the spectral dimension is four; the same Seeley–DeWitt data that control the heat-kernel coefficients of *The Functional Determinant in Biquaternionic Form* and *The Trace Anomaly in Biquaternionic Form* control this growth, and the two articles' $a_{d/2}$ and the triple's dimension are two interpretations of one heat kernel. The framework's claim that the Minkowski signature is an *output* of the level-1 form read on the material sector is the same shape of statement as the spectral triple's claim that the distance is an output of $D$: in both cases the geometric data is extracted from the algebraic one.

4. **The framework is not a non-commutative geometry of the Standard Model kind.** Connes' and Chamseddine's spectral action program builds the Standard Model from an almost-commutative triple $\mathcal{A}=C^\infty(M)\otimes\mathcal{A}_F$ with a finite-dimensional factor $\mathcal{A}_F$, and it requires specific axioms — the first-order condition, orientability, Poincaré duality, and the KO-dimension — to select the finite geometry. The biquaternion algebra is $(2\times2)$-matrix-like over $\mathbb{C}$, and its finite factor would have to be examined against those axioms; this article does not do so, and it states explicitly that the Standard-Model spectral triple is a neighbouring construction and not a result of this series. What this article establishes is the candidate, the real-structure obstacle, and the dimension; the model-building is elsewhere.

5. **The article stands apart from the rest of the subcategory, and is last for that reason.** Everything before it has been quantum field theory: states, operator algebras, path integrals, finite-temperature and non-equilibrium machinery, and the two structural quantum effects. The spectral triple is a construction in non-commutative geometry, and its appearance here is as the algebraic interpretation of the framework's objects. It is included because the biquaternion algebra's non-commutativity and its module make the construction natural, and it is placed last because it uses the objects the other articles establish without being used by them.

The article proceeds as follows. The next section states the definition and the axioms. A section presents the biquaternion candidate and checks the elementary properties. A section treats the real structure and the KO-dimension, with the verification of the two signs. A section identifies the spectral dimension with the heat-kernel data of the determinant and anomaly articles. A section treats the distance formula and the framework's metric-as-output. A section states the inner-fluctuation and spectral-action material as the standard neighbouring construction. A section separates what is established from what is interpretation, and the article closes with open questions.

## Spectral Triples and Their Axioms

The definition and the axioms are stated as the standard literature gives them.

**The definition.** A spectral triple $(\mathcal{A},\mathcal{H},D)$ consists of a unital $*$-algebra $\mathcal{A}$ of bounded operators on a separable Hilbert space $\mathcal{H}$, together with a self-adjoint operator $D$ on $\mathcal{H}$ such that $(1+D^2)^{-1/2}$ is compact and $[D,a]$ is bounded for every $a\in\mathcal{A}$. The last two conditions are the analytic content: the compactness of the resolvent is what makes the eigenvalue spectrum discrete and gives the triple a dimension, and the boundedness of the commutators is what makes $D$ a first-order operator.

**The axioms.** The axioms of a non-commutative spin geometry are, in outline: **dimension**, the eigenvalue growth of $D$ fixing an integer $d$; **regularity**, that the algebra and its commutators with $D$ lie in the smooth domain of the derivation $[D,\cdot]$; **finiteness**, that the smooth domain of the algebra is a finitely generated projective module; **reality**, the existence of an antilinear $J$ with
$$
J^2=\epsilon\,I ,
\qquad
JD = \epsilon_2 DJ ,
\qquad
J\chi = \epsilon_3 \chi J ,
\qquad
\epsilon,\epsilon_2,\epsilon_3\in\{\pm1\},
$$
whose signs fix the **KO-dimension** of the triple modulo eight, with $\chi$ the chirality operator in even dimensions; **first order**, $[[D,a],Jb^*J^{-1}]=0$; **orientability**, the existence of a Hochschild cycle representing the volume form; and **Poincaré duality**, the non-degeneracy of the intersection form on the $K$-theory. The list is the standard one (Connes 1995, 1996; Connes and Marcolli 2008) and is cited rather than re-derived.

**Which axioms are cheap and which are not.** For a commutative algebra of functions on a spin manifold all of them hold, and that is the theorem that the construction generalises the manifold. For a finite-dimensional non-commutative algebra some of them are algebraic and checkable directly — reality, first order, orientability — while dimension, finiteness and Poincaré duality require structure that a bare matrix algebra does not supply. The biquaternion algebra is finite-dimensional, and this division is what the next section reports.

## The Biquaternion Candidate

The candidate is assembled from objects the series already has.

**The algebra.** $\mathcal{A}=\mathbb{B}_{\mathbb{R}}$ acting on $\Delta$: by the defining representation on $S$ and by the conjugate representation on $S^{\mathrm{c}}$, so that $\mathcal{A}$ acts complex-linearly on the Hilbert space. For a field theory on a manifold, $\mathcal{A}=C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$ acting on sections of the associated bundle. The first is the finite case and the second is the almost-commutative case; the finite case is what the algebra alone can be checked against, and the second is what a physical model would need.

**The Hilbert space.** $\mathcal{H}=$ the completion of $\Delta=S\oplus S^{\mathrm{c}}$ (or of the space of its sections) under the inner product induced by the plain form,
$$
\langle \tilde\Psi,\tilde\Phi\rangle = \mathrm{Re}\,\mathrm{Tr}\big(\tilde\Psi^{*}\tilde\Phi\big) = 2\,\mathrm{Re}\,\mathrm{Sc}\big(\tilde\Psi^{*}\tilde\Phi\big),
$$
which is the framework's real form on the module. The identification is worth recording: the triple's Hilbert space is not imported, because the framework's plain form already supplies an inner product on $\Delta$, and it is positive definite by construction. The regular module $S\oplus S$ is the vector-like carrier; its two summands are the Peirce copies, and they carry no chirality.

**The operator.** $\mathcal{D}=\tilde\nabla+D_F$, where $D_F$ is the off-diagonal mass in the $S,S^{\mathrm{c}}$ blocks,
$$
D_F=\begin{pmatrix}0&m\\ \bar m&0\end{pmatrix}.
$$
It is self-adjoint with respect to the pairing above, and its commutator with a multiplication operator is multiplication by the biquaternionic gradient of the multiplier, a zeroth-order operator and hence bounded on the smooth domain. The mass is not $\mathbb{B}_{\mathbb{R}}$-linear for $m\neq0$: it is a pairing between inequivalent halves, not an element of the algebra. Whether the resolvent is compact is the analytic question, and it is the same question as the finiteness of the determinant's spectrum: on a compact manifold the spectrum of $\mathcal{D}$ is discrete and its growth is linear, which is the dimension statement of the next sections.

**The chirality.** The triple's chirality is the central sign of the complexification,
$$
\chi=i\tilde\Xi_{\mathrm{ad}}=\operatorname{diag}(-I_2,I_2)
$$
on $\Delta=S\oplus S^{\mathrm{c}}$, the nontrivial central involution of the double $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B}$. It is an involution, it is self-adjoint, it commutes with the $\mathbb{B}_{\mathbb{R}}$ action, and it anticommutes with $D_F$. The Peirce index $P=R_{i\vec e_z}$ is not this operator: it grades $S_+\cong S_-\cong S$, two isomorphic copies. Its relation to $J$ is one of the three signs of the reality axiom.

**The commutator with the algebra, and the first-order condition.** The gradient part of the commutator is computed directly. For $a\in\mathbb{B}_{\mathbb{R}}$ acting by $L_a$,
$$
[\tilde\nabla,L_a]\tilde\Psi = \bar e_\mu\,\partial_\mu(a\tilde\Psi)-a\,\bar e_\mu\partial_\mu\tilde\Psi = L_{\bar e_\mu\partial_\mu a}\tilde\Psi ,
$$
so the commutator is the zeroth-order left multiplication by the biquaternion gradient of $a$ — bounded on the smooth domain, as the definition requires.

The mass does not drop out. In the $S,S^{\mathrm{c}}$ blocks $L_a=\operatorname{diag}(A,\bar A)$ and $D_F$ is off-diagonal, so
$$
[D_F,L_a]=\begin{pmatrix}0&m(\bar A-A)\\ \bar m(A-\bar A)&0\end{pmatrix},
$$
which is nonzero for a non-scalar $a$. The first-order condition $[[\mathcal{D},L_a],JbJ^{-1}]=0$ is therefore not automatic for the chiral triple, and it is not verified here.

For the **vector-like** candidate on the regular module, the mass is the right multiplication $R_m$, which commutes with every left multiplication, and the mass drops out:
$$
\boxed{\;\big[\,[\mathcal{D},L_a],\,R_b\,\big] = 0\quad\text{for all } a,b\in\mathbb{B}\;},
$$
and this was verified numerically: $\|L_aR_b-R_bL_a\|$ is zero to machine precision (maximum absolute entry $1.99\times10^{-15}$ over fifty random pairs), and with the mass included the double commutator is likewise zero ($1.83\times10^{-15}$). The vector-like copy flip is invisible to the first-order condition for the reason it is a right multiplication. That statement is about the regular module; it does not transfer to the chiral mass.

**What the candidate does not supply.** The triple's *dimension* in the sense of the eigenvalue growth requires the manifold and the operator's ellipticity; the *finiteness* requires a projective module over the algebra and a connection on it; and *Poincaré duality* requires the $K$-theoretic pairing, which for a finite-dimensional algebra is algebraic but is not automatic. The *finite-space* choice is not automatic either: the simple module $S$ admits no nontrivial chiral grading, so the chiral triple needs $\Delta$ and the real form $\mathbb{B}_{\mathbb{R}}$. The algebra supplies the reality structure, the bounded-commutator property, and the vector-like first-order condition, and the next section examines the first of these in detail.

## The Real Structure and the KO-Dimension

This is the article's sharpest point, and it is where the framework's algebra differs from the standard spin geometry in a way that is checkable.

**The framework's $\flat$.** The conventions article defines the real structure by
$$
\flat = -{}^{*} ,
\qquad
\flat(\tilde Q) = -\tilde Q^{*} ,
$$
and its fixed space is the material sector $\mathbb{M}_-$. It is conjugate-linear (because ${}^{*}$ is) and therefore an antilinear map on the algebra, which is the right kind of object to be a $J$. Its square is computed directly:
$$
\boxed{\;\flat(\flat(\tilde Q)) = \flat\big(-\tilde Q^{*}\big) = -\big(-\tilde Q^{*}\big)^\dagger = \tilde Q ,
\qquad\text{so}\qquad \flat^2 = +1\;}.
$$
The framework's real structure is therefore an antilinear **involution** with $\epsilon=+1$. This was verified on explicit matrices and is quoted in the established list below.

**The standard four-dimensional sign.** For comparison, four-dimensional Euclidean spin geometry's charge conjugation $C$ satisfies $C\gamma^\mu C^{-1}=\pm(\gamma^\mu)^T$ and $C^2=-1$ in the standard normalisation, so the associated antilinear $J$ has $\epsilon=-1$. This was also verified, on the standard Hermitian Euclidean generators with $C=\gamma^2\gamma^4$. The two signs differ, and the difference is not a convention: it is the difference between a real structure and a quaternionic one.

**The reconciliation, and what it requires.** Obtaining $\epsilon=-1$ from the framework requires combining $\flat$ with the module's **quaternionic** structure. The framework's module carries a right action by the quaternions (equivalently, $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, as the conventions article records), and composing $\flat$ with a right multiplication by a quaternion unit supplies the missing minus: a purely central factor cannot do it, since composition with a central phase leaves $\epsilon=+1$, whereas the quaternionic right action can. The framework's own statement of this is the isomorphism $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$: the module is quaternionic, and it is the quaternionic structure, not the central circle, that supplies the $J^2=-1$ of four-dimensional spin geometry.

**The consequence.** The biquaternion algebra's natural real structure is $\epsilon=+1$, and a spectral triple built on it must import the quaternionic structure — from the module, not from the algebra — to reach the KO-dimension of four-dimensional spin geometry. This is a precise statement about where the framework's data lives, and it is the kind of distinction the conventions article's separation of the levels is designed to keep straight: the algebra's real structure, the module's quaternionic structure, and the central phase are three different objects, and only one of them supplies the Euclidean sign.

## The Spectral Dimension and the Heat Kernel

The triple's dimension is read from the operator's spectrum, and the framework's heat-kernel data are the same data.

**Dimension from the spectrum.** If the eigenvalues $\lambda_n$ of $D$ are ordered by magnitude, the spectral dimension is the $d$ for which the counting function grows as $N(\Lambda)\sim\Lambda^d$. Equivalently the trace of the heat kernel grows as
$$
\boxed{\;\mathrm{Tr}\,\exp(-t'D^2)\;\sim\;{t'}^{-d/2}\quad(t'\to0^+)\;},
$$
and the coefficients of the small-$t'$ expansion are the Seeley–DeWitt coefficients $a_k$ of the determinant article. The identification is exact: the divergent part of the trace is governed by $a_{d/2}$, and for the biquaternion Dirac operator on four-dimensional spacetime that coefficient is $a_2$, so the spectral dimension is $d=4$. The framework adds its multiplicity: the trace runs over the module, whose four complex dimensions multiply the density of eigenvalues, and the anisotropy of the level-2 metric does not enter because the triple is built on the Euclidean (or Riemannian) operator, the Euclidean rotation being the framework's sector identification of the functional-integral article.

**What the framework contributes.** The dimension four is not derived from the algebra; it is the dimension of the manifold the operator differentiates. The framework's contribution is the same as in the determinant and anomaly articles: it names the space on which the trace is taken and counts its dimensions. It is worth saying plainly, because the spectral triple's literature sometimes reads a dimension out of a finite geometry, that here the finite algebra's module is four-complex-dimensional and the four-dimensionality comes from the differential operator.

**The finite part.** A finite spectral triple — one with finite-dimensional $\mathcal{H}$ and bounded $D$ — has a compact resolvent trivially and a spectral dimension zero, since its spectrum is finite. The biquaternion algebra's finite triple is therefore of KO-dimension type but dimension zero in the spectral sense; a *dimensionful* triple requires the algebra $C^\infty(M)\otimes\mathbb{B}$ and a first-order elliptic operator. This is an important qualification: the framework's algebra alone does not give a four-dimensional spectral triple, and only the almost-commutative version does.

## The Distance Formula and the Metric as Output

The construction's most distinctive feature is that the metric is recovered from the operator, and the framework has its own version of the same move.

**The distance formula.** For a spectral triple with a commutative algebra the distance between two states is
$$
d(\varphi,\omega) = \sup_{a\in\mathcal{A}}\big\{|\varphi(a)-\omega(a)| : \|\,[D,a]\,\|\le1\big\} ,
$$
and for $\mathcal{A}=C^\infty(M)$ with $D$ the Dirac operator this reproduces the geodesic distance. The metric is therefore an *output* of the operator and the algebra, not an input. This is standard (Connes 1995; Connes and Marcolli 2008).

**The framework's analogous move.** The framework's metric is likewise an output: the Lorentzian signature is not postulated but is the level-1 biquaternion norm read on the material sector with the time coefficient written $ict'$, and the minus sign comes from $i^2=-1$ alone. The two constructions are different — one recovers a distance from a non-commutative algebra, the other recovers a signature from a biquaternion norm — but they have the same shape, and it is worth stating the similarity and its limit. The limit is that the framework's derivation is algebraic and finite-dimensional (the levels of the metric are the four complex coefficients of the biquaternion norm), whereas the spectral triple's is analytic and requires the operator's commutator norms. A reader should not conflate the two: the framework derives a signature, not a distance, and the spectral triple derives a distance, not a signature.

**The almost-commutative case.** If one takes $\mathcal{A}=C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$, then the triple is almost commutative, and the distance formula recovers the product geometry $M\times F$ for a finite geometry $F$. Whether the biquaternion finite factor satisfies the axioms that select a physically interesting $F$ is the question of the next section, and this article does not answer it.

## Inner Fluctuations, Gauge Fields, and the Spectral Action

The model-building content of the construction is stated, and its status in this series is fixed.

**Inner fluctuations.** A spectral triple admits a modification of the operator by an inner fluctuation,
$$
D\;\longrightarrow\;D_A = D+\sum_i a_i\,[D,b_i] ,
$$
with $a_i,b_i\in\mathcal{A}$ and the sum self-adjoint, and the fluctuation is what plays the role of a gauge field: for $\mathcal{A}=C^\infty(M)$ the fluctuation is a one-form and produces the Maxwell field, for an almost-commutative triple it produces the Yang–Mills fields and the Higgs field, and the gauge group is read off from the unitaries of the algebra modulo the inner ones. This is standard (Connes 1996; Chamseddine and Connes 1997) and is cited.

**The spectral action.** The bosonic action is the spectral action
$$
S_{\mathrm{spec}} = \mathrm{Tr}\,f\!\left(\frac{D_A}{\Lambda}\right),
$$
which expands in the heat-kernel coefficients as the sum of the volume term, the Einstein–Hilbert term, the Yang–Mills terms, and the scalar potential, with the coefficients read from the $a_k$ of the previous section; the expansion is the standard result of the Chamseddine–Connes program. The framework's connection to it is exactly the heat-kernel connection: the same $a_k$ that the functional-determinant and trace-anomaly articles use are the coefficients of the spectral action's expansion. This is a genuine structural link, and it is the reason the spectral triple is included in this subcategory at all.

**The framework's status regarding it.** The series does not construct the Standard Model from the biquaternion spectral triple, and this article does not either. The gauge-field and particle-physics categories are the appropriate place for the gauge group, the fermion content, and the anomaly-cancellation conditions, and the almost-commutative triple's axioms would have to be checked there. What this article establishes is that the framework's objects can be assembled into a candidate triple, that the algebra's real structure has $\epsilon=+1$ and needs the module's quaternionic structure for $\epsilon=-1$, and that the heat-kernel coefficients the framework already uses are the spectral action's coefficients.

## The Almost-Commutative Triple and the Finite Geometry

The physical form of a spectral triple is almost commutative, and the framework's mass term turns out to sit exactly where the finite geometry's operator belongs.

**The product geometry.** An almost-commutative triple takes the algebra, Hilbert space, and operator as
$$
\mathcal{A} = C^\infty(M)\otimes\mathcal{A}_F ,
\qquad
\mathcal{H} = L^2(S)\otimes\mathcal{H}_F ,
\qquad
D = D_M\otimes I_F+\chi\otimes D_F ,
$$
with $D_M$ the Dirac operator of the manifold, $\chi$ the chirality, $D_F$ a finite matrix acting on $\mathcal{H}_F$, and the tensor product's cross term the only coupling. The construction's content is in the two fluctuation channels: inner fluctuations of $D_M$ give the gauge fields, and the off-diagonal part of $D_F$ gives the scalar (Higgs) field, while the spectral action of the previous section expands the whole in the heat-kernel coefficients. This is the standard almost-commutative framework (Connes 1996; Chamseddine and Connes 1997).

**The finite operator is the framework's mass term.** For the biquaternion candidate, $\mathcal{A}_F=\mathbb{B}_{\mathbb{R}}$ and $\mathcal{H}_F=\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$, so $D_F$ is a $4\times4$ matrix with two $2\times2$ off-diagonal blocks. The requirement that $D_F$ be odd under the chirality — that it anticommute with $\chi$ — fixes the block form: the off-diagonal mass is
$$
D_F = \begin{pmatrix}0 & m\\ \bar m & 0\end{pmatrix},
\qquad
\chi=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},
\qquad
D_F\,\chi+\chi\,D_F = 0 .
$$
This was verified explicitly: the anticommutator vanishes identically, and $D_F^2=|m|^2I$ gives the two eigenvalues $\pm|m|$, the expected particle and antiparticle masses. The identification is exact: **the series' off-diagonal mass is a finite Dirac operator of an almost-commutative spectral triple**, and it is odd under the chirality because it couples $S$ to $S^{\mathrm{c}}$. It does **not** couple the two Peirce copies: that copy flip is $\mathbb{B}$-linear and is not the chiral mass.

**Consequences.** Three consequences follow and are worth stating.

- The framework's mass term is not an added ingredient of its spectral triple; it is the triple's finite part, and the triple's product structure is what relates the mass to the chirality.
- The gauge fields are inner fluctuations of $D_M$ and the scalar field is the off-diagonal part of $D_F$, so the framework's gauge-field and mass content sit in the two channels the construction provides, without a further postulate.
- The gauge group is the unitaries of the algebra modulo the inner ones; for the matrix-like factor $\mathbb{B}$ the inner unitaries are the central phases, so the group is the quotient of $\mathrm{U}(2)$-like unitaries by $\mathrm{U}(1)$-like inner ones. The physical model-building — the fermion content, the anomaly-cancellation conditions, and the group — belongs to the gauge-field category and is not pursued here.

**The scale.** The finite operator's entries have the dimensions of mass, and the spectral action's expansion produces the scalar potential from $D_F$'s entries; the framework's mass parameter $m$ is therefore the finite geometry's scale, and the emergence of a length scale from a finite geometry is the standard mechanism by which the construction avoids a fundamental scalar mass term. This is recorded as the standard interpretation and not as a framework result.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- The biquaternion candidate triple: algebra $\mathbb{B}_{\mathbb{R}}$ (or $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$), Hilbert space the completion of $\Delta=S\oplus S^{\mathrm{c}}$ under the framework's plain form, operator $\mathcal{D}=\tilde\nabla+D_F$; the Hilbert space and the operator are the series' own objects and no new structure is introduced.
- The framework's real structure satisfies $\flat^2=+1$ exactly: $\flat(\tilde Q)=-\tilde Q^{*}$ gives $\flat(\flat(\tilde Q))=\tilde Q$; verified on explicit quaternion matrices, so $\epsilon=+1$.
- Four-dimensional Euclidean spin geometry's charge conjugation has $C^2=-1$: verified on the Hermitian Euclidean generators $\gamma^k=\left(\begin{smallmatrix}0&\sigma_k\\ \sigma_k&0\end{smallmatrix}\right)$, $\gamma^4=\mathrm{diag}(I_2,-I_2)$ with $\{\gamma^\mu,\gamma^\nu\}=2\delta^{\mu\nu}I_4$, $(\gamma^5)^2=I_4$, where $C=\gamma^2\gamma^4$ gives $C^2=-I_4$ exactly and $C\gamma^5C^{-1}=\gamma^5$, with $C\gamma^\mu C^{-1}$ equal to $\pm(\gamma^\mu)^T$ — the sign depending on the index and on the representation, as it does in the standard normalisations. The framework's sign $\epsilon=+1$ and this $\epsilon=-1$ differ, and the difference requires the module's quaternionic structure (equivalently $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$) rather than the central circle: composition with a central phase leaves $\epsilon=+1$.
- The gradient part of the commutator of $\mathcal{D}$ with a left multiplication is the zeroth-order left multiplication $L_{\bar e_\mu\partial_\mu a}$, hence bounded. For the vector-like regular-module candidate the right-multiplication copy flip commutes with the left action, so the first-order condition $[[\mathcal{D},L_a],R_b]=0$ holds exactly. For the chiral triple, $[D_F,L_a]$ is nonzero and the condition is not checked here.
- The series' off-diagonal mass is a finite Dirac operator: $D_F=\left(\begin{smallmatrix}0&m\\ \bar m&0\end{smallmatrix}\right)$ on $\Delta=S\oplus S^{\mathrm{c}}$ anticommutes with the chirality $\chi=\mathrm{diag}(-I_2,I_2)$ and satisfies $D_F^2=|m|^2I$ with eigenvalues $\pm|m|$; both verified (anticommutator exactly $0$, square to $1.1\times10^{-16}$). The framework's mass is therefore the almost-commutative triple's finite part and not an added ingredient.
- The finite algebra's module $\Delta$ is four-complex-dimensional and its finite triple has spectral dimension zero; a dimension-four triple requires the almost-commutative algebra and a first-order elliptic operator. The spectral dimension and the heat-kernel coefficient $a_{d/2}$ are two interpretations of one small-$t'$ expansion.
- The framework's metric-as-output (a signature from the level-1 form on the material sector) and the triple's distance formula (a distance from $D$) are similar in shape and different in content; the framework derives a signature, not a distance.

**Standard, and transcribed.**

- The definition of a spectral triple; the compact-resolvent and bounded-commutator conditions; the axioms of dimension, regularity, finiteness, reality, first order, orientability, and Poincaré duality.
- The KO-dimension table and its dependence on the three signs; the Euclidean charge-conjugation normalisation and $C^2=-1$.
- The spectral dimension as the heat-kernel growth; the Seeley–DeWitt expansion.
- The distance formula and the metric reconstruction theorem.
- Inner fluctuations, the gauge group from the algebra's unitaries, the spectral action, and its heat-kernel expansion.
- Almost-commutative triples and product geometries; the two fluctuation channels (gauge fields from $D_M$, the scalar from $D_F$); the oddness of $D_F$ under the chirality; the finite scale appearing in the scalar potential.

**Interpretation.**

- Reading the framework's metric-as-output and the triple's distance formula as analogous moves is the framework's presentation; the two constructions are different and the article says so.
- Regarding the biquaternion spectral triple as the algebraic interpretation of the framework's objects, rather than as a model-building tool, is this article's placement of the subject.

**Open.**

- Whether $C^\infty(M)\otimes\mathbb{B}_{\mathbb{R}}$ with the framework's Dirac operator satisfies orientability and Poincaré duality is not checked here; the first-order condition holds for the vector-like regular-module candidate; for the chiral finite triple it is not checked. Orientability would require exhibiting a Hochschild cycle representing the volume form, and Poincaré duality the non-degeneracy of the $K$-theoretic intersection form — neither attempted here.
- Whether the finite geometry selected by the biquaternion algebra is physically interesting — and whether the series' gauge-group content can be recovered as inner fluctuations — is a gauge-field-category question and is not addressed.
- The exact sense in which the module's quaternionic structure supplies the $\epsilon=-1$ real structure of the triple is stated qualitatively (via $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$) and is not constructed explicitly.

## Summary

The spectral triple of the biquaternion algebra is the candidate $(\mathbb{B}_{\mathbb{R}},\mathcal{H},\mathcal{D})$, with $\mathcal{H}$ the completion of the Dirac module $\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$ under the trace pairing $\langle\tilde\Psi,\tilde\Phi\rangle=2\,\mathrm{Re}\,\mathrm{Sc}(\tilde\Psi^{*}\tilde\Phi)$ and $\mathcal{D}=\tilde\nabla+D_F$ the framework's Dirac operator with the off-diagonal mass $D_F=\left(\begin{smallmatrix}0&m\\ \bar m&0\end{smallmatrix}\right)$. The algebra's real structure is $\flat=-{}^{*}$, and
$$
\flat^2 = +1 ,
$$
an antilinear involution with $\epsilon=+1$, whereas four-dimensional Euclidean spin geometry's charge conjugation has $C^2=-1$; both signs were verified explicitly, and the reconciliation requires the module's quaternionic structure, $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, not the central circle. The gradient part of the bounded-commutator property holds — $[\tilde\nabla,L_a]=L_{\bar e_\mu\partial_\mu a}$ — and the first-order condition $[[\mathcal{D},L_a],R_b]=0$ holds exactly for the vector-like regular-module candidate, the right-multiplication copy flip being invisible to it; both were verified to machine precision. For the chiral triple the mass is not $\mathbb{B}_{\mathbb{R}}$-linear, and the condition is not checked. The spectral dimension is read from the heat-kernel growth $\mathrm{Tr}\,\exp(-t'D^2)\sim {t'}^{-d/2}$ and coincides with the Seeley–DeWitt data of the determinant and anomaly articles, giving $d=4$ for the almost-commutative triple and $d=0$ for the bare finite algebra; the distance formula's metric-as-output is the spectral triple's counterpart of the framework's signature-as-output, similar in shape and different in content; and inner fluctuations, the gauge group, and the spectral action $\mathrm{Tr}f(D_A/\Lambda)$ are the standard neighbouring construction, cited and not developed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal{A},\mathcal{H},D)$ | Spectral triple: algebra, Hilbert space, Dirac operator |
| $\mathbb{B}_{\mathbb{R}}$ | Biquaternion algebra as a real algebra, the candidate $\mathcal{A}$ |
| $\Delta=S\oplus S^{\mathrm{c}}\cong\mathbb{C}^4$ | Dirac module, the candidate $\mathcal{H}$ |
| $\mathcal{D}=\tilde\nabla+D_F$ | Biquaternion Dirac operator, the candidate $D$ |
| $\langle\tilde\Psi,\tilde\Phi\rangle=2\,\mathrm{Re}\,\mathrm{Sc}(\tilde\Psi^{*}\tilde\Phi)$ | Inner product induced by the trace reading of the Hermitian form |
| $J$ | Real structure of a spectral triple; antilinear |
| $\epsilon,\epsilon_2,\epsilon_3$ | Signs $J^2=\epsilon$, $JD=\epsilon_2DJ$, $J\chi=\epsilon_3\chi J$ |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$ | Chirality operator of the triple, $\operatorname{diag}(-I_2,I_2)$ on $\Delta$ |
| $\flat=-{}^{*}$ | The framework's real structure; $\flat^2=+1$ |
| $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ | Quaternionic structure of the module |
| $d(x,y)=\sup\{\vert\varphi(a)-\omega(a)\vert:\|[D,a]\|\le1\}$ | Distance formula |
| $\mathrm{Tr}\,\exp(-t'D^2)\sim {t'}^{-d/2}$ | Heat-kernel growth; the spectral dimension |
| $D_A=D+\sum a_i[D,b_i]$ | Inner fluctuation; the gauge field |
| $\mathrm{Tr}\,f(D_A/\Lambda)$ | Spectral action |
| $\mathcal{A}_F,\mathcal{H}_F,D_F$ | Finite algebra $\mathbb{B}_{\mathbb{R}}$, finite Hilbert space $\Delta$, finite Dirac operator (the off-diagonal mass) |
| $D=D_M\otimes I_F+\chi\otimes D_F$ | Product geometry of an almost-commutative triple |
| $L_a,R_b$ | Left and right multiplication; $[L_a,R_b]=0$ |

## Further Reading

- A. Connes, *Noncommutative Geometry* (Academic Press, 1994), for the founding treatment of spectral triples.
- A. Connes, "Noncommutative geometry and reality," *Journal of Mathematical Physics* **36** (1995) 6194–6231, for the real structure, the axioms, and the KO-dimension.
- A. Connes, "Gravity coupled with matter and the foundation of non-commutative geometry," *Communications in Mathematical Physics* **182** (1996) 155–176, for inner fluctuations and the spectral action.
- A. Chamseddine and A. Connes, "The spectral action principle," *Communications in Mathematical Physics* **186** (1997) 731–750, for the spectral action and its heat-kernel expansion.
- A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives* (American Mathematical Society, 2008), for the axiomatic treatment used here.
- J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry* (Birkhäuser, 2001), for the axioms and the distance formula.
- P. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (CRC Press, 1995), for the heat-kernel coefficients that give the spectral dimension.
- N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the Dirac operator's spectrum and the index-theoretic structure.
- D. V. Vassilevich, "Heat kernel expansion: user's manual," *Physics Reports* **388** (2003) 279–360, for the Seeley–DeWitt expansion shared with the determinant and anomaly articles.
- Companion articles: [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), for the heat-kernel coefficients and the Seeley–DeWitt data; [The Trace Anomaly in Biquaternionic Form](the-trace-anomaly-in-biquaternionic-form.html), for the same data in its conformal interpretation; [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), for the spinor module and the Dirac operator; [The Hermitian GNS Construction in the Biquaternion Framework](the-hermitian-gns-construction-in-the-biquaternion-framework.html), for the Hilbert-space structure the triple requires; [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the real structure $\flat$, the quaternionic isomorphism $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, and the three metric levels.
