# __The Alternatives of Writing: Side, Order, and the Notation of Two-Sided Operators__

## Introduction

The biquaternion corpus writes operators that act on the left, operators that act on the right, and operators that act on both sides at once. The last kind is the new one. Nobody is trained to read it, and the ordinary physics habit — an operator stands to the left of what it acts on — stops working the moment the operator is two-sided.

The question this note answers is narrow and practical. When an operator acts on the right, what does one write? Several answers are in use elsewhere in mathematics and in physics. The corpus has made two choices without stating either: it names the side in ninety-one articles, and it marks the side with an arrow in three. The note lists the options, shows each of them applied to twelve equations that matter to the corpus, measures what each option costs, and states the rule the corpus is in fact following.

Nothing here is a new result. It is an inventory, a set of tables, and a recommendation. The recommendation is that the choice is already made, that it is the right one, and that it should be stated once in the operator conventions so that no article has to rediscover it.

## The Four Levels

Most confusion about this subject comes from treating four different questions as one. They are separate, and they are answered by different objects.

| The level | The question | The corpus's answer | Fixed or free |
|---|---|---|---|
| Naming | What is the operator called? | $L_a$, $R_b$, $T_{a,b}$, $M$, $\mathsf C_\mu$ | Fixed by the conventions article |
| Display | How is the side marked on the page? | The arrow, and nothing else | Free, but should be uniform |
| Rewrite | May the operator be replaced by another? | $\operatorname{nat}$, and only on a whole operator | Fixed by a theorem |
| Components | Are indices written? | No | Fixed by the conventions |

The naming level is settled and needs no discussion. The two-sided operator is $T_{a,b}$, the left multiplication is $L_a$, the right multiplication is $R_b$, and *Operator and Calculus Conventions* fixes all three. A reader who writes $a\psi b$ has written a product, not an operator, and the operator that performs it already has a name.

The components level is settled too. The corpus bans indices as a carrier of the calculus: a contraction is a form and never an index. So the option of writing $\psi_i b_{ij}$ is available in principle and unavailable here.

What remains open is the display level, and one question at the rewrite level: whether the right action should be replaced by the left action through an anti-automorphism. The two are often confused, and the next section separates them.

## The Six Display Options

There are six ways to write a right action, and only one of them is used by the corpus.

| Code | Name | The form | Where it is standard |
|---|---|---|---|
| N0 | Bare juxtaposition | $\tilde\Psi\tilde\nabla$ | Nowhere; it is the ambiguous case |
| N1 | Arrow | $\tilde\Psi\overleftarrow{\tilde\nabla}$ | Quantum field theory, anomalies, chiral perturbation theory |
| N2 | Dot scope | $\vec A\,\dot{\vec\nabla}$ | Geometric algebra, calculus of variations |
| N3 | Opposite-algebra name | $\tilde\Psi\,\tilde\nabla^{\mathrm{op}}$ | Ring theory, module theory |
| N4 | Bimodule subscripts | ${}_{\tilde\nabla}\tilde\Psi$ | Module theory, in running text only |
| N5 | Row-vector flip | every field written as a row | Elementary matrix algebra |

**N0 is not an option.** If the operator is written after the field with no mark, the reader cannot tell whether it acts or whether it is a coefficient, and the physics prior is the opposite of what the corpus means. The corpus never does it: no article writes a right-acting gradient without a mark.

**N1 is the corpus's choice.** The arrow states the side and nothing else. It is the only one of the six that is already standard in physics for exactly this purpose, and it is the only one that reads as a mark rather than as a name. Its limit is that it exists only for differential operators. Nobody writes $\psi\overleftarrow{b}$.

**N2 is exact but barred.** The dot says which factor carries the derivative, so it survives products of three or more factors, where the arrow cannot say which one is meant. But the corpus has removed the glyph: *Operator and Calculus Conventions* states that no derivative is written with a dot, and a scan of the four hundred and four articles finds no derivative dot at all, every instance of the dot token in the corpus being the ellipsis of $\dots$. Reintroducing it for scope would collide with a rule the corpus has already paid for.

**N3 is exact and legal.** $\tilde\nabla^{\mathrm{op}}$ names the right-acting gradient and needs no glyph. The cost is that the side is fused into the name: a reader who does not know the convention reads $\tilde\nabla^{\mathrm{op}}$ as a different operator rather than as the same operator acting from the other side. It is the natural choice for a reader coming from algebra and the unnatural one for a reader coming from physics.

**N4 is exact and unreadable.** Subscripts state the module structure precisely and are unusable at display size. They are the right notation for a proof and the wrong notation for an equation.

**N5 is a global decision, not a local one.** Writing every field as a row makes the right action the default. The cost is not local: every matrix transposes, every dagger moves, and every equation already printed in the corpus has to be reread. It is not adoptable for one equation.

## Naming the Map

The corpus marks the value and almost never names the map. A scan of the four hundred and four articles returns five thousand five hundred and six occurrences of the glyph, in three hundred and fourteen of them. Five thousand four hundred and ninety-seven are a superscript on an element, $X^{\natural}$, or a subscript label, $\langle\cdot,\cdot\rangle_{\natural}$, $\bullet_{\natural}$. The other nine are the bare glyph, used as the name of the map, and one of those is the identity $\bar{\cdot}=\natural{}^{*}$, which is a statement about operators and needs the bare form.

So the corpus does write the map, in nine places, with the same glyph it uses for the value in five thousand four hundred and ninety-seven. That is the collision, and it already exists. A note that needs the map, as this one does, has to choose a form, and the choice is cheap if it is made once and made well.

This note uses $\operatorname{nat}$, defined by $\operatorname{nat}(X)=X^{\natural}$. The candidates it rejected are these.

| Candidate | Writing | In the corpus | Verdict |
|---|---|---|---|
| The bare glyph | $\natural\,L_a\,\natural$ | Five thousand four hundred and ninety-seven as a mark, nine as the map | Collides with the value form |
| Placeholder on the mark | $(\cdot)^{\natural}\circ L_a\circ(\cdot)^{\natural}$ | None | Correct, and a definition rather than a running form |
| Upright word | $\operatorname{nat}$ | None | Recommended |
| The sharp | $\sharp\,L_a\,\sharp$ | None | Free, and too close to the glyph it must not be confused with |
| A capital letter | $C$, $K$, $N$ | Two thousand five hundred to eight thousand two hundred each | All taken |

The corpus already owns the device that settles it. For the one map it does name as an operator it writes the mark on a placeholder, $\bar{\cdot}$, and the same construction on the natural mark gives $(\cdot)^{\natural}$. That is the honest definition, and $\operatorname{nat}$ is its abbreviation.

The collision is not hypothetical, and care alone does not remove it. The chiral-pair equation used below writes $\tilde\nabla^{\natural}$ for the mark on a value, and the corpus elsewhere writes the same glyph bare for the map. A document that quoted both would carry one sign with two meanings. The fault is the corpus's: of its three conjugations, one has a placeholder form, $\bar{\cdot}$, and two have only a mark.

## The Three Rewrite Options

The rewrite level asks a different question: not how to mark the side, but whether the right action can be replaced by a left action. Three routes exist.

| Code | Route | The form | The cost |
|---|---|---|---|
| R1 | Anti-automorphism | $R_b=\operatorname{nat}\circ L_{\natural(b)}\circ\operatorname{nat}$ | Two applications of $\operatorname{nat}$, of length four each |
| R2 | Left action plus commutator | $R_b=L_b+\mathrm{ad}_b$ | Blind on the central part, which is the mass |
| R3 | Components | $\psi_i b_{ij}$ | Barred with the index calculus |

**R1 is exact.** The natural sign is $\mathbb{C}$-linear, of order two, and an anti-automorphism, $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$. Write $\operatorname{nat}$ for the map that applies it, $\operatorname{nat}(X)=X^{\natural}$.

The identity follows in two steps, and the two steps are the two properties, in that order:

$$
\psi b=\operatorname{nat}\bigl(\operatorname{nat}(\psi b)\bigr)\quad(\text{order two}),
\qquad
\operatorname{nat}(\psi b)=\operatorname{nat}(b)\,\operatorname{nat}(\psi)\quad(\text{anti-automorphism}),
$$

so

$$
R_b(\psi)=\psi b=\operatorname{nat}\bigl(\operatorname{nat}(b)\,\operatorname{nat}(\psi)\bigr)=\bigl(\operatorname{nat}\circ L_{\natural(b)}\circ\operatorname{nat}\bigr)(\psi),
$$

with residual zero on twenty random $b$.

**The order reversal is the content.** The second step is the one that matters: it swaps the two factors, and the swap is what puts $b$ on the right. A display that writes the three maps in a row hides the swap, and a reader who drops the outer $\operatorname{nat}$ gets $\operatorname{nat}(b)\operatorname{nat}(\psi)$, which is $\operatorname{nat}(\psi b)$ and not $\psi b$. Recomputed on random pairs, that error is of size $20.7$, so the nesting is not decoration.

**Since the map is of order two it is its own inverse, and the sandwich is a conjugation**,

$$
R_b=\operatorname{nat}^{-1}\circ L_{\natural(b)}\circ\operatorname{nat},
$$

the left action by $\natural(b)$, conjugated. That is the shortest true reading of the identity, and it is the reason $\operatorname{nat}$ transports one factor cheaply and costs four cells when it wraps a whole operator.

It is the only one of the three routes that turns every right action into a left action.

**R2 is exact and cheap.** Write $\mathrm{ad}_b(\psi)=[\psi,b]$. Then $L_b+\mathrm{ad}_b=R_b$ holds by definition, since $b\psi+(\psi b-b\psi)=\psi b$. No new glyph, no anti-automorphism, no length. R2 is what a reader who refuses the arrow would naturally use.

**R2 is blind on the mass.** The admixture $[\psi,b]$ vanishes exactly when $b$ is central, and the centre of $\mathbb{B}$ is $\mathbb{C}e_t$, which is where the mass lives. A Lagrangian does not keep the commutator, it keeps the scalar part of a product, $\mathrm{Sc}(\bar\psi[\psi,b])$, and there the blindness is sharper. With the norm form $\bar\psi=\psi^{\natural}$ the term is zero exactly: $\psi^{\natural}\psi=\psi\psi^{\natural}=N(\psi)e_t$, both factors fixed by the natural sign, so $\psi^{\natural}[\psi,b]=N(\psi)(b-b)$. With a bar that is not the natural sign it is not zero: at $\psi=\vec e_x+i\vec e_y$ and $b=\vec e_z$ the product is $-4i\,e_t$ and the Lagrangian term is $-4i$. So R2 either deletes the term the corpus cares about or silently replaces it by another.

**R3 is barred.** Same reason as N4.

## Why the Arrow and the Transposition Do Not Compete

The arrow and R1 are usually presented as alternatives. They are not. One is a mark on a page, the other is a theorem about operators.

- The arrow says **which side** a written operator acts on. It changes nothing about the operator.
- R1 says the right action **is** a left action in disguise. It changes the operator and needs the disguise written twice.

The difference shows up the moment the operator carries a derivative, and it is a difference of length, not of possibility. R1 does reach a derivative. The natural sign acts on the coefficients and commutes with $\partial$, so for a single direction

$$
(\partial_\mu\tilde\Psi)\,\vec e_\mu=\operatorname{nat}\bigl(\operatorname{nat}(\vec e_\mu)\,\partial_\mu(\operatorname{nat}\tilde\Psi)\bigr),
$$

with residual zero, as the appendix verifies on sample fields. The middle operator is the natural conjugate of the gradient component, and it is not an element of $\mathbb{B}$.

What R1 cannot do is get shorter. On an element the composite collapses to a cell of length one and nobody writes it; on a derivative it collapses to nothing, so the sandwich costs three symbols and a flipped frame coefficient where the arrow costs one glyph. The arrow wins on length, and only on length.

A third operation is often confused with both. Integration by parts,

$$
\int(\tilde\Psi\overleftarrow{\partial_\mu})\tilde\Phi=-\int\tilde\Psi(\partial_\mu\tilde\Phi)+\text{boundary},
$$

moves differentiation between two factors of a bilinear form, and it preserves neither the operator nor the sign. No conjugation replaces it, and no arrow replaces it either.

This gives the reason the arrow is in the corpus and R1 is not. Algebraic right action is already a cell, $R_b=T_{e_t,b}$, of length one, so there is nothing to gain by rewriting it. Differential right action is not a cell, so the rewriting exists but is longer than the mark. The arrow covers the second case; the cells cover the first; and neither has any work left to do in the other's territory.

## The Transposition, Precisely

Three statements are often run together, and then a fourth question decides what one of them says. The three are the operator identity, its cost and its array form; the fourth is the frame, and it is treated last because it is the one that makes the array form true or false.

### The Operator Level

$R_b=\operatorname{nat}L_{\natural(b)}\operatorname{nat}$ is an identity between operators. It is basis-free, it holds for every $b$, and its residual is zero. Its cost is not the operator but the display: $\operatorname{nat}$ has to be written twice.

### The Cost of $\operatorname{nat}$

$\operatorname{nat}$ is not a cell. It decomposes as

$$
\operatorname{nat}=-\tfrac12\bigl(T_{e_t,e_t}+T_{e_x,e_x}+T_{e_y,e_y}+T_{e_z,e_z}\bigr),
$$

whose four coefficients are each $-\tfrac12$. Its matrix is not $-\tfrac12 I_4$ but $\operatorname{diag}(1,-1,-1,-1)$, as the appendix computes; the $-\tfrac12 I_4$ is the diagonal block of coefficients in the sixteen-cell basis, which is a different object from the matrix of the map. So $\operatorname{nat}$ has length four, the largest length that occurs. Writing R1 instead of a single arrow replaces one glyph by eight cells.

By contrast, conjugating a single factor is cheap and stays inside the cell calculus:

$$
\operatorname{nat}\,L_a\,\operatorname{nat}=R_{\natural(a)}=T_{e_t,\natural(a)},
$$

residual zero, length one. What is expensive is the map, not the transport.

### The Array Level

In the matrix model the same map is a conjugated transpose,

$$
\mathsf M_2\bigl(\operatorname{nat}(X)\bigr)=\sigma_2\,X^{\mathsf T}\,\sigma_2^{-1},
$$

residual zero on fifty random $X$. The plain transpose is a different map: it agrees with $\operatorname{nat}$ on $e_t$ and on $\vec e_y$, and differs by $2$ on $\vec e_x$ and on $\vec e_z$. A reader who transposes without the $\sigma_2$ gets two of the four units wrong.

### The Transposition Is Coordinate-Bound

The conventions article prints the array-level identity with the Peirce exchange,
$\mathsf M_4^{R}(\tilde Q)=\mathsf S\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$,
and it is correct: recomputed on the four printed matrices and on fifty random elements, the residual is zero. Two things follow that are worth stating, because both are easy to get wrong, and this note got both wrong at first.

**The two descriptions of $\mathsf S$ agree.** The swap matrix and the reflection $\operatorname{diag}(1,1,-1,1)$ are the same operator written in two bases. Let $P$ have for columns $e_t$, the two mixed Peirce units and $e_z$, expressed in the coefficient basis; then $P^{-1}\operatorname{diag}(1,1,-1,1)P$ is the swap matrix, residual zero. No inconsistency there, and nothing to correct.

**The identity does not survive a change of frame.** Write the same four $L_\nu$ from the multiplication itself, in the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and the printed identity fails by $2$. The sandwich that makes it true in that frame is $\operatorname{nat}$, residual zero. One identity, one algebra, two frames, two matrices.

So the argument for $\operatorname{nat}L_{\natural(b)}\operatorname{nat}$ is not that the printed formula is false. It is that $\operatorname{nat}$ names the object that makes the formula true, while $\mathsf S$ is the matrix of that object in one frame. A reader who carries $\mathsf S$ into another frame writes a false identity; a reader who carries $\operatorname{nat}$ writes a true one. And without any sandwich at all the identity fails in both frames: $R_\nu=L_\nu^{\mathsf T}$ has residual $1$ on $\vec e_x$ and $\vec e_y$ and $2$ on $\vec e_z$ in the corpus frame, and residual $2$ on all three in the coefficient frame. It never holds; on $\vec e_t$ alone both sides are the identity.

That is the general shape of the display level. A transposition is a statement about a pairing in a basis, so it is true or false only once the basis is named. A named operator is true in every basis, which is why the naming level comes first.

## The Census

The corpus has voted, and the vote is not close.

| Object | Articles that use it |
|---|---|
| $L_a$, left multiplication | 86 |
| $R_b$, right multiplication | 84 |
| $T_{a,b}$ or $T_{Q,P}$, two-sided | 61 |
| $T_{e_\mu,e_\nu}$, frame cells | 60 |
| Any of the three | 91 |
| The arrow, as a side mark | 3 |
| The arrow, as a decoration on an algebra | 4 |
| A derivative written with a dot | 0 |

The counts are of articles, not of occurrences, and each is a scan for the glyph in the subscript form the conventions fix: a single lowercase element name for $L$ and $R$, the brace form for $T$. The union of the three is ninety-one articles out of four hundred and four.

The two arrow rows are counted separately because the glyph carries two meanings in the corpus, and only one of them is the subject of this note. Three articles use it as a side mark: the Maxwell article once, the Poisson-bracket article once, the minimal-coupling article twice. Four articles use it on an algebra symbol instead, $\overleftarrow{\mathbb{C}}$ and $\overleftarrow{\mathbb C\otimes\mathbb O}$, in the quoted construction of the complex octonionic chain algebra, where it records a left action and not a body of differentiation.

Two conclusions follow. The cells are the corpus's ordinary language for operators, and they are used by ninety-one articles, near a quarter of the corpus. The arrow is the corpus's language for the one case the cells cannot express: in the three articles that use it as a side mark it is always on a derivative, never on an algebraic operator. No article writes a right-acting gradient without a mark.

## The Equations

Twelve equations follow, in the order of the corpus's own priority. Each is quoted as the corpus writes it, then shown under the options that could carry it, then given a verdict. Equations that need no mark are included deliberately: most of the corpus is in that case, and the note would be misleading if it only exhibited the hard ones.

### 1. The Chiral Pair of the Dirac Equation

*The Dirac Equation in Biquaternionic Form*, the chiral pair in the opening section:

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad \tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $\tilde\nabla\tilde\Psi_R$ | Correct here, because the operator is written first |
| N1 | — | Not applicable, the field is not to the left |
| N2 | — | Not applicable |
| N3 | $\tilde\nabla^{\mathrm{op}}\tilde\Psi_R$ | Legal, and it would state a side that is already stated |
| N4 | ${}_{\tilde\nabla}\tilde\Psi_R$ | Exact, noisy |
| N5 | unchanged | The field is a biquaternion, not a row |

No option is needed. This is the ordinary case: a first-order left operator applied to a field, which is what the physics convention was built for, and it is the case the rest of this note does not concern.

### 2. The Massless Dirac Equation

Same article, the massless limit:

$$
\tilde\nabla\tilde\Psi=0 .
$$

No option changes the display. A homogeneous equation cannot show a side ambiguity, because there is no second object for the operator to act on.

### 3. The Right-Acting Gradient with a Connection

*The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, the section on the left and right action:

$$
\tilde\Psi\overleftarrow{\tilde\nabla}+\frac{i\varrho}{\hbar}\,\tilde\Psi\tilde A,
\qquad
\tilde\Psi\overleftarrow{\tilde\nabla}:=\sum_\mu\Bigl(\partial/\partial Q_\mu\,\tilde\Psi\Bigr)e_\mu .
$$

This is the only one of the twelve where the display choice actually decides whether the equation can be read.

| Option | Writing | Verdict |
|---|---|---|
| N0 | $\tilde\Psi\tilde\nabla$ | No: indistinguishable from a left action |
| N1 | $\tilde\Psi\overleftarrow{\tilde\nabla}$ | Yes, and it is the corpus form |
| N2 | $\vec\nabla$ acting on the previous factor, marked by a dot | Yes, and unambiguous for three factors |
| N3 | $\tilde\Psi\,\tilde\nabla^{\mathrm{op}}$ | Yes, at the price of a name to remember |
| N4 | ${}_{\tilde\nabla}\tilde\Psi$ | Exact, unreadable in a display |
| N5 | transpose the field | Would change the whole article |

N1 is right. R1 does not apply, since $\tilde\nabla$ is differential. The article itself supplies the reason the arrow matters: the left form and the right form are both gauge covariant, and the mixed form is not. A notation that cannot separate the left gradient from the right gradient cannot state the difference the article is about.

### 4. Maxwell's Theory in Quaternion Form

*Maxwell's Theory on Non-Commutative Spaces and Quaternions*, the spin-tensor form:

$$
\nabla F+\tfrac12\bigl(\nabla G+G^+\overleftarrow{\nabla}\bigr)=-J .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $G^+\nabla$ | No |
| N1 | $G^+\overleftarrow{\nabla}$ | Yes, and it shows at a glance which of the two terms acts which way |
| N2 | $g_m$ times a scoped derivative | Yes, and less legible in a four-term sum |
| N3 | $G^+\nabla^{\mathrm{op}}$ | Exact, and shorter than the arrow |
| N4 | subscripted | No, in a display |
| N5 | transpose $G^+$ | Local only, and it hides the symmetry |

N1 is right, and this equation is the arrow's best case: the display is a sum of one left-acting and one right-acting term, and the arrow is the only mark that shows the difference without a name.

### 5. The Mass-Shell Cell

*Thomson and Compton Scattering*, the mass-shell cell built on the frame cells as *Anomalies and Anomaly Cancellation* defines them:

$$
D(p)=\mathsf C_\mu p_\mu+m\,T_{e_t,e_t},
\qquad
\mathsf C_0=iT_{e_t,e_x},\quad \mathsf C_k=iT_{e_k,e_y}.
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | impossible | The operator has no one-sided form |
| N1 | impossible | Not a differential operator |
| N2 | impossible | Same reason |
| N3 | impossible | The right factor is an element, not a derivation |
| N4 | impossible | Same reason |
| N5 | impossible | A two-sided product is not a matrix times a column |
| Cells | $\mathsf C_\mu p_\mu+mT_{e_t,e_t}$ | The only form that exists |

The equation is the argument for the naming level. Every option at the display level fails, and the reason is not that the notation is poor but that the object is genuinely two-sided. Recomputed on the mass shell at $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$: $\lVert D^2-2mD\rVert=4\times10^{-16}$, matrix rank two, length two, trace $4m=5.2$, and $\{\mathsf C_\mu,\mathsf C_\nu\}=2\operatorname{diag}(1,-1,-1,-1)$.

### 6. The Chirality Cell

*Anomalies and Anomaly Cancellation*, the table of frame cells:

$$
\mathsf C_5=-i\,T_{e_t,e_z}=-iR_{e_z},
\qquad
\mathsf C_5^2=1 .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | impossible | The operator is pure right action |
| N1 | $\psi\overleftarrow{\vec e_z}$ | No: the arrow is for derivatives only |
| N2 | impossible | Same reason |
| N3 | $R_{e_z}$ | Yes, and it is the same statement |
| N4 | subscript | No |
| N5 | transpose | No |
| Cells | $-iT_{e_t,e_z}$ | Yes |

$\mathsf C_5$ is a *right multiplication* and it is not a left one: $R_{e_z}\neq L_a$ for any $a$, the best residual over three hundred trials being $1.14$, and the reason is that $R_b=L_a$ forces $b=a$ and $b$ central, while $\vec e_z$ is not central. So the chirality operator has no one-sided left form at all. It nevertheless has a cell form of length one. This is the sharpest case in the corpus of the cell names doing work that no display convention can do.

Recomputed: $\mathsf C_5^2=1$ exactly, length one, anticommutes with all four $\mathsf C_\mu$, and $\operatorname{tr}(\mathsf C_5\mathsf C_0\mathsf C_1\mathsf C_2\mathsf C_3)=-4i$.

### 7. The Peirce Sign

*The Biquaternion Physical Interpretation of Chirality*, the right multiplication that grades the two ideals:

$$
P=R_{i\vec e_z},
\qquad
P(s)=s\ \text{on }S_+,
\qquad
P(s)=-s\ \text{on }S_- .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $s\,i\vec e_z$ | Correct and uninformative |
| N1 | — | Not applicable |
| N3 | $R_{i\vec e_z}$ | Yes, and it names the side |
| Cells | $T_{e_t,i\vec e_z}$ | Yes, and it is $-\mathsf C_5$ |
| N4, N5 | — | No |

The same object appears under two names in the corpus, and the relation between them is exact: $P=R_{i\vec e_z}=-\mathsf C_5$, residual $2$ against $\mathsf C_5$ itself. Both names are legitimate. The article that uses $P$ is about the module decomposition and wants the right multiplication visible; the article that uses $\mathsf C_5$ is about the trace and wants the sign fixed. A reader who meets one and then the other needs the identity, and no article currently states it.

### 8. The Chiral Projectors on a Field

*Chiral Fermions in the Biquaternion Framework*, the chirality operator on the field and its two projectors:

$$
\Psi\mapsto-i\,e_t\Psi e_z,
\qquad
P_L\Psi=\tfrac12\bigl(\Psi+i\,e_t\Psi e_z\bigr),
\qquad
P_R\Psi=\tfrac12\bigl(\Psi-i\,e_t\Psi e_z\bigr).
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $e_t\Psi e_z$ | Correct, and it is the only form that shows both factors |
| N1 | — | The operator is algebraic, not differential |
| N3 | $T_{e_t,e_z}\Psi$ | Yes, and it hides that the field sits between the factors |
| Cells | $-iT_{e_t,e_z}\Psi$ | Yes, compact, correct |
| N4, N5 | — | No |

The bare product $e_t\Psi e_z$ is right here, and it is the one place where N0 is the best answer rather than the worst: the field is visible between the two factors, which is what the projector formula is doing. Writing $T_{e_t,e_z}\Psi$ is equally correct and less immediate. This is worth stating, because it can look like an exception to the rule that the corpus never writes a bare product. It is not one: the corpus never writes a bare *operator*, and $e_t\Psi e_z$ is a product of three elements with the field among them.

### 9. The Spin Resolution

*Thomson and Compton Scattering*, the spin-resolved shell:

$$
D_s(p)=\tfrac12\,D(p)\bigl(1+\mathsf C_5\,\mathsf C_\mu s_\mu\bigr),
\qquad
\sum_{s=\pm}D_s(p)=D(p).
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | impossible | Four factors, two of them two-sided |
| N1 | impossible | Not differential |
| N4 | nested subscripts | Exact and unreadable |
| N5 | transpose | Would need the transposition theorem to see the sum is the same |
| Cells | $\tfrac12D(p)(1+\mathsf C_5\mathsf C_\mu s_\mu)$ | The corpus form, and the only legible one |

Recomputed on the mass shell with a spin vector satisfying both $s\cdot p=0$ and $s^2=-1$: $\lVert D_s^2-2mD_s\rVert=9\times10^{-16}$, the two spin cells are orthogonal to $8\times10^{-17}$, they sum to $D(p)$, $\frac{1}{2m}D_s$ has rank one and trace one, and $D_s$ has length four. The length is the point: the spin resolution doubles the length of the mass-shell cell, and no rewriting shortens it.

### 10. The Gauge Transformation and the Curvature

*The Gauge Principle in Biquaternionic Form*, the transformation law of the potential and its curvature:

$$
\tilde A_2=\tilde A-\tilde\nabla\Gamma,
\qquad
[D_\mu,D_\nu]=\frac{i\varrho}{\hbar}F_{\mu\nu},
\qquad
D_\mu=\partial/\partial Q_\mu+\frac{i\varrho}{\hbar}A_\mu .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $\tilde\nabla\Gamma$ | Correct: the operator is on the left and acts on what follows |
| N1 | — | Would add a side that the writing already fixes |
| N3 | $\Gamma\tilde\nabla^{\mathrm{op}}$ | Legal only if the convention were right-to-left |
| N4 | subscript | No |
| N5 | transpose | No |

No option is needed, and the table is here to make a point: the left differential operator is not a special case of the two-sided one. It is the ordinary case, it has been the ordinary case since Newton, and the corpus's two-sided operators did not change it.

The article records one thing about the right action and leaves it open: whether the physical matter representation is the left one or the right one. The mirror construction itself is written out in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, not here, and the mirror is where N1 is needed. The pair is the content: the left and the right form are both covariant, the mixed form is not.

### 11. The Anomaly Trace

*Anomalies and Anomaly Cancellation*, the trace of the chiral volume cell:

$$
\operatorname{tr}\bigl(\mathsf C_5\mathsf C_0\mathsf C_1\mathsf C_2\mathsf C_3\bigr)=-4i .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | the five cells written out | Correct and unreadable |
| N1 | — | Not differential |
| N3 | $R_{\mu}$ names in place of cells | The same statement, with five names to track |
| Cells | as written | Yes |
| N5 | transpose | Would break the order inside the trace |

The trace is where the order inside the product matters and where a row-vector convention would be actively wrong: $\operatorname{tr}(MN)$ is invariant under transposition of the whole product, but the individual factors are not invariant, and a display that transposes one of them changes the value. Recomputed: $-4i$ exactly, with $\mathsf C_5^2=1$ and $\{\mathsf C_5,\mathsf C_\mu\}=0$.

### 12. The Poisson Bracket Between Matrices and Operators

*Similitudes Between the Poisson Bracket and the Quantum Commutator*, the arrow at its weakest:

$$
\Lambda=\sum_i\Bigl(\overleftarrow{\partial/\partial q_i}\,\overrightarrow{\partial/\partial p_i}
-\overleftarrow{\partial/\partial p_i}\,\overrightarrow{\partial/\partial q_i}\Bigr).
$$

| Option | Writing | Verdict |
|---|---|---|
| N1 | as written | Correct, and ambiguous about the operand |
| N2 | dot scope on each factor | Clearer about which argument is differentiated |
| N3 | $\partial^{\mathrm{op}}$ | Exact, and hides that there are two operands |
| N4 | subscripts on both arguments | Exact, unreadable |
| N5 | — | No |

Here the arrow does its job and reaches its limit in the same expression. It says that the left derivative acts on what is to the left and the right derivative on what is to the right, which is exactly right. It cannot say what those two things are, because the bracket is written without arguments. This is the one equation in the corpus where the notation is genuinely under-determined, and it is under-determined for a reason outside the notation: the two arguments have been suppressed.

### What the Twelve Decide

The twelve fall into three classes, and the classes are the argument for the tiers.

| Decided by | Equations | Count |
|---|---|---|
| The naming level | 5, 6, 7, 8, 9 — mass shell, chirality cell, Peirce sign, chiral projectors, spin resolution | 5 |
| The display level | 3, 4, 12 — minimal coupling, Maxwell, Poisson bracket | 3 |
| Nothing | 1, 2, 10, 11 — Dirac pair, massless Dirac, gauge transformation, anomaly trace | 4 |

The naming level decides the most equations and the display level the fewest, and the display equations are all differential. That is the empirical case for naming first: the corpus's hardest objects are already handled by names, and the display is needed only where a derivative acts on what precedes it. It is also the reason a notation reform should start at the naming level and stop there unless an equation forces it further.

## The Measured Costs

Every claim above about cost is a computed number. The table collects them.

| Object | Length | Matrix rank | Note |
|---|---|---|---|
| $R_b=T_{e_t,b}$ | 1 | 4 | The right action is already a cell |
| $\operatorname{nat}L_a\operatorname{nat}=T_{e_t,\natural(a)}$ | 1 | 4 | Transporting one factor is cheap |
| $\operatorname{nat}$ | 4 | 4 | The map itself is not a cell |
| $\mathsf C_5=-iT_{e_t,e_z}$ | 1 | 4 | A right multiplication |
| $\mathsf C_\mu$ | 1 | 4 | Frame cell |
| $D(p)$ | 2 | 2 | Mass shell |
| $D_s(p)$ | 4 | 1 after $1/2m$ | Spin resolution |
| $P_+=\tfrac12(T_{e_t,e_t}-iT_{e_t,e_z})$ | 1 | 2 | Chiral projector |

| Residual | Value |
|---|---|
| $R_b-\operatorname{nat}L_{\natural(b)}\operatorname{nat}$ | 0 |
| $\mathsf M_2(\operatorname{nat}X)-\sigma_2X^{\mathsf T}\sigma_2^{-1}$ | 0 |
| $\operatorname{nat}$ against the plain transpose on $\vec e_x$ | 2 |
| $\min_a\lVert R_{e_z}-L_a\rVert$ | 1.14 |
| $D^2-2mD$ on shell | $4\times10^{-16}$ |
| $D_s^2-2mD_s$ on shell | $9\times10^{-16}$ |
| $R_\nu-\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$, corpus frame | 0 |
| $R_\nu-\operatorname{nat}L_\nu^{\mathsf T}\operatorname{nat}$, coefficient frame | 0 |
| $R_\nu-\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$, coefficient frame | 2 |
| $R_\nu-L_\nu^{\mathsf T}$, corpus frame | $1,1,2$ on $\vec e_x,\vec e_y,\vec e_z$ |

## The Rule in Tiers

The corpus follows a rule. It has never been written down, and it is short enough to write down.

**Tier one: name the operator.** Left multiplication, right multiplication, two-sided operator, frame cell, chirality cell, mass-shell cell. No glyph, no arrow, no dot. This covers the ordinary language of the corpus and should be the default in every article.

**Tier two: the arrow, for a differential operator acting rightward.** Written only where a derivative acts on what precedes it, and chosen here because it is shorter than the sandwich and not because the sandwich fails. Defined once, in the operator conventions, with two clauses fixed: that the arrow means the derivative acts on the factor to its left, and that the double arrow means one derivative on each side with the sign convention stated.

**Tier three: dot scope, for a product of three or more factors carrying derivatives.** The arrow cannot say which factor is meant when there are three. Dot scope can. It is currently barred by the no-dot rule, which is about $\dot x$ for $dx/dt$ and not about scope, and the ban could be narrowed to the case it was written for. Nothing in the corpus needs this tier yet; the Poisson bracket is the only expression that nearly does.

**Tier four: $\operatorname{nat}$, for a deliberate change of side.** Only on whole operators, never on one factor, and never as a way of avoiding the arrow. Its cost is length four per occurrence, and a display that uses it twice has replaced one glyph by eight cells. It can be applied to a derivative, and then it is longer still than it is on an element.

**Never: reading integration by parts as a rewrite.** It is a sign and a boundary term, not a change of side, and the arrow survives it. The side of a differential operator can be changed, at the cost of a longer display; the transfer of a derivative from one factor to another cannot.

## Deciding the Arrow

The collision recorded in *The Census* is cheap to settle now and expensive to settle later, because the four articles that decorate an algebra and the three that mark a side are still disjoint. A decision is needed, and the corpus has the material to make one.

The principle: **the arrow is a mark of a side for a derivative, and an algebra symbol is not a derivative.** An algebra written under the arrow is not being differentiated, so the mark is doing something else, and the two uses cannot both be the arrow.

| Candidate for the algebra left-action mark | Writing | Collision | Verdict |
|---|---|---|---|
| Prescript | ${}_{L}\mathbb{C}\otimes\mathbb{O}$ | None: prescripts in the corpus are index blocks only | Recommended |
| Superscript $L$ | $\mathbb{C}^{L}\otimes\mathbb{O}$ | The superscript $L$ is the sector label in eight articles, $M_4^{L}$, $\Psi_0^{L}$ | Reject |
| Second arrow | $\leftarrow\mathbb{C}\otimes\mathbb{O}$ | None, but two near-identical marks in one document | Weak |
| The word | the left action of the complex octonionic chain algebra | None, verbose | Acceptable in prose |

The recommendation is therefore: keep $\overleftarrow{\ }$ for derivatives and for nothing else, and write the algebra's left action with a prescript or with the word. Two sentences in the operator conventions would fix it, one for each mark, and the seven articles would need no rewriting today, only the four that quote the chain algebra would change a glyph.

This note does not make the change. It records the decision, because a reserve note is the right place to argue it and the conventions article is the right place to state it.

## Failure Modes

Six failures are easy to produce, and each has been produced during the writing of this note.

**Confusing the two transposes.** The plain array transpose and the corpus's $\operatorname{nat}$ differ on two of the four units, with residual $2$ on $\vec e_x$. A reader who transposes without the $\sigma_2$ in the matrix model gets $\vec e_y$ right and the other two wrong, which is the worst possible outcome: the formula looks like it works.

**Checking a basis-dependent identity in your own basis.** The first draft of this note filed the conventions article as carrying a false identity: recomputing $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ in the coefficient basis gives residual $2$, with either description of $\mathsf S$. The identity is true as printed, with residual zero on the four printed matrices and on fifty random elements. The failure came from testing it in a frame the corpus does not use, where the sandwich is $\operatorname{nat}$ instead. A statement about a transpose must be checked in the frame it was written for, and an erratum must not be filed on the strength of a mismatch of frames.

**Confusing the operator with its display.** Conjugating one factor does not destroy the cell form; it produces another cell, of length one. The statement "the transposition destroys the cell form" is therefore false as a statement about the algebra. What has length four is $\operatorname{nat}$ itself, so the cost sits in the display and nowhere else, and the two must be said separately.

**Confusing the scalar part of a commutator with the scalar part of a product.** $\mathrm{Sc}([\psi,b])=0$ is true by the trace property. The term in the Lagrangian is $\mathrm{Sc}(\bar\psi[\psi,b])$, which is a product and does not vanish, except when the bilinear is the norm form. A check that samples basis elements will pass, because on basis elements $\bar\psi\psi$ is central; the failure appears only on superpositions.

**Reading the sandwich as a chain.** $R_b=\operatorname{nat}\circ L_{\natural(b)}\circ\operatorname{nat}$ is three maps in a row, and the middle one's index is $\natural(b)$, not $b$. Two misreadings follow, and both are silent. Dropping the outer map gives $\operatorname{nat}(\psi b)$ instead of $\psi b$, wrong by $20.7$ on random pairs. Keeping $b$ in the middle gives the wrong operator, since $L_b$ and $L_{\natural(b)}$ differ on every non-central $b$. Write the identity as a conjugation, $\operatorname{nat}^{-1}\circ L_{\natural(b)}\circ\operatorname{nat}$, and use the two-step derivation, so that the reversal and the change of index are each visible at the step that causes them.

**Imposing one of two conditions in a check.** The spin resolution is idempotent only for a spin vector with both $s\cdot p=0$ and $s^2=-1$. A check that imposes one of the two reports a false failure, and a check that imposes neither reports a false success on the sum and a false failure on the square. Both happened here before the third attempt imposed both.

## What Is Not Settled

- **The relation between $P$ and $\mathsf C_5$.** It is exactly $P=-\mathsf C_5$, and no article states it. Two articles use the two names for the same object.
- **Whether tier three is needed.** The corpus has one expression that would benefit and none that requires it. Until an article writes a three-factor derivative product, dot scope is available and unused.
- **The double-arrow convention.** The corpus does not use the double arrow anywhere. If it ever does, the factor of $\tfrac12$ has to be fixed, because the literature is not unanimous.
- **One glyph, two meanings.** The arrow is a side mark in three articles and a left-action decoration on an algebra symbol in four. The two uses never meet in a single equation today, because the octonionic constructions and the Dirac equations live in different articles. They would meet in any article that quoted both. The candidates and a recommendation are in the section above, *Deciding the Arrow*; the decision is the author's, and it belongs in the operator conventions.
- **The corpus has no settled name for the natural map.** It marks the value, $X^{\natural}$, and names the operator $X\mapsto X^{\natural}$ only by writing the same glyph bare in nine places. *Naming the Map* supplies one, $\operatorname{nat}$, and a sentence in *Product and Form Conventions* beside the $\bar{\cdot}$ row would make it official. The same sentence would fix the placeholder form $(\cdot)^{\natural}$.
- **Which side is the matter representation.** The minimal coupling article records the left and the right construction as two covariant mirrors and calls the choice open. The notation question is downstream of that choice and cannot settle it: a corpus that had chosen the right action would write N1 everywhere and the cells would change roles. Until the choice is made, the arrow is the only mark that keeps both forms printable without rewriting the other.

## Summary

The right action is written in the corpus in one way out of six, and the corpus has never said so.

**The levels are four.** Naming is fixed by the conventions, display is free, rewrite is fixed by a theorem, and components are barred. Confusion comes from treating them as one.

**The arrow is not the transposition.** The arrow marks a side on a page and changes nothing. The transposition replaces the right action by a left one and costs two applications of $\operatorname{nat}$, of length four each. The arrow is used only for derivatives, and there it is the shortest form rather than the only one: the sandwich reaches a derivative too, at the cost of a longer display.

**Algebraic right action needs no arrow.** $R_b=T_{e_t,b}$ is a cell of length one. The corpus writes it as $R_b$, and the three articles that use the arrow as a side mark all put it on a derivative.

**Of twelve equations, the display decides three.** They are the right-acting gradient, the Maxwell sum of a left and a right term, and the Poisson bracket. Five are decided by the naming level, because they are two-sided or purely right-sided and no display option exists for them. Four are decided by nothing, because the operator is written first.

**The rule is four tiers.** Name the operator; arrow for a rightward derivative; dot scope for three factors with derivatives; $\operatorname{nat}$ only on whole operators. Never read integration by parts as a change of side.

**The transposition is coordinate-bound, the named operator is not.** The conventions' $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ is true, with residual zero, in the frame it was written for; the same identity in the coefficient frame needs $\operatorname{nat}$ instead of $\mathsf S$, and without a sandwich it fails in both. This note filed it as an erratum on a first pass and withdrew the erratum: the mismatch was one of frames.

**The map needs a name.** The corpus writes $X^{\natural}$ as a mark and the bare glyph as the map in nine places, so the same sign already means two things. $\operatorname{nat}$ is the cheapest name that does not collide, and one sentence in the conventions would settle it.

**The arrow needs a decision.** It marks a side in three articles and decorates an algebra in four. The recommendation is to reserve it for derivatives and give the algebra left-action a prescript.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a\psi=a\psi$ | Left multiplication by the element |
| $R_b\psi=\psi b$ | Right multiplication by the element |
| $T_{a,b}=L_aR_b$ | Two-sided operator, $\psi\mapsto a\psi b$ |
| $X^{\natural}$ | The natural sign applied to an element: the corpus's usual form |
| $\operatorname{nat}$ | The map $X\mapsto X^{\natural}$, which the corpus names only by writing the glyph bare |
| $\natural$ in a subscript | A label, as in $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\overleftarrow{\partial}$ | The derivative acting on what precedes it |
| $\overrightarrow{\partial}$ | The derivative acting on what follows it |
| $M^{\mathsf T}$ | The plain transpose of the array |
| $\mathsf S$ | The Peirce exchange; the matrix that carries the transpose in the canonical frame |
| $\operatorname{nat}$ as a matrix | $\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis |
| N0 to N5 | The six display options |
| R1 to R3 | The three rewrite options |
| Length | The coefficient rank in the sixteen-product basis |
| $\mathsf C_\mu$, $\mathsf C_5$ | Frame cells and the chirality cell |

## Further Reading

- [*Operator and Calculus Conventions*](../articles_physics/conventions-of-the-operators-and-the-calculus.html) for the naming level and the no-dot rule.
- [*Matrix Representations Conventions*](../articles_physics/conventions-of-the-matrix-models.html) for $\mathsf S$ and the array-level transposition.
- [*Product and Form Conventions*](../articles_physics/conventions-of-the-products-and-the-forms.html) for the four maps and the anti-automorphism.
- [*The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) for the only systematic use of the arrow.
- [*The Biquaternion Physical Interpretation of Chirality*](../articles_physics/biquaternion-physical-interpretation-of-chirality.html) for the Peirce sign as a right multiplication.
- [*Chiral Fermions in the Biquaternion Framework*](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) for the chirality cell as a two-sided operator on a field.
- [*Thomson and Compton Scattering: The Biquaternion Polarization Algebra*](../articles_physics/thomson-and-compton-scattering-the-biquaternion-polarization-algebra.html) for the mass-shell and spin-resolution cells.
- [*Anomalies and Anomaly Cancellation in Biquaternionic Form*](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) for the frame cells and the chirality trace.
- [*Maxwell's Theory on Non-Commutative Spaces and Quaternions*](../articles_physics/maxwells-theory-on-non-commutative-spaces-and-quaternions.html) for the mixed left-right display.
- [*The Gauge Principle in Biquaternionic Form*](../articles_physics/the-gauge-principle-in-biquaternionic-form.html) for the left differential operator as the ordinary case.
- [*Similitudes Between the Poisson Bracket and the Quantum Commutator*](../articles_physics/similitudes-between-the-poisson-bracket-and-the-quantum-commutator.html) for the arrow without an operand.

## Worked Examples on Matrices

Everything above is a statement about operators. This appendix puts numbers on it. Every matrix below was computed from the multiplication itself, every entry is an exact integer or a Gaussian integer, and every residual quoted as zero is exactly zero, not small.

### The Two Arrays

**The carrier array.** $L_a$ is the four-by-four matrix of left multiplication by $a$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and $R_b$ the same for right multiplication. The natural sign is the diagonal matrix

$$
N=\operatorname{diag}(1,-1,-1,-1),
$$

since it fixes $e_t$ and negates the three vectors. For $b=\vec e_x$ the two families are

$$
L_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
\qquad
R_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
$$

They agree in fourteen entries and differ in two, both in the lower block:

$$
R_{\vec e_x}-L_{\vec e_x}=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&2\\
0&0&-2&0
\end{pmatrix}.
$$

Both have four nonzero entries, determinant one, trace zero, rank four, and eigenvalues $(i,-i,i,-i)$. The whole of the right action is therefore a sign on one two-by-two block, which is why the corpus can afford to write $R_b$ and never say what it is.

### Example 1: One Vector, Three Steps

Take $b=\vec e_x$, so that $\operatorname{nat}(b)=-\vec e_x$ and the middle operator is

$$
L_{\natural(b)}=-L_{\vec e_x}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
$$

Apply the three maps in order to $\psi=e_t+2\vec e_x$. Each column is one map, and the last is the answer:

$$
\psi=\begin{pmatrix}1\\2\\0\\0\end{pmatrix}
\;\xrightarrow{\ \operatorname{nat}\ }\;
\begin{pmatrix}1\\-2\\0\\0\end{pmatrix}
\;\xrightarrow{\ L_{\natural(b)}\ }\;
\begin{pmatrix}-2\\-1\\0\\0\end{pmatrix}
\;\xrightarrow{\ \operatorname{nat}\ }\;
\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}.
$$

The last column is $\psi b$, computed directly: $(e_t+2\vec e_x)\vec e_x=\vec e_x-2e_t$. The same chain in the algebra, with no matrices at all:

$$
e_t-2\vec e_x\ \mapsto\ (-\vec e_x)(e_t-2\vec e_x)=-\vec e_x-2e_t\ \mapsto\ \natural\bigl(-\vec e_x-2e_t\bigr)=\vec e_x-2e_t.
$$

Every step is one property. The first map flips the vector part. The middle map is a left multiplication, and it reverses nothing. The last map reverses the factors of the product it receives, and that reversal is what turns the left factor $-\vec e_x$ into a right factor $+\vec e_x$.

### Why Both Ingredients Are Needed

Each of the two ingredients does half the work, and the matrices show the halves.

Conjugating $L_{\vec e_x}$ by $N$, with no change of index, gives

$$
N\,L_{\vec e_x}\,N^{-1}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix}
=-R_{\vec e_x}.
$$

That is the right family with the wrong sign. The sign is supplied by the index, because $\operatorname{nat}(\vec e_x)=-\vec e_x$:

$$
N\,L_{\natural(\vec e_x)}\,N^{-1}=-N\,L_{\vec e_x}\,N^{-1}=R_{\vec e_x}.
$$

So conjugation by the natural sign gets the shape right, and the flipped index gets the sign right. Drop either and the identity fails: with $b$ in the middle the residual is $2$ on the four units, and without any sandwich it is $2$ as well.

### Example 2: A Mixed Element

Take $b=e_t+\vec e_z$, so $\operatorname{nat}(b)=e_t-\vec e_z$. The scalar part survives the natural sign and the vector part flips, so only the $e_z$ contribution can move:

$$
L_{\natural(b)}=
\begin{pmatrix}
1&0&0&1\\
0&1&1&0\\
0&-1&1&0\\
-1&0&0&1
\end{pmatrix},
\qquad
R_b=
\begin{pmatrix}
1&0&0&-1\\
0&1&1&0\\
0&-1&1&0\\
1&0&0&1
\end{pmatrix}.
$$

Fourteen entries agree, and the two that differ are the corners $(1,4)$ and $(4,1)$. The residual of $R_b=N L_{\natural(b)}N^{-1}$ is zero.

The general lesson is the one the cells already suggest: the amount of rewriting an element needs is measured by its vector part. A central element needs none, which is Example 4.

### Example 3: Complex Coefficients and the Trap

Use the two-by-two module representation, where the field is a matrix $X$, left multiplication is $\mathsf M_2(a)X$, right multiplication is $X\mathsf M_2(b)$, and the natural sign is a transpose dressed by $\sigma_2$:

$$
\operatorname{nat}(X)=\sigma_2 X^{\mathsf T}\sigma_2^{-1}=\sigma_2 X^{\mathsf T}\sigma_2 .
$$

Take $b=(1+i)\vec e_x$, so $\operatorname{nat}(b)=-(1+i)\vec e_x$, and the test field $X_0=\begin{pmatrix}1&2i\\3&4\end{pmatrix}$:

$$
\mathsf M_2(b)=\begin{pmatrix}0&1-i\\1-i&0\end{pmatrix},
\qquad
\mathsf M_2(\natural b)=\begin{pmatrix}0&-1+i\\-1+i&0\end{pmatrix},
\qquad
\operatorname{nat}(X_0)=\begin{pmatrix}4&-2i\\-3&1\end{pmatrix}.
$$

The sandwich reproduces the right multiplication exactly:

$$
\operatorname{nat}\bigl(\mathsf M_2(\natural b)\operatorname{nat}(X_0)\bigr)
=
\begin{pmatrix}2+2i&1-i\\4-4i&3-3i\end{pmatrix}
=
X_0\mathsf M_2(b),
$$

residual zero.

**The trap is that the natural sign looks like a complex conjugation and is not one.** It is $\mathbb C$-linear: it acts on the quaternion units and leaves $i$ alone. Replacing it by the coefficient conjugation, which does touch $i$, gives residual $8.485$ on this example. Replacing the middle index $\operatorname{nat}(b)$ by $\bar b$ gives residual $8$. On elements with real coefficients the two readings are closer, so the error stays quiet until the first complex coefficient arrives. That is the worst kind of error and it is the reason the note insists on the mark.

| Wrong substitution | Residual, $b=\vec e_x$ | Residual, $b=(1+i)\vec e_x$ |
|---|---|---|
| Drop the outer $\operatorname{nat}$ | $8.000$ | $11.314$ |
| Keep $b$ in the middle | $8.000$ | $11.314$ |
| Plain transpose for $\operatorname{nat}$ | $8.000$ | $11.314$ |
| $\bar b$ for $\operatorname{nat}(b)$ | $8.000$ | $8.000$ |
| $\bar{\cdot}$ for $\operatorname{nat}$ throughout | $3.606$ | $7.071$ |

The test field is $X_0$ in every row, so the numbers are comparable. None of them is small, and none of them announces itself.

### Example 4: Where the Rewriting Does Nothing

Take $b=3e_t$. Then $\operatorname{nat}(b)=b$, the two families coincide, $L_b=R_b$, and the sandwich returns $L_b$ unchanged:

$$
N\,L_{3e_t}\,N^{-1}=L_{3e_t}=R_{3e_t},
\qquad
\text{residual } 0.
$$

The identity is true and empty. The centre is the mass direction, so R1 has nothing to say exactly where the mass sits. R2 fails there for the opposite reason: its commutator term vanishes, but its left term is already correct. One route loses the term, the other merely cannot improve it, and the two failures sit on the same subspace.

### Example 5: A Derivative

The corpus writes $\tilde\nabla^{\natural}$ many times, and that mark is the natural sign applied to the gradient as an element. The same construction reaches a rightward derivative. For a field $\Phi$ and a single direction,

$$
(\partial_\mu\Phi)\,\vec e_\mu=\operatorname{nat}\bigl(\operatorname{nat}(\vec e_\mu)\,\partial_\mu(\operatorname{nat}\Phi)\bigr),
$$

which holds at every point, residual zero on three sample points and on any polynomial or trigonometric field. The middle operator is the natural conjugate of the gradient component, so R1 extends to differential operators after all.

What it does not do is get shorter. For an element the composite collapses to a cell of length one, $R_b=T_{e_t,b}$, and nobody writes the sandwich. For a derivative it collapses to nothing: three symbols and a flipped frame coefficient, against one arrow. So the arrow is the shortest faithful form for a rightward derivative, not the only one, and the two are related by exactly the identity this note is about. Integration by parts is a third thing, and no conjugation replaces it: it moves differentiation between two factors of a bilinear form, and it changes the sign.
