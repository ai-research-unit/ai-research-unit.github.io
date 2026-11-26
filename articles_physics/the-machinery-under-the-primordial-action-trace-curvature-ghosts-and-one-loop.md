# __The Machinery Under the Primordial Action: The Trace, the Curvature, the Ghosts and the One-Loop Determinant__


## Introduction


**The claim.** Every step between the primordial block's field content and its numbers is derived here, in the block's notation, so that a reader who stays inside the category never needs a result stated in another block.


**Why one article and not four references.** Four steps are used by more than one article of the block. The trace fixes the $\tfrac14$ of the display and every vertex read from it. The curvature identity gives the fifteen Gauss laws that set the degree-of-freedom count. The ghosts enter the action written and are never derived. The one-loop coefficient is applied to the matrix but derived for the doublet. **None of the four is long**, and each is one page of algebra the block can own rather than rent.


| step | used by | enters at |

| --- | --- | --- |

| the cyclic trace and its normalisation | the display, every vertex, the instanton | §*The Trace* |

| $[D_{\imath},D_{\jmath}]=-ig_{4}F_{\imath\jmath}$, adjoint covariance, Bianchi | the Gauss laws, the Feynman rules, the instanton | §*The Curvature* |

| Faddeev–Popov fixing, fifteen ghosts, one $\zeta$ | $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{\mathrm{gh}}$, the count $78$ | §*The Ghosts* |

| the one-loop master formula and which determinants drop out | the $\rho^{4}\ln\rho^{2}$ coefficient | §*The Determinants* |


**What is assumed and not derived.** That the fifteen arrays exist, that the group is $\mathrm{SU}(4)$, that the content is the sixteen Weyl fields and the Hermitian matrix $\Xi$, and that the sector carries one coupling $g_{4}$. **The arrays are the boson block's subject**; this article takes them as the representation it is handed.


**The ceiling, stated at the door.** Only the first step needs a representation the algebra does not contain: the trace runs on $\mathbb{C}^{4}$ while $\mathbb{B}\cong M_{2}(\mathbb{C})$ holds $\mathbb{C}^{2}$, so the density is transcribed in a precise sense. **The other three steps are theorems about any connection or any first-class algebra** and do not inherit the ceiling. §*The Ceiling* separates the two cases and says what the difference costs.


## The Trace, and the Factor of Four


**The action needs a density, and a density has to be a number that no local transformation moves.** Three properties are wanted at once, and one functional supplies all three.


**It is invariant, because a trace is cyclic.** For $\mathbb{F}_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}$ and $F'_{\imath\jmath}=U\mathbb{F}_{\imath\jmath}U^{\dagger}$,


$$

\operatorname{tr}\bigl(F'^{2}\bigr)=\operatorname{tr}\bigl(U\mathbb{F}^{2}U^{\dagger}\bigr)=\operatorname{tr}\bigl(\mathbb{F}^{2}\bigr),

$$


so the density is the same at every representative. **The cyclicity is the whole of the invariance**, and a pairing that is not cyclic has no invariant square to offer.


**It is real, because the curvature is Hermitian.** With $t_{a}$ Hermitian and $F_{a,\imath\jmath}$ real, $\mathbb{F}$ is Hermitian, so $\mathbb{F}^{2}$ is Hermitian and its trace is real. **Positivity follows from the same fact**: the trace of the square of a nonzero Hermitian matrix is positive, which is what a kinetic term needs.


**It is a trace over $\mathbb{C}^{4}$, and that is the whole of what the block asks of the algebra.** The three requirements and the module criterion behind this section are stated once, before any block uses them, in [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html).


### Two Norms and One Normalisation


**The printed arrays are anti-Hermitian and their trace norms take two values, and the difference is a factor of six.**


| family | count | $\operatorname{tr}\bigl(G^{\dagger}G\bigr)$ | $\operatorname{tr}\bigl(G^{2}\bigr)$ |

| --- | --- | --- | --- |

| the twelve planes, $A_{\imath\jmath}$ and $iS_{\imath\jmath}$ | $12$ | $2$ | $-2$ |

| the spatial diagonals, before the rotation | $2$ | $2$ | $-2$ |

| the corner $iD$ | $1$ | $12$ | $-12$ |


**So a single normalisation constant cannot serve**, and the normalisation is $t_{a}=iG_{a}/\sqrt{2n_{a}}$ with $n_{a}$ the array's own norm: $t_{a}=iG_{a}/2$ on the fourteen of norm $2$, and $t_{15}=iG_{15}/\sqrt{24}$ on the corner. **The factor six is the reason a vertex read off $G_{a}$ instead of $t_{a}$ is wrong by $\sqrt{6}$ on the corner and by $1$ on the planes**, which is a mismatch no overall rescaling repairs.


**The condition $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ is then a condition on the basis and not only on the normalisation.** A norm fixes an array's length and not its angle, so two arrays can still fail to be transverse: on the set built from the printed rows, exactly two pairs fail, and both pair the corner with a spatial diagonal. **The rotation of the two spatial diagonals into an orthogonal pair is what removes them**, and that rotation is part of the block's normalisation rather than a convenience.


**With sixteen such generators the density identity is one line.**


$$

\mathbb{F}_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a}

\quad\Longrightarrow\quad

\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr)

=\tfrac12\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},

$$


so $-\tfrac12\operatorname{tr}(\sum\mathbb{F}\mathbb{F})=-\tfrac14\sum_{a}F_{a}F_{a}$. **The $\tfrac14$ is therefore not a choice of convention**: it is the coefficient the normalisation forces, and it moves if the normalisation does.


**Why the density is a trace and not a second invariant of the algebra.** The block has one pairing available on $\mathbb{B}$, the scalar part $2\operatorname{Sc}(\tilde Q_{1}\tilde Q_{2})$, and on $M_{2}(\mathbb{C})$ that pairing *is* the trace: the three imaginary units are traceless, so $\operatorname{tr}\tilde Q=2\operatorname{Sc}\tilde Q$ and $2\operatorname{Sc}(\tilde Q_{1}\tilde Q_{2})=\operatorname{tr}(\tilde Q_{1}\tilde Q_{2})$. **Its cyclicity is not in question; its dimension is.** The fifteen generators are $4\times4$ and the biquaternion is $2\times2$, so the algebra's pairing has no argument on which to act. **That is the precise content of the corpus's sentence that the algebra's pairing is unavailable for this action**, and it is a statement about the size of the matrix and not about the trace's symmetry.


**And the sign is a second trap in the same place.** On the printed anti-Hermitian arrays $\operatorname{tr}(G_{a}^{2})=-2$ and $-12$, so a density written on $G_{a}$ has the wrong sign for every one of the fifteen. **Two knobs, one number**: the normalisation and the sign are both fixed by the same table, which is why the block writes every vertex in $t_{a}$.


## The Curvature: Covariance, the Commutator, the Bianchi Identity


**Three statements, and the block uses each one for a different purpose.**


**The connection transforms inhomogeneously and the curvature transforms homogeneously.** With $A'_{\imath}=UA_{\imath}U^{\dagger}+\tfrac{i}{g_{4}}U\partial_{\imath}U^{\dagger}$,


$$

D'_{\imath}=\partial_{\imath}-ig_{4}A'_{\imath}=U\bigl(\partial_{\imath}-ig_{4}A_{\imath}\bigr)U^{\dagger}=UD_{\imath}U^{\dagger},

$$


and the inhomogeneous term is exactly what cancels the derivative of $U$. **So the covariant derivative is covariant by construction and not by a check**, and $[D'_{\imath},D'_{\jmath}]=U[D_{\imath},D_{\jmath}]U^{\dagger}$ follows without further work.


**The commutator of two covariant derivatives is the curvature, up to the coupling.**


$$

[D_{\imath},D_{\jmath}]=-ig_{4}\Bigl(\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}-ig_{4}[A_{\imath},A_{\jmath}]\Bigr)=-ig_{4}\mathbb{F}_{\imath\jmath},

$$


and the derivation is the product rule applied twice: the second derivatives cancel because partial derivatives commute, the two mixed terms cancel because each carries one derivative and one connection, and the leftover is the curl minus the commutator. **The $i$ in the definition of $\mathbb{F}$ is what makes it Hermitian**, since $[A_{\imath},A_{\jmath}]$ is anti-Hermitian for Hermitian $A$ and $-i$ times it is Hermitian.


**The Bianchi identity is the Jacobi identity in disguise.**


$$

D_{\imath}\mathbb{F}_{\jmath\kappa}+D_{\jmath}\mathbb{F}_{\kappa\imath}+D_{\kappa}\mathbb{F}_{\imath\jmath}=0,

$$


which follows from $[D_{\imath},[D_{\jmath},D_{\kappa}]]+\text{cyclic}=0$ and the identification above. **No equation of motion is used**: the identity holds for every connection, including the ones that solve nothing.


### Three Statements the Block Uses


**The Gauss law.** The $\imath=t$ component of the field equation contains no second time derivative of $A_{a,t}$, because $\mathbb{F}_{tt}=0$ identically. **It fixes $A_{a,t}$ in terms of the other fields rather than propagating it**, one constraint per generator, fifteen in all, and each is first class. That is the count's first line: $4\times15=60$ components of the fifteen, less two per first-class constraint, gives $30$.


**Covariant conservation.** $\sum_{\imath}\varepsilon_{\imath}D_{\imath}\mathbb{F}_{\imath\jmath}$ is not divergenceless in the ordinary sense, so the current it equals is conserved only with the connection term. **The conserved object is the covariant divergence, and above $M_{C}$ there is no charge**, only a current, because the charge is defined by a residual symmetry and the symmetry is broken.


**Why no component of $\mathbb{F}_{\imath\jmath}$ is a number.** The six components mix under the adjoint action, so a statement about one of them is a statement in one representative. **This is what forces every vertex and every mass to be read from invariants**, and it is the reason the block never quotes a single $F_{a,\imath\jmath}$ as a physical field.


**What survives the transcription and what does not.** The three statements above are properties of *any* connection: they hold for the fifteen exactly as they hold for the three of $\mathrm{SU}(2)$. **The curvature's algebra is free of the ceiling; the topological integrality is not**, and that distinction is what §*The Instanton* rests on.


## The Ghosts: One Parameter and Fifteen Grassmann Fields


**The action as written fixes nothing about the representative, so the path integral needs a fixing insert and a determinant.**


**One line of the Faddeev–Popov construction, in the block's notation.** Insert unity as


$$

1=\int\mathcal{D}\omega\;\delta\bigl(F_{a}-\omega_{a}\bigr)\det\frac{\delta F_{a}}{\delta\alpha_{b}},

\qquad

F_{a}=\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}A_{a,\imath},

$$


average over $\omega$ with a Gaussian of width $\zeta$, and represent the determinant by Grassmann fields in the adjoint. **The first factor is the fixing term the display already carries**,


$$

\mathcal{L}_{\mathrm{gf}}=-\frac{1}{2\zeta}\sum_{a}\Bigl(\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}A_{a,\imath}\Bigr)^{2},

$$


and the second is fifteen pairs of ghosts,


$$

\mathcal{L}_{\mathrm{gh}}=\sum_{a}\bar c_{a}\Bigl(-\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}D_{\imath}\Bigr)c_{a},

$$


**with the operator in the bracket being the variation of the fixing the representative function under a local transformation**, which is why the ghost couples to the connection and to nothing else.


### Why One $\zeta$ and Not Four


**Because the group is simple, and the number of fixing parameters is the number of independent invariants the orbit admits.** One factor means one; four factors would mean four plus the mixings between them, which is the difference between this block and the electroweak one. **A reader who carries four $\zeta$'s over from the electroweak sector has changed the theory**, since the extra three multiply terms that are not there.


**The ghosts are complex Grassmann scalars in the adjoint: fifteen fields, thirty real components.** A Grassmann field contributes minus one degree of freedom per real component in a loop and nothing on shell, so the pair subtracts two per generator. **That is exactly the two polarisations a first-class constraint removes**, and the two subtractions are the same subtraction counted twice in two ways.


### What the Ghost Subtracts


**The count, with the ghosts placed where they belong.**


| field | components | on shell |

| --- | --- | --- |

| the fifteen $A_{a,\imath}$ | $60$ | $30$ |

| the sixteen $\xi_{f}$ | $64$ real | $32$ states |

| $\Xi$ | $16$ real | $16$ |

| the ghosts $c_{a}$, $\bar c_{a}$ | $30$ Grassmann | $0$, loops only |

| **total** | | $\mathbf{78}$ |


**The two subtractions are one subtraction.** Sixty components, less two per first-class constraint, leaves thirty; the ghost pair then contributes minus two per generator to the *loop* count and nothing to the on-shell one. **So a table that subtracts the ghosts from the on-shell vectors subtracts twice** and leaves no vector at all. **The $78$ is a count of this phase only**, and it is the number the block's census quotes.


**The ghost operator is field-dependent, and the Faddeev–Popov determinant at the identity background is not.** That asymmetry is used in §*The Determinants*: the ghost loop depends on $\Xi$ through $[\Xi,\cdot]$, so at a background proportional to the identity it depends on nothing.


## The Determinants: Three Drop Out and One Does Not


**One formula, and every determinant in the block is a choice of what to put in it.**


$$

V_{\mathrm{eff}}(\Xi_{0})=V(\Xi_{0})+\frac{1}{64\pi^{2}}\operatorname{STr}\Bigl[M^{4}\Bigl(\ln\frac{M^{2}}{\mu^{2}}-\frac{3}{2}\Bigr)\Bigr],

$$


**with one factor of $1/64\pi^{2}$ per real bosonic degree of freedom, minus one per fermionic one.** The $\tfrac{1}{64\pi^{2}}$ is the constant-field value of $\tfrac12\int d^{4}k_{E}/(2\pi)^{4}\ln(k_{E}^{2}+m^{2})$; the $-\tfrac32$ is the scheme's, absorbed into $\mu$ by a finite renormalisation, and **the coefficient of the logarithm is the only part that survives a change of scheme**. That is why every effective-potential article in the corpus quotes a coefficient of $\rho^{4}\ln\rho^{2}$ and none quotes a constant.


**Three assumptions, each named.** The background is constant, so the result is a potential and not an action. Only the scalar has a background. The expansion is one loop in $\hbar$.


### The Connection and Ghost Determinants at the Identity Background


**Both drop out, and the reason is one commutator.**


$$

M^{2}_{ab}\;\propto\;\operatorname{tr}\bigl([\Xi_{0},t_{a}][\Xi_{0},t_{b}]\bigr)

=\Bigl(\frac{\rho}{2}\Bigr)^{2}\operatorname{tr}\bigl([\mathbb{1},t_{a}][\mathbb{1},t_{b}]\bigr)=0

\qquad\text{for}\quad \Xi_{0}=\frac{\rho}{2}\mathbb{1},

$$


**because the identity commutes with every generator.** No vector acquires a mass that depends on $\rho$, so the Faddeev–Popov determinant is a field-independent constant, and the ghost determinant is too, for the same reason through the same commutator. **The assumption in the one-loop article is therefore not an assumption but a consequence of the background it chooses** — and it fails at any background not proportional to the identity, which is why that article restricts itself to the identity direction.


**The same commutator is why the vacuum's trace costs nothing in the sector**: a shift $\Xi_{0}\mapsto\Xi_{0}+c\,\mathbb{1}$ leaves every $[\Xi_{0},t_{a}]$ unchanged.


### The Fermion Determinant, and the Sign It Can Flip


**The fermion determinant does not drop out, and the reason is the operator the block exists to have.**


**With the Yukawa $\mathcal{L}_{\mathrm{Yuk}}=y_{\alpha\beta}\bar\xi^{\alpha}\Xi\xi^{\beta}$ and the identity background, each of the sixteen Weyl fields acquires a mass**, and the $2\times2$ matrix $y_{\alpha\beta}$ gives two eigenvalues $y_{1}$, $y_{2}$, each carried by four copies:


$$

m_{i}=\frac{y_{i}\rho}{2},

\qquad i=1,2,

\qquad \text{eight Dirac fields in all.}

$$


**So the "no other field has a background" argument does not reach the fermions**: no fermion condenses, but every fermion is massive once $\Xi_{0}\neq0$, and its mass is proportional to $\rho$. **That is the phase's own mechanism read backwards**: the same coupling that gives the leptoquarks their masses in the broken phase gives the sixteen their masses in the symmetric one.


**The contribution follows from the master formula with the fermionic sign and the four states of a Dirac field.**


$$

V_{1}^{f}=-\frac{4}{64\pi^{2}}\sum_{i=1}^{2}4\,m_{i}^{4}\ln\frac{m_{i}^{2}}{\mu^{2}}

=-\frac{\rho^{4}}{64\pi^{2}}\bigl(y_{1}^{4}+y_{2}^{4}\bigr)\ln\frac{\rho^{2}}{\mu^{2}},

$$


**the $4$ inside from the Dirac trace and the $4$ outside from the copies, and the two $4$'s and the $16$ in $m^{4}$ leaving one.** With $y_{1}=y_{2}=y$ the coefficient is $-\dfrac{y^{4}}{32\pi^{2}}$.


**The total coefficient is the difference of the two, and the sign is not settled by the scalar sector.**


$$

\mathcal{C}_{\mathrm{tot}}=\frac{1}{16\pi^{2}}\Bigl(9\lambda_{1}^{2}-\frac{y^{4}}{2}\Bigr),

\qquad

\mathcal{C}_{\mathrm{tot}}>0\iff y^{4}<18\lambda_{1}^{2},

\qquad

y_{\mathrm{crit}}=1.456\,\sqrt{\lambda_{1}} .

$$


**So the scalar-only coefficient $\dfrac{9\lambda_{1}^{2}}{16\pi^{2}}$ is a ceiling and not the number.** The fermion loop subtracts from it, and for $y\gtrsim1.5\sqrt{\lambda_{1}}$ the total turns negative, which reverses the stability conclusion that the one-loop article draws from the scalar sector alone. **The condition is stated here so that the conclusion carries its warrant.**


**What the negative sign does not mean.** At large $\rho$ a negative $\rho^{4}\ln\rho^{2}$ term drives the potential down without bound, **but the logarithm is already larger than the tree term there**, at $\rho\gtrsim9\mu$ at $\lambda_{1}=1$ — so the region where the sign matters is the region where the one-loop potential is not a potential. **The statement is about the neighbourhood of $\mu$, and it is a statement about a sign and not about a minimum.**


## The Ceiling, Restated for the Machinery


**Four steps, and the ceiling cuts through two of them.**


- *The trace.* Invariance, reality and positivity are properties of a trace on any matrix algebra. **What the block cannot have is the algebra's own pairing**, because that pairing is the trace on $\mathbb{C}^{2}$ and the field lives on $\mathbb{C}^{4}$. The cost is a representation, not a structure.

- *The curvature identities.* $[D,D]=-ig_{4}\mathbb{F}$ and the Bianchi identity are theorems about connections. **They are not transcribed**: they hold on $\mathbb{C}^{4}$ for the same reason they hold on $\mathbb{C}^{2}$, and no coefficient from a table enters them.

- *The ghosts.* The Faddeev–Popov construction fixes the representative of any theory with a first-class algebra. **Fifteen is a number inside it**, not a hypothesis of it.

- *The one-loop formula.* Mode counting and one momentum integral. **It is transcription-free**, and the only input the block supplies is the Hessian.


**So the machinery is not the weak part of the block.** The transcribed objects are the fifteen arrays, the structure constants read from the table, and the topological charge whose integrality needs a bundle. **Everything between the arrays and the numbers is ordinary field theory**, and that is what makes the block's arithmetic checkable by anyone who never opens the corpus.


## The Checks


| claim | check | result |

| --- | --- | --- |

| the two trace norms | $\operatorname{tr}(G^{\dagger}G)$ over the fifteen printed arrays | $2$ and $12$ |

| the corner against a plane | $12/2$ | $6$ |

| the sign on the printed arrays | $\operatorname{tr}(G^{2})$ | $-2$ and $-12$ |

| transversality | $\max_{a,b}\lvert\operatorname{tr}(t_{a}t_{b})-\tfrac12\delta_{ab}\rvert$ after the rotation | $0$ |

| printed pairs that fail before it | $\operatorname{tr}(G_{a}G_{b})\neq0$, $a<b$ | $2$, both with $iD$ |

| the density identity | $\operatorname{tr}(\sum\mathbb{F}\mathbb{F})$ against $\tfrac12\sum_{a}F_{a}F_{a}$ | agree to $10$ digits |

| $[D_{\imath},D_{\jmath}]=-ig_{4}\mathbb{F}_{\imath\jmath}$ | random connection on a $32$-point periodic grid, spectral derivative | error $4.6\times10^{-14}$, scale $18.3$ |

| $F'=U\mathbb{F}U^{\dagger}$ | $U(x)=\exp(i\theta_{a}(x)t_{a})$, unitarity error $2.2\times10^{-15}$ | error $5.5\times10^{-9}$ |

| the density is invariant | $\operatorname{tr}(F'^{2})$ against $\operatorname{tr}(\mathbb{F}^{2})$ | differ by $2.3\times10^{-13}$ |

| the Bianchi identity | $D_{[\imath}\mathbb{F}_{\jmath\kappa]}$ on the same connection | error $6.5\times10^{-14}$ |

| $[\mathbb{1},t_{a}]=0$ | all fifteen | $0$, so the connection mass matrix vanishes at $\Xi_{0}\propto\mathbb{1}$ |

| the scalar coefficient | $\frac{36\lambda_{1}^{2}}{64\pi^{2}}$ | $\frac{9\lambda_{1}^{2}}{16\pi^{2}}$ |

| the fermion coefficient, $y_{1}=y_{2}=y$ | $-\frac{4\cdot4}{64\pi^{2}}\cdot\frac{y^{4}}{16}$ | $-\frac{y^{4}}{32\pi^{2}}$ |

| the sign condition | $9\lambda_{1}^{2}$ against $\tfrac12y^{4}$ | $y<1.456\sqrt{\lambda_{1}}$ |


**One methodological note, because it bit this article first.** A white-noise test field breaks the product rule on a grid, since products of Nyquist modes alias, and a commutator check run on white noise reports errors of order the field. **The test fields here are bandlimited to three modes**, which is what makes the errors above of order $10^{-14}$ and not of order one.


## Summary


**The primordial block rests on four results, and this article derives all four in its own notation: the cyclic trace with its two norms and the factor $\tfrac14$; the curvature's covariance, the commutator identity and the Bianchi identity; the Faddeev–Popov fixing the representative with one parameter and fifteen ghosts; and the one-loop master formula with its $1/64\pi^{2}$ per real mode.**


**The trace is a trace on $\mathbb{C}^{4}$ and not the algebra's scalar part, for a reason of dimension and not of symmetry**: $2\operatorname{Sc}$ equals $\operatorname{tr}$ on $M_{2}(\mathbb{C})$, and the fifteen generators do not live there.


**The connection and ghost determinants drop out at the identity background because the identity commutes with every generator**, so no vector mass depends on $\rho$; that is a consequence and not an assumption.


**The fermion determinant does not drop out, because the Yukawa gives the sixteen masses $y_{i}\rho/2$**, and its coefficient $-\frac{1}{64\pi^{2}}(y_{1}^{4}+y_{2}^{4})$ can make the total one-loop coefficient negative. **The scalar-only coefficient is a ceiling, and the sign condition is $y^{4}<18\lambda_{1}^{2}$.**


## Summary of Notation


| symbol | meaning |

| --- | --- |

| $t_{a}$ | the fifteen normalised Hermitian generators, $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ |

| $G_{a}$ | the printed anti-Hermitian arrays, $\operatorname{tr}(G_{a}^{\dagger}G_{a})=2$ or $12$ |

| $A_{a,\imath}$ | the fifteen connection components, real |

| $\mathbb{F}_{\imath\jmath}$ | $\sum_{a}F_{a,\imath\jmath}t_{a}$, the curvature as a matrix |

| $D_{\imath}$ | $\partial_{\imath}-ig_{4}A_{\imath}$, the covariant derivative in the representation |

| $\zeta$ | the one fixing parameter |

| $c_{a}$, $\bar c_{a}$ | fifteen ghosts and antighosts, complex Grassmann, adjoint |

| $\Xi_{0}$ | $\frac{\rho}{2}\mathbb{1}$, the identity background |

| $y_{1}$, $y_{2}$ | the two eigenvalues of the Yukawa matrix $y_{\alpha\beta}$ |

| $\mathcal{C}$ | the coefficient of $\rho^{4}\ln(\rho^{2}/\mu^{2})$ |


## Further Reading


- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The display these four steps support, and the article whose assumptions are discharged here.

- [The Yang–Mills Equation in Biquaternionic Form](the-yang-mills-equation-in-biquaternionic-form.html). The $\mathrm{SU}(2)$ action written in the algebra, against which the transcription of §*The Ceiling* is measured.

- [The One-Loop Effective Potential of the Scalar Matrix](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The Hessian and the coefficient this article supplies the fermionic half of.

- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The tree potential whose quartics enter the scalar coefficient.

- [The $\mathrm{SU}(4)$ Instanton](the-su4-instanton-a-matrix-transcription-outside-the-algebra.html). Where the topological density, and the bundle it needs, are the subject.

- [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The vertices read off the normalisation fixed in §*The Trace*.

