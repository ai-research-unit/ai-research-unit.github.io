# __The Alternatives of Writing: Side, Order, and the Notation of Two-Sided Operators__

## Introduction

The biquaternion corpus writes operators that act on the left, operators that act on the right, and operators that act on both sides at once. The last kind is the new one. Nobody is trained to read it, and the ordinary physics habit — an operator stands to the left of what it acts on — stops working the moment the operator is two-sided.

The question this note answers is narrow and practical. When an operator acts on the right, what does one write? Several answers are in use elsewhere in mathematics and in physics. The corpus has made two choices without stating either: it names the side in ninety-one articles, and it marks the side with an arrow in three. The note lists the options, shows each of them applied to twelve equations that matter to the corpus, measures what each option costs, and states the rule the corpus is in fact following.

Nothing here is a new result. It is an inventory, a set of tables, and a recommendation. The recommendation is that the choice is already made, that it is the right one, and that it should be stated once in the operator conventions so that no article has to rediscover it.

## Why This Calculus

A reader who has followed the tables can still ask what the exercise is for. The answer is physical, and it is the reason the corpus is unusual.

**The right action is not a stylistic choice in this program; it carries the physics.** The frame cells are right multiplications: $T_{e_t,b}=R_b$, so every cell of length one is a right action by an element. The chirality cell is one of them,

$$
\mathsf C_5=-iT_{e_t,e_z}=R_{-i\vec e_z},
$$

and the chiral projectors are built from the same cell:

$$
P_\pm=\tfrac12\bigl(T_{e_t,e_t}\mp iT_{e_t,e_z}\bigr)=R_{\frac12(e_t\mp i\vec e_z)} .
$$

Written with a side mark on each action, the same projectors are
$$
P_\pm\psi=\tfrac12\bigl(\psi\mp i\,e_t\overrightarrow{\psi}\overleftarrow{e_z}\bigr),
$$
and the two differ by the sign of the only arrowed term: one equation and its mirror. Writing them out as arrays, they are idempotent, orthogonal, complementary, and of rank two, and every one of those four facts is a fact about a right multiplication:

$$
P_+=\begin{pmatrix}
\tfrac12&0&0&\tfrac{i}{2}\\
0&\tfrac12&-\tfrac{i}{2}&0\\
0&\tfrac{i}{2}&\tfrac12&0\\
-\tfrac{i}{2}&0&0&\tfrac12
\end{pmatrix},
\qquad
P_+^2=P_+,\quad P_+P_-=0,\quad P_++P_-=1,\quad \operatorname{rank}P_\pm=2,
$$

all with residual zero. So chirality in this formalism is literally a multiplication on the right, and a reader trained on matrices will look for a projector and find a right action instead. That is the whole reason the notation has to be settled: the object that splits the field into its two chiral halves is not an operator standing on the left.

**That is where the difficulty starts, and it is not a difficulty of taste.** The inherited habit is that an operator stands to the left of its operand. A right action breaks the habit, and there is no free way to repair it. Three repairs exist, and each pays a specific price: the arrow marks the side on the page and changes nothing, the anti-automorphism turns the right action into a left one at the cost of a long display, and the commutator splits the action into a left part plus a bracket that vanishes on the centre. The corpus uses the first, sometimes reads the second, and never says why.

**The calculus is the accounting.** It answers three practical questions, and nothing else:

- Given an operator, which of the three forms should be written? The answer is a rule, not a preference, and the rule is four tiers: name it, arrow for either side, dot scope for three factors, $\operatorname{nat}$ only on a whole operator.
- Given two articles that wrote the same operator differently, how does one convert? The conversions are identities, and they hold exactly, so a reader can move between forms without losing a sign.
- Given a wrong form, how does one notice? Every wrong form returns a specific nonzero residual, and the residuals are computed in the appendix. This is the part that makes the subject more than bookkeeping: without it, a sign error on a right action looks like a chiral equation.

**Why this matters for the physics and not only for the typography.** A wrong side changes the sign of the vector part, and the vector part is where the frame, the spin axis, and the chirality content live. The failure is therefore silent in the way that matters most: the equation keeps its shape, keeps most of its signs, and describes a different physical object. The example below is the smallest case of that, and it is the reason the note insists on writing the middle index as $\operatorname{nat}(b)$ and not $b$.

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
| N3 | Opposite-algebra name | $\tilde\Psi\,\tilde\nabla^{\mathrm{opp}}$ | Ring theory, module theory |
| N4 | Bimodule subscripts | ${}_{\tilde\nabla}\tilde\Psi$ | Module theory, in running text only |
| N5 | Row-vector flip | every field written as a row | Elementary matrix algebra |

**N0 is not an option.** If the operator is written after the field with no mark, the reader cannot tell whether it acts or whether it is a coefficient, and the physics prior is the opposite of what the corpus means. The corpus never does it: no article writes a right-acting gradient without a mark.

**N1 is the corpus's choice.** The arrow states the side and nothing else. It is the only one of the six that is already standard in physics for exactly this purpose, and it is the only one that reads as a mark rather than as a name. In the corpus it is used only for differential operators, and nobody writes $\psi\overleftarrow{b}$. That is a fact about the corpus, not a limit of the mark: the appendix uses the pair $\overrightarrow{b}\psi$ and $\psi\overleftarrow{b}$ on elements without restriction, and *The Arrows Used Everywhere* renders all twelve of the equations below that way, so that the difference between four marks and twenty can be seen rather than argued. The limit of the arrow is not its reach. It is that the arrow says a side and nothing else, so it cannot carry a length, a rank or a name, and it cannot scope a derivative across three factors.

**N2 is exact but barred.** The dot says which factor carries the derivative, so it survives products of three or more factors, where the arrow cannot say which one is meant. But the corpus has removed the glyph: *Operator and Calculus Conventions* states that no derivative is written with a dot, and a scan of the four hundred and four articles finds no derivative dot at all, every instance of the dot token in the corpus being the ellipsis of $\dots$. Reintroducing it for scope would collide with a rule the corpus has already paid for.

**N3 is exact and legal, and the corpus already owns the spelling.** $\tilde\nabla^{\mathrm{opp}}$ names the right-acting gradient and needs no glyph. The cost is that the side is fused into the name: a reader who does not know the convention reads $\tilde\nabla^{\mathrm{opp}}$ as a different operator rather than as the same operator acting from the other side. It is the natural choice for a reader coming from algebra and the unnatural one for a reader coming from physics.

**The letters matter, and the corpus has now decided all of them.** *Algebra and Element Conventions* and *Index and Notation Conventions* both state that the opposite algebra carries the three-letter superscript, $\mathbb{B}^{\mathrm{opp}}$ with $a\cdot_{\mathrm{opp}}b=ba$, and both now state that the two-letter $\mathrm{op}$ is not a token of the corpus at all. The reason is the distance between the two: one letter out of three, at superscript size, does not separate two meanings at reading speed, so a page carrying both would be undecidable. A scan of the two collections returns one thousand and ninety-five occurrences of $\mathrm{opp}$ in one hundred and seventy-eight articles, every one of them naming an opposite algebra, and nine occurrences of $\mathrm{op}$ in five articles, every one of them inside the sentence that forbids it.

| The two-letter form | Now |
|---|---|
| $\lVert A\rVert_{\mathrm{op}}$ | $\lVert A\rVert$, bare; the rivals keep $\lVert A\rVert_{\mathrm{HS}}$, $\lVert A\rVert_{\mathrm{nuc}}$, $\lVert A\rVert_F$, $\lVert A\rVert_*$ |
| $\psi^{\mathrm{op}\mu}$ | $\psi_\mu$, the same letter as the Grassmann variable it quantizes |
| $p^{\mathrm{op}2}$ | $p^{2}$, the scalar square |
| $A^{\mathrm{op}}$ | $A^{\mathrm{opp}}$, the three-letter mark the conventions require |
| $\vec P_{\mathrm{op}}$, $P_{\mathrm{op}}$ | $\vec P$, and $P$ for the polarisation |

Twenty-three articles of the two collections carried one or another of these, and none of them survives. The nearest survivor is a single character, the bare bar of the norm, which is what the functional-analysis articles already wrote throughout, and which the matrix articles now write where they once wrote the two-letter label.

**So the spelling for the right-acting gradient is fixed twice over.** It cannot be $\tilde\nabla^{\mathrm{op}}$, because that token no longer exists. It can be $\tilde\nabla^{\mathrm{opp}}$, three letters, which is legal and correct under the corpus's rule. And it need not be either, because the arrow says the same thing in one glyph.

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
| N0 | $\tilde\nabla\tilde\Psi_R$ | The corpus form, correct because the operator is written first; the systematic form adds the left arrow, $\overrightarrow{\tilde\nabla}\tilde\Psi_R$ |
| N1 | — | Not applicable, the field is not to the left |
| N2 | — | Not applicable |
| N3 | $\tilde\nabla^{\mathrm{opp}}\tilde\Psi_R$ | Legal, and it would state a side that is already stated |
| N4 | ${}_{\tilde\nabla}\tilde\Psi_R$ | Exact, noisy |
| N5 | unchanged | The field is a biquaternion, not a row |

**With every action marked:** $\overrightarrow{\tilde\nabla}\tilde\Psi_R=\overrightarrow{m e_t}\tilde\Psi_L$, two left arrows, the second on the scalar multiple of the identity.

Under systematic use the mass term is an action too, and it is the only term on the page whose arrow could be dropped: the operator is $me_t$, so its left action and its right action agree exactly, $\lVert L_b-R_b\rVert=0$ for every $b\in\mathbb{C}e_t$. Here that is invisible, because the term is written on the left and no right arrow is printed. It becomes visible the moment the mass is written on the right, which the second half of the pair does not do either. So the pair as printed states the ordinary case twice and the mass's centrality not at all.

### 2. The Massless Dirac Equation

Same article, the massless limit:

$$
\tilde\nabla\tilde\Psi=0 .
$$

**With every action marked:** $\overrightarrow{\tilde\nabla}\tilde\Psi=0$, one left arrow.

A homogeneous equation cannot show a side ambiguity, because there is no second object for the operator to act on. The systematic arrow adds one mark and one statement, that $\tilde\nabla$ acts from the left, which the writing already said.

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
| N3 | $\tilde\Psi\,\tilde\nabla^{\mathrm{opp}}$ | Yes, at the price of a name to remember |
| N4 | ${}_{\tilde\nabla}\tilde\Psi$ | Exact, unreadable in a display |
| N5 | transpose the field | Would change the whole article |

**With every action marked:** $\tilde\Psi\overleftarrow{\tilde\nabla}+\frac{i\varrho}{\hbar}\tilde\Psi\overleftarrow{\tilde A}$, two right arrows.

The second arrow is the one the corpus leaves out, and it is a right action by an element: $\tilde\Psi\tilde A=T_{e_t,\tilde A}\overrightarrow{\tilde\Psi}$, a cell of length one, since $e_t$ is the identity and $T_{e_t,\tilde A}=R_{\tilde A}$. So the sum is two right actions in a row, one differential and one algebraic, and the printed form says that only the first is an action. This is the one repair the systematic pass finds in the twelve.

N1 is right. R1 does not apply, since $\tilde\nabla$ is differential. The article itself supplies the reason the arrow matters: the left form and the right form are both gauge covariant, and the mixed form is not. A notation that cannot separate the left gradient from the right gradient cannot state the difference the article is about.

### 4. Maxwell's Theory in Quaternion Form

*Maxwell's Theory on Non-Commutative Spaces and Quaternions*, the spin-tensor form:

$$
\nabla F+\tfrac12\bigl(\nabla G+G^+\overleftarrow{\nabla}\bigr)=-J .
$$

| Option | Writing | Verdict |
|---|---|---|
| N0 | $G^+\nabla$ | No |
| N1 | $G^+\overleftarrow{\nabla}$, and with the tilde restored $G^+\overleftarrow{\tilde\nabla}$ | Yes, and it shows at a glance which of the two terms acts which way |
| N2 | $g_m$ times a scoped derivative | Yes, and less legible in a four-term sum |
| N3 | $G^+\nabla^{\mathrm{opp}}$ | Exact, and shorter than the arrow |
| N4 | subscripted | No, in a display |
| N5 | transpose $G^+$ | Local only, and it hides the symmetry |

**With every action marked:** $\overrightarrow{\tilde\nabla}F+\tfrac12\bigl(\overrightarrow{\tilde\nabla}G+G^+\overleftarrow{\tilde\nabla}\bigr)=-J$, two left arrows and one right.

Both left arrows are redundant by position. The right one is not, and it is the only mark in the equation that carries information.

**The quotation drops the tilde, and the systematic form restores it.** The article prints $\nabla$ for what this series calls $\tilde\nabla$: *Operator and Calculus Conventions* fixes the biquaternionic gradient as $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$, four components, and reserves the bare $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial three-component gradient whose divergence and curl the series also uses. So the quoted line is a departure from the conventions and not a different operator, and the systematic form carries the tilde. This note states the departure and does not repair it: what a quotation prints is the quoted article's business.

N1 is right, and this equation is the arrow's best case: the display is a sum of one left-acting and one right-acting term, and the arrow is the only mark that shows the difference without a name.

### 5. The Mass-Shell Cell

*Thomson and Compton Scattering*, the mass-shell cell built on the frame cells as *Anomalies and Anomaly Cancellation* defines them:

$$
D(p)=\sum_\mu\mathsf C_\mu p_\mu+m\,T_{e_t,e_t},
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
| Cells | $\sum_\mu\mathsf C_\mu p_\mu+mT_{e_t,e_t}$ | The only form that exists |

**A summation sign was missing, and the omission was the corpus's.** The printed form repeated $\mu$ and did not sum it: $\mathsf C_\mu p_\mu$ is one cell against one component, and the object is a sum of four. *Operator and Calculus Conventions*, §*The Gradient*, states the rule without qualification — "an index that appears twice is summed only where a $\sum$ names it" — and applies it to the gradient, which is spelled $\tilde\nabla=\sum_{\mu}e_\mu\partial/\partial Q_\mu$ and never $\vec e_k\partial/\partial Q_k$. The pass counted the breaches and repaired them: one hundred and sixty-three sites in twenty-two articles, one $\sum$ before the cell at each. The largest family is $\mathsf C_\mu p_\mu$, sixty-three sites in twelve articles; the spatial $\mathsf C_k p_k$ follows with twenty-four in five; the derivative contractions, $\mathsf C_\mu D_\mu$, $\mathsf C_\mu\partial/\partial x_\mu$, $\mathsf C_\mu\partial/\partial Q_\mu$ and the two mixed forms, account for about a fifth of the total; the rest are single figures down to $\gamma_\mu p_\mu$ and $p_\mu p_\mu$. The index is not always $\mu$: sixteen of the sites carry $\nu$ and five carry $\rho$, so the omission was a habit of the hand and not of one letter. The doubled cell $\mathsf C_\mu\mathsf C_\mu$ was already summed in all three places it appears, so the corpus's habit was to sum where both indices are cells and to drop the sum everywhere else. The written form of the mass-shell cell is now

$$
D(p)=\sum_{\mu\in\{t,x,y,z\}}\mathsf C_\mu p_\mu+m\,T_{e_t,e_t},
$$

and it is this form that carries the two facts below.

**The sum is what makes the cell a shell.** With it, the Clifford relation gives one identity and no approximation:

$$
D^2-2mD=\Bigl(\sum_\mu p_\mu p_\mu-m^2\Bigr)T_{e_t,e_t},
$$

residual $2.2\times10^{-16}$ at $m=1.3$ and $p=(1.7748,0.4,-0.7,0.9)$, where $\sum_\mu p_\mu p_\mu=(p_t)^2-\lvert\vec p\rvert^2$. So $D$ is a shell cell exactly when the four-momentum is on shell, and the mass enters through the identity cell $T_{e_t,e_t}$, which is why it is written as a cell and not as the number $m$. Without the sum there is no identity at all, because a single term has nothing to square against.

**What the practice was, and what it is.** Before the repair the sum arrived where both indices are cells, arrived half the time where one index was a derivative — five unsummed against five summed for $\mathsf C_\mu\partial/\partial Q_\mu$ — and was dropped where one index was a component: sixty-three sites for $\mathsf C_\mu p_\mu$ against none summed, four for $\mathsf C_\mu s_\mu$, four for $\mathsf C_\mu k_\mu$, twenty-four for the spatial $\mathsf C_k p_k$. No article stated the habit and no article needed it: every one of the one hundred and sixty-three expressions means a sum, which is why the repair changes no physics. The sentence in the conventions is general, and the corpus now keeps it in all three cases. One place keeps the unsummed form on purpose, and it is a statement about the form rather than an instance of it: the operator conventions print $\vec e_k\partial/\partial Q_k$ in the sentence that declares it unused.

**This note writes the sum wherever it uses the expression**, and the corpus now does the same, so the note and the corpus agree. The repair was mechanical — one mark per site, no equation reordered — and it leaves every stated result where it was.

**The mass term is outside the question.** It carries no index, so no sum can be missing from it, and it is written $m\,T_{e_t,e_t}$ rather than $m$ for a reason of its own: a length-zero cell is the identity, and writing it as a cell says that the mass enters on neither side. That is the fact the next paragraph uses.
$$
\mathsf C_k\psi=i\,\overrightarrow{\vec e_k}\psi\overleftarrow{\vec e_y},
\qquad
mT_{e_t,e_t}\psi=\overrightarrow{m e_t}\psi\overleftarrow{e_t}=m\psi ,
$$
with $\mathsf C_0$ the same two arrows, $e_t$ on the left and $\vec e_x$ on the right. Two arrows on each frame cell, and two on the mass, of which the second collapses: $e_t$ is the identity and $m$ is central, so the mass keeps its value when either arrow is dropped, residual $0$. The frame cells do not: $\lVert T_{\vec e_x,\vec e_y}-T_{\vec e_y,\vec e_x}\rVert=2$, so their two arrows are two different operators and the order between them is content.

The equation is the argument for the naming level. Every option at the display level fails, and the reason is not that the notation is poor but that the object is genuinely two-sided. Recomputed on the mass shell at $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$, with the sum written: $\lVert D^2-2mD\rVert=4\times10^{-16}$, matrix rank two, length two, trace $4m=5.2$, and $\{\mathsf C_\mu,\mathsf C_\nu\}=2\operatorname{diag}(1,-1,-1,-1)$.

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
| N1 | $-i\psi\overleftarrow{\vec e_z}$ | Yes, in this note: the arrow carries the side, the coefficient carries the $-i$ |
| N2 | impossible | Same reason |
| N3 | $R_{e_z}$ | Yes, and it is the same statement |
| N4 | subscript | No |
| N5 | transpose | No |
| Cells | $-iT_{e_t,e_z}$ | Yes |

**With every action marked:** $-i\,\overrightarrow{e_t}\psi\overleftarrow{\vec e_z}$, and the left arrow sits on the identity. That is how a pure right multiplication looks under the rule: the left half of the cell is the unit, so its arrow is present and empty,
$$
-i\,\overrightarrow{e_t}\psi\overleftarrow{\vec e_z}=-i\,\psi\overleftarrow{\vec e_z},
$$
residual $0$. A one-sided operator is a two-sided one whose other side is $e_t$, and the rule prints that fact instead of hiding it. So the honest count for this equation is two arrows, one of which carries nothing.

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

**With every action marked:** $s\overleftarrow{i\vec e_z}=\pm s$, one right arrow, and the arrow is what makes the sign law readable: the operator grades the module by acting on the right, and the two eigenvalues are the two sides of the Peirce split.

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

**With every action marked:** $-i\,\overrightarrow{e_t}\Psi\overleftarrow{e_z}$, one arrow on each side of the field, and the projectors
$$
P_\pm\Psi=\tfrac12\bigl(\Psi\mp i\,\overrightarrow{e_t}\Psi\overleftarrow{e_z}\bigr),
$$
which differ by the sign of the only arrowed term. The pair of arrows also shows the structure of the projector: the field sits between two operators, and the term that splits the halves is the one marked on both sides.

The bare product $e_t\Psi e_z$ is right here, and it is the one place where N0 is the best answer rather than the worst: the field is visible between the two factors, which is what the projector formula is doing, and it is also what the two arrows say, since they point inward at the same field. Writing $T_{e_t,e_z}\Psi$ is equally correct and less immediate. This is worth stating, because it can look like an exception to the rule that the corpus never writes a bare product. It is not one: the corpus never writes a bare *operator*, and $e_t\Psi e_z$ is a product of three elements with the field among them.

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

**The same missing sum, and here it is inside four factors.** The spin vector is contracted the same way and needs the same sign,
$$
D_s(p)=\tfrac12\,D(p)\Bigl(1+\mathsf C_5\sum_\mu\mathsf C_\mu s_\mu\Bigr),
$$
with the sum between the chirality cell and the second frame cell. The identity $\sum_{s=\pm}D_s(p)=D(p)$ presumes it: a single term on each side of the $\mathsf C_5$ would not sum to the mass-shell cell.

**With every action marked:** no form. The product $\mathsf C_5\mathsf C_\mu s_\mu$ is a product of cells, and there is no field in it for an arrow to point at. A two-sided factor has two sides and the display has one operand, so the second arrow has nowhere to go.

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
| N3 | $\Gamma\tilde\nabla^{\mathrm{opp}}$ | Legal only if the convention were right-to-left |
| N4 | subscript | No |
| N5 | transpose | No |

**With every action marked:** $\tilde A_2=\tilde A-\overrightarrow{\tilde\nabla}\Gamma$, one left arrow, which states nothing new.

The table is here to make a point: the left differential operator is not a special case of the two-sided one. It is the ordinary case, it has been the ordinary case since Newton, and the corpus's two-sided operators did not change it.

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

**With every action marked:** no form. A trace has no operand, so nothing can be pointed at, and the order inside the product is stated by the order of the factors alone.

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
| N3 | $\partial^{\mathrm{opp}}$ | Exact, and hides that there are two operands |
| N4 | subscripts on both arguments | Exact, unreadable |
| N5 | — | No |

**With every action marked:** as printed. It is the only one of the twelve that is already systematic, and the only one where systematic use changes nothing, because the two arrows are the expression.

Here the arrow does its job and reaches its limit in the same expression. It says that the left derivative acts on what is to the left and the right derivative on what is to the right, which is exactly right. It cannot say what those two things are, because the bracket is written without arguments. This is the one equation in the corpus where the notation is genuinely under-determined, and it is under-determined for a reason outside the notation: the two arguments have been suppressed.

## The Arrows Used Everywhere

The twelve are quoted above as the corpus prints them. Each now carries its systematic form, and this section states what the pass returns, because four marks instead of twenty is a ration, not a law, and the difference has to be measured rather than assumed.

| # | Every action marked | Marks |
|---|---|---|
| 1 | $\overrightarrow{\tilde\nabla}\tilde\Psi_R=\overrightarrow{m e_t}\tilde\Psi_L$ | $2$ left |
| 2 | $\overrightarrow{\tilde\nabla}\tilde\Psi=0$ | $1$ left |
| 3 | $\tilde\Psi\overleftarrow{\tilde\nabla}+\frac{i\varrho}{\hbar}\tilde\Psi\overleftarrow{\tilde A}$ | $2$ right |
| 4 | $\overrightarrow{\tilde\nabla}F+\tfrac12\bigl(\overrightarrow{\tilde\nabla}G+G^+\overleftarrow{\tilde\nabla}\bigr)=-J$ | $2$ left, $1$ right |
| 5 | $i\,\overrightarrow{\vec e_k}\psi\overleftarrow{\vec e_y}$ for a frame cell, $\overrightarrow{m e_t}\psi\overleftarrow{e_t}$ for the mass | $2$ left, $2$ right |
| 6 | $-i\,\overrightarrow{e_t}\psi\overleftarrow{\vec e_z}$ | $1$ left, $1$ right |
| 7 | $s\overleftarrow{i\vec e_z}=\pm s$ | $1$ right |
| 8 | $-i\,\overrightarrow{e_t}\Psi\overleftarrow{e_z}$ | $1$ left, $1$ right |
| 9 | no form: a product of cells has no operand | $0$ |
| 10 | $\tilde A_2=\tilde A-\overrightarrow{\tilde\nabla}\Gamma$ | $1$ left |
| 11 | no form: a trace has no operand | $0$ |
| 12 | as printed, the two arrows are the expression | $2$ right |

**Every arrow sits on the operator, and points at the operand.** That is the placement, and it is not a preference: it is what the corpus does in the two articles that use the mark. The Maxwell article writes $G^+\overleftarrow{\nabla}$, the Poisson bracket writes $\overleftarrow{\partial/\partial q_i}$ and $\overrightarrow{\partial/\partial p_i}$, and in each case the arrow is on the operator and the tip points at the field. Under one rule the two sides become the same shape, $\overrightarrow{\tilde\nabla}F$ and $G^+\overleftarrow{\tilde\nabla}$, and a two-sided operator is a pair of arrows pointing inward at the field between them, $\overrightarrow{e_t}\Psi\overleftarrow{e_z}$.

**The arrow sits above the tilde, not instead of it.** In a biquaternion article the gradient is $\tilde\nabla$, and the tilde is part of its name and not a decoration: it is what separates the four-component element-valued operator from the three-component spatial $\nabla$. So the mark stacks, $\overrightarrow{\tilde\nabla}$ and $G^+\overleftarrow{\tilde\nabla}$, and the operator keeps its full spelling under the arrow. Stacking two marks is accepted in this note, exactly as an arrow is accepted above another arrow, $b_1\overrightarrow{b_2\overrightarrow{\psi}}$. The alternative — writing $\overrightarrow{\nabla}$ with the tilde dropped — would be worse than a stacked mark, because an arrow over a bare $\nabla$ is the shape of a vector accent and would read as $\vec\nabla$.

**Marking the field instead splits one equation into two conventions.** A draft of this note wrote the left arrows on the fields, $\tilde\nabla\overrightarrow{F}$, and kept $G^+\overleftarrow{\tilde\nabla}$ on the operator, in the same line of the same equation. Both marks were defensible one at a time and the line was not: the reader had to learn that the arrow sits on the second symbol in one term and on the first in the next. The rule that survives is the one the corpus already follows — the actor takes the mark — and it is the same rule for an element, a derivative and a cell.

**The placement has two costs, and both are visible.** An arrow over a frame unit stacks on the vector accent, $\overrightarrow{\vec e_x}$: heavy, and unambiguous, because the frame unit is one symbol under two marks. An arrow over the gradient stacks on the tilde, $\overrightarrow{\tilde\nabla}$: three levels on one base, and still unambiguous, because the tilde is there and a tilde'd gradient is never a vector accent. The heavy case is the honest one. What the two costs have in common is that both are paid on the operator and never on the field, and that is the reason the placement belongs in the operator conventions rather than in an example.

**Twenty marks replace four.** The corpus prints four side marks across the twelve, all of them right arrows, in equations 3, 4 and 12. Marking every action prints twenty: ten left arrows and ten right ones.

**The ten left arrows split, and the split is the sharper one.** Six sit on a derivative acting forward, and those six are pure cost, because juxtaposition already states it in an associative algebra read in order. Four sit on the identity up to a scalar, in equations 1, 5, 6 and 8, and those four are doing work: an arrow on $e_t$ is how this note writes a central term and a pure right action. So the empty-looking arrow carries the most. $me_t$ is the mass, and $e_t$ on the left of the chirality cell is the statement that the cell is one-sided.

**The ten right arrows split in half, and the split is the corpus's own rule.** Five are carried by a name that already states the side: $\mathsf C_\mu$, $\mathsf C_5$, $P$, $T_{e_t,e_z}$, in equations 5 to 8. There the arrow restates the name. Five stand on a bare product with no name — the two terms of equation 3, the gradient of equation 4, the two derivatives of equation 12 — and the corpus marks four of those five. The pass finds the fifth.

**The defect it finds is one term, and it is in equation 3.** The minimal-coupling sum marks the right action of the gradient and leaves the right action of the potential bare, in the same parenthesis. Both are multiplications of the field on the right; one is by a derivation and one by an element. The display as printed says that one is an action and the other is a coefficient, and nothing in the physics supports that reading. The repair is one glyph, $\tilde\Psi\overleftarrow{\tilde A}$, or the cell name $T_{e_t,\tilde A}\overrightarrow{\tilde\Psi}$, which is the tier-one form since $\tilde A$ is an element and the cell is of length one.

**What the many arrows buy is a separation the matrices cannot show.** A left arrow and a right arrow are the same mark exactly when the operator is central, and different otherwise. Measured: $\lVert L_b-R_b\rVert=0$ for $b\in\mathbb{C}e_t$, on four samples including $1.3e_t$ and $(2-i)e_t$; $2$ for one frame unit; $4$ for $e_t+2\vec e_y$. So a term written with two arrows that agree is a mass term, and a term whose two arrows disagree is a frame term. In the matrix formulation that distinction is a distinction between a multiple of the identity and four matrices, which a reader sees only by looking at matrices. On the page it is a distinction between one mark and two, and it is visible at reading speed. This is the one place where the notation reports a physical fact that the gamma matrices keep implicit: **the mass is the central multiplicand, and centrality is exactly the licence to drop a side.**

**Reversing the two arrows gives a different operator, not a copy.** $\lVert T_{\vec e_x,\vec e_y}-T_{\vec e_y,\vec e_x}\rVert=2$ exactly, and the same $2$ for $T_{e_t,e_z}$ against $T_{e_z,e_t}$. So a two-arrow term written in the other order is a different object, and the order between the arrows is content. The one exception is the centre: $T_{e_t,e_t}$ is the identity, $\lVert mT_{e_t,e_t}-m\rVert=0$, so $\overrightarrow{m e_t}\psi\overleftarrow{e_t}=m\psi$ and the second arrow restates the first. A two-sided mass is therefore the same statement written twice, and the reversal duplicates an equation exactly when the operator is central, which is where the mass sits.

**Chirality duplicates by sign, and there the duplication is genuine.** The projector pair is one arrowed term and its complement,
$$
P_\pm\Psi=\tfrac12\bigl(\Psi\mp i\,\overrightarrow{e_t}\Psi\overleftarrow{e_z}\bigr),
\qquad
P_++P_-=1,
$$
so the two chiral equations are not independent: the second is the first subtracted from the identity. This is the duplication the two-sided calculus predicts, and it costs nothing to print twice, because the second is the first with one sign changed. It is also the place where the arrows earn their keep, since the sign that separates the halves sits on a term that carries a mark on both sides — the only term in the equation that does.

**The chirality cell is the one object whose left half is empty.** Equation 6 has a right arrow, and its left arrow sits on $e_t$: $R_{\vec e_z}\neq L_a$ for any $a$, the best residual over three hundred trials being $1.14$, so no left arrow on a non-central element can replace it. Under the rule that is a visible fact rather than a remark — the cell is written $\overrightarrow{e_t}\psi\overleftarrow{\vec e_z}$, and the trivial factor is on the page. Chirality is a side, not a symmetric construction: the operator that splits the field into its chiral halves multiplies on the right and does nothing on the left, and the pair of arrows says so.

**Where the arrows fail, they fail for want of an operand.** Equations 9 and 11 have no field: one is a product of cells, the other a trace. A two-sided factor has two sides and the display has one operand, so the second arrow has nowhere to go. Equation 12 is the third case, and the opposite one: it has two arrows and no operands, which is why it is under-determined. So systematic use covers nine of the twelve, and the three it cannot cover are the three that have no operand of their own.

**What is lost is the warning.** In the corpus the arrow sits only on derivatives, so it doubles as a signal of the differential kind. Printed everywhere, it stops signalling anything but the side, and the reader who used it as a warning loses the warning. That is the whole trade: the mark becomes uniform and stops being informative about kind.

**The pass audits; it does not legislate.** Of its twenty marks, six state nothing, five restate a cell name, and nine carry information: the four left arrows on the identity, and the five right arrows on a bare product. The corpus already prints four of those nine. So the corpus's ration is not arbitrary: it is very nearly the informative subset, and the systematic rendering's only contribution is the one omission it found. The recommendation is therefore unchanged and is now measured: tier one names, tier two marks the side where no name carries it, and universal marking is worth doing once, on a page, to see what it costs.

### What the Twelve Decide

The twelve fall into three classes, and the classes are the argument for the tiers.

| Decided by | Equations | Count |
|---|---|---|
| The naming level | 5, 6, 7, 8, 9 — mass shell, chirality cell, Peirce sign, chiral projectors, spin resolution | 5 |
| The display level | 3, 4, 12 — minimal coupling, Maxwell, Poisson bracket | 3 |
| Nothing | 1, 2, 10, 11 — Dirac pair, massless Dirac, gauge transformation, anomaly trace | 4 |

The naming level decides the most equations and the display level the fewest. That is the empirical case for naming first: the corpus's hardest objects are already handled by names, and the display is needed only where a derivative acts on what precedes it. It is also the reason a notation reform should start at the naming level and stop there unless an equation forces it further.

The systematic rendering changes this count in one place only. Of the four equations that needed nothing, equations 1, 2 and 10 gain a left arrow that states nothing, and equation 11 gains nothing because it has no operand. Of the eight that needed a name or a mark, equation 3 gains a second right arrow, and it is the one mark in the twelve that the corpus was missing.

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

**Tier two: the arrow, for a side that needs marking.** $\overrightarrow{b}\psi$ for the left action and $\psi\overleftarrow{b}$ for the right one, on elements and on derivatives alike, always with the arrow on the operator and its tip on the operand, and above the tilde when the operator carries one, $\overrightarrow{\tilde\nabla}$. The tier is a ration and not a prohibition, and the ration is measured: marking every action prints twenty marks where the corpus prints four, and six of the twenty state nothing. It is chosen because it is shorter than the sandwich, not because the sandwich fails. For a derivative the arrow is not merely shorter but required, since a derivative has no cell form. Defined once, in the operator conventions, with two clauses fixed: that the arrow points at what the operator acts on, and that the double arrow means one derivative on each side with the sign convention stated.

**Tier three: dot scope, for a product of three or more factors carrying derivatives.** The arrow cannot say which factor is meant when there are three. Dot scope can. It is currently barred by the no-dot rule, which is about $\dot x$ for $dx/dt$ and not about scope, and the ban could be narrowed to the case it was written for. Nothing in the corpus needs this tier yet; the Poisson bracket is the only expression that nearly does.

**Tier four: $\operatorname{nat}$, for a deliberate change of side.** Only on whole operators, never on one factor, and never as a way of avoiding the arrow. Its cost is length four per occurrence, and a display that uses it twice has replaced one glyph by eight cells. It can be applied to a derivative, and then it is longer still than it is on an element.

**Never: reading integration by parts as a rewrite.** It is a sign and a boundary term, not a change of side, and the arrow survives it. The side of a differential operator can be changed, at the cost of a longer display; the transfer of a derivative from one factor to another cannot.

## Deciding the Arrow

The collision recorded in *The Census* is cheap to settle now and expensive to settle later, because the four articles that decorate an algebra and the three that mark a side are still disjoint. A decision is needed, and the corpus has the material to make one.

The principle, restated now that the side mark is allowed on any object: **the arrow is a mark of a side, and it is never a decoration on a name.** An algebra written under the arrow is not being acted on by anything, so the mark there is doing something else, and the two uses cannot both be the arrow. What the arrow may mark is an action of one object on another, whatever the objects are: a derivative on a field, an element on a field, an element on both sides at once.

| Candidate for the algebra left-action mark | Writing | Collision | Verdict |
|---|---|---|---|
| Prescript | ${}_{L}\mathbb{C}\otimes\mathbb{O}$ | None: prescripts in the corpus are index blocks only | Recommended |
| Superscript $L$ | $\mathbb{C}^{L}\otimes\mathbb{O}$ | The superscript $L$ is the sector label in eight articles, $M_4^{L}$, $\Psi_0^{L}$ | Reject |
| Second arrow | $\leftarrow\mathbb{C}\otimes\mathbb{O}$ | None, but two near-identical marks in one document | Weak |
| The word | the left action of the complex octonionic chain algebra | None, verbose | Acceptable in prose |

The recommendation is therefore two-sided. Allow the pair $\overrightarrow{\ }$ and $\overleftarrow{\ }$ on any object that acts, elements included, because there the mark states a side that no other single glyph states. Keep it off names: the algebra's left action takes a prescript, $\mathbb{C}\otimes\mathbb{O}$ becoming ${}_{L}\mathbb{C}\otimes\mathbb{O}$, or the word. Two sentences in the operator conventions would fix it, one per mark, and the seven articles would need no rewriting today; only the four that quote the chain algebra would change a glyph.

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
- **One glyph, two meanings.** The arrow is a side mark in three articles and a left-action decoration on an algebra symbol in four. The two uses never meet in a single equation today, because the octonionic constructions and the Dirac equations live in different articles. They would meet in any article that quoted both. This note settles the case it can settle: the mark is allowed on any object that acts, and it is kept off names, so the algebra decoration takes a prescript. What remains open is the corpus-wide change, which belongs in the operator conventions.
- **The corpus has no settled name for the natural map.** It marks the value, $X^{\natural}$, and names the operator $X\mapsto X^{\natural}$ only by writing the same glyph bare in nine places. *Naming the Map* supplies one, $\operatorname{nat}$, and a sentence in *Product and Form Conventions* beside the $\bar{\cdot}$ row would make it official. The same sentence would fix the placeholder form $(\cdot)^{\natural}$.
- **The summation sign, repaired.** *Operator and Calculus Conventions* says a repeated index is summed only where a $\sum$ names it, and the corpus kept that for a cell on a cell while breaking it for a cell on a derivative and for a cell on a component. One hundred and sixty-three breaches in twenty-two articles is not a slip of the pen, it is the Einstein habit, and the articles read the same either way, which is why the repair is a mechanical one: one $\sum$ before the cell at each site, no equation rewritten, no result touched. The identity $D^2-2mD=(\sum_\mu p_\mu p_\mu-m^2)T_{e_t,e_t}$ is the same statement whether the sum is printed or read. The convention needed no new sentence, only to be applied; the unsummed form survives in one place, the sentence that declares it unused.
- **Which side is the matter representation.** The minimal coupling article records the left and the right construction as two covariant mirrors and calls the choice open. The notation question is downstream of that choice and cannot settle it: a corpus that had chosen the right action would write N1 everywhere and the cells would change roles. Until the choice is made, the arrow is the only mark that keeps both forms printable without rewriting the other.

## Summary

The right action is written in the corpus in one way out of six, and the corpus has never said so.

**The levels are four.** Naming is fixed by the conventions, display is free, rewrite is fixed by a theorem, and components are barred. Confusion comes from treating them as one.

**The arrow is not the transposition.** The arrow marks a side on a page and changes nothing. The transposition replaces the right action by a left one and costs two applications of $\operatorname{nat}$, of length four each. The arrow is the shortest faithful form for a side, on a derivative and on an element alike, but shortest is all it is: the sandwich reaches both, at the cost of a longer display.

**Algebraic right action needs no arrow.** $R_b=T_{e_t,b}$ is a cell of length one. The corpus writes it as $R_b$, and the three articles that use the arrow as a side mark all put it on a derivative.

**Placed on the actor, the arrow makes the two sides one shape.** $\overrightarrow{\tilde\nabla}F$ and $G^+\overleftarrow{\tilde\nabla}$ are read by one rule, and a two-sided cell is a pair of arrows pointing inward. The arrow goes above the tilde, $\overrightarrow{\tilde\nabla}$, because the tilde is part of the operator's name: it is what separates the four-component biquaternionic gradient from the three-component spatial $\nabla$. Marking the field instead would put the two placements in one equation; the corpus never does, and its two arrow users both mark the operator.

**Used without ration, the arrow prints twenty marks where the corpus prints four.** Six are left arrows on a forward-acting derivative, five restate a cell name, and nine carry information. The corpus already prints four of the nine. The arrow on the identity is the mark that turns out to be worth printing: it is how a central term and a one-sided operator are recognised. The pass found the fifth: the minimal-coupling sum marks the right action of the gradient and leaves the right action of the potential bare. Its real yield is elsewhere. Two arrows that agree mean a central operator, and the centre is where the mass sits; two arrows that disagree mean a frame term. Reversal duplicates an equation only at the centre, where the mass sits; chirality duplicates by sign, and the projector pair is one formula and its complement.

**Of twelve equations, the display decides three.** They are the right-acting gradient, the Maxwell sum of a left and a right term, and the Poisson bracket. Five are decided by the naming level, because they are two-sided or purely right-sided and no display option exists for them. Four are decided by nothing, because the operator is written first.

**The rule is four tiers.** Name the operator; arrow for either side, on elements and derivatives; dot scope for three factors with derivatives; $\operatorname{nat}$ only on whole operators. Never read integration by parts as a change of side.

**The transposition is coordinate-bound, the named operator is not.** The conventions' $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ is true, with residual zero, in the frame it was written for; the same identity in the coefficient frame needs $\operatorname{nat}$ instead of $\mathsf S$, and without a sandwich it fails in both. This note filed it as an erratum on a first pass and withdrew the erratum: the mismatch was one of frames.

**The map needs a name.** The corpus writes $X^{\natural}$ as a mark and the bare glyph as the map in nine places, so the same sign already means two things. $\operatorname{nat}$ is the cheapest name that does not collide, and one sentence in the conventions would settle it.

**The arrow needs a decision, and this note takes it.** The pair $\overrightarrow{\ }$, $\overleftarrow{\ }$ is allowed on any object that acts, elements included, and it is always placed on the actor, never on the operand; the appendix uses it systematically so that the cost can be compared with the name and with the sandwich. It stays off names: the algebra's left-action decoration becomes a prescript.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a\psi=a\psi$ | Left multiplication by the element |
| $R_b\psi=\psi b$ | Right multiplication by the element |
| $T_{a,b}=L_aR_b$ | Two-sided operator, $\psi\mapsto a\psi b$ |
| $X^{\natural}$ | The natural sign applied to an element: the corpus's usual form |
| $\operatorname{nat}$ | The map $X\mapsto X^{\natural}$, which the corpus names only by writing the glyph bare |
| $\natural$ in a subscript | A label, as in $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\psi\overleftarrow{b}$, $\psi\overleftarrow{\partial}$ | The element, or the derivative, acting on what precedes it |
| $\overrightarrow{b}\psi$, $\overrightarrow{\partial}\psi$ | The element, or the derivative, acting on what follows it |
| $\overrightarrow{\tilde\nabla}$ | The biquaternionic gradient acting on what follows it: the arrow goes above the tilde, which is part of the name |
| $\sum_\mu\mathsf C_\mu p_\mu$ | A repeated index, summed in writing: the corpus printed it without the sum until this pass |
| $\vec\nabla$ | The spatial three-component gradient, which is not the operator above |
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

Everything above is a statement about operators. This appendix puts numbers on it.

### What These Examples Are For

The tables above say which form is correct. This appendix shows the forms doing work, one job per example, and it keeps the two sides apart on purpose:

| Example | The job | What it settles |
|---|---|---|
| 0 | The left action $\overrightarrow{b}\psi$, every step | The baseline: one glyph, one array product, no rewriting |
| 1 | The right action $\psi\overleftarrow{b}$, every step, from scratch | The three-step chain, and the two independent routes to it |
| 2 | The two side by side | They differ by the sign of the frame term, and nothing else |
| 3 | A mixed element $e_t+\vec e_z$ | How much rewriting an element needs, measured by its vector part |
| 4 | Complex coefficients | That the natural sign is not a complex conjugation, with residuals |
| 5 | A central element | Where the rewriting does nothing, which is where the mass sits |
| 6 | A derivative | That the sandwich reaches it, and why the arrow is still shorter |
| 7 | The arrows used systematically | What the pair buys, what it costs, and one order reversal it exposes |

Example 0 exists because the note makes it necessary. The whole difficulty is that the right action has no free notation. The way to see what "free" means is to write the left action first, in one line, and then write the right action, which takes three maps.

Examples 0 and 1 are independent. Each starts from the multiplication table and the definition of its own side, and neither uses the other's result. They meet only in Example 2, which compares them.

Every matrix below was computed from the multiplication and checked against the printed form, thirty blocks with no mismatch. Every entry is an exact integer or a Gaussian integer, so every residual quoted as zero is exactly zero.

### The Two Arrows

Both marks are used in this appendix, without restriction, on elements and on derivatives alike:

$$
\overrightarrow{b}\psi:=L_b(\psi)=b\psi,
\qquad
\psi\overleftarrow{b}:=R_b(\psi)=\psi b .
$$

The arrow sits **on the operator** and points at what that operator acts on. Read it as a preposition: $\overrightarrow{b}\psi$ is "$b$ acting on $\psi$", $\psi\overleftarrow{b}$ is "$\psi$ acted on by $b$". The mark states the side and carries nothing else, and its placement is fixed: the operator takes the arrow, never the operand. That is the corpus's own practice — the Maxwell article writes $G^+\overleftarrow{\nabla}$, and the Poisson bracket writes both directions on the derivatives, $\overleftarrow{\partial/\partial q_i}$ and $\overrightarrow{\partial/\partial p_i}$, and no article writes the arrow on a field. The names $L_b$ and $R_b$ remain available, and the cells $T_{a,b}$ remain available; the arrows are a display, not a definition.

The carrier arrays are the same objects written as matrices in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$:

$$
\bigl(L_a\bigr)_{\mu\nu}\ \text{is the }\mu\text{-th coordinate of }a\,e_\nu,
\qquad
\bigl(R_b\bigr)_{\mu\nu}\ \text{is the }\mu\text{-th coordinate of }e_\nu\,b .
$$

The two definitions differ in one word: the product is taken in the other order. That is the entire difference between the two sides, and everything below is a consequence of it. The natural sign is the diagonal array

$$
N=\operatorname{diag}(1,-1,-1,-1),
$$

since it fixes $e_t$ and negates the three frame units.

### Example 0: The Left Action, Every Step

**The question.** Compute $\overrightarrow{b}\psi$ for $b=\vec e_x$ and $\psi=e_t+2\vec e_y$.

**The table.** Every number in this appendix comes from one product table, so it is stated once. The scalar unit is the identity, the three frame units square to minus it, two different frame units anticommute, and the triple is cyclic. Read a row label on the left against a column label on the top:

| $\cdot$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

**Predict the answer before writing any array.** Left multiplication distributes over the sum, so

$$
\overrightarrow{\vec e_x}(e_t+2\vec e_y)=\overrightarrow{\vec e_x}e_t+2\,\overrightarrow{\vec e_x}\vec e_y
=\vec e_x+2\vec e_z,
$$

using two entries of the table: $\vec e_xe_t=\vec e_x$ in row 2, column 1, and $\vec e_x\vec e_y=\vec e_z$ in row 2, column 3. So the expected answer is the coordinate column

$$
(0,1,0,2)^{\mathsf T},
$$

that is no $e_t$, one $\vec e_x$, no $\vec e_y$ and two $\vec e_z$, which is $\vec e_x+2\vec e_z$.

**Build the array, column by column.** Column $j$ of $L_{\vec e_x}$ is the image of the $j$-th basis element, that is $\vec e_xe_j$. Each column is one table entry:

| Column | Basis element | Product | Coordinates |
|---|---|---|---|
| 1 | $e_t$ | $\vec e_xe_t=\vec e_x$ | $(0,1,0,0)$ |
| 2 | $\vec e_x$ | $\vec e_x\vec e_x=-e_t$ | $(-1,0,0,0)$ |
| 3 | $\vec e_y$ | $\vec e_x\vec e_y=\vec e_z$ | $(0,0,0,1)$ |
| 4 | $\vec e_z$ | $\vec e_x\vec e_z=-\vec e_y$ | $(0,0,-1,0)$ |

so

$$
L_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix}.
$$

Read the array by its columns, not its rows: the first column says "sends $e_t$ to $\vec e_x$", the third says "sends $\vec e_y$ to $\vec e_z$". The rows are just where the coordinates land.

**Multiply.** With $\psi=(1,0,2,0)^{\mathsf T}$, every term of every row:

$$
L_{\vec e_x}\psi=
\begin{pmatrix}
0\cdot1+(-1)\cdot0+0\cdot2+0\cdot0\\
1\cdot1+0\cdot0+0\cdot2+0\cdot0\\
0\cdot1+0\cdot0+0\cdot2+(-1)\cdot0\\
0\cdot1+0\cdot0+1\cdot2+0\cdot0
\end{pmatrix}
=
\begin{pmatrix}0\\1\\0\\2\end{pmatrix}.
$$

Two rows are nonzero because two coordinates of $\psi$ are nonzero. Only row 2 receives from column 1, and only row 4 receives from column 3.

**Read back.** $(0,1,0,2)^{\mathsf T}=\vec e_x+2\vec e_z$, which is the predicted answer. Nothing was reversed, nothing changed sign, and no mark was needed.

**The column picture, which is what the array means.** A matrix times a column is a weighted sum of its columns, the weights being the coordinates of the column:

$$
1\cdot\begin{pmatrix}0\\1\\0\\0\end{pmatrix}
+0\cdot\begin{pmatrix}-1\\0\\0\\0\end{pmatrix}
+2\cdot\begin{pmatrix}0\\0\\0\\1\end{pmatrix}
+0\cdot\begin{pmatrix}0\\0\\-1\\0\end{pmatrix}
=\begin{pmatrix}0\\1\\0\\2\end{pmatrix}.
$$

The two surviving terms are exactly the two products computed by hand at the start. The array adds nothing; it is the same two table entries, arranged so that a machine can repeat them.

**The array is faithful to the table.** Left multiplication is a homomorphism, so composing arrays multiplies the elements:

$$
L_{a}L_{c}=L_{ac}\qquad\text{for all }a,c ,
$$

residual $2\times10^{-15}$ over two hundred random pairs. Concretely, $L_{\vec e_y}L_{\vec e_z}=L_{\vec e_x}$, because $\vec e_y\vec e_z=\vec e_x$ in the table. So a chain of left actions is read straight off the elements, in the same order, and no bookkeeping is lost.

### Example 1: The Right Action, Independently

**The question.** Compute $\psi\overleftarrow{b}$ for the same $\psi=e_t+2\vec e_y$ and $b=\vec e_x$. This example shares nothing with the previous one except the table. It does not use $L_{\vec e_x}$, it does not use the sandwich as a definition, and it does not assume the answer.

**Predict the answer from the table alone.** Right multiplication also distributes over the sum:

$$
(e_t+2\vec e_y)\overleftarrow{\vec e_x}=e_t\vec e_x+2\,\vec e_y\vec e_x=\vec e_x-2\vec e_z ,
$$

with the two entries now read in the other order: $e_t\vec e_x=\vec e_x$ in row 1, column 2, and $\vec e_y\vec e_x=-\vec e_z$ in row 3, column 2. The second entry carries a minus sign, because the two frame units anticommute. So the expected answer is

$$
(0,1,0,-2)^{\mathsf T},
$$

which differs from the left action's answer in the sign of the last coordinate and nowhere else.

**Build the array, column by column, by the same rule.** Column $j$ of $R_{\vec e_x}$ is the image of $e_j$ under right multiplication, that is $e_j\vec e_x$:

| Column | Basis element | Product | Coordinates |
|---|---|---|---|
| 1 | $e_t$ | $e_t\vec e_x=\vec e_x$ | $(0,1,0,0)$ |
| 2 | $\vec e_x$ | $\vec e_x\vec e_x=-e_t$ | $(-1,0,0,0)$ |
| 3 | $\vec e_y$ | $\vec e_y\vec e_x=-\vec e_z$ | $(0,0,0,-1)$ |
| 4 | $\vec e_z$ | $\vec e_z\vec e_x=\vec e_y$ | $(0,0,1,0)$ |

so

$$
R_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
$$

Columns 1 and 2 are the same as in the left array, because $e_t$ and $\vec e_x$ commute with $\vec e_x$; columns 3 and 4 are not, because $\vec e_y$ and $\vec e_z$ do not.

**Multiply**, every term:

$$
R_{\vec e_x}\psi=
\begin{pmatrix}
0\cdot1+(-1)\cdot0+0\cdot2+0\cdot0\\
1\cdot1+0\cdot0+0\cdot2+0\cdot0\\
0\cdot1+0\cdot0+0\cdot2+1\cdot0\\
0\cdot1+0\cdot0+(-1)\cdot2+0\cdot0
\end{pmatrix}
=
\begin{pmatrix}0\\1\\0\\-2\end{pmatrix}.
$$

**Read back.** $(0,1,0,-2)^{\mathsf T}=\vec e_x-2\vec e_z$, matching the prediction. The array and the hand computation agree, and they were done independently.

**The column picture.** The same two terms, now with the sign from the anticommuting entry:

$$
1\cdot\begin{pmatrix}0\\1\\0\\0\end{pmatrix}
+2\cdot\begin{pmatrix}0\\0\\0\\-1\end{pmatrix}
=\begin{pmatrix}0\\1\\0\\-2\end{pmatrix}.
$$

**Second route to the same answer: the sandwich.** The right action can also be written as three maps. Define the natural sign by its action on the four units, which is also read off the table:

$$
\operatorname{nat}(e_t)=e_t,\qquad
\operatorname{nat}(\vec e_x)=-\vec e_x,\qquad
\operatorname{nat}(\vec e_y)=-\vec e_y,\qquad
\operatorname{nat}(\vec e_z)=-\vec e_z ,
$$

extended to coefficients by $\operatorname{nat}\bigl(\sum_\mu a_\mu e_\mu\bigr)=\sum_\mu a_\mu\operatorname{nat}(e_\mu)$ with $a_\mu\in\mathbb C$ untouched, so that $i$ is fixed. It satisfies two identities, each used once below: it is an anti-automorphism, $\operatorname{nat}(ac)=\operatorname{nat}(c)\operatorname{nat}(a)$, and it has order two, $\operatorname{nat}(\operatorname{nat}(a))=a$.

The claim, to be checked rather than assumed, is

$$
\psi\overleftarrow{b}=\operatorname{nat}\Bigl(\overrightarrow{\operatorname{nat}(b)}\operatorname{nat}(\psi)\Bigr)
=\operatorname{nat}\bigl(\overrightarrow{\operatorname{nat}(\vec e_x)}\operatorname{nat}(\psi)\bigr)
=\operatorname{nat}\bigl(\overrightarrow{-\vec e_x}\operatorname{nat}(\psi)\bigr).
$$

Here $\operatorname{nat}(b)=\operatorname{nat}(\vec e_x)=-\vec e_x$, so the middle operator is left multiplication by $-\vec e_x$, and its array is $L_{-\vec e_x}=-L_{\vec e_x}$:

$$
L_{\operatorname{nat}(b)}=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
$$

**Step 1, the natural sign.** It is linear, so it acts coordinate by coordinate, and it is the diagonal array $N$:

$$
N\psi=
\begin{pmatrix}1\cdot1\\-1\cdot0\\-1\cdot2\\-1\cdot0\end{pmatrix}
=\begin{pmatrix}1\\0\\-2\\0\end{pmatrix},
\qquad
\operatorname{nat}(e_t+2\vec e_y)=e_t-2\vec e_y .
$$

The scalar part survives because $\operatorname{nat}$ fixes $e_t$; the frame part flips because $\operatorname{nat}$ negates $\vec e_y$. Nothing is reordered, because there is only one element.

**Step 2, left multiplication by $\operatorname{nat}(b)$.** Now there are two elements, so the table is needed, and every term is written out:

$$
L_{\operatorname{nat}(b)}\operatorname{nat}(\psi)=
\begin{pmatrix}
0\cdot1+1\cdot0+0\cdot(-2)+0\cdot0\\
-1\cdot1+0\cdot0+0\cdot(-2)+0\cdot0\\
0\cdot1+0\cdot0+0\cdot(-2)+1\cdot0\\
0\cdot1+0\cdot0+(-1)\cdot(-2)+0\cdot0
\end{pmatrix}
=
\begin{pmatrix}0\\-1\\0\\2\end{pmatrix}.
$$

The same step in the algebra, with each product shown:

$$
(-\vec e_x)(e_t-2\vec e_y)
=(-\vec e_x)e_t+(-\vec e_x)(-2\vec e_y)
=-\vec e_x+2\,\vec e_x\vec e_y
=-\vec e_x+2\vec e_z .
$$

Two signs enter and they come from different places: the minus in front of $\vec e_x$ from the coefficient of $b$, and the plus in front of $2\vec e_z$ from the table entry $\vec e_x\vec e_y=+\vec e_z$. This map reverses nothing; the left factor stays on the left.

**Step 3, the natural sign again.** Linear again, so it distributes over the two terms:

$$
N\begin{pmatrix}0\\-1\\0\\2\end{pmatrix}
=\begin{pmatrix}0\\1\\0\\-2\end{pmatrix},
\qquad
\operatorname{nat}(-\vec e_x+2\vec e_z)=\vec e_x-2\vec e_z .
$$

**The two routes agree.** The direct product gave $\vec e_x-2\vec e_z$ and the sandwich gives $\vec e_x-2\vec e_z$. Residual zero, exactly zero, and it is zero for every field rather than for this one: over three hundred random complex fields the largest residual is $0.0$.

$$
\psi\overleftarrow{\vec e_x}
=\underbrace{\operatorname{nat}}_{\text{flip}}\circ\underbrace{L_{-\vec e_x}}_{\text{multiply left}}\circ\underbrace{\operatorname{nat}}_{\text{flip}}
=\underbrace{R_{\vec e_x}}_{\text{multiply right}} .
$$

**Why it works, in one line.** The last map receives a product of two elements, with left factor $a=\operatorname{nat}(b)$ and right factor $c=\operatorname{nat}(\psi)$. The anti-automorphism swaps them and un-flips each:

$$
\operatorname{nat}(ac)=\operatorname{nat}(c)\operatorname{nat}(a)
=\operatorname{nat}\bigl(\operatorname{nat}(\psi)\bigr)\operatorname{nat}\bigl(\operatorname{nat}(b)\bigr)
=\psi\,b ,
$$

using order two twice at the end. Checked on the numbers: $\operatorname{nat}(c)=\operatorname{nat}(e_t-2\vec e_y)=e_t+2\vec e_y=\psi$, and $\operatorname{nat}(a)=\operatorname{nat}(-\vec e_x)=+\vec e_x=b$.

**The two ingredients, separately.** Each half of the sandwich does half the work, and the arrays show it. Conjugating $L_{\vec e_x}$ by $N$ without touching the index gives

$$
N\,L_{\vec e_x}\,N^{-1}=N\,L_{\vec e_x}\,N=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix}
=-R_{\vec e_x},
$$

which is the right family with the wrong sign. The sign is then supplied by the index, because $\operatorname{nat}(\vec e_x)=-\vec e_x$:

$$
N\,L_{\operatorname{nat}(\vec e_x)}\,N^{-1}=-N\,L_{\vec e_x}\,N^{-1}=R_{\vec e_x}.
$$

Drop either ingredient and the identity fails. With $b$ in the middle, $N L_{\vec e_x}N=-R_{\vec e_x}$, so the same three steps return the negative of the answer; the chain reads

$$
\psi\ \mapsto\ e_t-2\vec e_y\ \mapsto\ \vec e_x(e_t-2\vec e_y)=\vec e_x-2\vec e_z\ \mapsto\ -\vec e_x+2\vec e_z ,
$$

and $\vec e_x-2\vec e_z$ is not $-\vec e_x+2\vec e_z$. Without the sandwich at all there is no chain to run, and the right action is simply unrepresented.

**Where the two arrays differ.** Only in the frame block:

$$
R_{\vec e_x}-L_{\vec e_x}=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&2\\
0&0&-2&0
\end{pmatrix}.
$$

Fourteen entries agree and two do not. That is why the corpus can write $R_b$ and say nothing: the whole difference between the two sides is one sign on one two-by-two block, the block where the frame unit being multiplied by meets the other two frame units. On the central direction the difference is empty, which is Example 5.

### Example 2: The Two Side by Side

Examples 0 and 1 were computed independently and differ in one sign, which is the whole subject.

| | Left action $\overrightarrow{b}\psi$ | Right action $\psi\overleftarrow{b}$ |
|---|---|---|
| Glyph cost | one | one if written with the arrow, eight cells as a sandwich |
| Array | $L_{\vec e_x}$ | $R_{\vec e_x}$ |
| Building rule | column $j$ is $\vec e_xe_j$ | column $j$ is $e_j\vec e_x$ |
| Product on $\psi=e_t+2\vec e_y$ | $\vec e_x+2\vec e_z$ | $\vec e_x-2\vec e_z$ |
| Coordinates | $(0,1,0,2)$ | $(0,1,0,-2)$ |
| Commutes with the action? | $e_t$ and $\vec e_x$ yes, $\vec e_y$ and $\vec e_z$ no | same |
| Array identity | $L_aL_c=L_{ac}$ | $R_aR_c=R_{ca}$ (see Example 7) |

Read the product row as a physics statement. The two actions agree on the first two coordinates and disagree on the last one, which is the frame part. The frame part is where the axis, the spin content and the chirality content sit, so the difference between acting on the left and acting on the right is exactly the sign of the physical direction that carries the label. Same magnitude, same scalar, same shape.

That is why the note treats the side as a physics question and not a typographic one. A reader who writes $b$ in the middle of the sandwich, or who drops the outer map, does not get a slightly different notation; they get $\vec e_x+2\vec e_z$ where the theory says $\vec e_x-2\vec e_z$, which is a field pointing the other way in the frame direction.

### Example 3: A Mixed Element

Take $b=e_t+\vec e_z$, so $\operatorname{nat}(b)=e_t-\vec e_z$. The scalar part survives the natural sign and the frame part flips, so only the $\vec e_z$ contribution can move:

$$
L_{\operatorname{nat}(b)}=
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

Fourteen entries agree, and the two that differ are the corners $(1,4)$ and $(4,1)$. The residual of $R_b=N L_{\operatorname{nat}(b)}N^{-1}$ is zero.

The column rule explains the count. Right multiplication by $e_t$ moves nothing, so all the difference comes from $\vec e_z$, which anticommutes with $\vec e_x$ and $\vec e_y$ but commutes with $e_t$ and itself. Only the $e_t$-$\vec e_z$ corner can see the sign.

### Example 4: Complex Coefficients and the Trap

Use the two-by-two module representation, where the field is a matrix $X$, left multiplication is $\mathsf M_2(a)X$, right multiplication is $X\mathsf M_2(b)$, and the natural sign is a transpose dressed by $\sigma_2$:

$$
\operatorname{nat}(X)=\sigma_2 X^{\mathsf T}\sigma_2^{-1}=\sigma_2 X^{\mathsf T}\sigma_2 .
$$

Take $b=(1+i)\vec e_x$, so $\operatorname{nat}(b)=-(1+i)\vec e_x$, and the test field $X_0=\begin{pmatrix}1&2i\\3&4\end{pmatrix}$:

$$
\mathsf M_2(b)=\begin{pmatrix}0&1-i\\1-i&0\end{pmatrix},
\qquad
\mathsf M_2(\operatorname{nat}b)=\begin{pmatrix}0&-1+i\\-1+i&0\end{pmatrix},
\qquad
\operatorname{nat}(X_0)=\begin{pmatrix}4&-2i\\-3&1\end{pmatrix}.
$$

The sandwich reproduces the right multiplication exactly:

$$
\operatorname{nat}\bigl(\mathsf M_2(\operatorname{nat}b)\operatorname{nat}(X_0)\bigr)
=
\begin{pmatrix}2+2i&1-i\\4-4i&3-3i\end{pmatrix}
=
X_0\mathsf M_2(b),
$$

residual zero.

**The trap is that the natural sign looks like a complex conjugation and is not one.** It is $\mathbb C$-linear: it acts on the quaternion units and leaves $i$ alone. Replacing it by the coefficient conjugation, which does touch $i$, gives residual $8.485$ on this example. Replacing the middle index $\operatorname{nat}(b)$ by $\bar b$ gives residual $8$. On elements with real coefficients the two readings are closer, so the error stays quiet until the first complex coefficient arrives.

| Wrong substitution | Residual, $b=\vec e_x$ | Residual, $b=(1+i)\vec e_x$ |
|---|---|---|
| Drop the outer $\operatorname{nat}$ | $8.000$ | $11.314$ |
| Keep $b$ in the middle | $8.000$ | $11.314$ |
| Plain transpose for $\operatorname{nat}$ | $8.000$ | $11.314$ |
| $\bar b$ for $\operatorname{nat}(b)$ | $8.000$ | $8.000$ |
| $\bar{\cdot}$ for $\operatorname{nat}$ throughout | $3.606$ | $7.071$ |

The test field is $X_0$ in every row, so the numbers are comparable. None of them is small, and none of them announces itself.

### Example 5: Where the Rewriting Does Nothing

Take $b=3e_t$. Then $\operatorname{nat}(b)=b$, the two families coincide, $L_b=R_b$, and the sandwich returns $L_b$ unchanged:

$$
N\,L_{3e_t}\,N^{-1}=L_{3e_t}=R_{3e_t},
\qquad
\text{residual } 0.
$$

The identity is true and empty. The centre is the mass direction, so R1 has nothing to say exactly where the mass sits. R2 fails there for the opposite reason: its commutator term vanishes, but its left term is already correct. One route loses the term, the other merely cannot improve it, and the two failures sit on the same subspace.

### Example 6: A Derivative

The corpus writes $\tilde\nabla^{\natural}$ many times, and that mark is the natural sign applied to the gradient as an element. The same construction reaches a rightward derivative. For a field $\Phi$ and a single direction,

$$
(\partial_\mu\Phi)\vec e_\mu=\operatorname{nat}\bigl(\operatorname{nat}(\vec e_\mu)\,\partial_\mu(\operatorname{nat}\Phi)\bigr),
$$

which holds at every point, residual zero on three sample points and on any polynomial or trigonometric field. The middle operator is the natural conjugate of the gradient component, so R1 extends to differential operators after all.

What it does not do is get shorter. For an element the composite collapses to a cell of length one, $R_b=T_{e_t,b}$, and nobody writes the sandwich. For a derivative it collapses to nothing: three maps and a flipped frame coefficient, against one arrow. So the arrow is the shortest faithful form for a rightward derivative, not the only one, and the two are related by exactly the identity this note is about. Integration by parts is a third thing, and no conjugation replaces it: it moves differentiation between two factors of a bilinear form, and it changes the sign.

### Example 7: The Arrows Used Systematically

The decision taken above is that $\overrightarrow{\ }$ and $\overleftarrow{\ }$ may mark any action on any object, and *The Arrows Used Everywhere* applies it to all twelve equations. This example records what the pair does mechanically when used that way, because three things follow and two of them are not obvious.

**One: the display collapses.** The chirality cell of equation 6 acts as $-iR_{\vec e_z}$, so on a field it is written

$$
-i\,\psi\overleftarrow{\vec e_z}
$$

against eight cells for the same statement written as a sandwich. The arrow carries the side, the coefficient carries the $-i$, and nothing has been lost. The cell name $-iT_{e_t,e_z}$ remains the right form when the operator is the subject of a sentence, and the arrow is the right form when the field is.

**Two: the arrows merge in reading order, the arrays in the reverse order.** Because the product is associative,

$$
\psi\overleftarrow{b_1}\overleftarrow{b_2}=\psi\overleftarrow{b_1b_2},
\qquad
\overrightarrow{b_1}\bigl(\overrightarrow{b_2}\psi\bigr)=\overrightarrow{b_1b_2}\psi,
$$

so a chain of arrows is read straight off, left to right, with no reordering. The arrays do not behave the same way. Left multiplication is a homomorphism and right multiplication is an anti-homomorphism:

$$
L_{a}L_{c}=L_{ac},
\qquad
R_{a}R_{c}=R_{ca}.
$$

Both verified: first residual $2\times10^{-15}$, second $2.5\times10^{-15}$ over two hundred random pairs; concretely $R_{\vec e_x}R_{\vec e_y}=R_{\vec e_y\vec e_x}=R_{-\vec e_z}$ exactly. This is the fact that makes N3 in the display table the *opposite*-algebra name: the right action is a left action of the opposite algebra, and the word "opposite" is exactly this order reversal. A reader using arrows never meets it, and a reader multiplying arrays meets it on the first composite.

**Three: under the natural sign the arrow reverses.** Since $\operatorname{nat}$ is an anti-automorphism,

$$
\operatorname{nat}\bigl(\overrightarrow{b}\psi\bigr)=\operatorname{nat}(\psi)\overleftarrow{\operatorname{nat}(b)},
\qquad
\operatorname{nat}\bigl(\psi\overleftarrow{b}\bigr)=\overrightarrow{\operatorname{nat}(b)}\operatorname{nat}(\psi),
$$

residual $1.8\times10^{-15}$ over two hundred random pairs. Read that as a rule of the page: applying $\operatorname{nat}$ to a product flips its arrow and conjugates both entries. Then R1 stops being a formula and becomes a sentence. The sandwich

$$
R_b=\operatorname{nat}\circ L_{\operatorname{nat}(b)}\circ\operatorname{nat}
$$

says: flip the arrow, conjugate both entries, flip the arrow back, and the result is the other side. Nothing else in the identity is doing work.

**Four: the arrows do retire one name, and only one.** The right-acting derivative had a candidate name, $\tilde\nabla^{\mathrm{opp}}$, and it is now unnecessary: with the arrow allowed on any object, $\tilde\Psi\overleftarrow{\tilde\nabla}$ says the same thing in one glyph and needs no convention. Nothing is lost, because that name was never used. A scan of the four hundred and four articles returns no occurrence of $\tilde\nabla^{\mathrm{opp}}$, $\partial^{\mathrm{opp}}$ or $\nabla^{\mathrm{opp}}$ outside this note: the option existed only as a candidate in the table.

**What the arrows do not retire is the algebra.** $\mathbb{B}^{\mathrm{opp}}$ is not an action, it is an object: it is the algebra with the product reversed, and it is what makes the multiplication map readable as a homomorphism,

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}\longmapsto T_{\tilde Q,\tilde P},
$$

with the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ mapping to the sixteen cells $T_{\mu\nu}$. An arrow cannot do that job, because an arrow says which side an operator acts on and the enveloping algebra is not acting on anything. The two notations answer different questions, and the corpus needs both: one thousand one hundred and twenty-one occurrences of the algebra in one hundred and seventy-eight articles, against three articles that mark a side.

**What the arrow still cannot do.** It states one side and nothing else, so it cannot carry a length, a rank or a name; those are the cells' job. It cannot scope a derivative across a product of three factors, which is tier three. And it cannot replace the sandwich in a proof, because the sandwich is the proof: the arrow is the display of the result, not the derivation of it.

**What it costs.** A mark that appears everywhere stops contrasting with the cases where it is required. That contrast was never the arrow's function; its function is to state the side, and a reader who sees it always knows the side. What is lost is the signal "this one is a derivative", which is a signal about the operator's kind, not about its side, and belongs to the conventions article rather than to the mark.

**The measured order of cost**, per occurrence of a right action: one glyph for the arrow, one symbol for the name $R_b$ together with the reader's knowledge of what $R$ means, and eight cells for the sandwich. So the arrow is cheapest, the name is cheapest when the operator is being discussed rather than used, and the sandwich is the derivation. The three are not rivals; they are three registers of the same statement, and Example 1 walks through all three of them on one field.

